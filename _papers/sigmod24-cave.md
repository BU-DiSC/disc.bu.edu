---
title: 'CAVE: Concurrency-Aware Graph Processing on SSDs'
date: 2024-05-02 04:47:28 +0000
tags:
- ACM SIGMOD
- PACMMOD
venue: Proceedings of the ACM Management of Data (PACMMOD), Vol. 2(3), 2024
authors: Tarikul Islam Papon, Taishan Chen, Shuo Zhang, Manos Athanassoulis
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3654928
- label: Local PDF
  url: https://cs-people.bu.edu/papon/pdfs/paper-sigmod24-cave.pdf
- label: Code
  url: https://github.com/BU-DiSC/CAVE
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/sigmod24-papon-poster.pdf
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/sigmod24-papon-CAVE-slides.pdf
order: 62
permalink: /papers/sigmod24-cave
---

Large-scale graph analytics has become increasingly common in areas like social networks, physical sciences, transportation networks, and recommendation systems. Since many such practical graphs *do not fit in main memory*, graph analytics performance depends on efficiently utilizing underlying storage devices. These *out-of-core* graph processing systems employ sharding and sub-graph partitioning to optimize for storage while relying on efficient sequential access of traditional hard disks. However, today’s storage is increasingly based on solid-state drives (SSDs) that exhibit *high internal parallelism* and *efficient random accesses*. Yet, state-of-the-art graph processing systems do not explicitly exploit those properties, resulting in subpar performance.

In this paper, we develop CAVE, the first graph processing engine that optimally exploits underlying SSD-based storage by harnessing the available storage device parallelism via carefully selecting graph I/Os that can be issued concurrently. Thus, CAVE *traverses multiple paths* and *processes multiple nodes and edges concurrently*, achieving parallelization at a granular level. We identify two key ways to parallelize graph traversal algorithms based on the graph structure and algorithm: *intra* and *inter*-subgraph parallelization. The first identifies subgraphs that contain vertices that can be accessed in parallel, while the latter identifies subgraphs that can be processed in their entirety in parallel. To showcase the benefit of our approach, we build within CAVE parallelized versions of five popular graph algorithms (Breadth-First Search, Depth-First Search, Weakly Connected Components, PageRank, Random Walk) that exploit the full bandwidth of the underlying device. CAVE uses a blocked file format based on adjacency lists and employs a concurrent cache pool that is essential to the parallelization of graph algorithms. By experimenting with different types of graphs on three SSD devices, we demonstrate that CAVE utilizes the available parallelism, and scales to diverse real-world graph datasets. CAVE achieves up to one order of magnitude speedup compared to the popular out-of-core systems Mosaic and GridGraph, and up to three orders of magnitude speedup in runtime compared to GraphChi.
