---
title: 'BoDS: A Benchmark on Data Sortedness'
date: 2022-08-01 19:43:41 +0000
tags:
- TPCTC Workshop
venue: ', 2022'
authors: Aneesh Raman, Konstantinos Karatsenidis, Subhadeep Sarkar, Matthaios Olma, Manos Athanassoulis
links:
- label: Official Page
  url: https://link.springer.com/chapter/10.1007/978-3-031-29576-8_2
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/tpctc22-raman.pdf
- label: Presentation Video
  url: https://www.youtube.com/watch?v=sb6jw0zz-CU
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/tpctc22-raman.pdf
- label: Code
  url: https://github.com/BU-DiSC/bods
order: 43
permalink: /papers/tpctc22-raman
---

# Abstract

Indexes in data systems accelerate data access by adding structure to otherwise unstructured data at the cost of index construction and maintenance. Data systems, and particularly, the underlying indexing data structures are designed to offer favorable ingestion (and query) performance for the two extremes of data sortedness, i.e., unsorted data (often assumed to follow a uniform random distribution) or fully-sorted data. However, in practice, data may arrive with an intermediate degree of pre-sortedness. In such cases, where data arrives nearly (but not necessarily fully) sorted, the intuition is that the indexing cost should be lower than when ingesting unsorted data. Such sortedness-aware index designs lack from the literature. In fact, there is a need for a framework to explore how index designs may be able to exploit pre-existing sortedness during data ingestion to amortize the index construction cost.

In this paper, we present Benchmark on Data Sortedness, BoDS for short, that highlights the performance of data systems in terms of index construction and navigation costs when operating on data ingested with variable sortedness. To quantify data sortedness, we use the state-of-the-art (K,L)-sortedness metric. Specifically, BoDS benchmarks the indexing performance of a data system as we vary the two fundamental components of the metric: (i) K, that measures how many elements are out-of-order in a data collection; and (ii) L, that measures by how much the out-of-order entries are displaced from their respective in-order positions; as well as (iii) the distribution of L. We present in detail the benchmark, and we run it on PostgreSQL, a popular, production-grade relational database system. Unsurprisingly, we observe that PostgreSQL cannot exploit data sortedness; however, through our experiments we show the headroom for improvement, and we lay the groundwork for experimentation with sortedness-aware index designs.
