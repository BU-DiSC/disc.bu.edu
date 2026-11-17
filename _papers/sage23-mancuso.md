---
title: Software-Shaped Platforms
date: 2023-05-10 01:28:00 +0000
tags:
- RAGE
venue: Proceedings of the Cyber-Physical Systems and Internet of Things Week (CPS-IoT Week Workshops), 2023
authors: Renato Mancuso, Shahin Roozkhosh, Denis Hoornaert, Ju Hyoung Mun, Tarikul Islam Papon, Manos Athanassoulis
links:
- label: ACM DL
  url: https://dl.acm.org/doi/10.1145/3576914.3587546
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/rage23-mancuso.pdf
order: 51
permalink: /papers/sage23-mancuso
---

# Abstract

This paper outlines the vision for a new type of software-shaped platforms, or SOSH platforms for short, that can be implemented in commercial CPU+FPGA platforms. At the core of the SOSH paradigm is the idea of exposing direct control over the flow of data exchanged between hardware components in embedded System-on-Chips (SoC). Data flow manipulation primitives are synthesized in reprogrammable hardware and interposed between central processors, memory modules, and I/O devices. A new layer of system software is then introduced to leverage such primitives and to achieve fine-grained control and introspection over the interaction of SoC resources. By turning memory and I/O data flows into manageable entities, a new degree of internal awareness can be achieved in complex systems. We first review recent works that are well aligned with the concept of data flow manipulation primitives that can be deployed in SOSH platforms. Next, we outline future research avenues concerning the use of the SOSH paradigm for workload profiling and prediction, to implement advanced memory models, and to perform security threat identification and mitigation.
