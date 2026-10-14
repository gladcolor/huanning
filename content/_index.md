---
title: ""
date: 2026-10-13
type: landing
design:
  spacing: "4rem"
sections:
  - block: markdown
    content:
      title: "Huan Ning"
      subtitle: "Geospatial AI · Autonomous GIS · AI for Science"
      text: |-
        I am a computational data scientist studying geospatial AI, intelligent agents, spatial data science, and scientific discovery.

        This site brings together my research projects, publications, news, technical articles, and reflections.

        [Research projects](./projects/) · [Publications](./publication/) · [About me](./about/)
    design:
      columns: "1"
  - block: collection
    id: news
    content:
      title: "Latest News"
      page_type: news
      count: 5
      filters:
        folders:
          - news
    design:
      view: date-title-summary
      columns: 1
  - block: collection
    content:
      title: "Featured Research Projects"
      page_type: project
      count: 6
      filters:
        folders:
          - project
    design:
      view: article-grid
      columns: 3
  - block: collection
    content:
      title: "Research Articles"
      page_type: articles
      count: 4
      filters:
        folders:
          - articles
    design:
      view: date-title-summary
      columns: 1
  - block: collection
    content:
      title: "From the Blog"
      page_type: post
      count: 4
      filters:
        folders:
          - post
    design:
      view: date-title-summary
      columns: 1
  - block: collection
    content:
      title: "Selected Publications"
      page_type: publication
      count: 4
      filters:
        folders:
          - publication
    design:
      view: citation
---
