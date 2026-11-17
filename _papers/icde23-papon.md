---
title: ACEing the Bufferpool Management Paradigm for Modern Storage Devices
date: 2023-04-03 22:57:00 +0000
tags:
- IEEE ICDE
venue: Proceedings of the IEEE International Conference on Data Engineering (IEEE ICDE), 2023
authors: Tarikul Islam Papon, Manos Athanassoulis
links:
- label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/10184709
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/icde23-papon.pdf
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/icde23-papon.pdf
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/icde23-ACE.pdf
order: 48
permalink: /papers/icde23-papon
---

# Abstract

Over the past few decades, solid-state drives (SSDs) have been replacing hard disk drives (HDDs) due to their faster reads and writes, as well as their superior random access performance. Further, when compared to HDDs, SSDs have two fundamentally different properties: (i) read/write asymmetry (writes are slower than reads) and (ii) access concurrency (multiple I/Os can be executed in parallel to saturate the device bandwidth). However, several database operators are designed without considering storage asymmetry and concurrency resulting in device underutilization, which is typically addressed opportunistically by device-specific tuning during deployment. As a key example and the focus of our work, the bufferpool management of a Database Management System (DBMS) is tightly connected to the underlying storage device, yet, state-of-the-art approaches treat reads and writes equally, and do not expressly exploit the device concurrency, leading to subpar performance.

In this paper, we propose a new Asymmetry & Concurrency-aware bufferpool management (ACE) that batches writes based on device concurrency and performs them in parallel to amortize the asymmetric write cost. In addition, ACE performs parallel prefetching to exploit the device’s read concurrency. ACE does not modify the existing bufferpool replacement policy, rather, it is a wrapper that can be integrated with any replacement policy. We implement ACE in PostgreSQL and evaluate its benefits using a synthetic benchmark and TPC-C for several popular eviction policies (Clock Sweep, LRU, CFLRU, LRU-WSR). The ACE counterparts of all four policies lead to significant performance improvements, exhibiting up to 32.1% lower runtime for mixed workloads (33.8% for write-intensive TPC-C transactions) with a negligible increase in total disk writes and buffer misses, which shows that incorporating asymmetry and concurrency in algorithm design leads to more faithful storage modeling and, ultimately, to better device utilization.
