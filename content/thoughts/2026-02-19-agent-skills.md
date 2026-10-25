---
title: 'From Data Source Handbooks to Agent Skills: How Academic Research Anticipated Industry Trends'
date: '2026-02-19T21:42:28-05:00'
summary: 'In May 2024, our team (Zhenlong Li Temitope Ezekiel Akinboyewa M. Naser Lessani) developed LLM-Find — an autonomous
  GIS agent framework for geospatial data retrieval. At its core is a concept we call the “data source handbook”: a structured,
  plug-and-play knowledge package that teaches an LLM how to retrieve data from a specific source, including […]'
original: https://gladcolor.wordpress.com/2026/02/19/from-data-source-handbooks-to-agent-skills-how-academic-research-anticipated-industry-trends/
wordpress_id: 62
aliases:
- /post/from-data-source-handbooks-to-agent-skills-how-academic-research-anticipated-industry-trends/
- /post/2026-02-19-agent-skills/
---

In May 2024, our team ([**Zhenlong Li**](https://www.linkedin.com/in/zhenlongli?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAARvnTYBvom3tpF9GgXgXHu0V8PeJ1E6PaE) [**Temitope Ezekiel Akinboyewa**](https://www.linkedin.com/in/temitope-akinboyewa?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABcwlx4BqVa2mvISnAMmeos0wwVeN6AE1MQ) [**M. Naser Lessani)**](https://www.linkedin.com/in/ACoAADABFKAB7Cu_KWpvkP3doI3LM8okUuzDyj8?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAADABFKAB7Cu_KWpvkP3doI3LM8okUuzDyj8) developed LLM-Find — an autonomous GIS agent framework for geospatial data retrieval. At its core is a concept we call the **“data source handbook”**: a structured, plug-and-play knowledge package that teaches an LLM *how* to retrieve data from a specific source, including metadata, API details, code patterns, and technical requirements.

The mechanism: when a user makes a natural language data request, the LLM browses brief descriptions from all available handbooks, selects the most relevant data source, loads the full handbook, and generates executable code to fetch the data. New data sources can be added simply by writing a new handbook file — no retraining, no code changes.

Fast forward to **October 2025**, about 1.5 years later, Anthropic announced **Claude Skills**: reusable, modular instruction sets packaged as folders with a `SKILL.md` file that Claude can browse, select from, and load on demand. Simon Willison called it “maybe a bigger deal than MCP.” The parallel is striking:

|  | LLM-Find Handbooks (2024) | Claude Skills (2025) |
| --- | --- | --- |
| Format | `.toml` files with metadata + instructions | `SKILL.md` files with YAML frontmatter + instructions |
| Discovery | LLM reads brief descriptions, selects the best match | Claude scans frontmatter descriptions, finds relevant matches |
| Loading | Full handbook loaded only when selected | Full skill loaded only when needed |
| Extensibility | Add a new `.toml` file → new capability | Add a new skill folder → new capability |
| Design philosophy | Plug-and-play | Composable and portable |

The conceptual alignment goes deeper. In our research agenda paper *“GIScience in the Era of Artificial Intelligence”* (arXiv: March 2025, 7 months before Claude Skills launched), we explicitly defined **“skills”** as **“practical abilities to operate data and solve problems”** — distinguishing them from mere textual knowledge. We argued that AI’s lack of domain-specific skills is the key bottleneck for autonomous systems, and proposed “self-growing” agents that learn from documentation to expand their capabilities over time.

This is exactly the paradigm Claude Skills now implements at scale — and what LLM-Find demonstrated in the geospatial domain a year and a half earlier.

**This convergence points to a broader truth: there is no such thing as a truly “general” agent.** An LLM foundation model is a general *understanding* of its training data — it can reason, follow instructions, and generate code. But general understanding is not the same as specific competence. An LLM that has never seen the OpenTopography API documentation cannot reliably fetch elevation data, no matter how powerful the model is. The real architecture for capable agents is not a monolithic super-model — it is **a foundation model + pluggable skill/knowledge sets**. The foundation model provides reasoning, language comprehension, and planning; the skills provide the domain-specific knowledge, tool interfaces, and procedural expertise that turn reasoning into reliable action. This is precisely the pattern both LLM-Find handbooks and Claude Skills implement: the LLM remains general-purpose, while skills make it specifically capable. As new domains emerge, you don’t retrain the model — you write a new handbook. This “foundation model + skills” paradigm may well be the general architecture for AI agents across all fields, not just GIS.

I’m not claiming Anthropic borrowed from our work. Great ideas often converge independently. But I do think this convergence validates the research direction: **the future of AI agents is not just bigger models; it’s structured, shareable skill libraries that let agents learn new capabilities without retraining.**

If you’re interested:

- LLM-Find paper: <https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2458688>
- LLM-Find code: <https://github.com/gladcolor/LLM-Find>
- Autonomous GIS research agenda: <https://www.tandfonline.com/doi/full/10.1080/19475683.2025.2552161>

#AI #LLM #GIS #AutonomousGIS #AgentSkills #Research #Innovation #GIScience #ArtificialIntelligence #Geospatial
