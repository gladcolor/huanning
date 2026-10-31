---
title: "No AI? No Geo!"
date: '2026-10-30T23:25:00-04:00'
summary: "Over the past decade or so, GeoAI has spread across geographic information science. Why? Not because AI is hot, but because Geo and AI are naturally alike: both are webs of complex, nonlinear connections."
---

![A globe whose cities, shipping routes, and rivers are linked by glowing arcs that lift off the surface and straighten into the layers of a neural network](media/thoughts/no-ai-no-geo/cover-globe.webp)

Over the past decade or so, GeoAI has spread across geographic information science. You could say: no AI? no Geo! Why? Not because AI is hot and everything must have AI in it now. The reason lies in the nature of things: Geo and AI are naturally alike. The geographic sciences study human-environment interaction. AI builds input-output relationships. By AI, I mainly mean artificial neural networks and related technologies, such as large language models. In essence, they use complex, nonlinear algorithms to model the inputs and outputs of the real world. Human-environment interaction is also complex and nonlinear. So artificial neural networks may well become a foundation for modeling and studying it.

## More and more connections

![A quiet village and farmland growing into a dense web of cities, factories, ports, and global routes, with a drought-stricken field linked to a grain ship and a distant market](media/thoughts/no-ai-no-geo/connections.webp)

Geography studies the relationship between people and their environment. In the past, human activities had a limited reach. What happened in a place was shaped mainly by a few nearby factors, and life and production moved at a slower pace. A few variables and one clear formula could often explain a phenomenon.

Today is different. Our power to develop land, move resources, and change the environment keeps growing, and the population has grown enormously. The human-environment system now has more and more connections, and they reach farther and farther. A war can push up prices thousands of miles away through the energy trade. A single online message can change how people move around a city within hours. Social media and generative AI turn everyone into a producer and spreader of information. These connections are intertwined, full of feedback and nonlinearity: A affects B, and B affects A in return; the size of an effect is not a simple proportion; and the feedback keeps getting faster. From a systems science view, once there are this many connections, a phenomenon is no longer the sum of a few factors. We can write down parts of the mechanism, but it is hard to capture the whole with one simple, clear model.

## More and more data

![Satellites, drones, sensors, street view cars, and people with smartphones sending streams of images, messages, and trajectories into a neural network](media/thoughts/no-ai-no-geo/data.webp)

The problems have become harder, but we also have far more observations. Satellites, drones, and ground sensors watch the Earth nonstop, and some satellite fleets image the whole planet every day. On the internet, massive amounts of phone locations, photos, and text are produced every day. The inputs available to a model have grown from a few variables to thousands.

These data are not only large but mostly unstructured: raw pixels, text, and trajectories, not tidy tables. In the past, we first designed features by hand, such as computing a vegetation index from imagery, and then fed them into a model. With this much data, in this many forms, manual work cannot keep up. More importantly, many of these data record the connections themselves: phone locations record people moving between places, and social media records information spreading between people. Neural networks can learn directly from such raw data. Add the computing power of GPUs and cloud computing, and data, computing power, and algorithms have finally come together.

## Connections to match connections

![Two transparent boxes with identical inputs and outputs: one holds a human-environment system tangled with connections, the other a neural network](media/thoughts/no-ai-no-geo/black-boxes.webp)

A model must be at least as complex as the system it describes. A model with a few parameters cannot hold thousands of interacting connections.

A neural network is itself a web of weighted connections, often with millions or even billions of parameters, and in theory it can approximate any nonlinear relationship. Even more important, these connections can be learned from massive data. The human-environment system is a web of influences with many inputs, nonlinear effects, and complex connections. A neural network is a web too. It meets connections with connections, and complexity with complexity. It is a bit like using one black box to replicate another: we cannot spell out every connection inside the system, nor every parameter inside the network, but the network can learn the relationship between the system's inputs and outputs. Its explainability may be poor, but being able to predict beats being unable to.

## AI starts doing the work

![An AI assistant made of network nodes working at four screens to find data, write code, draw a map, and check the result, while a researcher sets the question and reviews the map](media/thoughts/no-ai-no-geo/ai-agent.webp)

Over the past ten years, AI has mainly done two things in geography: recognizing information in data, such as finding buildings in imagery, and making predictions, such as forecasting air quality. Large language models take AI a step further. They are neural networks too, but they learn from the vast amount of text and code that humans have written. What they learn is not only how the world works but also how humans solve problems: how to read documentation, how to write programs, and how to break a task into steps.

So AI has started to find data, write code, run analyses, make maps, and check whether the results are right, all on its own. In 2023, Dr. Zhenlong Li and I proposed Autonomous GIS with exactly this in mind: the user only needs to ask a question, and AI agents plan and carry out the rest. The idea has already moved from papers into policy. The U.S. Federal Geographic Data Committee (FGDC) has written the goals of self-generating, self-organizing, self-verifying, and self-executing into its 2026–2027 plan for modernizing the spatial data infrastructure. In other words, even the data infrastructure itself must be redesigned for AI.

The human role changes too: from an operator clicking buttons to a manager and decision-maker who asks questions and makes judgments. Knowing how to operate software matters less. Asking good questions and spotting what is wrong in a result matter more. AI also gives old data new value. More than a decade of historical street view imagery can become a growth record for every street tree. Google's 3D city models can become pre-disaster images that help drones assess damage. None of these data were collected for these purposes; AI put them to new use.

## The cost of the black box

![A researcher with a magnifying glass at an opened black box, where one connection unfolds into a chain: rain, river, standing water, mosquito larvae, mosquito, and a person](media/thoughts/no-ai-no-geo/open-black-box.webp)

Replicating one black box with another does come at a cost in explainability. Science wants to know not only "what will happen" but also "why." Decision-makers need reasons too. A model that cannot explain itself, however accurate, is hard to trust, because we cannot tell when it will be wrong, and when it is wrong, we do not know where to fix it.

This is exactly where the geographic sciences should push hardest. On one hand, we should combine known mechanisms with data, letting physical and social laws constrain the model instead of letting it search the data blindly. On the other hand, we should reopen the "connections" a neural network has learned: unfold one connection into a chain of mechanisms, and keep asking, layer by layer, until it can be explained.

We should also remember that neural networks are not a cure-all. When data are scarce, or when the question is about causes and policies, traditional mechanistic and statistical models remain irreplaceable. When the dominant factors are stable and the environment changes slowly, a simple model may be enough. The three-body problem, for example, is chaotic in theory, yet the motions of the bodies in our solar system are stable enough on human time scales to be predicted precisely. Geography also has a problem of its own: places differ. A model trained in one place may fail in another, and last year's model may not work this year. Clearly, neither AI nor AI experts alone can solve these problems.

## Closing

Connections within the human-environment system keep multiplying, and observations keep pouring in. Neural networks meet connections with connections. Since large language models arrived, AI has grown from a tool into an assistant that can do the work itself. So "No AI? No Geo!" (No Geo Without AI) is not a slogan; it is already reality, just as there is no GIS without computers.
