---
title: The Zeroth Law of Geography and Geospatial Modeling
date: '2025-03-19T00:22:25+00:00'
summary: "Geospatial modeling is the process of combining observations and spatial data to investigate the dynamic of phenomena over the Earth, covering physical and societal processes. Such investigations may provide explanations or predictions of phenomena (Crooks et al. 2019)."
original: https://gladcolor.wordpress.com/2025/03/19/the-zeroth-law-of-geography-and-geospatial-modeling/
wordpress_id: 4
aliases:
- /post/the-zeroth-law-of-geography-and-geospatial-modeling/
- /post/2025-03-19-zeroth-law/
---

1. Introduction

Geospatial modeling is the process of combining observations and spatial data to investigate the dynamic of phenomena over the Earth, covering physical and societal processes. Such investigations may provide explanations or predictions of phenomena (Crooks et al. 2019). Various modeling methods have been established, such as physical modeling, statistical modeling, simulation, network analysis, and machine learning. These modeling approaches are mainly based on several geographic principles, including:

1) Toblers’ first law of geography (First Law hereafter): “Everything is related to everything else, but near things are more related than distant things (W. R. Tobler 1970).”  The First Law can be considered as spatial autocorrelation.

2) Harvey’s spatial heterogeneity (Goodchild 2004), or non-stationarity in statistics, referring the uncontrolled variance of geographic variables.

3) Zhu’s third law of geography (Third Law hereafter): the more similar geographic factors of two locations, the more similar the values (processes) of the target variable at these two locations (A. Zhu et al. 2018; A.-X. Zhu and Turner 2022; A.-X. Zhu 2022). Third Law indicates that similar geographic observations imply similar values of other variables. Essentially, this principle is the widely-used nearest neighbor method in machine learning: near entities share similar attributes.

These principles are based on the reality that phenomena change over space. Although geographers mainly refer to space on the Earth surface, they also extend the space concept beyond the geographic metric. Indeed, humans act in the geographic space, but human behaviors are also subject to also various socioeconomic or cultural determinants, such as ideology, historical context, governance, and political preference (W. Tobler 2004). Consequently,  the distance metrics may refer to time cost, ordinal distance, or financial cost (W. Tobler 2004; Goodchild 2004). Relation in the First Law can be interpreted as similarity or mechanical processes (Goodchild 2004).

Nearness, i.e., distance, is the core concept in the abovementioned principles.  To establish a relative universal definition of distance, we propose the **zeroth law of geography**:

**The distance is the cost to transport force (Zeroth Law hereafter).**

Where:

cost: the friction of force.

force: the power imposing changes.

transport: the causal process through which the source force imposes chain reactions from the source entities to the destination entity.

Figure 1 shows a simple path of force transportation via a causality chain. *force*a is sourced from  *Entity*1 , then impose chances on *Entity*3 via the intermedia *Entity*2. Note that the source force, *force*a, will suffer a *cost*a to arrive at *Entity*2, then transforms to *force*b.

![](media/wordpress/the-zeroth-law-of-geography-and-geospatial-modeling/image-d484b42f4.jpg)

Figure1 Forces can be transported between entities while cost (friction) occurs.

 On the other hand, the entity receiving force will change its state according to the magnitude of the force and its resistance. The resistance is the inertia to persist in the current state. Therefore, the future state of an entity is subject to the source forces, the costs along all causal paths, and its current resistance. Such a prospect provides a universal framework for phenomena analysis.

Figure 2 presents a simple causal graph of the individual *income level*. Higher *education attainment* may have a relatively high *income level*, but we cannot ignore that *education attainment* does not directly impose the *income level*; instead, the *education attainment* holders need to win a position in the *job market* to obtain income, while the job market may highly depend on the *local economy*. COVID-19 patient death prediction is another example: a reliable and explanatory spatial model needs to consider the key variables of the causal graph, such as the historical COVID-19 case, healthcare capacity, and vaccination rate.

