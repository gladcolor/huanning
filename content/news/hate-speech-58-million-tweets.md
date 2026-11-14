---
title: "New paper: AI-assisted surveillance of hate speech in U.S. cities"
date: '2026-11-14T17:25:00-05:00'
summary: "We used AI to identify racial hate speech from 58 million tweets and conducted a spatiotemporal analysis across U.S. cities. Behind the research: two months of processing on four or five machines with limited computing resources."
tags: [GeoAI, Hate speech, Social media, Big data]
---

Thanks to the leadership and coordination of Siqin (Sisi) Wang at the University of Southern California, and the efforts of our entire research team, Alexander Hohl, Prisha Malik, and Zhenlong Li, we have published a [new study](https://doi.org/10.1016/j.tele.2026.102486) using AI to investigate racial hate speech on social media.

In this study, we used AI to identify racial hate speech from 58 million tweets and conducted a spatiotemporal analysis across U.S. cities.

We found that peaks in online hate speech coincided with major social events, particularly in June 2020, amid the COVID-19 pandemic, the killing of George Floyd, and the Black Lives Matter movement. Our results revealed significant statistical associations between online hate speech and reported hate crimes, with these associations becoming stronger over time for most racial groups. We also observed a one-month lag in anti-Asian hate speech, suggesting delayed public and media responses during the pandemic.

![Line chart of the monthly percentage of hate-related tweets toward African, Asian, Hispanic, and Brown groups in 2018, 2020, and 2022, with the peaks labeled by events such as the June 2020 COVID-19 milestone, George Floyd protests, and Black Lives Matter protests](media/news/hate-speech-58-million-tweets/hate-tweet-peaks.webp)

*Monthly share of hate-related tweets toward African, Asian, Hispanic, and Brown groups in 2018, 2020, and 2022. The peaks line up with major social events. Figure 2 of the paper (CC BY 4.0).*

![Daily percentage of hate-related tweets in each group's peak months, shown as line charts on the left, with U.S. state maps for the same months on the right](media/news/hate-speech-58-million-tweets/hate-tweet-maps.webp)

*Daily share of hate-related tweets in each group's peak months (left) and state maps for the same months (right). Figure 3 of the paper (CC BY 4.0).*

## Behind the research: processing 58 million tweets with limited computing resources

My primary responsibility in this project was classifying the 58 million tweets. This involved organizing a limited number of labeled training samples and supplementing the dataset with additional negative samples.

I handled this massive data-processing task. At the same time, I was juggling several other major responsibilities: preparing my PhD dissertation, searching for jobs, attending interviews, and collaborating with more than a dozen leading scholars on a roadmap paper for the development of Autonomous GIS.

Our research group had two shared workstations, and I had one personal desktop. None of the GPUs were particularly powerful. My advisor had previously purchased an NVIDIA RTX 3090, but it was so large that it wouldn't fit into any of our workstations, so we had never used it.

Given the enormous amount of data, I finally decided to make it work. I had to physically destroy the GPU back panel to squeeze it inside.

To speed things up, I also subscribed to Google Colab and ran two additional processing jobs in parallel.

Large-scale data processing is never as simple as starting a program and walking away.

For roughly two months, I remember spending time every day checking on jobs running across four or five machines.

Each machine came with its own challenges:

- The workstations were shared. Whenever other group members needed computing resources, I sometimes had to pause my jobs to avoid affecting their work.
- One server was located in a conference room and was so noisy that we occasionally had to shut it down during meetings.
- University network and system maintenance required servers to be updated and restarted every few weeks, interrupting long-running tasks.
- Google Colab sessions couldn't run indefinitely and needed frequent monitoring.
- Programs crashed. Bugs had to be fixed. Jobs had to be restarted.
- Sometimes an error in a prompt or data preparation meant that several days of processing had to be discarded and repeated.

And remember, this was early 2025, back in the "old-fashioned" days of coding before AI coding assistants became as capable as they are today. Most of the code was still written manually.

Even after the processing was finished, there was more work: sampling and checking the results in batches, documenting them, compressing files, uploading and sharing datasets.

Data management was another challenge. Datasets needed to be partitioned, tracked, and sometimes reorganized as the workflow evolved. There was no way to keep everything in my head. Without detailed work logs, a few days later I might not even remember which machine held which results or how far a particular job had progressed.

This kind of "dirty work" is tedious and time-consuming, but it has become a familiar part of my research life.

Working with massive datasets requires thinking through many details from the very beginning: data quality and cleaning, workload estimation and reduction, workflow design and testing, code robustness, data storage and sharing, parallel processing across multiple machines and CPU cores, computing resource management, checkpointing and resuming interrupted jobs, and quality control.

It is mentally demanding, but also an excellent learning experience.

Today, AI can automate much of the coding process. However, many other parts of large-scale data processing still require substantial human effort, supervision, and judgment.

I hope future AI systems will take on more of this tedious work, not just writing code, but helping manage and execute entire data-processing workflows.

And, of course, perhaps the most important thing is having enough funding for adequate computing resources in the first place. 😊

Wang, S., Ning, H., Hohl, A., Malik, P., & Li, Z. (2026). Urban intelligence for social cohesion in smart cities: AI-assisted spatiotemporal surveillance of hate speech in the United States. *Telematics and Informatics*, 102486. <https://doi.org/10.1016/j.tele.2026.102486>

*This post first appeared on [LinkedIn](https://www.linkedin.com/pulse/behind-research-processing-58-million-tweets-limited-computing-ning-belve/).*
