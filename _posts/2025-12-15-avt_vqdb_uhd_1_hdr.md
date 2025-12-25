---
title: AVT-VQDB-UHD-1-HDR - An Open Video Quality Dataset for Quality Assessment of UHD-1 HDR Videos
database: AVT-VQDB-UHD-1-HDR
categories:
- video
author: Rakesh Rao Ramachandra Rao, Benjamin Herb, Helmi-Aurora Takala, Mohamed Tarek Mohamed Ahmed, Alexander Raake (Audiovisual Technology Group, Technische Universität Ilmenau)
external_link: https://github.com/Telecommunication-Telemedia-Assessment/AVT-VQDB-UHD-1-HDR
access: Openly available for download from https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1-hdr/
publicly_available: true
doi: 10.1109/QoMEX61742.2024.10598284
citation: 'Rao, R. R. R., Herb, B., Takala, H.-A., Ahmed, M. T. M., & Raake, A. (2024). AVT-VQDB-UHD-1-HDR: An Open Video Quality Dataset for Quality Assessment of UHD-1 HDR Videos. In 2024 16th International Conference on Quality of Multimedia Experience (QoMEX), 179-185. https://doi.org/10.1109/QoMEX61742.2024.10598284'
license: GNU General Public License v3.0 (code), videos sourced from SJTU and GamingHDRVideoSet datasets
subjective_scores: true
total: 195
src: 5
method: ACR-HR (Absolute Category Rating - Hidden Reference)
resolution: 720p, 1080p, 1440p, 2160p
tags:
- uhd
- 4k
- hdr
- h265
- av1
- vvc
- acr-hr
---

This open video quality database presents a comprehensive empirical investigation combining subjective and objective methods for assessing the perceived quality of UHD-1 HDR videos. The dataset was developed within the PoQuMo8K project (ZIM No. KK5112706ER1) and presented at QoMEX 2024 in Karlshamn, Sweden.

The dataset contains 195 encoded videos derived from 5 source videos, all with 60 fps frame rate. The videos span four resolutions (720p to 2160p) and bitrates ranging from 0.5 to 40 Mbps, encoded using modern video codecs including H.265/HEVC, AV1, and VVC (Versatile Video Coding). Subjective testing was conducted using the ACR-HR (Absolute Category Rating - Hidden Reference) methodology.

The repository includes source videos, test videos rescaled to native display resolution, generated bitstreams, and both subjective test scores from AVRateNG and objective quality predictions from P.1204.3, hyn0 hybrid model, and VMAF. The research evaluates different full reference, bitstream, and hybrid instrumental models for their HDR quality prediction capability.