There are other examples that show the limitation of First Law. Suppose we adopt the First Law on geographical nearness without considering other distances, such as *education attainment* and *local economy*. In that case, the income level of two nearby places may not have a meaningful relation. For instance, California State’s median household income is much higher than its neighbor Nevada State ($95,971 vs. $78,456, 2017 – 2021) in the USA (HDPulse, 2024); similarly, the per capita Gross Domestic Product (GDP) in Guangxi is much lower than its neighbor, Guangdong ($ 7,755 vs. $15,151, 2022) in China. In these two cases, the First Law of geography does not fit the reality at the state/provide level on the relation of income or per capita GDP.

![](media/wordpress/the-zeroth-law-of-geography-and-geospatial-modeling/image-1-07e3303b5.jpg)

Figure 2  The casual graph shows how individual education attainment impacts income.

Overall, when investigating phenomena using spatial modeling, only considering the geographic distance, such as traditional Geographically Weighted Regression (GWR), may not be enough. Many studies applied various factors, such as demographic and socioeconomic determinants, to discover the correlation between dependents and independents; for instance, the relationship between obesity prevalence and Social Determinants of Health (SDOH). Another example is flood modeling, which requires various input data types, such as precipitation, streamflow, soil moisture, and land cover; although these datasets are usually spatial, they are not dependent on geographic distance. Thus, scholars input other observations in various metrics to the vanilla first law. The force of high precipitation breaks down the drainage system and then causes floods; we can carefully select the key variables along with the causal chain to better predict the flood events. In reality, the changes are the results of comminated force from multiple sources, forming a causal graph rather than a chain. Meanwhile, since the force transportation may have time lags, we need to choose the measurements in appropriate retrospective periods. For example, the precipitation at the upstream may need hours to arrive at the downstream, so the prediction of the downstream flood needs to have the precipitation data at the upstream hours ago. Similarly, the newborn population estimation may require the newborn data two decades ago because the number of potential presents is critical.

2. How does Zero**th** Law benefit spatial modeling?

Many traditional spatial modeling approaches, such as regression, adopt a static perspective that records “how the world looks” rather than “how the world works”(Goodchild 2004). Crooks et al. (2019) considered the phenomena’s dynamic nature and used agents for dynamic spatial modeling instead of the static viewpoint, but more focus on reaction from the decision makers, such as individuals, to investigate phenomena. Combining these thoughts and attempts, the Zeroth Law reminds researchers to adopt a holistic, dynamic, and causal view to model the phenomena.

In scientific research, it is challenging to establish a correct causal graph containing all critical variables and causalities. Correlation studies are the alternatives when causal modeling is not feasible. The limitations of these studies include: 1) sometimes it is difficult to find appropriate proxy variables, and 2) the missing causality leads to difficulty of intervention. Thoroughly adopting the Zeroth Law needs to consider the causality, key variables, proxy variables, spatiotemporal lags, and uncertainties. This mindset helps researchers understand the strong points and weaknesses of their studies, increasing the robustness of spatial modeling for complex dynamic systems.

Geographers believe that a place’s state will be influenced by events that occurred in other locations, so that they can make spatiotemporal predictions or explanations (W. Tobler 2004), and they have employed similar ideas on causality (Zou and Cheng 2024; Akbari, Winter, and Tomko 2023). For example, the geographic convergent crossing mapping  (Gao et al. 2023) method has been developed to create causal graphs from multiple spatiotemporal observations. The existing techniques of general causal learning (S. Li and Chu 2023; Liu, Shao, and Chen 2024) can also help create causal graphs for geospatial modeling.

Once the spatial model is created based on the causal graph, that causal graph can be viewed as the basic structure of phenomena; investigating how the forces are transported and their limitations may reveal further insights for the targeted phenomena, such as how to conduct interventions.

3. Artificial general intelligence (AGI) assisted automatic spatial modeling based on Zeroth Law

Since creating the correct causal graph for spatial modeling is challenging, we can use tried-and-error to obtain an approximate result with the help of AGI. We can design autonomous agents to create various possible causal graphs according to the given data, or the agent can gather needed data according to the generated causal graph. Researchers can define modeling templates or guidance for agents to ensure they do not go off the track far away. For example, one template can use the neural network to simulate the cause graph while a neuron or a sub-network represents each entity. Simulation templates can also be pre-defined. An error analysis mechanism needs to be built so that the AGI can select the models that most fit the expected results.

