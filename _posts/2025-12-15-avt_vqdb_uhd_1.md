---
title: AVT-VQDB-UHD-1 - A Large Scale Video Quality Database for UHD-1
database: AVT-VQDB-UHD-1
categories:
- video
author: Rakesh Rao Ramachandra Rao, Steve Göring, Werner Robitza (Audiovisual Technology Group, Technische Universität Ilmenau), Bernhard Feiten (Deutsche Telekom AG), Alexander Raake (Audiovisual Technology Group, Technische Universität Ilmenau)
external_link: https://github.com/Telecommunication-Telemedia-Assessment/AVT-VQDB-UHD-1
access: Openly available for download from https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/ (approximately 55GB)
publicly_available: true
doi: 10.1109/ISM46123.2019.00012
citation: 'Rao, R. R. R., Göring, S., Robitza, W., Feiten, B., & Raake, A. (2019). AVT-VQDB-UHD-1: A Large Scale Video Quality Database for UHD-1. In 2019 IEEE International Symposium on Multimedia (ISM), 17-177. https://doi.org/10.1109/ISM46123.2019.00012'
license: GNU General Public License v3 (code), mixed licenses for video content including Creative Commons Attribution 3.0 (Big Bucks Bunny), Netflix licensing, and CC BY-NC 4.0 for TU Ilmenau content
subjective_scores: true
resolution: 360p, 540p, 720p, 1080p, 1440p, 2160p
method: Subjective quality assessment with MOS scores and confidence intervals
tags:
- uhd-1
- 4k
- h264
- hevc
- vp9
- dash
- vmaf
- mos
---

This large-scale video quality database presents comprehensive subjective and objective quality assessment of 4K ultra-high-definition videos. Initially published at IEEE ISM 2019, the database consists of short-term videos of segment length similar to DASH segments, based on several short movies that are either publicly available or created by TU Ilmenau.

The dataset contains four subjective test datasets (test_1 through test_4) with videos encoded using three different video codecs: H.264, HEVC, and VP9. The resolutions of the compressed videos range from 360p to 2160p with frame rates varying from 15fps to 60fps. All source 4K contents use 60fps, maintaining 3840 × 2160 pixel resolution (UHD-1).

The database includes encoded video segments, source videos, subjective ratings presented as Mean Opinion Scores (MOS) with confidence intervals, objective quality scores, and additional metrics including BRISQUE, NIQE, and VMAF reports. This comprehensive collection enables research on codec performance comparison and quality model validation.

The database has been utilized in multiple QoMEX conference publications, particularly for ITU-T P.1204.3 video quality model evaluation and related video quality assessment research.
