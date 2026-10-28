---
title: "What Role Does AI Play in Geospatial Science?"
date: '2026-10-27T23:20:00-04:00'
summary: "Before generative AI, AI played three roles in geospatial science: filter (information extractor), spatial model, and autonomous agent. Large pre-trained generative AI plays four roles, defined by how the information volume changes from input to output: purifier, converter, generator, and reasoner."
---

When we use AI in geospatial research, what role is it playing, and where does the information in its output come from?

## Three roles of AI in GeoAI

AI was widely used in geospatial science long before generative AI arrived. In GeoAI, it plays three roles:

1. **Filter.** AI works like an information extractor: it distills the information we need from massive data, such as identifying suicide-related tweets or marking buildings in remote sensing images.
2. **Spatial model.** AI absorbs spatiotemporal information to model geographic dynamics and make predictions.
3. **Autonomous agent.** AI conducts intelligent tasks without human intervention. [Autonomous GIS](https://doi.org/10.1080/17538947.2023.2278895) is one example: an AI-powered GIS that collects, analyzes, and maps spatial data on its own.

![Three roles of AI in GeoAI with examples: AI as information extractors (water depth from flood photos, sidewalks from street view images, suicide-related tweets), AI as spatial models (PM2.5 prediction, land cover maps, traffic noise), and AI as GIS agents (spatial analysis, data retrieval, and cartography agents as building blocks of autonomous GIS)](media/thoughts/gai-roles/geoai-three-roles.webp)

*Three roles of AI in GeoAI, with examples from our work: extracting water depth from flood photos and sidewalks from street view images, modeling land cover and PM2.5 air quality, and building GIS agents for autonomous GIS.*

## Four roles of generative AI

Large pre-trained generative AI (GAI) brings many more applications. Some models embed data, and some generate new data such as images. Some are specialized for a single task, such as image segmentation, while others, such as GPT-4, are general. To understand these applications, we need a framework for the roles GAI plays. A good framework should cover today's models and remain compatible with future ones, which may be beyond our current imagination. It is both an axis on which researchers can locate their work and a guide for finding possible improvements.

We proposed four roles, according to the **information gain** between a model's output and its input: **purifier, converter, generator, and reasoner**. Here, information gain has its literal meaning, how the information volume changes, not the technical term used in decision trees.

![The four roles of generative AI in geospatial science from the information gain perspective: a purifier outputs less information than its input, a converter keeps about the same amount in a new form, a generator outputs more than its input, and a reasoner outputs structured thoughts](media/thoughts/gai-roles/gai-four-roles-information-gain.webp)

*The four roles of generative AI from the information gain perspective. The size of the blue area indicates the information volume. From Wang et al. (2024).*

The key rule follows from the figure. The information we expect in the output must come from one of two sources: the **input data** or the **training data**. If neither provides it, GAI may generate unreliable results.

### Purifier: less information out than in

A purifier returns only the information of interest, such as extracting location descriptions from flood-related tweets. Most classification and clustering tasks are purification. The output is a part of the input, and the original cannot be restored: once a tweet is tagged "flood relevant," its details are gone. Likewise, place names extracted by GPT are a part of the input text. To use a purifier well, amplify the characteristics of interest in the input; feature engineering may be a critical step. Asking GPT for the coordinates of a city with no input data is also purification: the "input" is the training data the model has absorbed.

### Converter: the same information in a new form

A converter changes the format, form, or modality of the input while keeping most of its information, at least the aspect we care about. Examples include transcribing interview audio, converting satellite images into land cover maps, and writing detailed captions for street view images. Since these are transformations between representation spaces, practitioners should pay close attention to data embedding and representation.

### Generator: more information out than in

A generator creates new data from little input, such as creative writing, code, or an image from a prompt. Data augmentation and 3D reconstruction from a single image are geospatial examples. Because the only source of the extra information is the training data, the output depends on the model's capability and on the variety, quality, and volume of its training data.

### Reasoner: thoughts and the reasons behind them

The most exciting progress is that GAI can reason like humans and explain its reasoning in natural language. We use "reason" in a pragmatic sense: the output follows human language, cognition, and logic so closely that it is nearly indistinguishable from human thinking.

Flood depth estimation from onsite photos shows the difference between roles. If the model says, "The flood reaches the adult man's knee, so I estimate the depth is about 0.5 meters," it plays a reasoner. If it only outputs "0.5," it plays a purifier, and an end-to-end model trained on many flood photos could do the same job. As a reasoner, a pre-trained multimodal model can be an explainable, universal method for estimating flood depth, without separate training data and algorithms for each submerged object, such as vehicles, people, bikes, and stop signs.

In 2020, Janowicz and colleagues proposed a moonshot: an artificial GIS analyst that passes a domain-specific Turing Test by 2030. With GAI as a reasoner, we might reach it years early. Autonomous GIS, GeoGPT, and MapGPT were early attempts to use GPT as the reasoning core that analyzes spatial data, provides solutions, and makes decisions. A reasoner's output usually holds less information than its input, but the information volume matters less than the thoughts and the reasons for them. Since users can rarely fine-tune a model's reasoning ability, they need to give it the necessary and sufficient information in the input.

## Trace the information back

The framework identifies the role GAI plays, not the type of model. Its main lesson for researchers is to trace back the expected information in every output to the input data or the training data. Examples in a prompt (few-shot examples) count as input data, because they supply information rather than change the model's weights.

The framework covers most of the studies we reviewed. The exception is GAI used as a numerical model, such as ranking population or detecting abnormal trajectories. These attempts gave the models too little information to produce accurate numbers. GAI may be a compressed representation of its training data and is weak at numerical processing: geometries encoded by GPT-2 and BERT, for example, could not be decoded back into accurate areas, centroids, or distances. A promising workaround is to turn a numeric problem into a sequence problem, as one study did by encoding daily trajectories as grid cells and time slots written in characters, then training GPT-2 to predict them.

Roles can also be chained. In one study, BLIP-2 captioned street view images, acting as a purifier that extracted lighting, lane number, and road surface, and GPT-3.5 then acted as a second purifier that assigned road tags from those captions. Overall, GAI performs purification, conversion, generation, and reasoning better than numerical analysis. Users who can trace the source of each piece of output information will be better at coordinating several models to finish complex tasks.

Since 2024, the reasoner role has become the core of autonomous GIS agents, such as [LLM-Find](../../project/llm-find/) and GIS Copilot, and autonomous GIS now has its own [entry in the Encyclopedia of GIS](../../news/encyclopedia-autonomous-gis/).

This essay revises Section 3.2, "The diverse roles that large pre-trained GAI plays," of our 2024 systematic review of GPT, large language models, and other generative AI (GAI) models in geospatial science ([Wang et al. 2024](https://doi.org/10.1080/17538947.2024.2353122)).
