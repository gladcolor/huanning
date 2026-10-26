---
title: "A Coding Agent for Computer-Vision Algorithm Development: Removing the Jello Effect from Drone Images"
date: 2026-10-25T23:33:00-04:00
area: Computer vision, drones, human-AI teaming
summary: Correcting rolling-shutter "jello" distortion in drone images with an AI coding agent, and lessons on where the agent helps and where it still needs a human driver.
image: media/projects/jello-correction/cover.webp
tags:
- Computer Vision
- Drones
- AI Agents
- Human-AI Teaming
---

Recently I had to solve an urgent problem: the "jello" effect, the wavy edges, in a batch of drone images.

The cause is a familiar one. The RGB camera uses a rolling shutter, so it reads the image out one row at a time from top to bottom. When the drone vibrates, the camera is pointing in a slightly different direction as each row is captured, so the rows end up shifted sideways relative to one another. Straight edges come out wavy. That is the jello.

![Before and after: a drone image of a house roof with wavy, jello-distorted edges, and the same image after correction](media/projects/jello-correction/roof-before-after.webp)

I honestly did not know whether the problem could be fixed, but I wanted to give the most advanced AI model, Claude Fable 5, a try. It produced a first attempt in 20 minutes. Out of a couple of test images, exactly one looked corrected and the others failed. Still, one success told me there might be a path, so I kept pushing. With the strong support of the research group, after two days we had a plausible workflow, and after a few more days digging into the theory and verifying the results, we had something real. The correction is not perfect, but a large part of the waviness can be removed, enough that the drone images become usable for building an orthomosaic.

To be honest, a task like this draws on a huge range of knowledge: drone photogrammetry, camera and lens geometry, computer vision, signal processing, image matching, remote sensing, neural networks, and software engineering. Without AI, it would have taken me at least a month, and I probably would never have started such a risky project, because I was not sure it could be done at all.

Here are the lessons on human-AI collaboration I took from it.

## What worked well

1. **Framing the problem.** The model's broad knowledge, plus web search, made it easy to build an analytical framework quickly. It located the culprit right away, rolling shutter combined with vibration, and built a prototype around that diagnosis.
2. **Doing the tedious coding.** Pixel-level image processing is slow and painstaking to write by hand. The AI produced it fast.

## Where it struggled

1. **It cannot really see pixels.** State-of-the-art models still have trouble with the parts of computer-vision development that need close pixel-level observation and careful parameter tuning, simply because they do not perceive image pixels in a meaningful way. In my case, the model computed numerical indicators to judge its own results, but the indicators were not valid for the problem, so the whole workflow was fragile and there was no reliable feedback loop for debugging. It also struggled to draw conclusions from the results: what does a failure mean, why did it happen, and how should we fix it? This maps onto one of the levels in my earlier "autonomous GIS" framework: being result-aware. You need not only a working feedback loop, but a deep understanding of why things succeed and fail.

![The five levels of autonomous GIS, from manual to knowledge-aware; level 4 is result-aware](media/projects/jello-correction/autonomous-gis-levels.webp)

2. **It cannot hold images in memory.** This project involved thousands of images. A human developer keeps the big picture and countless local details in mind at once, and can flip through thousands of raw and processed images quickly to spot the suspicious ones worth a closer look. Fable 5 can only crop and view a handful per round. That opportunistic, partial view led to many mistakes and wasted both time and tokens.

## Suggestions

1. **Know more than the AI, or you may be misled.** This is especially true for exploratory projects with no existing solution. If you cannot judge the implementation and the results, a confident but wrong answer can send you down the wrong road. Pushing the model harder without your own guidance and insight mostly wastes time and tokens.
2. **Have the AI build your analysis tools and educational apps.** Ask it to make small interactive tools and explanatory HTML apps. These let you and the AI dig into the research question far more deeply than prompting alone.

![Jello Inspector, an interactive web tool built by the AI coding agent: synchronized RGB and multispectral band images, their edge maps, and a profile chart along a movable scan line](media/projects/jello-correction/jello-inspector.webp)

*Jello Inspector, an interactive tool the AI coding agent built for tuning the correction. The top row shows the RGB image and four multispectral bands, the second row their edge maps, and the chart profiles all five channels along a movable scan line: aligned peaks mark the same edge, and horizontal offsets reveal the distortion.*

AI has genuinely changed how scientific inquiry works. The analytical work can now move much faster, which means the bottleneck shifts to the human expert. To keep up with that shift, we need to build better research infrastructure around it, which is my current research interest.

## Before and after

![Before and after: wavy wall edges in a raw drone image, and the corrected image](media/projects/jello-correction/walls-before-after.webp)

![Before and after, close-up: wall edges that wave from side to side in the raw image are straight after correction](media/projects/jello-correction/walls-closeup-before-after.webp)

![Before and after: a narrow alley between roofs, with wavy edges in the raw image and straight edges after correction](media/projects/jello-correction/alley-before-after.webp)

*First published on [LinkedIn](https://www.linkedin.com/pulse/coding-agent-computer-vision-algorithm-development-wonderful-ning-l1nie/) on July 12, 2026.*
