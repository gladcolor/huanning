---
title: AI-assisted scientific research
date: '2025-09-11T13:01:39-05:00'
summary: 'Huan Ning | 2025-09-11 Recently, Google released a wonderful paper:  An AI system to help scientists write expert-level
  empirical software ( https://research.google/blog/accelerating-scientific-discovery-with-ai-powered-empirical-software ).
  The authors synthesized the following ideas to enable LLM to write programs for scientific research:  Genetic Programming,
  Generative Prog'
original: https://gladcolor.wordpress.com/2025/09/11/ai-assisted-scientific-research/
wordpress_id: 49
aliases:
- /post/ai-assisted-scientific-research/
---

Huan Ning | 2025-09-11

Recently, Google released a wonderful paper:  An AI system to help scientists write expert-level empirical software (<https://research.google/blog/accelerating-scientific-discovery-with-ai-powered-empirical-software>). The authors synthesized the following ideas to enable LLM to write programs for scientific research:  Genetic Programming, Generative Programming, LLM coding, Automated Machine Learning (AutoML), and agents for scientific discovery.

Simply speaking, let LLM conduct model and parameter search to find out the best-fitting models to the training/testing data. This work proves that AI can help researchers in scientific modeling, although this idea is straightforward and has been tested in various domains. The key point is to use LLM as the decision core to propose hypotheses, conduct experiments, and assess results.

In one of our research team’s papers, GIScience in the Era of Artificial Intelligence: A Research Agenda Towards Autonomous GIS (<https://arxiv.org/abs/2503.23633>), we proposed autonomous geographic modeling, which discussed the possibility of autonomous research in this discipline. We will work on the concept-of-proof project to demonstrate this trend.

![](media/wordpress/ai-assisted-scientific-research/image-cb65d2b2a.png)

*Schematic of the algorithm that feeds a scorable task and research ideas to an LLM, which generates evaluation code in a sandbox. This code is then used in a tree search, where new nodes are created and iteratively improved using the LLM.* (source: <https://research.google/blog/accelerating-scientific-discovery-with-ai-powered-empirical-software>)
