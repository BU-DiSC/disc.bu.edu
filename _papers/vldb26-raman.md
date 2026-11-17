---
title: Demonstrating Indexing for Near-Sorted Data
date: 2026-08-20 14:25:19 +0000
tags:
- PVLDB
- Demo
venue: Proceedings of the VLDB Endowment, Vol. 19(12), 2026
authors: Aneesh Raman, Philip Chindris, Anwesha Saha, Teona Bagashvili, Manos Athanassoulis
links:
- label: Official PDF
  url: https://www.vldb.org/pvldb/vol19/p4694-raman.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/vldb26-raman.pdf
- label: Demo website
  url: https://disc-projects.bu.edu/sortedness/
order: 75
permalink: /papers/vldb26-raman
---

# Abstract

Indexing sits at the heart of database systems due to its ability to support efficient queries. Classical indexes like B+-trees accelerate lookups by imposing order at the leaf level of the index, thereby adding structure (or sortedness) to otherwise unstructured data. However, when data arrives pre-sorted or nearly-sorted, B+-trees fail to leverage the intrinsic order and perform redundant indexing effort. Near-sorted data is increasingly common in modern applications like the stock market or sensor readings. In such applications, the redundant indexing effort leads to sub-optimal performance.

In this paper, we demonstrate recently proposed indexing techniques for near-sorted data, highlighting the performance implications of textbook ingestion in B+-trees as well as how our method achieves better ingestion performance. The demonstration integrates tail-leaf optimization - a widely deployed production technique for efficient ingestion, alongside SWARE and QuIT - our recently proposed index designs that harness sortedness to improve performance. Users can visualize differently sorted data workloads, view the complete index ingestion cycle, as well as analyze performance metrics that measure the impact of intrinsic order.
