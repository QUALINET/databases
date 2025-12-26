---
access: 'The files are available for download via HTTP. Link: http://home.ifi.uio.no/paalh/dataset/alfheim/'
author: University of Oslo
categories:
- video
citation: Use of the datasets in published work should be acknowledged by a full citation
  to the authors' papers [PJJ14] at the MMSys conference (Proceedings of ACM MMSys
  2014, March 19 - March 21, 2014, Singapore, Singapore).
contact_name: Svein Arne Pettersen (svein.arne.pettersen@uit.no)
database: Soccer Video and Player Position Dataset
broken_link: false
excerpt: ''
external_link: http://home.ifi.uio.no/paalh/dataset/alfheim/
other: ZXY sensor data
publicly_available: true
references:
  PJJ14: S. A. Pettersen, D. Johansen, H. Johansen, V. Berg-Johansen, V. R. Gaddam,
    A. Mortensen, R. Langseth, C. Griwodz, H. K. Stensland, and P. Halvorsen, Soccer
    video and player position dataset, Proceedings of ACM MMSys 2014, March 19 - March
    21, 2014, Singapore, Singapore.
subjective_scores: false
tags:
- video
title: Soccer Video and Player Position Dataset
---

Dataset of elite soccer player movements and corresponding videos. The dataset is captured at Alfheim Stadium -- the home arena for Tromsø IL (Norway). The player postions are measured at 20 Hz using the ZXY Sport Tracking system, and the video is captured from the middle of the field using two camera arrays. The player tracking system provides the player coordinates on the field, their speed, acceleration and force together with an ID and timestamp. The camera array covers the entire field, and each camera can be used individually or as a stitched panorama video. In addition to the obvious sport analytics scenario, the dataset can be used several ways. In the multimedia scenario, the combination of sensor data and video gives a researcher a video dataset with a ground truth object position from the sensor data, i.e., it can be used to test algorithms used for feature extraction, object tracking, background substraction, etc. The sensor data itself can also be used alone in simulations or experiments where for example the users with devices move on a limited area (the field) with a varying speed and direction.