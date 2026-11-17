---
title: 'SHaMBa: Reducing Bloom Filter Overhead in LSM Trees'
date: 2023-08-01 01:09:00 +0000
tags:
- PhD Workshop VLDB
venue: Proceedings of the VLDB PhD Workshop, 2023
authors: Zichen Zhu (supervised by Manos Athanassoulis)
links:
- label: Official PDF
  url: https://ceur-ws.org/Vol-3452/paper5.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/zczhu/files/SHaMBa-VLDB-PhD-Workshop.pdf
order: 53
permalink: /papers/vldb23-phdworkshop-shamba
---

Bloom Filiters (BFs) are typically employed to alleviate unnecessary disk accesses to facilitate point lookup in LSM trees. They
are particularly beneficial when there is a significant performance difference between probing a Bloom filter (hashing and
accessing memory) and accessing data (on secondary storage). However, this gap is decreasing as SSDs and NVMs have
increasingly lower latency, to the point that the cost of accessing data can be comparable to that of hashing and filter probing,
especially for large key sizes that results in high hashing cost. In addition, BFs are beneficial for empty queries while they are
a burden for positive queries (i.e., on an existing key). Also, with larger datasets, the total memory consumed by also increases
making it less feasible to keep in memory all BFs. Coupling this, with the increasing price of memory and the need to reduce
the memory-to-data ratio in many practical deployments, we are seeing an increased memory pressure. In this setting, fewer
BF blocks are cached, thus causing additional storage accesses, since they have to be fetched in memory to answer a query.

In this PhD work, we introduce SHaMBa (Shared Hash Modular Bloom Filter), a new LSM-based key-value engine that
addresses both (a) the increasing hashing overhead and (b) the suboptimal performance when BFs do not fit in memory.
First, SHaMBa decouples the hashing cost from the data size by sharing a single hash digest across different levels. Second,
SHaMBa applies a workload-aware BF skipping policy based on Modular Bloom Filter (i.e., a set of mini-BFs that replace a
single large BF) to avoid accessing BFs when they are not useful. Our evaluation shows that SHaMBa reduces the CPU cost
for BF probing, and substantially outperforms the state of the art under memory pressure, having the same average number
of I/Os - using only one-third of the memory consumption of the state of the art.
