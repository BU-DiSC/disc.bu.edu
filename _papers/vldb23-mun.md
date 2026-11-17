---
title: On-the-fly Data Transformation in Action
date: 2023-08-02 23:11:00 +0000
tags:
- PVLDB
- Demo
venue: Proceedings of the VLDB Endowment, Vol. 16(12), 2023
authors: Ju Hyoung Mun, Konstantinos Karatsenidis, Tarikul Islam Papon, Shahin Roozkhosh, Denis Hoornaert, Ahmed Sanaullah, Ulrich Drepper, Renato Mancuso, Manos Athanassoulis
links:
- label: Official PDF
  url: https://www.vldb.org/pvldb/vol16/p3950-mun.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/vldb23-mun.pdf
- label: Code
  url: https://github.com/BU-DiSC/relational-memory/tree/master/vldb2023
- label: Poster
  url: https://cs-people.bu.edu/mathan/publications/posters/vldb23-mun-demo-poster.pdf
order: 54
permalink: /papers/vldb23-mun
---

# Abstract

Transactional and analytical database management systems (DBMS) typically employ different data layouts: row-stores for the first and column-stores for the latter.
In order to bridge the requirements of the two without maintaining two systems and two (or more) copies of the data,
our proposed system Relational Memory employs specialized hardware that transforms the base row table into arbitrary column groups at query execution time. This approach maximizes the cache locality and is easy to use via a simple abstraction that allows transparent on-the-fly data transformation.
Here, we demonstrate how to deploy and use Relational Memory via four representative scenarios. The demonstration uses the full-stack implementation of Relational Memory on the Xilinx Zynq UltraScale+ MPSoC platform. Conference participants will interact with Relational Memory deployed in the actual platform.
