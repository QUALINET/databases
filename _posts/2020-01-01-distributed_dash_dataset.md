---
access: 'The content is available via HTTP: Link: http://www-itec.aau.at/ftp/datasets/mmsys13/'
author: "Alpen-Adria-Universit\xE4t Klagenfurt"
categories:
- audiovisual
citation: If you use our data for your own publications please do not forget to reference
  the website and our paper [LMT13].
contact_name: Information for the database may be obtained by contacting Christian
  Timmerer (christian.timmerer@itec.uni-klu.ac.at)
database: Distributed DASH Dataset
deprecated: false
excerpt: ''
external_link: http://www-itec.uni-klu.ac.at/dash/?page_id=958
hrc: 17
partner: true
publicly_available: true
references:
  LMT13: "Lederer, S., Mueller, C., Timmerer, C., Concolato, C., Le Feuvre, J., and\
    \ Fliegel, K., 2013. Distributed DASH dataset. In Proceedings of the 4rd Multimedia\
    \ Systems Conference (MMSys \u201913). ACM, New York, NY, USA."
resolution: 320x240, 480x360, 854x480, 1280x720, 1920x1080
src: 1
subjective_scores: false
tags:
- audiovisual
title: Distributed DASH Dataset
total: 17
---

D-DASH is a dataset of content for the Dynamic Adaptive Streaming over HTTP (DASH) standard from MPEG. It is mirrored over different sites at different locations to perform, e.g.,  CDN-based scientific evaluations. The delivery of multimedia content over HTTP and on top of existing Internet infrastructures is becoming the preferred method within heterogeneous environment. The basic design principle is having an intelligent client which selects given and applicable media representations by issuing HTTP requests for individual segments based on the users' context and current conditions. Typically, this client behavior differs between implementations of the same kind and for the objective evaluations thereof appropriate datasets are needed. This paper presents a distributed dataset for the recently published MPEG-DASH standard which is mirrored at different sites across Europe, namely Klagenfurt, Paris, and Prague. A client implementation may choose to request segments from these sites and dynamically switch to a different location, e.g., in case the one currently used causes any issues. Hence, this distributed DASH dataset can be used for real-world evaluations enabling the simulation of switching between different content delivery networks. Finally, it is also offers a registration service for additional sites to join and, thus, expand the distribution of the dataset even further.