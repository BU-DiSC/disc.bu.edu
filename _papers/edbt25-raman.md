---
title: QuIT your B+Tree for Quick Insertion Tree
date: 2024-10-22 15:09:00 +0000
tags:
- EDBT
venue: Proceedings of the International Conference on Extending Database Technology (EDBT), 2025
authors: Aneesh Raman, Konstantinos Karatsenidis, Shaolin Xie, Matthaios Olma, Subhadeep Sarkar, Manos Athanassoulis
links:
- label: Official PDF
  url: https://openproceedings.org/2025/conf/edbt/paper-118.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/edbt25-raman.pdf
- label: Artifact
  url: https://github.com/BU-DiSC/quick-insertion-tree
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/edbt25-raman-slides.pdf
order: 65
permalink: /papers/edbt25-raman
---

# Abstract

Search trees, like B+-trees, are often used as index structures in data systems to improve query performance at the cost of index construction and maintenance. Production data systems drastically reduce the index construction cost when the data arrives fully sorted by employing a fast-path ingestion technique to their B+-tree that directly appends the incoming entries to the tail leaf. However, this optimization is only effective if the incoming data is fully sorted or has very few out-of-order entries. The state-of-the-art sortedness-aware design (SWARE) employs an in-memory buffer to capture near-sortedness to reduce the index construction cost when the data is nearly sorted. This, however, sacrifices performance during lookups and introduces additional design complexity.

To address these challenges, we present Quick Insertion Tree (QuIT), a new sortedness-aware index that improves ingestion performance with minimal design complexity and no read overhead. QuIT maintains in memory a pointer to the predicted-ordered-leaf (pole) that provides a sortedness-aware fast-path optimization, and facilitates faster ingestion. The key benefit comes from accurately predicting pole throughout data ingestion. Further, QuIT achieves high memory utilization by maintaining tightly packed leaf nodes when the ingested data arrives with high sortedness. This, in turn, helps improve performance during range lookups. Overall, QuIT outperforms B+-tree (SWARE) by up to 3x (2x) for ingestion, while also offering up to 1.32x faster (than SWARE) point lookup performance and accessing up to 2x fewer leaf nodes than the B+-tree during range lookups.
