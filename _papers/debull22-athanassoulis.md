---
title: Building Deletion-Compliant Data Systems
date: 2022-03-02 03:21:00 +0000
tags:
- IEEE DEBULL
venue: IEEE Data Engineering Bulletin, Vol. 45(1), 2022
authors: Manos Athanassoulis, Subhadeep Sarkar, Tarikul Islam Papon, Zichen Zhu, Dimitris Staratzis
links:
- label: Official PDF
  url: http://sites.computer.org/debull/A22mar/p21.pdf
- label: Local PDF
  url: https://cs-people.bu.edu/mathan/publications/debull22-athanassoulis-preprint.pdf
order: 38
permalink: /papers/debull22-athanassoulis
---

# Abstract

Most modern data systems have been designed with two goals in mind – fast ingestion and low-latency query processing. The first goal has led to the development of a plethora of write-optimized data stores that employ the out-of-place paradigm. Due to their write-optimized design, out-of-place data systems perform deletes logically via invalidation, and retain the invalid data for arbitrarily long. However, due to the recent enactment of new data privacy regulations, the requirement of timely deletion of user data has become central. The right to be forgotten (in EU’s GDPR), right to delete (in California’s CCPA and CPRA), or deletion right (in Virginia’s VCDPA) mandates that service providers persistently delete a user’s data within a pre-set time duration. Logical deletion in out-of-place data systems, however, does not offer guarantees for timely and persistent deletion, and attempting to enforce it using existing tools leads to poor performance and increased operational costs.

In this paper, we present a new framework for building deletion-compliant data systems from a holistic perspective. We analyze the new regulations and the requirements derived from the new policies, and we propose changes in the application and the system layer of data management. We outline the new types of deletion requests that need to be supported, the query language modifications needed to be able to request for timely persistent data deletion, and the system-level changes needed to realize timely and persistent deletes. The proposed framework for deletion compliance lays the groundwork for a new class of data systems that can offer system-level guarantees for user data privacy. We present recent results spanning all layers of the framework: the requirements and the application layer target any database system, while the system layer discussion is geared towards out-of-place systems. Finally, we conclude with a discussion on next steps and open challenges on building deletion-compliant data systems.
