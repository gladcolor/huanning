---
title: AI-Generated Synthetic Users for Software Testing
date: 2026-10-25T16:26:12-04:00
area: AI agents, synthetic data
summary: Fictional users, each with a simulated year of life, for testing the memory system of an AI companion without using private conversations.
image: media/linkedin/synthetic-users/synthetic-users-cover.webp
tags:
- AI Agents
- AI Memory
- Synthetic Data
- Software Testing
---

Recently, I have been exploring memory systems for AI companions. One particularly interesting goal is to build a user's digital twin from their conversation history, including their personal profile, social relationships, cognitive patterns, and behavioral preferences.

Interestingly, this challenge has a lot in common with scientific research. In both cases, we try to infer underlying mechanisms from incomplete observations. What we observe is often the result of multiple interacting factors, many of which are hidden. The challenge is to use prior knowledge, theories, and available evidence to reconstruct a plausible representation of reality.

## Ideas from sociology and psychology

1. **Socioeconomic status and demographics.** Occupation, income, education, age, gender, and other socioeconomic characteristics provide a foundation for understanding an individual's life circumstances.
2. **The iceberg model: what people say versus what remains hidden.** Conversations reveal only a fraction of someone's thoughts, emotions, and experiences. People may have things they want to say but cannot express, things they do not want to disclose, or feelings they have not fully recognized themselves. Their perspectives may also be shaped by cultural, geographical, and social environments in ways they are not consciously aware of.
3. **Maslow's hierarchy of needs.** Human behavior is influenced by different levels of needs, from physiological security and belonging to esteem and self-actualization. These needs change over time and help explain why the same individual may respond differently under different circumstances.
4. **Personality traits and cognitive patterns.** People differ in how they think, make decisions, communicate, establish relationships, and prioritize values. These relatively stable characteristics can help make simulated behavior more coherent over time.

## From human understanding to synthetic data

There is a practical challenge when developing such a system: how can we test a model of human memory without accessing real users' private conversations? We do not yet have real user conversation histories for testing. Even if we did, privacy and ethical considerations would significantly constrain how they could be used. Our solution is to generate synthetic users and synthetic conversation histories using AI.

One interesting reference is [SocioVerse](https://arxiv.org/abs/2504.10157), developed by researchers including a team from Fudan University. The framework uses a pool of approximately 10 million real-world social media users to support large-scale social simulations, including an economic survey experiment with 16,000 simulated agents.

Inspired by this work, we use population-level information and established social science theories to create fictional individuals with plausible personal histories. Rather than generating isolated conversations, we ask AI to construct an entire year of simulated life experiences for each synthetic user. The process is similar to how screenwriters develop detailed character biographies before producing a film. Each fictional person has a background, personality, family and social relationships, life goals, daily activities, important events, and evolving circumstances. From these simulated lives, we generate realistic conversation histories that reflect what users might share with an AI companion over time.

![Five steps from seed data to automated testing: seed data, theory-informed modeling, synthetic digital twins, simulated life histories, and automated testing](media/linkedin/synthetic-users/synthetic-users-workflow.webp)

## Turning synthetic lives into software tests

These synthetic users provide a valuable foundation for automated testing. We can use them for both:

- **White-box testing** evaluates whether the memory system correctly extracts, updates, organizes, and retrieves information based on the known simulated history.
- **Black-box testing** evaluates how the AI companion responds to natural conversations, changing personal circumstances, incomplete information, and long-term contextual questions.

For example, can the memory system distinguish between a temporary emotional state and a persistent personality trait? Can it recognize when a relationship or life circumstance changes? Can it avoid treating an AI-generated inference as an established fact? Because the underlying simulated life history is known, we can systematically compare the system's memory against a predefined reference.

Synthetic data cannot fully reproduce real human complexity, and it does not eliminate the need for eventual validation with appropriately consented real users. However, it allows us to conduct large-scale, repeatable testing before involving real people.

The broader insight is that AI can help us not only build intelligent software, but also create complex and realistic environments for testing that software. By combining generative AI, social science, and automated evaluation, we hope to improve the reliability, consistency, and long-term performance of AI memory systems.

Related post: [How to build a memory system for an AI agent?](../../post/ai-agent-memory-system/)

*First published on [LinkedIn](https://www.linkedin.com/pulse/ai-generated-synthetic-users-software-testing-simulating-huan-ning-p9sde/) on October 25, 2026.*
