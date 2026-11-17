---
title: The LSM Design Space and its Read Optimizations (Tutorial)
date: 2023-04-04 15:19:00 +0000
tags:
- IEEE ICDE
venue: Proceedings of the IEEE International Conference on Data Engineering (IEEE ICDE), 2023
authors: Subhadeep Sarkar, Niv Dayan, Manos Athanassoulis
links:
- label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/10184626/
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/icde23-tutorial.pdf
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/icde23-tutorial.pdf
order: 49
permalink: /papers/icde23-tutorial
---

# Abstract

Log-structured merge (LSM) trees have emerged as one of the most commonly used storage-based data structures in modern data systems as they offer high throughput for writes and good utilization of storage space. However, LSM-trees were not originally designed to facilitate efficient reads. Thus, state-of- the-art LSM engines employ numerous optimization techniques to make reads efficient. The goal of this tutorial is to present the fundamental principles of the LSM paradigm along with the various optimization techniques and hybrid designs adopted by LSM engines to accelerate reads.

Toward this, we first discuss the basic LSM operations and their access patterns. We then discuss techniques and designs that optimize point and range lookups in LSM-trees: (i) index and (ii) filter data structures, (iii) caching, and (iv) read- friendly data layouts. Next, we present the performance tradeoff between writes and reads, outlining the rich design space of the LSM paradigm and how one can navigate it to improve query performance. We conclude by discussing practical problems and open research challenges.
