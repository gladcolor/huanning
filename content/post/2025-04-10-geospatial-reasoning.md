---
title: 'Geospatial Reasoning by Google: A Leap Towards Autonomous GIS'
date: '2025-04-10T10:02:53-05:00'
summary: Huan Ning | 04/09/2025 Google Research released a framework named Geospatial Reasoning, which provides a user-friendly
  inference for spatial analysis and visualization. By receiving users’ requests in natural language about geospatial tasks,
  Geospatial Reasoning can choose appropriate data sources and foundation models and then create and execute geoprocessing
  workflows to extr
original: https://gladcolor.wordpress.com/2025/04/10/geospatial-reasoning-by-google-a-leap-towards-autonomous-gis/
wordpress_id: 40
aliases:
- /post/geospatial-reasoning-by-google-a-leap-towards-autonomous-gis/
---

**Huan Ning | 04/09/2025**

Google Research released a framework named [Geospatial Reasoning](https://research.google/blog/geospatial-reasoning-unlocking-insights-with-generative-ai-and-multiple-foundation-models/), which provides a user-friendly inference for spatial analysis and visualization. By receiving users’ requests in natural language about geospatial tasks, Geospatial Reasoning can choose appropriate data sources and foundation models and then create and execute geoprocessing workflows to extract information and insights from data to reply to users’ requests. One application of Geospatial Reasoning is to assess the damaged building for emergency response. This is fantastic work, and many congratulations to the team!

Geospatial Reasoning can be viewed as an autonomous agent for GIS/RS (Geographic Information Systems and Remote Sensing). It reflects the vision of our 2023 paper “[Autonomous GIS: the next-generation AI-powered GIS](https://www.tandfonline.com/doi/full/10.1080/17538947.2023.2278895)“. The core idea of that paper is converting the spatial analysis to a geoprocessing workflow using the reasoning and coding capabilities of generative AI, i.e., dividing the task into small pieces and solving them (divide-and-conquer). A step can be a small function, a tool, a model, or a smaller geoprocessing workflow. Google’s Geospatial Reasoning adopts the strategy of using GIS tools and foundation models as the steps in the geoprocessing workflow.

Recently, in collaboration with other 14 leading GIScience scholars, our team released another paper to further the discussion of autonomous GIS: “[GIScience in the Era of Artificial Intelligence: A Research Agenda Towards Autonomous GIS](https://arxiv.org/abs/2503.23633)“. Besides five autonomous levels (routine-, workflow-, data-, result-, and knowledge-aware), we also proposed three agent scales: local, centralized, and infrastructure. Geospatial Reasoning can be categorized as an earlier stage of **Level 3 data-aware GIS** as it is supposed to be able to use appropriate data for the given task. It is designed as a **centralized GIS agent** because it serves multiple users and runs on computing clusters under centralized management. Agents at this scale can process geospatial big data for analysis.

Since early 2023, we released the [LLM-Geo](https://giscience.psu.edu/llm-geo-an-open-source-autonomous-gis-prototype/) among the first attempts of autonomous GIS agents, we are witnessing more and more GIS agents being researched and developed. We believe that Autonomous GIS is emerging as a new sub-field of GIScience, and our team is collaborating with various domain experts to advance the research of autonomous geospatial agents. The combination of large language models (or more broadly generative AI) and domain knowledge can significantly automate research productivity.
