#!/usr/bin/env python3
"""Public WordPress + Google Sites migration into independent Hugo Markdown pages.
Preserves API and page archives and writes an explicit coverage report.
"""
import datetime, hashlib, html, json, re, unicodedata
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import requests, yaml
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
ROOT=Path(__file__).resolve().parent.parent
WP="https://gladcolor.wordpress.com"
GS="https://www.huanning.me"
S=requests.Session()
S.headers.update({"User-Agent":"HuanNing-Public-Website-Migration/1.0"})
S.mount("https://",HTTPAdapter(max_retries=Retry(total=3,backoff_factor=1,status_forcelist=[429,500,502,503,504])))
R={"run_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"wordpress":{},"google_sites":{},"assets":{"saved":0,"failed":[],"oversize":[]},"errors":[]}
media_cache={}
def write(p,s):
    p=ROOT/p if not isinstance(p,Path) else p
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s,encoding="utf-8")
def slug(s):
    s=unicodedata.normalize("NFKD",unquote(str(s))).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9._-]+","-",s).strip("-._")[:115] or "untitled"
def fetch(u,**kw):
    r=S.get(u,timeout=40,**kw);r.raise_for_status();return r
def page(meta,body):
    return "---\n"+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=120)+"---\n\n"+body.strip()+"\n"
def asset(u,site,group):
    u=u.strip()
    if u.startswith("//"):u="https:"+u
    if not u.startswith(("https://","http://")):return None
    if u in media_cache:return media_cache[u]
    try:
        with S.get(u,timeout=35,stream=True) as response:
            response.raise_for_status()
            if int(response.headers.get("Content-Length","0"))>16000000:
                R["assets"]["oversize"].append(u);return None
            ctype=response.headers.get("Content-Type","").split(";")[0]
            ext=Path(urlparse(u).path).suffix.lower().strip(".")
            ext=ext if ext in ("jpg","jpeg","png","webp","gif","svg","avif","pdf") else {
               "image/jpeg":"jpg","image/png":"png","image/webp":"webp","image/gif":"gif",
               "image/svg+xml":"svg","application/pdf":"pdf"}.get(ctype)
            if not ext:return None
            data=bytearray()
            for chunk in response.iter_content(65536):
                data.extend(chunk)
                if len(data)>16000000:
                    R["assets"]["oversize"].append(u);return None
            name=slug(Path(urlparse(u).path).stem)[:55]+"-"+hashlib.sha256(u.encode()).hexdigest()[:9]+"."+ext
            local="media/"+site+"/"+slug(group)+"/"+name
            p=ROOT/"static"/local;p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes(data)
            R["assets"]["saved"]+=1
            media_cache[u]=local
            return local
    except Exception as e:
        R["assets"]["failed"].append({"url":u,"reason":str(e)[:150]})
        return None
def convert(h,url,site,slug_value):
    soup=BeautifulSoup(h,"html.parser")
    for item in soup.select("script,style,noscript,form"):item.decompose()
    for img in soup.select("img"):
        src=next((img.get(x) for x in ("data-orig-file","data-src","src") if img.get(x)),"")
        if src:
            src=urljoin(url,src)
            img["src"]=asset(src,site,slug_value) or src
        for k in list(img.attrs):
            if k not in ("src","alt","title"):del img[k]
    for a in soup.select("a[href]"):
        a["href"]=urljoin(url,a["href"])
    for iframe in soup.select("iframe[src]"):
        a=soup.new_tag("a",href=urljoin(url,iframe["src"]))
        a.string="Open embedded media or application"
        iframe.replace_with(a)
    text=md(str(soup),heading_style="ATX",bullets="-")
    return re.sub(r"\n{4,}","\n\n\n",text).strip()
