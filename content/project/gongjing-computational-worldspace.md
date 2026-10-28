---
title: "Gongjing 共境: A Shared Computational Worldspace"
date: 2026-10-27T21:35:00-04:00
area: AI for science, computational modeling
summary: An experimental framework that represents how parts of a system influence one another, so that people and scientific AI tools can use the same computer model to test changes and compare outcomes.
image: media/projects/gongjing/gongjing-computational-worldspace.webp
tags:
- AI for Science
- Computational Modeling
- Cellular Automata
- Influence
---

Gongjing (共境) is an experimental framework for representing **how parts of a system influence one another**. Its goal is to help people and scientific AI tools use the same computer model to test changes and compare outcomes. This shared environment, called a **computational worldspace**, holds the parts of a system, their current conditions, their influences, the rules for change, and the observations collected as the model runs.

![Gongjing computational worldspace: sunlight and gravity drive the water cycle, while a human agent uses channels, a dam and a power plant to change water flow and generate electricity. An inset connects the water cycle, watershed and local infrastructure as entities, states and influences.](media/projects/gongjing/gongjing-computational-worldspace.webp)

*Conceptual overview. Natural processes and purposeful actions both change influences within a shared world. The inset represents the same system at three connected scales.*

## The core idea: influence

An **influence** describes how one part of a system can change another part's state or behavior. For example, sunlight warms water, gravity moves water downhill, and a dam changes where water is stored and when it is released.

| Concept | Plain-English meaning | Example in the figure |
|---|---|---|
| **Entity** | A part of the world represented in the model. | Water, a river, a dam or a person. |
| **Influence** | The capacity of one entity to change another. | Solar heating changes water temperature; a gate changes flow. |
| **Resource** | An entity or relationship that is useful for a particular goal. | Stored water and the energy available as it moves to a lower elevation can support electricity generation. |
| **Agent** | An entity with agency: it can observe conditions and choose actions toward a goal. | A person monitors water level, flow and power, then adjusts a gate. |

**Agents can reorganize entities and use resources to change influences.** A channel redirects water, a dam regulates its release, and a turbine makes its energy useful for generating electricity. An agent is therefore a kind of entity; being a resource is a role that depends on the goal and situation.

The figure links the water cycle, a watershed, and a dam and power plant. In the computational view, nodes represent entities and their recorded states, such as water level, gate opening and power output. Arrows represent influences. Connecting these scales lets a model relate local actions to wider changes.

## A watershed as a shared, testable world

The main demonstration is a live 60 × 60 grid model of a watershed. Terrain, water, vegetation and resources are represented as changing entities. Lower ground attracts more flow; water changes plants; plants add flow resistance and reduce erosion. The next step uses the changed ground and plants, so channel paths develop from the starting terrain and the update rules.

![The Gongjing watershed worldspace: blue flow paths across a green landscape, with controls to advance the world, compare influence rules such as full feedback, no erosion and no plants, and read the worldspace measurements](media/projects/gongjing/watershed-worldspace-overview.webp)

*The watershed worldspace. Each condition starts from the same landscape, so differences can be traced to changed rules.*

Visitors can compare six conditions from the same landscape: full feedback, no erosion, no plants, no water damage, stronger smoothing, and more erosion. They can also change selected influence rules, step through the timeline, and save the experiment state.

![The Gongjing worldspace parameters panel: a live worldspace record with the domain adapter, observation scale, grid, step, entity kinds, state fields, observations, candidate path groups and calibration status](media/projects/gongjing/watershed-worldspace-parameters.webp)

*The worldspace record. Gongjing is domain-neutral: the core exposes a common record and intervention interface, and each domain module surfaces its own influence rules through it.*

## One interface for people and AI

The watershed runs on **GongjingCore** and a **WatershedAdapter**. The calculation code is separate from the drawing code, and every control makes an actual call to the core through six commands:

| Command | Plain-English purpose |
|---|---|
| `initialize` | Create a world from a starting number and settings. |
| `step` | Advance the model. |
| `observe` | Read the model's recorded results. |
| `describe` | Inspect its rules and settings. |
| `intervene` | Change a rule or restore a starting state. |
| `coarseGrain` | Summarize candidate patterns across several cells. |

The longer-term aim is that a person clicking a button and a scientific AI tool sending a command use the same interface, so both can explore, compare, and explain the same model. At landscape number 0 and step 280, the live JavaScript model matches the original Python calculation, with the largest field difference below 1e-8 in model units.

## Influence cells and a river

The other demonstrations are cellular automata: grids of small cells that change according to rules. In the influence cell models (v17 and v18.1), colored cells reduce, redirect, amplify, or reflect the influence passing through them, and that influence affects which cells survive or appear.

![Influence cells v17: sources along the top send influence down a grid, where colored cells alter it and form patterns](media/projects/gongjing/influence-cells-v17.webp)

*Influence cells v17. Visitors can pause, step once, and draw new cells on the grid to see how the pattern responds.*

In the related river experiment, water follows a winding river, and small colony cells redirect it. Water can help cells survive, remove them, or support new cells nearby. This repeating loop is feedback.

![A river and its changing banks: blue water flows along a winding river, with small brown colony cells along its path](media/projects/gongjing/river-feedback-world.webp)

*The river and colony experiment, built on the same Gongjing core.*

## Scope

These are simplified, synthetic worlds and early proofs of concept. Influence values in the cell models are abstract quantities, and the watershed has not been calibrated to a real watershed. The demonstrations support exploration of feedback and pattern formation, not forecasting or engineering decisions. No account, installation, or API key is needed: the models run in the browser.

## Related

- Essay: [The Zeroth Law of Geography and Geospatial Modeling](../../thoughts/2025-03-19-zeroth-law/), where an entity changes its state according to the force it receives and its own resistance.
- Project: [Fractal Research Graph](../fractal-research-graph/), which measures influence magnitude across scales.
- Project: [Research Architect](../research-architect/), an AI copilot for framing hypotheses on an influence graph.

**Links:** [Open the demonstrations](https://gladcolor.github.io/Gongjing_computational_worldspace/) · [Watershed worldspace](https://gladcolor.github.io/Gongjing_computational_worldspace/watershed.html) · [Source on GitHub](https://github.com/gladcolor/Gongjing_computational_worldspace)
