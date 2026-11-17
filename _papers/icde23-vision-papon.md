---
title: 'Relational Fabric: Transparent Data Transformation'
date: 2023-04-04 15:24:00 +0000
tags:
- IEEE ICDE
venue: Proceedings of the IEEE International Conference on Data Engineering (IEEE ICDE), 2023
authors: Tarikul Islam Papon, Ju Hyoung Mun, Shahin Roozkhosh, Denis Hoornaert, Ahmed Sanaullah, Ulrich Drepper, Renato Mancuso, Manos Athanassoulis
links:
- label: IEEE Xplore
  url: https://ieeexplore.ieee.org/document/10184831
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/icde23-vision.pdf
- label: Slides
  url: https://cs-people.bu.edu/mathan/publications/slides/icde23-RelFabric.pdf
order: 50
permalink: /papers/icde23-vision-papon
---

# Abstract

A key design decision for data systems is whether they follow the row-store or the column-store paradigm. The former supports transactional workloads, while the latter is better for analytical queries. This decision has a significant impact on the entire data system architecture. The multiple-decade-long journey of these two designs has led to a new family of hybrid transactional/analytical processing (HTAP) architectures. Several efforts have been proposed to reap the benefits of both worlds by proposing systems that maintain multiple copies of data (in different physical layouts) and convert them into the desired layout as required. Due to data duplication, the additional necessary bookkeeping, and the cost of converting data between different layouts, these systems compromise between efficient analytics and data freshness. We depart from existing designs by proposing a radically new approach. We ask the question:

> “What if we could access any layout and ship only the relevant data through the memory hierarchy by transparently converting rows to (arbitrary groups of) columns?”

To achieve this functionality, we capitalize on the reinvigorated trend of hardware specialization (that has been accelerated due to the tapering of Moore’s law) to propose Relational Fabric, a near-data vertical partitioner that allows memory or storage components to perform on-the-fly transparent data transformation. By exposing an intuitive API, Relational Fabric pushes vertical partitioning to the hardware, which profoundly impacts the process of designing and building data systems. (A) There is no need for data duplication and layout conversion, making HTAP systems viable using a single layout. (B) It simplifies the memory and storage manager that needs to maintain and update a single data layout. (C) It reduces unnecessary data movement through the memory hierarchy allowing for better hardware utilization and, ultimately, better performance. In this paper, we present Relational Fabric for both memory and storage. We present our initial results on Relational Fabric for in-memory systems and discuss the challenges of building this hardware and the opportunities it brings for simplicity and innovation in the data system software stack, including physical design, query optimization, query evaluation, and concurrency control.
