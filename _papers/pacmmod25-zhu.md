---
title: 'Mnemosyne: Dynamic Workload-Aware BF Tuning via Accurate Statistics in LSM trees'
date: 2025-04-16 04:00:00 +0000
tags:
- ACM SIGMOD
- PACMMOD
venue: Proceedings of the ACM Management of Data (PACMMOD), Vol. 3(3), 2025
authors: Zichen Zhu, Yanpeng Wei, Ju Hyoung Mun, Manos Athanassoulis
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3725327
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/pacmmod25-zhu.pdf
- label: Artifact
  url: https://github.com/BU-DiSC/Mnemosyne
- label: Presentation Video
  url: https://www.youtube.com/watch?v=Kspwlo1vi48
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/sigmod25-zhu-mnemosyne-slides.pdf
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/sigmod25-zhu-poster.pdf
order: 68
permalink: /papers/pacmmod25-zhu
---

# Abstract

Log-structured merge (LSM) trees typically employ Bloom Filters (BFs) to prevent unnecessary disk accesses for point queries. The size of BFs can be tuned to navigate a memory vs. performance tradeoff. State-of-the-art memory allocation strategies use a worst-case model for point lookup cost to derive a closed-form solution. However, existing approaches have three limitations: (1) the number of key-value pairs to be ingested must be known a priori, (2) the closed-form solution only works for a perfectly shaped LSM-tree, and (3) the model assumes a uniform query distribution in the key domain. Due to these limitations, the available memory budget for BFs is sub-optimally utilized, especially when the system is under memory pressure (i.e., less than 7 bits per key).

In this paper, we design Mnemosyne, a BF re-allocation framework for evolving LSM-trees that does not require prior workload knowledge. We use a more general query cost model that considers the access pattern per file, and an optimal memory allocation algorithm that converges 1000× faster than the gradient descent algorithm used by the state of the art. Further, we find that no system accurately maintains access statistics per file, and that simply maintaining a counter per file significantly deviates from the ground truth. To address this, we propose Merlin, a dynamic sliding-window-based tracking mechanism that accurately captures these statistics. The upgraded Mnemosyne+ combines Merlin with our new cost model. In our evaluation, Mnemosyne reduces query latency by up to 20% compared to RocksDB under memory pressure, and Mnemosyne+ further improves throughput by another 30% when workloads exhibit higher skew.
