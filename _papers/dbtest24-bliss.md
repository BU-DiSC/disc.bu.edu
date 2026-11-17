---
title: Benchmarking Learned and LSM Indexes on Data Sortedness
date: 2024-05-02 01:41:00 +0000
tags:
- DBTest Workshop
venue: Proceedings of the International Workshop on Testing Database Systems (DBTest), 2024
authors: Aneesh Raman, Andy Huynh, Jinqi Lu and Manos Athanassoulis
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3662165.3662764
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/dbtest24-raman.pdf
- label: Artifacts
  url: https://github.com/BU-DiSC/bliss_benchmark
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/dbtest24-bliss-slides.pdf
order: 61
permalink: /papers/dbtest24-bliss
---

# Abstract

Database systems use indexes on frequently accessed attributes to accelerate query and transaction processing. This requires paying the cost of maintaining and updating those indexes, which can be thought of as the process of adding structure (e.g., sort) to an otherwise unstructured data collection. The indexing cost is redundant when data arrives pre-structured, i.e., pre-sorted, even if only *up to some degree*. While recent work has studied how classic indexes like B+-trees cannot fully exploit the intrinsic *near-sortedness* during ingestion, this exploration is lacking on index designs like read-optimized learned indexes or write-optimized LSM-trees.

In this paper, we bridge this gap by conducting the first-ever study on the behavior of state-of-the-art learned indexes and LSM-trees when varying the degree of data sortedness in an ingestion workload. Specifically, we build on prior work on benchmarking data sortedness on B+-trees and we expand the scope to benchmark:

(i) ALEX and LIPP, which are updatable learned index designs; and

(ii) the LSM-tree engine offered by RocksDB.

We present in detail, our evaluation framework and present key insights on the performance of learned indexes and LSM-tree designs with respect to data sortedness. Our observations indicate that learned indexes exhibit unpredictable performance when ingesting differently sorted data, while LSM-trees can benefit from sortedness-aware optimizations. We highlight the potential headroom for improvement and lay the groundwork for further research in this domain.
