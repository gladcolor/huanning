---
title: "Fractal Research Graph: Scientific Infrastructure for the Age of AGI"
date: 2026-10-26T11:18:00-04:00
area: AI for science, AI agent swarms
summary: A research graph with the same form at every scale, built from standardized research units, so that AI agent swarms and human experts can grow scientific knowledge together.
image: media/projects/fractal-research-graph/cover.webp
tags:
- AI for Science
- AI Agents
- Fractal Research Graph
- Human-AI Teaming
---

On September 3, 2026, OpenAI released GPT-6 and formally declared that the era of artificial general intelligence, or AGI, had arrived, meaning that artificial intelligence now surpasses most humans in most domains. Regardless of how AGI is defined, AI has clearly reached an exceptionally high level of analytical and reasoning capability, at a cost that is increasingly affordable. When our team was writing about this topic two years ago, we still had to carefully consider whether to mention AGI. Today, perhaps that debate is no longer necessary.

For academia, the first challenge of the AGI era is determining how to reorganize this new productive force: a continuous supply of high-level reasoning and programming intelligence. In the past, developing such human expertise required many years of training, followed by considerable effort to bring experts together. Now, comparable intellectual capabilities can be accessed at the cost of tokens.

For several years, our team has been envisioning what future scientific research might look like and exploring the application of AI agents to geographic information science. After years of exploration, research, and practice, we believe that disciplinary barriers will continue to exist. Scientific research will still take the form of AGI combined with domain knowledge, but cross-disciplinary research will become the norm. Research involving AI will increasingly be organized around the problem itself rather than around established academic disciplines.

AI will primarily perform implementation and exploration, searching for possible solutions tens, hundreds, or even thousands of times faster than humans. Human experts, meanwhile, will guide AI toward deeper levels of inquiry within their areas of expertise.

## The infrastructure problem

Under these emerging conditions, what kind of scientific infrastructure do we need? We now have access to a nearly continuous supply of intelligence, represented operationally by tokens. Yet today's research system, including how knowledge is represented and stored and how experts divide and coordinate their work, was largely designed around the cognitive capacities and working boundaries of humans.

For example, a scientific paper is typically limited to approximately 5,000 words. It prioritizes a small number of successful findings while omitting numerous failed explorations. Research evaluation is closely tied to publications and citations. A paper may be published once it receives the approval of one journal editor and two reviewers, who may be researchers or doctoral students from adjacent fields. Meanwhile, the complexity of research processes and outputs often makes scientific findings difficult to understand, verify, and reproduce.

## The Fractal Research Graph

The scientific community clearly needs to redesign its infrastructure to accommodate this transformation in productive capacity. Our team has begun with the representation, storage, and updating of scientific knowledge. We have proposed the Fractal Research Graph, which converts scientific outputs into basic units with a standardized form of representation and organizes them into research graphs that retain similar structures across different scales.

![A research graph of environmental effects on mosquito larval productivity, built from 14,000 mosquito-related papers, with the evidence summary for one factor](media/projects/fractal-research-graph/grounded-research-graph.webp)

*A research graph grounded in the scientific record: environmental effects on mosquito larval productivity, built from 14,000 mosquito-related papers. [Open the interactive graph](https://gladcolor.github.io/Ethiopia_larva/lore_reports/dry_season_anopheles_stephensi_larval_productivity_factors.html).*

This self-similarity supports the long-term operation of AI agent swarms while reducing the need for extensive orchestration. It also enables crowdsourced participation. Much like SETI@home once allowed citizen scientists to contribute their personal computers to the search for extraterrestrial intelligence at home, individuals could contribute their unused AGI capacity or computing resources to automated scientific research.

![A coarser-level graph of environmental effects on mosquito larval productivity, with one link opened into a finer-level subgraph of mosquito indoor resting height factors](media/projects/fractal-research-graph/fractal-subgraph.webp)

*The fractal structure: a link in the coarser-level graph opens into a finer-level subgraph with the same form. [Open the finer-level graph](https://gladcolor.github.io/Ethiopia_larva/lore_reports/aedes_aegypti_indoor_resting_height_factors.html).*

## Two fractal methods

The graph grows to finer scales through two methods that apply in the same way at every level.

**Mechanism chain.** A link A → B can be opened into the chain of mechanisms that carry it, A → M1 → M2 → B, and each step of the chain can open again into a finer subgraph. For example, human population density does not change mosquito larval density directly: female mosquitoes need blood meals, and their resting, flying, biting, and egg-laying behavior carries the effect from people to the water bodies where larvae grow. The figure above shows one such link opened into a finer subgraph of mosquito indoor resting behavior.

**Influence magnitude.** The magnitude of an influence is the amount of resources needed to impose a state change on the target, such as energy, time, information, or matter. The same measure applies to a link at any scale, so a coarse link and the finer links inside it can be described in the same terms. The starting point of this method is my essay [The Zeroth Law of Geography and Geospatial Modeling](../../thoughts/2025-03-19-zeroth-law/), where an entity changes its state according to the magnitude of the force it receives and its own resistance.

## Review, record, and grow

Research outputs would be reviewed by domain experts through a model resembling a combination of Wikipedia + GitHub. Both successful and unsuccessful explorations would be recorded, allowing AI systems and human researchers to examine, verify, and reproduce them. We have presented an initial formulation of this proposal in a paper available on SSRN, and we plan to explore its implementation in future work.

![Fractal Research Graph expansion: stage 1 grounds the research graph in papers, datasets, methods, and observations; stage 2 runs a research loop of check out, work, quality check, and commit](media/projects/fractal-research-graph/graph-expansion-loop.webp)

*Expanding the graph with agent swarms and version control. Agents check out a working subgraph, propose updates to research cells, pass quality checks, and commit accepted updates under human oversight; rejected and set-aside updates are kept as memory.*

Once a unified form of knowledge representation has been established, what should come next?

We plan to explore a unified approach to scientific modeling that would allow AI agents to investigate problems across different domains using a common methodology. The goal is to take full advantage of AI's exceptional capacity for execution and exploration.

By combining the Fractal Research Graph with AI agent swarms, we aim to make scientific research increasingly automated, self-organizing, and decentralized. Ultimately, such a system could become self-growing, rapidly expanding the body of scientific knowledge.

## Related

- Paper: Ning, H., & Huang, X. (2026). [Agent-Hive: A Fractal Research Graph Architecture for Long-Running Scientific Agent Swarms](https://ssrn.com/abstract=7380678). SSRN preprint 7380678.
- Project: [Research Architect](../research-architect/), our AI copilot for framing hypotheses on an influence graph.

*Adapted from my LinkedIn article [What Should Be the Scientific Community's Immediate Priorities in the Age of AGI?](https://www.linkedin.com/pulse/what-should-scientific-communitys-immediate-priorities-huan-ning-zpose/) (September 3, 2026), also on this site under [Thoughts](../../thoughts/2026-09-03-scientific-priorities-agi/).*
