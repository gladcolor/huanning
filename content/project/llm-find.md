---
title: 'LLM-Find: A Geospatial Data Retrieval Agent'
date: 2025-01-01
area: AI agents, data discovery
repo_url: https://github.com/gladcolor/LLM-Find
paper_url: https://doi.org/10.1080/17538947.2025.2458688
summary: Natural-language discovery and downloading of geospatial datasets, guided by reusable data source handbooks.
image: media/projects/llm-find/qgis-nigeria.webp
tags:
- Autonomous GIS
- AI Agents
- Geospatial Data
google_sites_source: https://www.huanning.me/projects
---


LLM-Find is an autonomous agent for geo-spatial data retrieval and downloading. It can help to obtain data from your favorite data sources, such as OpenStreetMap. It is very convenient for data scientists who need to collect various data for analyzing tasks. I like this agent very much and will use it for future research on autonomous modeling.

What the user needs to do is type in the request in natural language, and the agent will return the data for you in minutes. For example, if you want to download all coffee shop locations from OpenStreetMap in New York City, all you need to do is input "download all coffee shop locations in New York City", and the agent will download the location points for you. More details can be found [here](https://github.com/gladcolor/LLM-Find?tab=readme-ov-file). 

Below is an example of downloading the boundary and image for Tempe, Arizona, US.

[![Video: GeoData Retrieve Agent (QGIS plugin) downloading data for Tempe, Arizona](media/projects/llm-find/video-tempe.webp)](https://www.youtube.com/watch?v=oVxNnF3CU7o&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1)

*Tempe, Arizona data download demo in the QGIS plugin (3:33). Click to watch on YouTube.*

## How it works

![LLM-Find framework: a data source index and an inventory of handbooks, each with data access entries, data format, key program code, saving method, and example code](media/projects/llm-find/framework.webp)

*LLM-Find framework. Each data source has a handbook that records its metadata and the technical details for data retrieval. Human users or autonomous agents can add a new data source by adding a new handbook.*

The data source handbook anticipated an industry trend. We developed LLM-Find in May 2024; in October 2025, about 1.5 years later, Anthropic announced Claude Skills: modular instruction packages that the agent browses, selects, and loads only when needed, just as LLM-Find selects and loads a handbook. I compare the two designs in [From Data Source Handbooks to Agent Skills](../../thoughts/2026-02-19-agent-skills/).

![LLM-Find agent workflow: select a data source, retrieve its handbook, generate fetching code, and execute it, with a self-debug module that regenerates code on errors](media/projects/llm-find/agent-workflow.webp)

*LLM-Find agent workflow. The agent selects a data source, reads its handbook, and generates, executes, and debugs the data fetching program until the requested data is downloaded.*

## More examples

![The GeoData Retrieve Agent QGIS plugin with cities, rivers, and state boundaries of Nigeria on a satellite basemap](media/projects/llm-find/qgis-nigeria.webp)

*The QGIS plugin of the GeoData Retrieve Agent and the downloaded data of Nigeria: cities (points), rivers (lines), and state boundaries (polygons) from OpenStreetMap, on an ESRI World Imagery basemap. Each layer came from one natural-language request, such as "Download the rivers in Nigeria."*

![LLM-Find downloading a satellite image of the FAST Telescope in Guizhou, China](media/projects/llm-find/fast-telescope.webp)

*The LLM-Find agent downloaded a satellite image of the FAST Telescope from ESRI World Imagery.*

LLM-Find is also released as a QGIS plugin, the GeoData Retrieve Agent: [plugin page](https://plugins.qgis.org/plugins/AutonomousGIS_GeodataRetrieverAgent/) and [source code](https://github.com/Teakinboyewa/AutonomousGIS_GeodataRetrieverAgent).

## Demonstration videos

The full [YouTube playlist](https://www.youtube.com/playlist?list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) from GIBD Lab @ Penn State:

- [Introduction to Autonomous GIS: GeoData Retrieve Agent](https://www.youtube.com/watch?v=1mY_bIK_Y54&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (2:02)
- [Tempe, Arizona data download](https://www.youtube.com/watch?v=oVxNnF3CU7o&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (3:33)
- [Nigeria data download](https://www.youtube.com/watch?v=4otpdHUlpwE&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (6:04)
- [Puerto Rico data download](https://www.youtube.com/watch?v=HzyJBiCRsjM&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (8:45)
- [OpenStreetMap](https://www.youtube.com/watch?v=4yVhVPFjCsw&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (3:16)
- [U.S. administrative boundaries](https://www.youtube.com/watch?v=WZhVv2st6Tw&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (3:44)
- [U.S. Census data](https://www.youtube.com/watch?v=ABhpBw5fkRo&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (3:39)
- [U.S. COVID-19 data](https://www.youtube.com/watch?v=gckLlrk-E9w&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (3:19)
- [OpenTopography elevation data (DEM)](https://www.youtube.com/watch?v=laruNGMzEfo&list=PL6ON3gdLloDE9NynwhMxYNDoFukbNJnf1) (4:16)