def wp_list(kind):
    out=[]
    for i in range(1,100):
        try:
            r=fetch(WP+"/wp-json/wp/v2/"+kind,params={"per_page":100,"page":i,"_embed":1})
            data=r.json()
            if not isinstance(data,list):raise ValueError("REST API did not return list")
            out.extend(data)
            print("WordPress",kind,"page",i,"received",len(data),"expected",r.headers.get("X-WP-Total"),flush=True)
            if i>=int(r.headers.get("X-WP-TotalPages","0"))>0 or len(data)<100:break
        except requests.HTTPError as e:
            if i>1 and e.response.status_code==400:break
            raise
    return out
def wp_proxy_posts():
    # WordPress.com fallback if a site restricts the self-hosted REST route.
    data=[];offset=0
    while True:
        r=fetch("https://public-api.wordpress.com/rest/v1.1/sites/gladcolor.wordpress.com/posts/",params={"number":100,"offset":offset,"status":"publish"})
        d=r.json();chunk=d.get("posts",[])
        if not chunk:break
        for p in chunk:
            data.append({"id":p.get("ID"),"date":p.get("date"),"slug":p.get("slug"),"link":p.get("URL"),"title":{"rendered":p.get("title","")},"content":{"rendered":p.get("content","")},"excerpt":{"rendered":p.get("excerpt","")},"categories":[],"tags":[]})
        offset+=len(chunk)
        if offset>=d.get("found",offset) or len(chunk)<100:break
    return data
def old_post_paths():
    result={}
    for p in (ROOT/"content/post").rglob("*.md"):
        txt=p.read_text(encoding="utf-8")
        m=re.match(r"\A---\s*\n(.*?)\n---",txt,re.S)
        if not m:continue
        try:meta=yaml.safe_load(m.group(1)) or {}
        except Exception:continue
        if meta.get("original"):result[meta["original"].rstrip("/")]=p
        if meta.get("title"):result["title:"+slug(meta["title"])]=p
    return result
def import_wp():
    out=R["wordpress"]={"status":"started","posts_api_count":0,"posts_migrated":0,"pages_api_count":0,"pages_migrated":0,"files":[]}
    refs=old_post_paths()
    for kind in ("posts","pages"):
        try:
            records=wp_list(kind)
        except Exception as e:
            print("WP REST error",kind,str(e),flush=True)
            if kind=="posts":
                try:records=wp_proxy_posts()
                except Exception as e2:
                    R["errors"].append({"source":"WordPress","kind":kind,"message":str(e2)});continue
            else:
                try:
                    r=fetch("https://public-api.wordpress.com/rest/v1.1/sites/gladcolor.wordpress.com/pages/",params={"number":100})
                    data=r.json()
                    records=[{"id":p.get("ID"),"date":p.get("date"),"slug":p.get("slug"),"link":p.get("URL"),"title":{"rendered":p.get("title","")},"content":{"rendered":p.get("content","")},"excerpt":{"rendered":p.get("excerpt","")}} for p in data.get("pages",[])]
                except Exception as e2:
                    R["errors"].append({"source":"WordPress","kind":kind,"message":str(e2)});continue
        out[kind+"_api_count"]=len(records)
        for p in records:
            title=html.unescape(p.get("title",{}).get("rendered","Untitled"))
            original=p.get("link") or WP
            s=slug(p.get("slug") or title)
            path=(refs.get(original.rstrip("/")) or refs.get("title:"+slug(title))) if kind=="posts" else None
            if not path:path=ROOT/"content"/("post" if kind=="posts" else "pages")/(s+".md")
            date=p.get("date") or "2020-01-01"
            raw=p.get("content",{}).get("rendered","")
            if not raw.strip():
                R["errors"].append({"source":"WordPress","url":original,"message":"empty post body"});continue
            try:
                text=convert(raw,original,"wordpress",s)
                summary=BeautifulSoup(p.get("excerpt",{}).get("rendered",""),"html.parser").get_text(" ",strip=True)[:380]
                meta={"title":title,"date":date,"summary":summary,"original":original,"wordpress_id":p.get("id")}
                if kind=="pages":meta["type"]="pages"
                if kind=="posts" and path.stem!=s:meta["aliases"]=["/post/"+s+"/"]
                write(path,page(meta,text))
                write("archive/wordpress/"+kind+"/"+s+".html",raw)
                write("archive/wordpress/"+kind+"/"+s+".json",json.dumps(p,ensure_ascii=False,indent=2))
                out[kind+"_migrated"]+=1
                out["files"].append({"source":original,"destination":str(path.relative_to(ROOT))})
            except Exception as e:R["errors"].append({"source":"WordPress","url":original,"message":str(e)})
    out["status"]="completed" if not any(x["source"]=="WordPress" for x in R["errors"]) else "partial"
