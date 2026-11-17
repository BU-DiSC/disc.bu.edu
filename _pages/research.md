---
title: Projects
permalink: /research
banner: research
---

The common theme of our research is **data systems** and **access methods**. Key to our approach is studying the **workload properties**, **data properties**, and the **underlying hardware**. We are interested in supporting new complex workloads, integrating new technologies, exploit data characteristics, offering algorithmic improvements in system design, and building new data management technology for the cloud.

Our work is supported by NSF Grants [IIS-1850202](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1850202&HistoricalAwards=false) and [IIS-2144547](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2144547&HistoricalAwards=false), as well as multiple gifts and fellowships from Facebook, Cisco, Red Hat, IBM, and Meta.

# Data Structures for Hybrid Analytics

Data-intensive real-time applications need data systems that support very efficient updates for incoming data. In addition, they need to provide fast access to old and fresh data alike for both historical analytics (i.e., long-term decisions) and real-time analytics. Building systems that can support such hybrid transactional/analytical processing (HTAP), however, is challenging the state-of-the-art data systems architectures; it requires rethinking of aspects like resource management, data layout, data organization, indexing, physical design, and query processing.

We propose new solutions that balance the conflicting requirements of read-intensive and update-intensive workloads by proposing new access method designs, and leveraging optimization techniques that have not been traditionally used for real-time decisions for data systems design and tuning.

**Access Method Design Space.**
An organic result of this research is a new classification of access method designs that enables both researchers and practitioners to have a better understanding of the access method design space and its tradeoffs. Several open questions remain, including how to combine seemingly incompatible designs, how to adapt to incoming workloads, and how to monitor and predict workload changes.

We perform extensive work on:

- LSM-Trees, where we focus on tuning, performance improvements, reducing CPU and memory consumption, optimize compaction policy design and decisions, and meeting requirements for user data deletion.
- B-Tree variants, where we focus on building tree indexes that are capable of exploiting any degree of data sortedness to accelerate ingestion without jeopardizing their good properties.
- Bitmap Indexes, where we focus on making them update-friendly and concurrency-aware. This works makes Bitmap Indexes suitable for general-purpose use, allowing for a paradigm shift.

# Exploiting Workload and Dataset Knowledge

We study how to use knowledge for the nature of the workload and the (pre-existing or inherent) organization of the data to (i) avoid redundant work, (ii) reduce the update and/or the read cost, and (iii) select the best access and query processing strategy.

**Uncertainty in Workload (LSM).**
In addition to using *exact* workload knowledge to find the best tuning of the system, we consider having a degree of workload *uncertainty* in our inputs when tuning. To address this challenge, we develop a Robust Tuning paradigm which tries to find a "good enough" solution when the observed workload is in a neighborhood of an expected workload. More accurately, we search for the tuning that minimized the worst-case in this neighborhood.

**Access Patter Skew (LSM).** If we have fine-grained information of access patterns, we can allocated auxiliary metadata in a way that maximizes their impact. We apply this principle in buffering and memory allocation for Bloom filters for LSM-trees. We use simple statistics including queries received and empty vs. non-empty queries to estimate the utility of the BF for every LSM component (SST file) and allocate memory or buffer filters accordingly.

**Join Correlation Skew.**
When considering binary joins, knowing the join correlation distribution unlocks the potential for an optimal partitioning strategy. We use the join correlation skew (that is, the matches of each row with the joining relation) and propose an algorithm that provably has lower number of expected I/O cost than any prior binary join algorithm.

**Data Sortedness (Tree Indexes).**
One way to think indexes, is as "the process of adding structure to an otherwise unstructured data collection". In this work, we examine near-sorted data collections that may be ingested to an index. This property can be found in many practical use-cases, for example, near-monotonically increasing stock-market data, a previously sorted but updated data collection, and multi-plexed time series data from different sources that may not come in perfect order. Our intuition is that near-sorted data ingestion should be very close to bulk loading, but in practice this is not the case. Here, we employ a collection of techniques that includes buffering, query-driven sorting, and partial bulk loading to achieve our goal. We also investigate simpler and more elegant designs that can be easily integrated in production systems.

# Timely Persistent Deletes

The new paradigm of large-scale data management in the cloud has focused on supporting fast ingestion rates and efficient access times, leaving data privacy, data stewardship, and minimizing data retention cost as secondary goals. A key aspect of data privacy and stewardship is to offer efficient and definite deletion when it is required by an application, a user, or the legislation. In addition to privacy, efficient deletion also helps to manage storage resources, by limiting the storage utilization and the corresponding energy consumption over data that are scheduled to be deleted. In the context of cloud computing, excessive storage utilization, and energy consumption amount to wasting petabytes of storage space and tens of millions of dollars.

In this work, we study how storage engines implement deletion, and we develop a family of algorithms (targeting the way LSM is compacting data), to offer concrete guarantees about the maximum persistent deletion delay so that systems can be compliant with regulation. We also propose an extension to SQL to declaratively express such requirements. Different types of deletes (e.g., point deletes, range deletes) pose new interesting challenges. Further, erasure of a data object physically from all layers of the cloud hierarchy including data systems, caching, file systems, and device drivers, remains an interesting open challenge.

# Integrating New Storage Hardware

New storage and processing devices are challenging traditional assumptions when designing a data system. Rotational disks have been very well modeled and studied, however, modern devices have very different behavior. We propose a new way to view this problem by augmenting the hardware modeling flexibility without proposing a complex model; usability of the model is the primary goal. Our research focuses on capturing the fundamental behavioral changes of storage hardware: *concurrency* and cost *asymmetry* of read vs. write operations, that are common in modern SSD devices.

We propose a Parametric I/O Cost Model that makes asymmetry and concurrency first class citizens and we use it to propose new data-intensive algorithms. We propose a family of new bufferpool management strategies that carefully exploit the concurrency of the devices to counteract the asymmetry by writing-back pages in parallel. We also propose new variations of graph traversal algorithms that allow for traversing a frontier of the graph while maitaining the classical guarantees of the traversal algorithm (e.g., BFS), leaving to faster exploration of the graph.

# Effortless Locality via On-the-fly Data Transformation

A key bottleneck in data-intensive applications is data movement through the memory hierarchy, since often an application (a database accessing a table, or an ML system accessing a tensor) is interested for a subset of a data object (e.g., only 3 of the table's columns) but other data may be also shipped, or a tuple reconstruction cost has to be paid in the case of columnstores.

In this work, we build custom hardware that sits between the physical memory and the CPU and acts as an on-the-fly data transformation engine. It captures declarative representations of the data transformation and reads from a standard dense representation of the data discarding unnecessary data on the fly and shipping to the CPU cache lines that useful data packed. This leads to better locality and overall performance than the state of the art. Our next steps include integrating this to the memory controller.
