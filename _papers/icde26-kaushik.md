---
title: 'RangeReduce: Query-Driven LSM Compactions'
date: 2026-03-03 16:45:00 +0000
tags:
- IEEE ICDE
venue: Proceedings of the IEEE International Conference on Data Engineering (IEEE ICDE), 2026.
authors: Shubham Kaushik, Manos Athanassoulis, Subhadeep Sarkar
links:
- label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/11629347
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/icde26-kaushik.pdf
- label: Talk
  url: https://www.youtube.com/watch?v=xgJ2g_CLjSQ
order: 73
permalink: /papers/icde26-kaushik
---

# Abstract

Log-structured merge (LSM) trees are widely used in the storage layer of modern ingestion-optimized data stores. The high ingestion throughput, however, comes at the cost of sub-optimal range query (RQ) performance. This is because LSM-trees arrange the data as a hierarchical collection of sorted runs, which implies that every RQ must (i) probe all sorted runs to locate the qualifying entries, (ii) scan and merge the entries from all qualifying runs, (iii) filter out the logically invalidated entries by updates and deletes on the fly, and (iv) return the most recent version of each qualifying key. This leads to high read amplification and significant redundant work in terms of superfluous I/Os to storage and wasted CPU cycles, which is exacerbated in the presence of updates and deletes. Additionally, during compactions, the same data is read and written multiple times, further amplifying the read and write amplification.

In this paper, we introduce RangeReduce, an RQ-optimized LSM-engine that uses RQs as a hint to compact data that is already read into memory as part of the query, and thereby, improves the overall performance of the storage engine. The key intuition is to take advantage of the I/Os and CPU cycles spent on reading and merging data from slow storage during RQs and write the RQ-qualifying data back as part of a single sorted run. Such RQ-driven compactions enable RangeReduce to (i) read less data from fewer sorted runs for subsequent RQs, (ii) reduce overall data movement (reads and writes) due to RQs and compactions, and (iii) improve space amplification, while (iv) significantly reducing compaction debt. Experiments show that RangeReduce offers up to 90% lower compaction debt, 12% less data movement, and 20% lower space amplification while improving average RQ latency by up to 18%.
