---
title: Exploring Wavelet Trees as Space-Efficient Physical-to-Sorted Mapping for Learned Indexes
date: 2025-08-20 23:26:45 +0000
tags:
- AIDB Workshop @ VLDB
venue: Proceedings of the International Workshop of Applied AI for Database Systems and Applications (AIDB), 2025
authors: Anwesha Saha, Aneesh Raman, Ryan Marcus, Manos Athanassoulis
links:
- label: Official PDF
  url: https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/AIDB/AIDB25_10.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/aidb25-saha.pdf
order: 70
permalink: /papers/aidb25-saha
---

# Abstract

Learned indexes are strong competitors to classical indexes like B+-trees due to efficient query performance and low space utilization. They operate by replacing the internal nodes of the index with a hierarchy of machine learning models that capture the data distribution. However, to achieve high accuracy, learned indexes store a copy of the underlying data in sorted order. This restricts their space efficiency to the internal nodes of the index, that occupy only a minor fraction of the index's overall memory footprint.

In this work, we explore space-efficient mappings between the sorted and the physical order of the data using Wavelet Trees (a succinct data structure to represent permutations of symbols). We first evaluate the Integer Wavelet Tree (IWT), a Wavelet Tree adapted to the integer domain (to capture physical-to-sorted order permutations). While IWT drastically reduces the memory footprint of the mapping, it incurs a high access cost due to increased cache-misses as a result of its two-branched design. We then design and evaluate a Wavelet Tree with increased fanout, termed T-way IWT, and discuss its tradeoffs. Our analysis shows that although Wavelet Trees fall short as permutation mappings, they help identify the properties needed to balance fast lookups with low memory footprint in structures that map permutations for learned indexes.