def extract_main(soup):
    # Google Sites uses a title-only ARIA main and separate content tiles.
    # Prefer the actual tyJCtd content tiles over [role=main].
    tiles=soup.select(".tyJCtd")
    if tiles:
        holder=BeautifulSoup("<div></div>","html.parser").div
        for tile in tiles:holder.append(BeautifulSoup(str(tile),"html.parser"))
        return holder
    main=soup.select_one("main, [role=main]")
    return main or soup.body or soup
def plain(el):
    copy=BeautifulSoup(str(el),"html.parser")
    for t in copy.select("script,style,nav,header,footer,button,iframe,svg"):t.decompose()
    # Each Google Sites text tile is one semantic content block. Reading
    # individual span nodes separately can fragment bibliography citations.
    tiles=copy.select(".tyJCtd")
    if tiles:
        return "\n".join(x.get_text(" ",strip=True) for x in tiles if x.get_text(" ",strip=True))
    lines=[t.strip() for t in copy.get_text("\n",strip=True).splitlines() if t.strip()]
    return "\n".join(lines)
def update_projects(text):
    markers=[("mosquito-habitat","Mosquito larval habitat and productivity prediction"),
             ("llm-find","LLM-Find: Data retrieval agent for Autonomous Geographic Information System (GIS)"),
             ("hourly-population","Hourly population estimation at neighorhood level"),
             ("street-tree-diameter","Street tree diameter measurement")]
    positions=sorted([(text.lower().find(label.lower()),name,label) for name,label in markers if text.lower().find(label.lower())>=0])
    updated=0
    for i,(start,key,label) in enumerate(positions):
        stop=positions[i+1][0] if i+1<len(positions) else len(text)
        chunk=text[start+len(label):stop]
        chunk=chunk.split("LinkedIn")[0].split("Page updated")[0]
        chunk="\n\n".join([x for x in chunk.split("\n") if len(x.strip())>5 and x.strip() not in ("Image","iframe")]).strip()
        if len(chunk)<60:continue
        path=ROOT/"content/project"/(key+".md")
        if not path.exists():continue
        old=path.read_text(encoding="utf-8")
        m=re.match(r"\A---\s*\n(.*?)\n---\s*\n",old,re.S)
        if not m:continue
        meta=yaml.safe_load(m.group(1));meta["google_sites_source"]=GS+"/projects"
        existing=old[m.end():];resources=re.search(r"\*\*Resources\*\*[\s\S]*",existing)
        write(path,page(meta,chunk+"\n\n"+(resources.group(0) if resources else "")))
        updated+=1
    return updated
def publication_list(text):
    lines=[x.strip() for x in text.splitlines() if x.strip()]
    entries=[];last=""
    for t in lines:
        year=re.fullmatch(r"20\s*\d\s*\d",t)
        if year:
            last=re.sub(r"\s+","",t);entries.append("\n### "+last+"\n");continue
        if len(t)>60 and ("ning" in t.lower() or "GIScience in the Era" in t):
            entries.append("- "+t)
    count=sum(x.startswith("- ") for x in entries)
    if count<8:R["errors"].append({"source":"GoogleSites","page":"publications","message":"bibliography extraction only "+str(count)+" items; raw source archived"})
    if count>=8:
        content="For an up-to-date list, see [Google Scholar](https://scholar.google.com/citations?user=aK57tWMAAAAJ).\n\n## Full historical bibliography from huanning.me\n\n"+"\n".join(entries)+"\n\n## Selected publication pages\n"
        write("content/publication/_index.md",page({"title":"Publications","description":"Full academic bibliography archived from the previous Google Sites website."},content))
    return count
