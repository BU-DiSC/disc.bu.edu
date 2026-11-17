---
title: 'CUBIT: Concurrent Updatable Bitmap Indexing'
date: 2024-10-23 15:26:49 +0000
tags:
- PVLDB
venue: Proceedings of the VLDB Endowment, Vol. 18(2), 2024
authors: Junchang Wang, Manos Athanassoulis
links:
- label: Official PDF
  url: https://www.vldb.org/pvldb/vol18/p399-athanassoulis.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/vldb24-wang.pdf
- label: Artifacts
  url: https://github.com/junchangwang/CUBIT
order: 66
permalink: /papers/vldb24-wang
---

# Abstract

Bitmap indexes are widely used for read-intensive analytical workloads because they are clustered and offer efficient reads with a small memory footprint. However, they are notoriously inefficient to update. As analytical applications are increasingly fused with transactional applications, leading to the emergence of hybrid transactional/analytical processing (HTAP), it is desirable that bitmap indexes support efficient concurrent real-time updates. In this paper, we propose Concurrent Updatable Bitmap indexing (CUBIT) that offers efficient real-time updates that scale with the number of CPU cores used and do not interfere with queries. Our design relies on three principles. First, we employ a horizontal bitwise representation of updated bits, which enables efficient atomic updates without locking entire bitvectors. Second, we propose a lightweight snapshotting mechanism that allows queries (including range queries) to run on separate snapshots and provides a wait-free progress guarantee. Third, we consolidate updates in a latch-free manner, providing a strong progress guarantee. Our evaluation shows that CUBIT offers 3–16x higher throughput and 3–220x lower latency than state-of-the-art updatable bitmap indexes. CUBIT’s update-friendly nature widens the applicability of bitmap indexing. Experimenting with OLAP workloads with standard, batched updates shows that CUBIT overcomes the maintenance downtime and outperforms DuckDB by 1.2–2.7x on TPC-H. For HTAP workloads with real-time updates, CUBIT achieves 2–11x performance improvement over the state-of-the-art approaches.
