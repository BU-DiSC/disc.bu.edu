---
title: A Parametric I/O Model for Modern Storage Devices
date: 2021-05-28 02:42:17 +0000
tags:
- DAMON Workshop
venue: Proceedings of the International Workshop on Data Management on New Hardware (DaMoN), 2021
authors: Tarikul Islam Papon, Manos Athanassoulis
links:
- label: Local PDF
  url: http://cs-people.bu.edu/mathan/publications/damon21-papon.pdf
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3465998.3466003
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/damon21-papon.pdf
- label: Presentation Video
  url: https://www.youtube.com/watch?v=wBhxFxVbh3I
- label: Project website
  url: http://disc-projects.bu.edu/parametric-io-model/
- label: Experimental Codebase
  url: https://github.com/BU-DiSC/PIO-model
order: 32
permalink: /papers/damon21-papon
---

# Abstract

Storage devices have evolved to offer increasingly faster read/write access, through flash-based and other solid-state storage technologies. When compared to classical rotating hard disk drives (HDDs), modern solid-state drives (SSDs) have two key differences: (i) the absence of mechanical parts, and (ii) an inherent difference between the process of reading and writing. The former removes a key performance bottleneck, enabling internal device parallelism, whereas the latter manifests as a read/write performance asymmetry. In other words, SSDs can serve multiple concurrent I/Os, and their writes are generally slower than reads; none of which is true for HDDs. Yet, the performance of storage-resident applications is typically modeled by the number of disk accesses performed, inherently assuming symmetric read and write performance and the ability to perform only one I/O at a time, failing to accurately capture the performance of modern storage devices.

To address this mismatch, we propose a simple yet expressive storage model, termed Parametric I/O Model (PIO) that captures contemporary devices by parameterizing read/write asymmetry (α) and access concurrency (k). PIO enables device-specific decisions at algorithm design time, rather than as an optimization during deployment and testing, thus ensuring optimal algorithm design by taking into account the properties of each device. We present a benchmarking of several storage devices that shows that α and k vary significantly across devices. Further, we show that using carefully quantified values of α and k for each storage device, we can fully exploit the performance it offers, and we lay the groundwork for asymmetry/concurrency-aware storage-intensive algorithms. We also highlight that the degree of the performance benefit due to concurrent reads or writes depends on the asymmetry of the underlying device. Finally, we summarize our findings as a set of guidelines for designing storage-intensive algorithms and discuss specific examples for better algorithm and system designs as well as runtime tuning.
