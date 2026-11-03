---
title: "Introducing Generalized Geography"
date: '2026-11-03T08:45:00-05:00'
summary: "Generalized Geography is a cross-disciplinary framework for representing, composing, computing, explaining, and testing how interacting entities change in space and time. It asks a geographic question in an expanded sense: what exists where and when, how it is configured, what influences pass among its parts, and how these configurations arise, persist, adapt, or disappear."
---

Geography has always asked what is where, and why. I have come to believe this question reaches far beyond the Earth's surface. A watershed, a city's road network, a mosquito population, a cell, and an organization all have parts that sit somewhere, connect in particular ways, push on one another, and change over time. **Generalized Geography** (广义地理学) is my attempt to give these systems one shared language, so that people and AI agents can represent them, compose them from existing scientific models, compute what follows, and test the results against observations.

It starts from a geographic question in an expanded sense: what exists where and when, how it is configured, what influences pass among its parts, what resources make change possible, and how these configurations arise, persist, adapt, or disappear.

## From location to configuration and influence

A useful informal starting point is "moving things". The things moved may be water, vehicles, people, money, energy, control signals, or the use of a capacity. Not every change is literal movement, though. Chemical reactions, gene regulation, learning, and legal authorization also change what entities can do and how they affect one another.

So the organizing ideas are **configuration** and **influence**. Configuration is where the parts are, how they connect, who has access to what, and which constraints apply. A road closure changes reachability; a dam gate changes flow; a command changes permissions. Reconfiguring a system can change its behavior even when its resources stay the same. Influence is how one part changes another part's state, behavior, opportunities, or constraints.

![A computational worldspace: sunlight and gravity drive the water cycle, while a human agent uses channels, a dam and a power plant to change water flow and generate electricity; an inset shows the same system as entities and influences at three connected scales](media/projects/gongjing/gongjing-computational-worldspace.webp)

*Entities, influences, resources, and agents in one system: the water cycle, a watershed, and a hydropower plant. Natural processes and purposeful actions both change influences. From the [Gongjing](../../project/gongjing-computational-worldspace/) project.*

## A small vocabulary

| Concept | Plain-English meaning | Example |
|---|---|---|
| **Entity** | A part of the world with an identity, a boundary, and a state | A water container, a mosquito, a road, a city |
| **Configuration** | Where the parts are, how they connect, and what constraints apply | Which houses store water outdoors |
| **Influence** | How one entity changes another's state or behavior | Rainfall fills containers |
| **Mechanism** | The process that carries an influence | Female mosquitoes lay eggs in standing water |
| **Resource** | A stock or capacity useful for maintaining or changing a system | Water, energy, time, money |
| **Agent** | An entity that chooses actions toward a goal | A person who covers containers |
| **Space and time** | Where and when an influence acts, how far it reaches, and how long it takes | Larvae respond to rain after days, not minutes |

Influences come in different kinds: physical transport, a control signal, a causal effect, a statistical association, or an institutional rule. The framework keeps them typed and never converts one into another silently. A correlation between rainfall and taxi demand is useful for prediction, but it cannot be used to simulate what a policy would do.

## Three principles

**Heterogeneity.** The world contains different kinds of entities, processes, state variables, geometries, and clocks. A graph is a useful way to coordinate them, not a mandate to replace differential equations, detailed simulators, or field data.

**Compositionality.** Established domain models, such as a hydrology model or a traffic simulator, should be reusable modules with explicit inputs, outputs, units, spatial support, time steps, resource accounts, uncertainty, and evidence. The goal is to join disciplines, not to reinvent them.

**Recursive abstraction.** An entity can be treated as one unit or opened into a network of smaller entities. A city can start as aggregate demand and capacity; one district can then open into roads, vehicles, drainage, and control rules. Likewise, an influence A→B can open into the chain of mechanisms that carries it. This is the same fractal idea behind my [Fractal Research Graph](../../project/fractal-research-graph/), now applied to runnable models, where opening and closing must keep quantities, units, and boundaries consistent.

## A world of mechanisms, not merely connections

