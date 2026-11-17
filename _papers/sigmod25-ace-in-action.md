---
title: 'ACE-in-Action: A Smart DBMS Bufferpool for SSDs'
date: 2025-04-14 21:04:37 +0000
tags:
- ACM SIGMOD
- Demo
categories:
- SIGMOD
venue: Proceedings of the ACM SIGMOD International Conference on Management of Data, 2025
authors: Teona Bagashvili, Tarikul Islam Papon, Manos Athanassoulis
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3722212.3725077
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/sigmod25-bagashvili.pdf
- label: Demo website
  url: https://disc-projects.bu.edu/ACE/
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/sigmod25-ace-in-action-bagashvili-poster.pdf
order: 67
permalink: /papers/sigmod25-ace-in-action
---

# Absrtact

Solid-State Drives (SSDs) have two key properties: (i) read/write asymmetry, where writes are slower than reads, and (ii) access concurrency, allowing multiple I/O operations in parallel to maximize the bandwidth. However, many applications treat reads and writes equally and do not fully utilize the device concurrency, a behavior observed in traditional database bufferpool managers. To address this, we propose an Asymmetry & Concurrency-Aware bufferpool manager (ACE that batches writes based on the device's write concurrency and amortizes the high asymmetric write cost by issuing them in parallel. ACE notably improves the application performance (e.g., PostgreSQL) and is easy to integrate since it can work as a wrapper around any existing page replacement policy. In this demonstration, we present a web simulation of the ACE bufferpool manager integrated with three popular page replacement policies (LRU, CFLRU and LRU-WSR). The conference participants can configure the simulation, view the real-time bufferpool animation and statistics, as well as run various experiments to compare the performance of different page replacement policies and their ACE counterparts. The demonstration is available at <https://disc-projects.bu.edu/ACE/research.html>.
