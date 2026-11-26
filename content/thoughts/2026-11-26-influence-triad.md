---
title: "Influence Triad: How Could We See the World with AI?"
date: '2026-11-26T01:10:00-05:00'
summary: "AI agent swarms work around the clock, know every discipline, and code well, so a research system built for people may not fit them. Three designs toward cyberinfrastructure for AI agent swarms, the cases I have tried, and three slogans that sum them up. These ideas are still developing."
---

*These ideas are still developing. They are some ideas I have, not a finished theory, and their names and boundaries will likely change as the work goes on.*

How could we see, and study, the world with AI? Over the past two years, my answer has taken the form of three designs. Their goal is to build **cyberinfrastructure for AI agent swarms** in the coming AI era.

## AI agent swarms are not human researchers

AI agent swarms can work 24 hours a day, 7 days a week. They know something about every discipline, reason well about research problems, and are highly skilled at coding.

Today's research system was built around human limits. A researcher trains in one discipline, reads a small part of the literature, and works limited hours. Knowledge is shared as papers of about 5,000 words, which keep a few successful findings and leave out the failed attempts, and a few reviewers decide what gets published.

For a swarm, reading and coding are no longer the slow parts. The hard parts become choosing questions worth asking, keeping track of what is known and what evidence supports it, checking results against real observations, and letting thousands of results build on each other. The current pattern of research, and the infrastructure behind it, may not fit the AI era.

![Two ways of doing research: built for human researchers, with limited working hours, one discipline, papers of about 5,000 words, and a few reviewers; and AI agent swarms, which work 24/7, know every discipline, reason well, and code well; research patterns and infrastructure need to change](media/thoughts/influence-triad/research-for-swarms.webp)

*A research system built around human limits, and what changes when AI agent swarms join the work.*

## Three designs

- **[Research Architect](../../project/research-architect/)** is a shared place where people and agents frame a question, set the scope, and check what the data can measure.
- **[The Fractal Research Graph](../../project/fractal-research-graph/)** is a shared memory of questions, claims, evidence, and models, stored as research cells that can open into finer detail. Failed attempts are kept, so one agent can pick up where another left off.
- **[The computational worldspace](../../project/gongjing-computational-worldspace/)** is a shared world model. It aims at a universal modeling method, so that agents can run models and test explanations against observations.

New observations return to the graph as new questions, so the three form a loop.

## Where the modeling idea came from

![Three versions of one modeling idea: the raw version, the Zeroth Law, where distance is the cost to transport force; the pre-version, the computational worldspace, a universal modeling method for research; and the current version, Generalized Geography, which starts from geographic sciences and then reaches beyond](media/thoughts/influence-triad/idea-lineage.webp)

**Raw version: the Zeroth Law.** In 2025 I proposed [the Zeroth Law of Geography](../2025-03-19-zeroth-law/): *distance is the cost to transport force.* Force passes along a causal chain and pays a cost, a kind of friction, at each step.

**Pre-version: a computational worldspace.** [Gongjing](../../project/gongjing-computational-worldspace/) (共境) aimed at a universal modeling method for research in any field. Water, traffic, and disease keep their own laws; what is shared is the computational language that describes them. Its demonstrations were synthetic worlds.

**Current version: Generalized Geography.** [Generalized Geography](../2026-11-03-generalized-geography/) (广义地理学) takes a step back. It starts from the geographic sciences, where places, flows, and scales are well studied and real data are rich, and builds a framework of entities, influences, and mechanisms across space and time. Any influence can open into the chain of mechanisms that carries it. From this base, it then reaches outside geography.

## How the three would work together

Take a future study of standing water and mosquitoes. Research Architect helps the team state the place, the season, and what needs explaining. Then the swarm divides the work: one agent gathers rainfall records, another reads studies of mosquito development, a third runs a water model, and a fourth checks the results. Like ants following trails, each agent leaves its work in the graph for the others to pick up. New field observations then go back into the graph.

## The hardest part: a grounded case study

This scenario has not yet been tested from end to end. Building a grounded case study has been the hardest part for me. I have tested many examples with AI, at different scales and with real data:

| Attempt | Scale | Data |
|---|---|---|
| Mosquito larval habitats | About 14,000 research papers | Mosquito research literature |
| Peachtree Creek flood, Atlanta | A 340 km² watershed, 11 stream gauges, and four floods, including Hurricane Helene | Elevation, radar rainfall, soils, land cover, stream gauge records |
| Disasters and daily life | U.S. counties, day by day, from 2017 to early 2026 | Smartphone-based mobility, consumer spending, storms, power outages, weather alerts, flood insurance claims |

Each taught me something. The mosquito graph made missing evidence visible, the flood case opened one influence into several sources, and the disaster tests showed that shared, recorded knowledge helps agents catch hidden data problems. But none is yet a solid case: one where the whole loop leads to a better explanation that others can check.

## Three slogans

I sum up the framework, still at an early stage, with three slogans:

| Design | Slogan | 中文 |
|---|---|---|
| [Research Architect](../../project/research-architect/) | One Interface, Anyone. | 一个界面，人机共研。 |
| [Fractal Research Graph](../../project/fractal-research-graph/) | One Graph, Anything. | 一张图谱，万物可联。 |
| [Computational Worldspace](../../project/gongjing-computational-worldspace/) | One Model, Anywhere. | 一个模型，跨域通用。 |

![Three connected designs: Research Architect, one interface shared by people and AI to frame the question; the Fractal Research Graph, one graph that connects knowledge and evidence; and the computational worldspace, one model to run and test; new observations loop back as new questions](media/thoughts/influence-triad/three-designs-loop.webp)

*Three designs in one loop: frame the question, connect knowledge and evidence, run and test models, then return with new questions.*

"One" means a shared base, not a single tool: one interface that people and agents both use, one graph that keeps even conflicting findings in their own places, and one modeling language that can describe very different systems without forcing them into one equation. "Any" means an open scope: anyone, including AI agents; anything, from any field; and anywhere, meaning across disciplines. That is why the Chinese says "跨域通用" (general across domains) rather than "处处可用" (usable everywhere).

The title uses my earlier name for the framework, the "Influence Triad" (影响三元论). The name is now a bit outdated, because "Triad" counts the parts but does not say what they are for. Influence remains the main theoretical thread.

## Open questions

- **What does "influence" cover?** A process in the world, a measurement of it, and evidence for an explanation are different kinds of arrows. How to connect them is still open.
- **What will people do?** People may spend more of their time choosing questions, judging evidence, and bringing local knowledge that is not written down.
- **Does more AI mean more discovery?** A swarm does not by itself produce better findings. How people and agents divide the work and share failures is a research question in its own right.
- **How should such infrastructure be judged?** By whether it leads to well-grounded explanations and findings that others can build on, not by how many tasks it finishes.

What is your idea? How would you see the world with AI, and what case would you test it on? I would be glad to hear it; feel free to [contact me](../../about/).
