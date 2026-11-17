---
title: 'KVBench: A Key-Value Benchmarking Suite'
date: 2024-05-01 20:16:17 +0000
tags:
- DBTest Workshop
venue: Proceedings of the International Workshop on Testing Database Systems (DBTest), 2024
authors: Zichen Zhu, Arpita Saha, Manos Athanassoulis, and Subhadeep Sarkar
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3662165.3662765
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/dbtest24-zhu.pdf
- label: Artifacts
  url: https://github.com/BU-DiSC/kv-bench
order: 60
permalink: /papers/kvbench-dbtest24-zczhu
---

# Abstract

Key-value stores are at the core of several modern NoSQL-based data systems, and thus, a comprehensive benchmark tool is of paramount importance in evaluating their performance under different workloads. Prior research reveals that real-world workloads have a diverse range of characteristics, such as the fraction of point queries that target non-existing keys, point and range deletes, as well as, different distributions for queries and updates, all of which have very different performance implications. State-of-the-art key-value workload generators, such as YCSB and db_bench, fail to generate workloads that emulate these practical workloads, limiting the dimensions on which we can benchmark the systems' performance.

In this paper, we present KVBench, a novel synthetic workload generator that fills the gap between classical key-value workload generators and more complex real-life workloads. KVBench supports a wide range of operations, including point queries, range queries, inserts, updates, deletes, range deletes, and among these options, inserts, queries, and updates can be customized by different distributions. Compared to state-of-the-art key-value workload generators, KVBench offers a richer array of knobs, including the proportion of empty point queries, customized distributions for updates and queries, and range deletes with specific selectivity, constituting a significantly flexible framework that can better emulate real-world workloads.
