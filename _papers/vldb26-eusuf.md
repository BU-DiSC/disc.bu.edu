---
title: 'ReStore-in-Action: Adaptive Multi-Tier Storage Management via Intelligent Data Migration Policy'
date: 2026-08-20 14:28:25 +0000
tags:
- PVLDB
- Demo
venue: Proceedings of the VLDB Endowment, Vol. 19(12), 2026
authors: Shadman Saqib Eusuf, Tianru Zhang, Teona Bagashvili, Manos Athanassoulis, Tarikul Islam Papon
links:
- label: Official PDF
  url: https://www.vldb.org/pvldb/vol19/p4702-zhang.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/vldb26-eusuf.pdf
- label: Demo website
  url: https://disc-projects.bu.edu/ReStore/research.html
order: 76
permalink: /papers/vldb26-eusuf
---

# Abstract

Modern data systems employ a diverse range of storage devices, from high-performance, expensive SSDs to capacity-oriented SSDs and cost-effective, high-capacity HDDs. To leverage these varying characteristics, storage devices are often organized into MultiTiered Storage (MTS) systems. In MTS, data placement must be dynamic to align with evolving workload patterns through a migration policy that continuously upgrades or downgrades pages between tiers. However, managing these movements is challenging, as traditional rule-based methods often lack the flexibility to handle complex workloads and fail to account for hardwarespecific properties, such as SSD read-write asymmetry and internal parallelism. To address these limitations, we recently presented ReStore, a lightweight, page-level Reinforcement Learningbased migration policy that adaptively optimizes data placement by considering both workload and storage device characteristics. Experimental results using industry-grade benchmarks and reallife traces show that ReStore achieves up to 6x lower runtime and 48x fewer migrations compared to state-of-the-art baselines. In this demonstration, we present a web simulation of an MTS where we integrate ReStore along with five other baseline policies. The conference participants can configure storage tier properties, generate custom workloads, and observe ReStore’s realtime behavior (data placement and migration between tiers) alongside the baseline approaches. The demonstration is available at: <https://disc-projects.bu.edu/ReStore/research.html>.
