---
title: Benchmarking, Analyzing, and Optimizing Write Amplification of Partial Compaction in RocksDB
date: 2024-10-21 02:09:00 +0000
tags:
- EDBT
venue: Proceedings of the International Conference on Extending Database Technology (EDBT), 2025
authors: Ran Wei, Zichen Zhu, Andrew Kryczka, Jay Zhuang, Manos Athanassoulis
links:
- label: Official PDF
  url: https://openproceedings.org/2025/conf/edbt/paper-114.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/edbt25-wei.pdf
- label: Artifact
  url: https://github.com/BU-DiSC/Benchmark-Analyze-Optimize-Partial-Compaction-in-RocksDB-Codebase
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/edbt25-zhu-slides.pdf
order: 64
permalink: /papers/edbt25-wei
---

# Abstract

Log-structured merge (LSM) trees are widely used because they offer high ingestion throughput via appending incoming data in a memory buffer, which, when filled up, is *flushed* to storage as a sorted run.
To reduce space amplification and facilitate queries, LSM-trees periodically merge data on storage to form larger but fewer sorted runs, with a process termed *compaction*.
In commercial LSM-based systems like RocksDB, sorted runs are often stored as a set of small files, allowing *partial compaction* (i.e., of a subset of a sorted run), reducing the worst-case compaction latency without increasing the amortized compaction cost.

In this paper, we focus on the four different file-picking policies offered by RocksDB (*MinOverlappingRatio*, *RoundRobin*, *OldestLargestSeqFirst*, and *OldestSmallestSeqFirst*).
While some heuristics to guide which compaction policies to use are given in the literature and the documentation of RocksDB, we highlight that an up-to-date, in-depth, and comprehensive analysis and guidelines for the partial compaction policies in RocksDB is needed, as earlier guidelines are now *obsolete* in the presence of new optimizations/implementations of RocksDB.
Further, we investigate the headroom for improvement by comparing each policy with the optimal WA, obtained by enumerating all possible picking decisions.
From our comprehensive experimental results, we distill 10 key observations, which rectify obsolete heuristics/observations and also provide valuable insights for LSM-based systems that employ partial compactions.
