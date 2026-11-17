---
title: Reducing Bloom Filter CPU Overhead in LSM-Trees on Modern Storage Devices
date: 2021-06-22 18:21:00 +0000
tags:
- DAMON Workshop
venue: Proceedings of the International Workshop on Data Management on New Hardware (DaMoN), 2021
authors: Zichen Zhu, Ju Hyoung Mun, Aneesh Raman, Manos Athanassoulis
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3465998.3466002
- label: Local PDF
  url: http://cs-people.bu.edu/mathan/publications/damon21-zhu.pdf
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/damon21-lsm-bf-overhead-slides.pdf
order: 33
permalink: /papers/reducing-bloom-filter-cpu-overhead-in-lsm-trees-on-modern-storage-devices
---

# Absrtact

Bloom filters (BFs) accelerate point lookups in Log-Structured
Merge (LSM) trees by reducing unnecessary storage accesses to
levels that do not contain the desired key. BFs are particularly beneficial when there is a significant performance difference between
querying a BF (hashing and accessing memory) and accessing data
(on secondary storage). This gap, however, is decreasing as modern
storage devices (SSDs and NVMs) have increasingly lower latency,
to the point that the cost of accessing data can be comparable to
that of filter probing and hashing, especially for large key sizes that
exhibit high hashing cost. In an LSM-tree, BFs are employed when
querying each level of the tree, thus, exacerbating the CPU cost
as the data size – and thus, the tree height – grows. To address
the increasing CPU cost of BFs in LSM-trees, we propose to re-use
hash calculations aggressively within and across BFs, as well as
between different levels, and we show both analytically and experimentally that we can maintain a close-to-ideal false positive rate
while significantly reducing the runtime. The reduced CPU cost
for queries using the proposed hash sharing leads to 10% higher
lookup performance in an LSM-tree with 22GB of data (5 levels)
stored in a state-of-the-art PCIe SSD. The benefit further increases
for faster underlying storage. Specifically, we show that for faster
NVM devices, hash sharing leads to performance gains up to 40%.
