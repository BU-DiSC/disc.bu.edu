---
title: Towards Flexibility and Robustness of LSM Trees
date: 2023-12-02 05:25:00 +0000
tags:
- VLDBJ
venue: The VLDB Journal, Vol. 33(4), Special Issue on Machine Learning and Databases, 2024
authors: Andy Huynh, Harshal Chaudhari, Evimaria Terzi, Manos Athanassoulis
links:
- label: Official Version
  url: https://link.springer.com/article/10.1007/s00778-023-00826-9
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/vldbj24-huynh.pdf
- label: ArXiv
  url: https://arxiv.org/abs/2311.10005
order: 58
permalink: /papers/vldbj-23-huynh
---

# Abstract

Log-Structured Merge trees (LSM trees) are increasingly used as part of the storage engine behind several data systems, and are frequently deployed in the cloud. As the number of applications relying on LSM-based storage backends increases, the problem of performance tuning of LSM trees receives increasing attention. We consider both *nominal* tunings -- where workload and execution environment are accurately known *a priori* -- and *robust* tunings -- which consider *uncertainty* in the workload knowledge. This type of workload uncertainty is common in modern applications, notably in shared infrastructure environments like the public cloud.

To address this problem, we introduce Endure, a new paradigm for tuning LSM trees in the presence of workload uncertainty. Specifically, we focus on the impact of the choice of compaction policy, size ratio, and memory allocation on the overall performance. Endure considers a robust formulation of the throughput maximization problem and recommends a tuning that offers near-optimal throughput when the executed workload is not the same, instead in a *neighborhood* of the expected workload. Additionally, we explore the robustness of flexible LSM designs by proposing a new unified design called K-LSM that encompasses existing designs. We deploy our robust tuning system, Endure, on a state-of-the-art key-value store, RocksDB, and demonstrate throughput improvements of up to 5x in the presence of uncertainty. Our results indicate that the tunings obtained by Endure are more robust than tunings obtained under our expanded LSM design space. This indicates that robustness may not be inherent to a design, instead, it is an outcome of a tuning process that explicitly accounts for uncertainty.