def import_google():
    out=R["google_sites"]={"status":"started","pages_requested":4,"pages_saved":0,"projects_updated":0,"bibliography_entries":0,"assets_by_page":{},"pages":[]}
    for key in ("home","projects","publications","thoughts"):
        url=GS+("/" if key=="home" else "/"+key)
        try:
            resp=fetch(url)
            soup=BeautifulSoup(resp.text,"html.parser");main=extract_main(soup);text=plain(main)
            write("archive/google-sites/"+key+".html",resp.text)
            write("archive/google-sites/"+key+".txt",text)
            write("archive/google-sites/"+key+".md",md(str(main),heading_style="ATX"))
            assets=[]
            for img in main.select("img"):
                src=img.get("data-src") or img.get("src")
                if src and "googleusercontent" in src:
                    local=asset(urljoin(url,src),"google-sites",key)
                    if local:assets.append(local)
            out["assets_by_page"][key]=sorted(set(assets))
            out["pages_saved"]+=1
            out["pages"].append({"source":url,"text_characters":len(text),"images":len(set(assets))})
            print("Google Sites",key,"text",len(text),"saved images",len(set(assets)),flush=True)
            if key=="projects":out["projects_updated"]=update_projects(text)
            if key=="publications":out["bibliography_entries"]=publication_list(text)
            if key=="home" and len(text)>200:
                about=ROOT/"content/about.md"
                if about.exists():
                    old=about.read_text(encoding="utf-8")
                    if "## Original Google Sites biography" not in old:
                        write(about,old.rstrip()+"\n\n## Original Google Sites biography\n\n"+text+"\n")
            if key=="thoughts" and len(text)>100:
                write("content/articles/google-sites-thoughts.md",page({
                   "title":"Spatial Computing Thoughts (Google Sites archive)",
                   "summary":"Preserved ideas and essays from the former personal academic website.",
                   "date":"2025-01-01","original":url},text))
        except Exception as e:
            print("Google Sites error",key,str(e),flush=True)
            R["errors"].append({"source":"GoogleSites","page":key,"message":str(e)})
    out["status"]="completed" if not any(x["source"]=="GoogleSites" for x in R["errors"]) else "partial"
def main():
    try:import_wp()
    except Exception as e:R["errors"].append({"source":"WordPress","message":str(e)})
    try:import_google()
    except Exception as e:R["errors"].append({"source":"GoogleSites","message":str(e)})
    write("migration-report.json",json.dumps(R,ensure_ascii=False,indent=2))
    wp=R["wordpress"];gg=R["google_sites"];media=R["assets"]
    summary="WordPress posts "+str(wp.get("posts_migrated",0))+"/"+str(wp.get("posts_api_count","?"))+", pages "+str(wp.get("pages_migrated",0))+"; Google Sites "+str(gg.get("pages_saved",0))+"/4, projects "+str(gg.get("projects_updated",0))+", bibliography entries "+str(gg.get("bibliography_entries",0))+"; media files "+str(media["saved"])+"; failed media "+str(len(media["failed"]))+"; errors "+str(len(R["errors"]))
    print(summary,flush=True)
    write("MIGRATION_STATUS.md","# Migration report\n\n"+summary+"\n\nRead migration-report.json for all source URLs and individual failures. The public API does not include private posts, drafts or restricted media. The original websites remain unchanged.\n")
if __name__=="__main__":main()
