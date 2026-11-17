---
title: 'Acheron: Persisting Tombstones in LSM Engines'
date: 2023-06-20 03:54:00 +0000
tags:
- ACM SIGMOD
- Demo
categories:
- SIGMOD
venue: Proceedings of the ACM SIGMOD International Conference on Management of Data, 2023
authors: Zichen Zhu, Subhadeep Sarkar, Manos Athanassoulis
links:
- label: ACM DL
  url: https://doi.org/10.1145/3555041.3589719
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/sigmod23-zhu.pdf
- label: Demo website
  url: https://disc-projects.bu.edu/acheron/
- label: Demonstration Video
  url: https://youtu.be/irjcsT_qhoY
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/sigmod23-zhu-Acheron-demo-poster.pdf
order: 52
permalink: /papers/sigmod23-acheron
---

# Absrtact

Modern NoSQL storage engines frequently employ Log-structured merge (LSM) trees as their core data structures because they offer high ingestion rate and low latency for query processing. Client writes are captured in memory first and are gradually merged on disk in a level-wise manner. While this out-of-place paradigm sustains fast ingestion rate, it implements delete operations via inserting tombstones which logically invalidate older entries. Thus obsolete data cannot be removed instantly and may be retained in LSM trees for an arbitrarily long time. Therefore, out-of-place deletion in LSM trees may on the one hand, violate data privacy regulations (e.g., the right to be forgotten in EU's GDPR, right to delete in California's CCPA and CPRA), and on the other hand, it hurts performance.

In this paper, we develop Acheron, which demonstrates the performance implications of out-of-place deletes and how our method achieves timely persistent deletes. We integrate both prior state-of-the-art compaction policies and our recently presented method, FADE, into Acheron and visualize the life cycle of tombstones in LSM trees. Using Acheron visualization, the users can observe that the state of the art does not provide guarantees on when obsolete entries can be physically removed, and also observe that FADE can achieve timely persistent deletes without full tree compaction. The users can further customize the workload, LSM tuning knobs, and disk parameters to investigate the impact of different factors on tombstones and the performance. This demonstration provides key insights into the impact of tombstones for LSM-interested researchers and practitioners.
