---
title: The Need for a New I/O Model
date: 2020-12-22 02:26:41 +0000
tags:
- CIDR
venue: Proceedings of the Annual Conference on Innovative Data Systems Research (CIDR), 2021
authors: Tarikul Islam Papon, Manos Athanassoulis
links:
- label: Local PDF
  url: http://cs-people.bu.edu/mathan/publications/cidr21-papon.pdf
- label: Official PDF
  url: http://cidrdb.org/cidr2021/papers/cidr2021_abstract04.pdf
- label: Project Website
  url: http://disc-projects.bu.edu/parametric-io-model/
order: 31
permalink: /papers/cidr21-papon
---

# Abstract

Data-intensive applications performance is typically bounded by
the time needed to transfer data through the storage and memory
hierarchy. The traditional I/O model considers a two-level memory hierarchy with a fast internal memory of bounded size (memory) and a slow unbounded external memory (storage). This modeling approach closely describes reality when two key underlying assumptions hold: (i) disk reads and writes have similar cost, and (ii) applications can perform one I/O at a time. However, none of these assumptions are not true for solid-state disks (SSD) because of two fundamental SSD properties: (i) read/write asymmetry (writes are slower than reads) and (ii) concurrency (multiple I/Os can be processed because of high internal parallelism). The question we set out to answer is: How should the I/O model be adapted in light of read/write asymmetry and concurrency? We need a richer I/O model that can capture contemporary state-of-the-art (and future) devices by parameterizing asymmetry and concurrency. By capturing the device asymmetry and concurrency, we can make device-specific decisions at algorithm design time, rather than as an optimization during deployment and testing. Specifically, we envision better algorithm design for almost any component of a system that interacts with storage.
