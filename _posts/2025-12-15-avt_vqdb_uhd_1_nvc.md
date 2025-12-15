---
title: AVT-VQDB-UHD-1-NVC - A Subjective and Objective Video Quality Dataset for Neural and Traditional Video Codecs
database: AVT-VQDB-UHD-1-NVC
categories:
- video
author: Benjamin Herb, Rakesh Rao Ramachandra Rao, Steve Göring (Technische Universität Ilmenau), Alexander Raake (RWTH Aachen University)
external_link: https://github.com/Telecommunication-Telemedia-Assessment/AVT-VQDB-UHD-1-NVC
access: Openly available for download from https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1-nvc/ (source videos ~13 GB, processed videos ~74 GB)
publicly_available: true
doi: 10.48550/arXiv.2511.00969
citation: 'Herb, B., Rao, R. R. R., Göring, S., & Raake, A. (2025). Evaluating Video Quality Metrics for Neural and Traditional Codecs using 4K/UHD-1 Videos. Preprint submitted to Picture Coding Symposium (PCS) 2025. arXiv:2511.00969'
license: Open access
subjective_scores: true
total: 216
src: 6
ratings: 6480
method: 5-point Absolute Category Rating (ACR)
resolution: 360p, 720p, 1080p, 2160p
tags:
- uhd-1
- 4k
- neural video codec
- nvc
- av1
- vvc
- dcvc-fm
- dcvc-rt
- acr
- vmaf
---

This comprehensive dataset presents subjective and objective video quality evaluation for both neural and traditional video codecs using 4K/UHD-1 resolution videos. The research, to be presented at Picture Coding Symposium (PCS) 2025 in Aachen, Germany, addresses the critical question of whether existing quality metrics remain valid for evaluating neural video codecs (NVCs) as they emerge as promising alternatives to traditional compression methods.

The dataset contains 216 encoded sequences derived from 6 source videos (8-10 seconds each, 4K/UHD-1, 60 fps, YUV420p 8-bit format) selected from the AVT-VQDB-UHD-1 database. Videos were encoded at four resolutions (360p to 2160p) using nine different quality parameters with four codecs: traditional codecs AV1 (v3.12.0) and VVC/H.266 (vvencFFapp v1.13.1), and neural codecs DCVC-FM and DCVC-RT.

Subjective testing involved 30 participants (students and employees) with 26 passing outlier detection (Pearson correlation >0.75), collecting 6,480 ratings (33 excluded due to technical errors) using the 5-point Absolute Category Rating (ACR) method. The controlled viewing environment used a 43-inch UHD monitor at 1.5H viewing distance.

The research evaluated 13 quality metrics across full-reference (PSNR, SSIM, MS-SSIM, VMAF variants, CVQA-FR, LPIPS), no-reference (MUSIQ, CVQA-NR, FasterVQA, Dover, Q-Align), and hybrid (AVQBits|H0|f) categories. Results showed that VMAF and AVQBits|H0|f demonstrated strong Pearson correlation, while FasterVQA excelled among no-reference metrics. Notably, metric reliability showed no significant performance differences between traditional and neural video codecs, validating the use of existing quality metrics for evaluating neural codec performance.
