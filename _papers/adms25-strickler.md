---
title: Micro-architectural Exploration of the Relational Memory Engine (RME) in RISC-V and FireSim
date: 2025-08-20 23:24:13 +0000
tags:
- ADMS Workshop @ VLDB
venue: Proceedings of the International Workshop on Accelerating Analytics and Data Management Systems Using Modern Processor and Storage Architectures (ADMS), 2025
authors: Cole Strickler, Ju Hyoung Mun, Connor Sullivan, Denis Hoornaert, Renato Mancuso, Manos Athanassoulis, Heechul Yun
links:
- label: Official PDF
  url: https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/ADMS/ADMS25-08.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/adms25-strickler.pdf
order: 69
permalink: /papers/adms25-strickler
---

# Absrtact

There is no ideal data layout. Even for pure analytical workloads, different queries access a different subset of each relation's columns. This is further exacerbated by Hybrid Transactional/Analytical Processing (HTAP) workloads, which have led to systems converting from row to columnar or hybrid layouts, thereby increasing memory usage and code complexity. The recently proposed Relational Memory Engine (RME) is a hardware accelerator designed to address these challenges by transparently presenting the optimal layout to the CPU. The original RME prototype, built on a PS-PL platform, had limited micro-architectural configurability and a fixed low clock speed, restricting performance analysis and ASIC portability.

In this work, we re-implement RME on a RISC-V system-on-chip (SoC) platform using FireSim to address these limitations by enabling flexible SoC design parameterization and detailed performance evaluation. We simplify and improve the prior RME hardware design and leverage the increased flexibility of our platform to further explore RME's performance characteristics under various micro-architectural settings. We show that hardware prefetching significantly enhances RME performance by effectively masking latency, even for low clock speeds. Out-of-order CPU cores further amplify performance gains, indicating a synergistic relationship between RME and high-performance core designs. We also identify a critical RME clock speed threshold, beyond which performance degradation becomes substantial. Finally, we open-source our design to facilitate further research on TileLink-based RISC-V SoCs.
