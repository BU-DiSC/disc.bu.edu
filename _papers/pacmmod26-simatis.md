---
title: 'TIDY: Temporal Indexing for Die-Young Objects'
date: 2026-09-08 15:44:00 +0000
tags:
- ACM SIGMOD
- PACMMOD
venue: Proceedings of the ACM Management of Data (PACMMOD), Vol. 4(6), 2026
authors: Panagiotis Simatis, Panagiotis Bouros, Manos Athanassoulis, Nikos Mamoulis
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3856375
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/pacmmod26-simatis.pdf
order: 78
permalink: /papers/pacmmod26-simatis
---

# Abstract

Managing temporal intervals for processing time-travel queries has recently gained interest, with new indices proposed for memory-resident data. General-purpose interval data structures are not designed to handle highingestion workloads involving “die-young” temporal objects, i.e., short-lived temporal objects. In addition, they are not optimized for time intervals inserted in order of their end times. We show that this case of temporal data is quite common in real applications and propose a new temporal index, called TIDY, that achieves superior search performance compared to the state-of-the-art while supporting insertions in O(1) amortized time, which is asymptotically lower than current interval indices. We model the intervals as points in a 2-d (end-time, duration) space and decompose the data into frequent short-lived intervals and less frequent long-lived ones. We manage each of these two data partitions in a dedicated index, called B-Rail, which is cache-friendly and append-only. We show that a time-range query can be decomposed to a 1-d range query in the end-time dimension and a triangular query in the 2-d (end-time, duration) space, both efficiently evaluated by the B-Rail modules of TIDY. Our experimental analysis on real-world datasets demonstrates that TIDY outperforms state-of-the-art in-memory methods for temporal objects.
