---
title: 'AXE: A Task Decomposition Approach to Learned LSM Tuning'
date: 2025-08-24 10:06:46 +0000
tags:
- PVLDB
venue: Proceedings of the VLDB Endowment, Vol. 18(13), 2025
authors: Andy Huynh, Anwesha Saha, Harshal Chaudhari, Manos Athanassoulis
links:
- label: Official PDF
  url: https://www.vldb.org/pvldb/vol18/p5582-huynh.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/vldb25-huynh.pdf
order: 71
permalink: /papers/vldb25-huynh
---

# Abstract

Log-Structured Merge (LSM) trees are used as the data structure of choice for key-value stores supporting a wide variety of applications. A common challenge for LSM-based systems is tuning them effectively, particularly as the complexity and number of tuning knobs increase. Prior work relies on expert-created cost models and expert-configured numerical solvers to produce high-quality tunings; however, these methods do not address tuning multiple instances at scale for various execution environments.
On the other hand, using iterative learning, such as Bayesian Optimization (BO), relaxes the requirements for domain expertise and provides generalizability; however, it comes at a high cost, as it involves learning directly from database executions at deployment time. Furthermore, both approaches struggle with categorical tuning knobs that create a hard-to-navigate optimization space.

To address these challenges, we introduce AXE, a novel learned LSM tuning paradigm that decomposes the tuning task into two steps.
First, AXE trains a *learned cost model* using existing performance modeling or execution logs, acting as a surrogate cost function in the tuning process. Second, AXE efficiently generates arbitrarily many training samples for a *learned tuner* optimized to identify high-performance tunings using the learned cost model as its loss function. This task decomposition approach generalizes well for tuning simple and complex LSM designs and requires no retraining, allowing AXE to be used for tuning at scale. Compared to BO, AXE recommends higher performing tunings than BO 71% of the time while incurring 100x smaller tuning overhead. We further show that AXE requires less domain knowledge to produce optimal tunings than traditional expert-configured tuning pipelines. Lastly, we compare AXE to both state-of-the-art machine learning methods and analytical methods to show that AXE outperforms all other LSM tuning baselines.
