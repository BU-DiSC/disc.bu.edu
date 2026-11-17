---
title: 'Endure: A Robust Tuning Paradigm for LSM Trees Under Workload Uncertainty'
date: 2022-05-21 01:17:13 +0000
tags:
- PVLDB
venue: Proceedings of the VLDB Endowment, Vol. 15(8), 2022
authors: Andy Huynh, Harshal Chaudhari, Evimaria Terzi, Manos Athanassoulis
links:
- label: Official PDF
  url: http://vldb.org/pvldb/vol15/p1605-huynh.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/vldb22-huynh.pdf
- label: Presentation Video
  url: https://www.youtube.com/watch?v=RsatTbzOZuI
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/vldb2022-endure-slides.pdf
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/vldb2022-endure-poster.pdf
order: 41
permalink: /papers/vldb22-huynh
---

# Abstract

Log-Structured Merge trees (LSM trees) are increasingly used as the storage engines behind several data systems, frequently deployed in the cloud. Similar to other database architectures, LSM trees consider information about the expected workload (e.g., reads vs. writes, point vs. range queries) to optimize their performance via tuning. However, operating in a shared infrastructure like the cloud comes with workload uncertainty due to the fast-evolving nature of modern applications. Systems with static tuning discount the variability of such hybrid workloads and hence provide an inconsistent and overall suboptimal performance.

To address this problem, we introduce Endure - a new paradigm for tuning LSM trees in the presence of workload uncertainty. Specifically, we focus on the impact of the choice of compaction policies, size ratio, and memory allocation on the overall performance. Endure considers a robust formulation of the throughput maximization problem and recommends a tuning that maximizes the worst-case throughput over the neighborhood of each expected workload. Additionally, an uncertainty tuning parameter controls the size of this neighborhood, thereby allowing the output tunings to be conservative or optimistic. Through both model-based and extensive experimental evaluations of Endure in the state-of-the-art LSM-based storage engine, RocksDB, we show that the robust tuning methodology consistently outperforms classical tuning strategies. The robust tunings output by Endure lead up to a 5x improvement in throughput in the presence of uncertainty. On the flip side, Endure tunings have negligible performance loss when the observed workload exactly matches the expected one.
