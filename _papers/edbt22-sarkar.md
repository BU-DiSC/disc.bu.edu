---
title: Query Language Support for Timely Data Deletion
date: 2022-02-08 01:11:01 +0000
tags:
- EDBT
venue: Proceedings of the International Conference on Extending Database Technology (EDBT), 2022
authors: Subhadeep Sarkar, Manos Athanassoulis
links:
- label: Official PDF
  url: https://openproceedings.org/2022/conf/edbt/paper-131.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/edbt22-sarkar.pdf
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/edbt2022-sql-deletes.pdf
- label: Presentation Video
  url: https://www.youtube.com/watch?v=lcWj6b8EKFg
order: 37
permalink: /papers/edbt22-sarkar
---

# Abstract

A key driver of modern data systems is the requirement for fast ingestion while ensuring low-latency query processing. This has led to the birth of write-optimized data stores that realize ingestion (inserts, updates, and deletes) in an out-of-place manner. Deletes in such out-of-place data stores are performed logically via invalidation while retaining the invalidated data for arbitrarily long. At the same time, with new policy changes, such as the introduction of the right to be forgotten (in EU’s GDPR), the right to delete (in California’s CCPA and CPRA), and the deletion right (in Virginia’s VCDPA), the importance of timely and persistent deletion of user data has become critical.

In this paper, we point out that state-of-the-art query languages lack the necessary support to express a user’s preferences for data retention and deletion. Toward this, we first identify two classes of deletes: (i) retention-based deletion and (ii) on-demand deletion, that need to be supported for regulation compliance. Next, we present the challenges in transforming these user deletion requirements into application-level specifications. For this, we propose query language extensions that can express both ondemand and timely persistent deletion of user data. Finally, we discuss how the application and system level modifications work hand-in-hand under the privacy regulations and act as stepping stones toward designing deletion-compliant data systems.
