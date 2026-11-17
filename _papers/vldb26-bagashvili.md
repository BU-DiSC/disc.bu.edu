---
title: Eliminating the Hidden Cost of Zone Management in ZNS SSDs
date: 2026-09-16 15:42:59 +0000
tags:
- PVLDB
venue: Proceedings of the VLDB Endowment, Vol. 20(2), 2026
authors: Teona Bagashvili, Tarikul Islam Papon, Subhadeep Sarkar, Manos Athanassoulis
links:
- label: Official PDF
  url: https://www.vldb.org/pvldb/vol20/p270-bagashvili.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/vldb26-bagashvili.pdf
order: 79
permalink: /papers/vldb26-bagashvili
---

# Abstract

Zoned Namespace (ZNS) SSDs offer a new storage model that allows for high-throughput and low-latency storage by eliminating device-side garbage collection. The ZNS interface exposes storage as append-only zones , thus requiring host applications (e.g., database systems) to append, read, and garbage collect their pages. However, the ZNS storage abstraction hides the substantial differences across ZNS SSD controller designs. These differences affect both the performance and predictability of host applications. We find that existing ZNS designs exhibit (a) increased device-level write amplification (DLWA), (b) increased wear, and (c) increased interference with host I/O. We identify that (i) zone allocation granularity, (ii) zone geometry, (iii) write order, and (iv) zone mapping and management are the four main causes behind this.

To provide a predictable storage device, we propose SilentZNS, a new holistic zone management approach that expands the design space of zones and allocates blocks to zones on the fly, while minimizing wear, maintaining parallelism, and avoiding superfluous writes to the device. SilentZNS is a flexible zone allocation scheme that departs from traditional logical-to-physical zone mapping and allows arbitrary collections of blocks to be assigned to a zone. SilentZNS uses wear-aware allocation and maintains competitive read latency, while substantially reducing DLWA. We implement SilentZNS using the state-of-the-art ConfZNS++ emulator and evaluate it on synthetic microbenchmarks and a key-value storage engine. We show that SilentZNS reduces DLWA by 92% at a 10% zone occupancy threshold, reduces wear by 12%, and achieves up to 3.7x faster workload execution.
