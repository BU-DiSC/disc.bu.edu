---
title: 'Telomere: Real-Time NAND Flash Storage'
date: 2022-01-14 19:27:00 +0000
tags:
- ACM TECS
venue: ACM Transactions on Embedded Computing Systems, Vol. 21(1), 2022, (Special Issue on Memory and Storage Systems for Embedded and IoT Applications)
authors: Katherine Missimer, Manos Athanassoulis, Rich West
links:
- label: ACM DL
  url: https://dl.acm.org/doi/fullHtml/10.1145/3479157
order: 36
permalink: /papers/tocs22-missimer
---

# Abstract

Modern solid-state disks achieve high data transfer rates due to their massive internal parallelism. However, out-of-place updates for flash memory incur garbage collection costs when valid data needs to be copied during space reclamation. The root cause of this extra cost is that solid-state disks are not always able to accurately determine data lifetime and group together data that expires before the space needs to be reclaimed. Real-time systems found in autonomous vehicles, industrial control systems, and assembly-line robots store data from hundreds of sensors and often have predictable data lifetimes. These systems require guaranteed high storage bandwidth for read and write operations by mission-critical real-time tasks. In this article, we depart from the traditional block device interface to guarantee the high throughput needed to process large volumes of data. Using data lifetime information from the application layer, our proposed real-time design, called Telomere, is able to intelligently lay out data in NAND flash memory and eliminate valid page copies during garbage collection. Telomere’s real-time admission control is able to guarantee tasks their required read and write operations within their periods. Under randomly generated tasksets containing 500 tasks, Telomere achieves 30% higher throughput with a 5% storage cost compared to pre-existing techniques.
