---
title: Programmable Data Layouts via On-The-Fly Data Transformation
date: 2026-10-18 16:47:00 +0000
tags:
- ACM ASPLOS
venue: Proceedings of the ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), Volume 1, 2027
authors: Cole Strickler, Manos Athanassoulis, Renato Mancuso, Heechul Yun
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3845814.3850077
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/asplos27-strickler.pdf
order: 80
permalink: /papers/asplos27-strickler
---

# Abstract

The performance of modern computing systems is heavily bottlenecked by the widening gap between processing throughput and main memory latency, a problem exacerbated when an application’s logical data access patterns misalign with the physical layout of data in memory. To address this, we propose a hardware-software co-design framework comprising the Data Transformation Language (DTL) and the Data Transformation Unit (DTU). DTL allows programmers to concisely express complex data layout reorganizations, which the compiler translates into efficient hardware routing configurations. The DTU, a hardware engine logically situated between the Last-Level Cache (LLC) and main memory, transparently evaluates these configurations on-the-fly to gather scattered data elements into dense, logically contiguous cache lines. By converting explicit layout transformations into virtual views, this approach eliminates the need for explicit data materialization in software. We evaluate the DTU within a quad-core RISC-V SoC using FireSim, demonstrating substantial improvements in execution speed and memory efficiency.