An arrow on a graph does not explain how a change travels. For computation, each influence should be linked to a mechanism: a process with preconditions, state updates, resource use, uncertainty, and evidence.

![A coarse influence from A to B opens into a chain of mechanisms: A leads to an intermediate state M1, then an intermediate process M2, then B; M1 sets a condition or trigger that acts on M2, and M2 feeds back to M1](media/thoughts/generalized-geography/mechanism-expansion.webp)

*One coarse influence opened into the mechanisms that carry it, including a condition or trigger and a feedback loop.*

For example, human population density does not change mosquito larval density directly. Female mosquitoes need blood meals, and their resting, biting, and egg-laying behavior carries the effect from people to the water bodies where larvae grow. Each step can be studied and modeled on its own, and each step can open again.

Two more ideas run through the framework. The first is **Trigger-Response**: a small signal can start a large action when a receiver, a rule, an actuator, and stored resources are already in place. A relay switching a circuit, a hormone binding to a receptor, a software command launching a process, and an order mobilizing an organization share this structure, though their physics and meaning differ. The signal is not the energy source of the response.

The second is **passive and active persistence**. A rock lasts because it is stable; an animal or an organization lasts because it keeps acquiring and spending resources to maintain itself. Intelligence and greater influence do not automatically mean longer survival, and asking when active adaptation pays off is a research question in itself.

## Two graphs: knowledge and computation

Generalized Geography separates two structures. The **Research Graph** records what we know and how well we know it: theories, causal claims, data, models, tests, the conditions under which each finding holds, and its uncertainty. The **World Graph** is a runnable model of a specific system: entities, their states, and the mechanisms that update them.

The two form a loop. The Research Graph suggests which mechanisms matter. The World Graph computes what follows from them. The results are compared with observations, and the mismatches become new research questions: a missing mechanism, a wrong time window, or a limit on where a finding applies.

![The knowledge-computation loop: a Fractal Research Graph of influences such as rainfall, water containers, and larval productivity is compiled into a computational worldspace of houses, containers, and mosquitoes; mismatches with field observations become new questions; a decentralized agent swarm works on both](media/thoughts/generalized-geography/knowledge-computation-loop.webp)

*The loop between knowledge and computation, shown with mosquito habitat research. AI agents can help propose, build, compare, and document mechanisms, while people review what matters most.*

This is where AI agents fit. They can read the literature, extract influences and their conditions, assemble models from mechanism modules, run interventions, and report what does not match. My essay [What Would Science Look Like with 100,000 AI Agents?](../2026-11-02-science-with-100000-ai-agents/) describes how a decentralized swarm of agents could keep this loop running.

## Where the work stands

The prototypes so far show that the software can scale. A compact engine updated a synthetic graph of 10 million entities and 40 million directed relations at about 1.2 seconds per step on one machine. A synthetic city coupled rainfall, drainage, and commuting through typed interfaces with a closed water balance. Later versions added adapters for professional hydrology and traffic simulators and data pipelines for New York, Chicago, and Philadelphia.

The next milestone is a real-data, cross-domain study: established domain models joined through a common interface, tested on held-out places and periods, and compared with simpler alternatives. Mosquito-borne disease, where my team has a large literature warehouse and field data, is a natural first case, because rainfall, water storage, temperature, urban form, and human behavior all meet in one outcome.

## How it connects

- [The Zeroth Law of Geography and Geospatial Modeling](../2025-03-19-zeroth-law/): distance as the cost to transport force, the starting point for measuring influence.
- [Rethinking GeoAI: No AI? No Geo!](../2026-10-30-no-ai-no-geo/): why richly connected human-environment systems need models built from connections. Generalized Geography keeps mechanisms and evidence alongside learned models.
- [Fractal Research Graph](../../project/fractal-research-graph/): the Research Graph side of the loop.
- [Gongjing](../../project/gongjing-computational-worldspace/): an early computational worldspace with one interface for people and AI.
- [Research Architect](../../project/research-architect/): an AI copilot for framing hypotheses on an influence graph.

Geography's question, what is where and why, turns out to be a question about any system of interacting parts. Generalized Geography is my attempt to make that question computable.
