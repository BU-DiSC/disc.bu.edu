---
title: Dissecting, Designing, and Optimizing LSM-based Data Stores (Tutorial)
date: 2022-03-04 01:18:00 +0000
tags:
- ACM SIGMOD
venue: Proceedings of the ACM SIGMOD International Conference on Management of Data, 2022
authors: Subhadeep Sarkar, Manos Athanassoulis
links:
- label: Official Page
  url: https://dl.acm.org/doi/10.1145/3514221.3522563
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/sigmod22-sarkar-tutorial.pdf
- label: Presentation Video
  url: https://www.youtube.com/watch?v=hkMkBZn2mGs
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/sigmod2022-Tutorial.pdf
order: 39
permalink: /papers/sigmod22-tutorial
---

# Abstract

Log-structured merge (LSM) trees have emerged as one of the most commonly used disk-based data structures in modern data systems. LSM-trees employ out-of-place ingestion to support high throughput for writes, while their immutable file structure allows for good utilization of disk space. Thus, the log-structured paradigm has been widely adopted in state-of-the-art NoSQL, relational, spatial, and time-series data systems. However, despite their popularity, there is a lack of pedagogical textbook-like material on LSM designs. The goal of this tutorial is to present the fundamental principles of the LSM paradigm along with a digest of optimizations and new designs proposed in recent research and adopted by modern LSM engines. This will serve as introductory material for non-experts, and as a roadmap to cutting-edge LSM results for the LSM-aware researchers and practitioners.

Toward this, we first discuss in detail the basic operations (inserts, updates, deletes, point and range queries), their access patterns, and their paths through the LSM data structure. We then dive into the details of recent research on optimizing each of those operations. We first discuss techniques and designs that optimize data ingestion in LSM-trees and the performance tradeoff constructed by writes and reads for the LSM engines. Finally, we present the rich design space of the log-structured paradigm and outline how to navigate it and tune LSM-based systems. We conclude with a discussion on open challenges on LSM systems.
