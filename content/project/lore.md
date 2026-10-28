---
title: "LORE: Literature-driven Open Research Engine"
date: 2026-10-27T22:40:00-04:00
area: AI for science, literature mining
summary: A warehouse of research knowledge built from the paper corpus. Every paper becomes a case, and the theories, data, models, math, tools, evaluation metrics, and reasoning patterns emerge from mining the cases, so that researchers, mainly AI, can stand on the shoulders of giants.
image: media/projects/lore/lore-overview.webp
tags:
- AI for Science
- Literature Mining
- Knowledge Base
- Large Language Models
---

Before we start a research project, we do a literature review. It often starts out as a simple task and piles up into information overload. LORE, the Literature-driven Open Research Engine, builds a warehouse for researchers, mainly AI agents, so that they can stand on the shoulders of giants: the knowledge the research community has already produced, distilled from the papers and made easy to navigate.

![LORE, Literature-driven Open Research Engine: build a warehouse for researchers (mainly AI), standing on the shoulders of giants. A cartoon of a researcher buried in papers, and a pyramid of eight bases: Case, Data, Model, Math, Eval, Tool, Theory, and Thinking](media/projects/lore/lore-overview.webp)

*LORE organizes the literature into eight bases, with the Case-Base at the foundation.*

## Eight bases shaped by the paper corpus

The core principle is simple: the Case-Base is the paper corpus. Every paper becomes a case, recording its research question, study type, scope, methods, theories, and results. The other seven bases emerge from the cases. An extraction pipeline mines what appears across all cases, counts it, and links every entry back to the papers that use it.

| Base | The question it answers |
|---|---|
| **Case-Base** | How have others tackled similar problems? |
| **Data-Base** | What data exist, and how do I get them? |
| **Model-Base** | What research methods can I use? |
| **Math-Base** | What formal ideas underlie the methods? |
| **Eval-Base** | How do I judge the quality of my work? |
| **Tool-Base** | What software and instruments do I use? |
| **Theory-Base** | What domain theories and frameworks apply? |
| **Thinking-Base** | How should I reason about this problem? |

The Thinking-Base is the most distinctive part. Most literature tools help with methods and data. LORE also records how researchers reason about a problem, such as inductive, deductive, or comparative reasoning, and presents it as a prompt for reflection before a method is chosen.

The content is shaped entirely by the papers fed into it. Feed it geographic science papers and it becomes a geographic science warehouse; feed it medical papers and medical content emerges. Domain tags keep all fields in one shared warehouse, so cross-disciplinary connections, such as the same method under different names in two fields, can appear naturally.

## How LORE works

![LORE architecture in three layers: ingest (paper corpus, crawler and full-text extractor), extraction and storage (an LLM pipeline with three evidence tiers feeding eight bases linked by relations), and retrieval (a user question and scope leading to cases, aggregated base entries, and competing study designs)](media/projects/lore/lore-architecture.webp)

*Three layers: ingest the papers, extract and store the knowledge, and retrieve it for a research question.*

- **Ingest.** A crawler collects papers from OpenAlex, downloads the open-access full texts, and converts them to plain text.
- **Extract and store.** For each paper, a large language model writes the case and its entries in the seven other bases, plus links between them, such as *evaluated with*, *used with data*, *implemented in*, *grounded in*, *contrasted with*, and *not suitable for*. Variants are merged (RF and Random Forest become one entry), and each entry gets a short definition grounded in the papers that mention it.
- **Retrieve.** A research question returns similar cases, together with the methods, theories, data, math, tools, metrics, and reasoning those cases used, with counts and links to the source papers.

Every piece of knowledge carries an evidence tier, so users know how far to trust it. Tier A is named explicitly in the paper, Tier B is mapped from an alias to a standard name, and Tier C is inferred from context. The planned next version adds semantic search over the cases and groups the retrieved cases into two to four competing study designs, so that researchers see alternatives and trade-offs, not only the most popular method.

## Warehouses built so far

| Warehouse | Papers | Base entries | Cross-base relations |
|---|---|---|---|
| Geographic information science (37 journals, 2006 to 2026) | 1,132 | 5,556 | 11,152 |
| Mosquito-borne disease (24 high-impact journals) | 14,954 | 46,421 | 139,080 |

Smaller warehouses cover regional water and environmental research. The GIS warehouse was built with a free open-weight model (gpt-oss-120b) at zero API cost. In a 50-paper check against Claude Opus 4.6, the two models agreed on the study type for 76% of the papers and often extracted the same concepts under different names, which is why LORE merges variants into standard names.

![The LORE mosquito research warehouse: a search for larval habitat returns 104 cases, each tagged with its methods, data, theories, math, and reasoning](media/projects/lore/mosquito-cases.webp)

*Searching the mosquito warehouse for "larval habitat" returns 104 cases. Each case shows its methods, data, theories, math, and reasoning as colored tags.*

![The Method-Base of the mosquito warehouse: cards for phylogenetic analysis, PCR, and logistic regression, each with a paper count, an evidence tier, a definition, and citing papers](media/projects/lore/mosquito-method-base.webp)

*The Method-Base of the mosquito warehouse. Each entry shows how many papers use it, its evidence tier, a definition grounded in those papers, and the list of citing papers.*

## From the warehouse to evidence-backed research graphs

LORE also supports research design. In LORE × GeoArchitect, a research question is drawn as a causal graph, and LORE retrieves the literature evidence for every factor and link. A language model then summarizes what those papers actually say about each claim, and each link is marked as having strong, moderate, weak, conflicting, or absent support in the literature. Links with weak or absent support point to gaps in the literature.

![LORE × GeoArchitect evidence-backed causal graph of Zika transmission factors in Merida, Mexico, with 24 factors and 30 links shaded by literature support](media/projects/lore/zika-evidence-graph.webp)

*An evidence-backed causal graph of Zika transmission factors in Mérida, Mexico. Click any factor or link in the live graph to read the evidence. [Open the interactive graph](https://gladcolor.github.io/Ethiopia_larva/lore_reports/zika_transmission_factors_merida_mexico.html).*

Two more graphs built from the mosquito warehouse: [dry-season *Anopheles stephensi* larval productivity](https://gladcolor.github.io/Ethiopia_larva/lore_reports/dry_season_anopheles_stephensi_larval_productivity_factors.html) and [*Aedes aegypti* indoor resting height](https://gladcolor.github.io/Ethiopia_larva/lore_reports/aedes_aegypti_indoor_resting_height_factors.html). Two of these graphs also appear in the [Fractal Research Graph](../fractal-research-graph/) project.

## Related

- Project: [Fractal Research Graph](../fractal-research-graph/), which grows research graphs grounded in the scientific record with AI agent swarms.
- Project: [Research Architect](../research-architect/), an AI copilot for framing hypotheses on an influence graph.
