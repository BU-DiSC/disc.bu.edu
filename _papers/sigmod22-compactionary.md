---
title: 'Compactionary: A Dictionary for LSM Compactions'
date: 2022-03-04 03:18:05 +0000
tags:
- ACM SIGMOD
- Demo
venue: Proceedings of the ACM SIGMOD International Conference on Management of Data, 2022
authors: Subhadeep Sarkar, Kaijie Chen, Zichen Zhu, Manos Athanassoulis
links:
- label: Official Page
  url: https://dl.acm.org/doi/10.1145/3514221.3520169
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/sigmod22-sarkar-demo.pdf
- label: Demo website
  url: https://disc-projects.bu.edu/compactionary/
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/sigmod2022-compactionary-poster.pdf
order: 40
permalink: /papers/sigmod22-compactionary
---

# Abstract

Log-structured merge (LSM) trees are widely used as the storage layer of modern NoSQL data stores, as they offer efficient ingestion performance. To enable competitive read performance and reduce space amplification, LSM-trees re-organize data layout on disk iteratively, through compactions. Compactions are at the heart of every LSM-based storage engine, fundamentally influencing their performance. However, the process of compaction in LSM-engines is often treated as a black-box that is rarely exposed as a tuning knob. In this paper, we demonstrate Compactionary, a dictionary for LSM compactions, that helps to visualize the implications of compactions on performance for different workloads and LSM tunings. Compactionary breaks down the LSM compaction black-box, expressing compactions as an ensemble of four first-order design choices: (i) when to compact, (ii) how to organize the data after compaction, (iii) how much data to compact, and (iv) which data to compact. We configure Compactionary to demonstrate the operational flow of several state-of-the-art LSM compaction strategies and how each strategy affects performance. The participants can (i) customize the workload, (ii) configure the LSM tuning, and (iii) switch between advanced compaction options, to understand individually the impact of the different factors on performance. Further, to engage the interested participants, we extend the demonstration by allowing the participants to create custom hybrid compaction strategies, as well as to configure the settings separately for each strategy in an individual analysis phase. The demo is available at <https://disc-projects.bu.edu/compactionary/#interactiveDemo>.
