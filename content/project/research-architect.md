---
title: "Research Architect: An AI Copilot for Human-AI Scientific Inquiry"
date: 2026-10-25T22:35:00-04:00
area: AI for science, human-AI teaming
summary: An AI copilot for human-AI research collaboration that frames grounded, testable hypotheses around a shared influence graph.
image: media/projects/research-architect/cover.webp
tags:
- AI for Science
- Human-AI Teaming
- AI Agents
- Hypothesis Framing
---

Our team is pleased to release Research Architect, an AI copilot for human-AI research collaboration, specifically for hypothesis framing. You are warmly invited to try it at [researcharchitect.ai](https://researcharchitect.ai).

When people and AI agents conduct research together, the hardest part is often not performing the analysis, but thinking clearly before the analysis begins. How should the research question be defined? How can existing literature be used systematically? How can expert knowledge be incorporated? How can the main mechanisms be identified? How should the research scope be determined? How can we avoid losing sight of the forest for the trees? And how can we determine what the available data actually cover?

Research Architect helps AI agents avoid proposing hypotheses blindly or becoming overly confident. It also helps them avoid abandoning valuable research directions too early because of incomplete information.

![A foundation model gives a general understanding of the world, while the real world is specific and detailed; AI needs context knowledge to serve the real world](media/projects/research-architect/context-knowledge.webp)

The product uses an influence graph as its central shared medium. AI first identifies and visualizes the factors and relationships relevant to a research question, then assesses the research scope and data coverage. Users can inspect these factors, conduct literature searches, and revise the influence graph using their domain expertise. Based on the improved graph, Research Architect proposes more grounded and testable hypotheses while showing the mechanisms, evidence, and remaining uncertainties associated with each hypothesis.

Since our team introduced the concept of Autonomous GIS, we have believed that AI agents are becoming important executors of scientific research. Human experts serve as a vital interface between the digital and real worlds. They need better tools to identify meaningful research directions, correct the understanding of AI, and allocate research resources more effectively. Research Architect was designed and implemented in response to this need.

The real challenge in building this tool was not software development. It was reviewing our previous projects, studying the research practices of our colleagues, and turning an experience dependent process of research conception into a general workflow that can be expressed, inspected, and revised. To support this goal, we developed a tri-projection framework that moves from the real world to an influence graph, then to research scope, and finally to data. We also distinguish influence relationships as necessary, driving, or modifying.

![The tri-projection connects the real world to an influence graph, a defined research scope, and available data](media/projects/research-architect/tri-projection.webp)

![The Research Architect interface: graph view in the center, operation panel on the left, chat box at the bottom, and result panel on the right](media/projects/research-architect/interface.webp)

People familiar with systems science and dialectics may recognize some familiar ideas in Research Architect. We also welcome researchers to share their experience and guide AI reasoning in the same way they would mentor a graduate student.

We will soon share several AI for Science studies and continue exploring how to build new research infrastructure for AI agent swarms. We welcome you to try the platform, exchange ideas, collaborate with us, or discuss investment opportunities.

## Tutorial video

There is no doubt that AI and AI agents have been deeply involved in scientific research. The cross-domain knowledge and outstanding coding skills of the frontier AI models are astonishing. However, before conducting solid research, framing a reasonable hypothesis for the research question requires more context and curated data. Research Architect gives users an interface to combine their contextual knowledge and expertise with AI's broad knowledge and skills.

Researchers can explore relationships, examine their supporting explanations, define the study's scope, and check data coverage. They can also give the AI explicit guidance, preserving important mechanisms even when current data cannot measure them.

One of our team members, Prof. Xiao Huang at Emory University, created a nice video tutorial on how to use Research Architect. You are welcome to watch this 3-minute video and try it on [researcharchitect.ai](https://researcharchitect.ai) for free now.

[![Video: Research Architect tutorial, "Better science starts with a better question"](media/projects/research-architect/video-tutorial.webp)](https://www.linkedin.com/pulse/tutorial-video-research-architect-ai-copilot-human-ai-huan-ning-gz2ve/)

*Research Architect tutorial (3 minutes). Click to watch on LinkedIn.*

The video walks through a mosquito ecology example. Knowing that a container holds water is different from knowing how long the water remains. That distinction matters when studying mosquito development. Research Architect makes the missing measurement visible, connects literature to the relevant factor, and helps turn a candidate explanation into a study design involving repeated observations.

Research Architect is our first step in re-engineering scientific inquiry infrastructure for the AI era. We will continue developing Fractal Research Graph and Computational Worldspace to connect research knowledge and support shared modeling:

**One Interface, Anyone. One Graph, Anything. One Model, Anywhere.**

## The mosquito example in Research Architect

![Data coverage projected onto the mosquito influence network: the complete candidate network on the left, and how well the supplied data represent its variables on the right](media/projects/research-architect/data-coverage.webp)

![Scope assessment](media/projects/research-architect/scope-assessment.webp)

*Scope assessment: each factor is in scope, partial, or out of scope for the study period and area.*

![A literature review attached to the link from water-holding duration to larval productivity](media/projects/research-architect/literature-review.webp)

*A literature review attached to the necessary link from water-holding duration to larval productivity.*

![Generated hypotheses with their confidence, the measurement needed to unblock each one, and a study design](media/projects/research-architect/hypotheses.webp)

*Generated hypotheses, each with its confidence, the measurement needed to unblock it, and a study design.*

*First published on LinkedIn: [An AI Copilot for human-AI scientific inquiry: Research Architect](https://www.linkedin.com/pulse/ai-copilot-human-ai-scientific-inquiry-research-architect-huan-ning-rc1ke/) (August 10, 2026) and [Tutorial video for Research Architect](https://www.linkedin.com/pulse/tutorial-video-research-architect-ai-copilot-human-ai-huan-ning-gz2ve/) (September 14, 2026).*
