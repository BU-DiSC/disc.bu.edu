---
title: Indexing for Near-Sorted Data
date: 2023-04-03 16:00:00 +0000
tags:
- IEEE ICDE
venue: Proceedings of the IEEE International Conference on Data Engineering (IEEE ICDE), 2023
authors: Aneesh Raman, Subhadeep Sarkar, Matthaios Olma, Manos Athanassoulis
links:
- label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/10184781
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/icde23-raman.pdf
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/icde23-raman-slides.pdf
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/icde23-SWARE.pdf
- label: Code
  url: https://github.com/BU-DiSC/sware
order: 47
permalink: /papers/icde23-raman
---

# Abstract

Indexing in modern data systems facilitates efficient query processing when the selection predicate is on an indexed key. As new data is ingested, indexes are gradually populated with incoming entries. In that respect, indexing can be perceived as the process of adding structure to incoming, otherwise unsorted data. Adding structure, however, comes at a cost. Instead of simply appending the incoming entries, we insert them into the index. If the ingestion order matches the indexed attribute order, the ingestion cost is entirely redundant and can be avoided altogether (e.g., via bulk loading in a B+-tree). However, classical tree index designs do not benefit when incoming data comes with an implicit ordering that is close to being sorted, but not fully sorted.

In this paper, we study how indexes can exploit near-sortedness. Particularly, we identify sortedness as a resource that can accelerate index ingestion. We propose a new sortedness-aware (SWARE) design paradigm that combines opportunistic bulk loading, index appends, variable node fill and split factors, and an intelligent buffering scheme, to optimize ingestion and read queries in a tree index in the presence of near-sortedness. We apply SWARE to two state-of-the-art search trees (B+-tree and Bϵ-tree), and we demonstrate that their Sortedness-Aware counterparts (SA B+-tree and SA Bϵ-tree) outperform their respective baselines by up to 8.8× (SA B+-tree) and 7.8× (SA Bϵ-tree) for a write-heavy workload in the presence of data sortedness, while offering competitive read performance, leading to overall benefits between 1.3× – 5× for mixed read/write workloads with near-sorted data. Overall, we highlight that SWARE can be applied to other tree-like data structures to accelerate index ingestion and improve their performance in the presence of data sortedness.