The possible benefit of adopting the causal graph in Zeroth Law is we can form causal sequences then push these squences into sequence-to-sequence models like transformer (Vaswani et al. 2017), widely used in the successful large language models such as GPTs (OpenAI 2023).

Reference:

Akbari, Kamal, Stephan Winter, and Martin Tomko. 2023. “Spatial Causality: A Systematic Review on Spatial Causal Inference.” *Geographical Analysis* 55 (1): 56–89. <https://doi.org/10.1111/gean.12312>.

Crooks, Andrew, Nick Malleson, Ed Manley, and Alison Heppenstall. 2019. *Agent-Based Modelling and Geographical Information Systems: A Practical Primer*. First Edition. Thousand Oaks, CA: SAGE Publications Ltd.

Gao, Bingbo, Jianyu Yang, Ziyue Chen, George Sugihara, Manchun Li, Alfred Stein, Mei-Po Kwan, and Jinfeng Wang. 2023. “Causal Inference from Cross-Sectional Earth System Data with Geographical Convergent Cross Mapping.” *Nature Communications* 14 (1): 5875. <https://doi.org/10.1038/s41467-023-41619-6>.

Goodchild, Michael F. 2004. “The Validity and Usefulness of Laws in Geographic Information Science and Geography.” *Annals of the Association of American Geographers* 94 (2): 300–303. <https://doi.org/10.1111/j.1467-8306.2004.09402008.x>.

HDPulse: 2024. “Income Map for US by State | HDPulse Data Portal.” 2024. <https://hdpulse.nimhd.nih.gov/data-portal/social/map?race=00&race_options=race_7&sex=0&sex_options=sexboth_1&age=001&age_options=ageall_1&statefips_options=area_states&demo=00010&demo_options=income_3&socialtopic=030&socialtopic_options=social_6&statefips=00>.

Li, Sheng, and Zhixuan Chu, eds. 2023. *Machine Learning for Causal Inference*. Cham: Springer International Publishing. <https://doi.org/10.1007/978-3-031-35051-1>.

Liu, Xiaolu, Qi Shao, and Duxin Chen. 2024. “Long-Term Prediction on Graph Data with Causal Network Construction.” *IEEE Transactions on Artificial Intelligence*, 1–11. <https://doi.org/10.1109/TAI.2024.3351105>.

OpenAI. 2023. “GPT-4 Technical Report.” arXiv. <https://doi.org/10.48550/arXiv.2303.08774>.

Tobler, W. R. 1970. “A Computer Movie Simulating Urban Growth in the Detroit Region.” *Economic Geography* 46 (June): 234. <https://doi.org/10.2307/143141>.

Tobler, Waldo. 2004. “On the First Law of Geography: A Reply.” *Annals of the Association of American Geographers* 94 (2): 304–10. <https://doi.org/10.1111/j.1467-8306.2004.09402009.x>.

Zhu, A-Xing. 2022. “On the Third Law of Geography.” In *New Thinking in GIScience*, edited by Bin Li, Xun Shi, A-Xing Zhu, Cuizhen Wang, and Hui Lin, 85–94. Singapore: Springer Nature. <https://doi.org/10.1007/978-981-19-3816-0_10>.

Zhu, A‐Xing, Guonian Lu, Jing Liu, Cheng‐Zhi Qin, and Chenghu Zhou. 2018. “Spatial Prediction Based on Third Law of Geography.” *Annals of GIS* 24 (4): 225–40. <https://doi.org/10.1080/19475683.2018.1534890>.

Zhu, A-Xing, and Matthew Turner. 2022. “How Is the Third Law of Geography Different?” *Annals of GIS* 28 (1): 57–67. <https://doi.org/10.1080/19475683.2022.2026467>.

Zou, Zhixiao, and Changxiu Cheng. 2024. “A Review of Causal Analysis Methods in Geographic Research.” *Environmental Modelling & Software* 172 (January): 105929. <https://doi.org/10.1016/j.envsoft.2023.105929>.
