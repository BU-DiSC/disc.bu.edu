---
title: LSM-Tree Under (Memory) Pressure
date: 2022-09-06 01:17:00 +0000
tags:
- ADMS Workshop
venue: Proceedings of the International Workshop on Accelerating Data Management Systems Using Modern Processor and Storage Architectures (ADMS), 2022
authors: Ju Hyoung Mun, Zichen Zhu, Aneesh Raman, Manos Athanassoulis
links:
- label: Official PDF
  url: https://www.adms-conf.org/2022-camera-ready/ADMS22_mun.pdf
- label: Local PDF
  url: http://cs-people.bu.edu/mathan/publications/adms22-mun.pdf
- label: Presentation Video
  url: https://www.youtube.com/watch?v=DtvKxqxNiEY
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/adms22-mun.pdf
order: 44
permalink: /papers/adms22-mun
---

# Abstract

Log-structured merge trees (LSM-trees) are widely used in modern key-value stores since they offer efficient data ingestion. To accel- erate point lookups, LSM-trees employ filters such as Bloom filters (BFs) to reduce unnecessary storage accesses to levels that do not contain the desired key. BFs are particularly beneficial for empty queries while they might be a small burden for non-empty queries. Further, with larger datasets, the size of metadata like index and filters also increases, making it less feasible to keep all BFs in cache. Coupling this, with the increasing price of memory and the need to reduce the memory-to-data ratio in many practical deployments, we are seeing an increased memory pressure. In this setting, fewer BF blocks are cached, thus causing additional storage accesses, since they have to be fetched in memory to answer a query.

In this paper, we introduce SHaMBa, a new LSM-based key-value engine that addresses the suboptimal performance when BFs do not fit in memory. SHaMBa integrates a new variation of BF, called Modular Bloom filters (MBFs) that replace a single Bloom filter with a set of mini-BFs (modules) having the same aggregate size and requiring the same total number of probes, distributed among the modules. Querying MBFs accesses the modules sequentially, resulting in the first module being more frequently in memory while the remaining modules compete with data blocks in case of positive queries. Further, we propose a new memory management policy and two BF-skipping strategies to avoid accessing BFs when they are ineffective. Our evaluation shows that SHaMBa substantially outperforms the state of the art under memory pressure, having the same average number of I/Os, needing only one-third of the memory consumed by the state of the art.
