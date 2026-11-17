---
title: 'NOCAP: Near-Optimal Correlation-Aware Partitioning Joins'
date: 2023-12-01 06:23:00 +0000
tags:
- ACM SIGMOD
- PACMMOD
venue: Proceedings of the ACM Management of Data (PACMMOD), Vol. 1(4), 2023
authors: Zichen Zhu, Xiao Hu, Manos Athanassoulis
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3626739
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/pacmmod23-zhu.pdf
- label: Code
  url: https://github.com/BU-DiSC/NOCAP-join
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/sigmod24-zhu-NOCAP-slides.pdf
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/sigmod24-zhu-poster.pdf
order: 57
permalink: /papers/pacmod23-zhu
---

# Abstract

Storage-based joins are still commonly used today because the memory budget does not always scale with the data size. One of the many join algorithms developed that has been widely deployed and proven to be efficient is the Hybrid Hash Join (HHJ), which is designed to exploit any available memory to maximize the data that is joined directly in memory. However, HHJ cannot fully exploit detailed knowledge of the join attribute correlation distribution.

In this paper, we show that given a correlation skew in the join attributes, HHJ partitions data in a suboptimal way. To do that, we derive the optimal partitioning using a new cost-based analysis of partitioning-based joins that is tailored for primary key - foreign key (PK-FK) joins, one of the most common join types. This optimal partitioning strategy has a high memory cost, thus, we further derive an approximate algorithm that has tunable memory cost and leads to near-optimal results. Our algorithm, termed NOCAP (Near-Optimal Correlation-Aware Partitioning) join, outperforms the state-of-the-art for skewed correlations by up to 30%, and the textbook Grace Hash Join by up to 4×. Further, for a limited memory budget, NOCAP outperforms HHJ by up to 10%, even for uniform correlation. Overall, NOCAP dominates state-of-the-art algorithms and mimics the best algorithm for a memory budget varying from below sqrt(|relation|) to more than |relation|.
