---
title: Enhancing Data Systems Performance by Exploiting SSD Concurrency &amp; Asymmetry
date: 2024-02-17 09:34:48 +0000
tags:
- PhD Symposium
- IEEE ICDE
venue: Proceedings of the IEEE ICDE PhD Symposium, 2024
authors: Tarikul Islam Papon (supervised by Manos Athanassoulis)
links:
- label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/10597931
- label: Local PDF
  url: https://cs-people.bu.edu/papon/pdfs/paper-icde24-phd-symposium.pdf
order: 59
permalink: /papers/icde24-phdsymp-ssd-aware-system
---

Solid-state drives (SSDs) have become the dominant storage technology because of their faster read and write speeds and superior random access performance.
Unlike their ancestor hard disk drives, SSDs exhibit two distinct characteristics: (i) *read/write asymmetry*, where writes are slower than reads, and (ii) *access concurrency*, allowing multiple I/O operations to run simultaneously and fully utilize device bandwidth.
Despite these, most storage-intensive applications are not optimized for SSD asymmetry and concurrency, often leading to device underutilization.

In this thesis, we uncover these crucial SSD properties and outline how we can better exploit these properties from the application perspective.
First, we augment the traditional I/O model with the Parametric I/O Model (**PIO**), a new storage model that faithfully represents storage devices by parameterizing read/write asymmetry (*α*) and access concurrency (*k*).
Second, using this novel storage modeling, we propose a new *Asymmetry & Concurrency-aware* bufferpool management (**ACE**) that batches writes based on device concurrency and performs them in parallel to *amortize* the asymmetric write cost while performing parallel prefetching to exploit the device's read concurrency.
Third, we further present a *Concurrency-aware* graph processing engine **CAVE** that harnesses the parallelism supported by the underlying SSD device via concurrent I/Os.
CAVE traverses multiple paths and processes multiple nodes and edges concurrently without altering the fundamental graph traversal algorithm guarantees.
Overall, our analysis shows that more faithful storage modeling leads to higher performance and better device utilization.
