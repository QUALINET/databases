---
access: 'The files are available for download via HTTP. The raw datasets contain the
  original trace files logged by our measurement tools, compressed using crtpdumpz,
  and traceroute output for each trace (with IP addresses and hostnames anonymised).
  The processed datasets contain end-to-end queueing delay time series (both dataset-A
  and dataset-B), and end-to-middle delay measurements and packet-pair capacity measurements
  (dataset-B only). Link: http://web.cs.wpi.edu/~claypool/mmsys-dataset/2011/isp/'
author: University of Glasgow
categories: []
citation: Use of the datasets in published work should be acknowledged by a full citation
  to the paper [EPP11] at the MMSys conference (MMSys 11, February 23-25, San Jose,
  California, USA, Copyright 2011 ACM 978-1-4503-0517-4/11/02).
database: End-to-End and Network-Internal Measurements of Real-Time Traffic to Residential
  Users
broken_link: false
excerpt: ''
external_link: http://web.cs.wpi.edu/~claypool/mmsys-dataset/2011/isp/author.html
partner: false
publicly_available: true
references:
  EPP11: Martin Ellis, Colin Perkins, and Dimitrios Pezaros, End-to-End and Network-Internal
    Measurements on Real-Time Traffic to Residential Users, Proceedings of the First
    ACM Multimedia Systems Conference (MMSys), San Jose, CA, USA, February 23-25,
    2011.
subjective_scores: false
tags:
- network traces
title: End-to-End and Network-Internal Measurements of Real-Time Traffic to Residential
  Users
---

Little performance data currently exists for streaming high-quality Internet video to residential users. Data on streaming performance provides valuable input to the design of new protocols and applications, for example when evaluating congestion control and error-correction schemes, and for sizing playout buffers in video receivers. This paper presents measurements of streaming real-time UDP traffic to a number of residential users, and discusses the basic characteristics of the data. The following datasets are referenced from the paper. They contain measurements of CBR RTP traffic, sent from a campus machine to receivers connected to the Internet via ADSL and Cable links. Dataset-A contains only end-to-end measurements, while Dataset-B also includes some end-to-middle measurements obtained using TTL-limited probes, and packet-pair measurements from which the path capacities can be estimated. Dataset-A was collected between June and October 2009, while Dataset-B was collected between April and September 2010.