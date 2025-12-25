---
title: AVT-VQDB-UHD-1-Appeal - A UHD-1/4K Open Dataset for Video Quality and Appeal Assessment
database: AVT-VQDB-UHD-1-Appeal
categories:
- video
author: Rakesh Rao Ramachandra Rao, Steve Göring, Bassem Elmeligy, Alexander Raake (Audiovisual Technology Group, Technische Universität Ilmenau)
external_link: https://github.com/Telecommunication-Telemedia-Assessment/AVT-VQDB-UHD-1-Appeal
access: Openly available for download via provided download.sh tool (requires wget and unzip)
publicly_available: true
doi: 10.1109/MMSP59012.2023.10337713
citation: 'Rao, R. R. R., Göring, S., Elmeligy, B., & Raake, A. (2023). AVT-VQDB-UHD-1-Appeal: A UHD-1/4K Open Dataset for Video Quality and Appeal Assessment Using Modern Video Codecs. In 2023 IEEE 25th International Workshop on Multimedia Signal Processing (MMSP), 1-6. https://doi.org/10.1109/MMSP59012.2023.10337713'
license: GNU General Public License v3.0 (code), mixed licenses for videos (Creative Commons BY 3.0, Netflix license, NASA license, CC BY-NC 4.0 for original content)
subjective_scores: true
resolution: 360p, 720p, 1080p, 2160p
tags:
- uhd-1
- 4k
- video appeal
- hevc
- av1
- vvc
- h265
- h266
---

This UHD-1/4K open dataset examines both video quality and appeal assessment using modern video codecs, addressing the important distinction between technical quality and aesthetic appeal in video streaming content. Presented at IEEE MMSP 2023 in Poitiers, France, the research was conducted as part of the Deutsche Forschungsgemeinschaft (DFG) funded Sophoappeal project (DFG-437543412).

The dataset contains short video segments (8-10 seconds each) from various sources, encoded using three modern video codecs: HEVC/H.265, AV1, and VVC/H.266. Videos span multiple resolutions (360p to 2160p) and bitrates (100kbps to 15mbps), enabling comprehensive analysis of encoding parameter effects on perceived video quality and appeal.

The subjective methodology employed a unique three-part experimental protocol. First, participants rated the appeal of uncompressed UHD-1/4K source content. Second, they assessed the quality of encoded versions across various codec, resolution, and bitrate combinations. Third, participants re-rated the source content appeal, allowing investigation of the bidirectional relationship between appeal and quality perception. This approach enables research on how encoding-related degradations interact with inherent content appeal.

The database includes both subjective scores collected via the AVRateNG tool and objective quality predictions from multiple models including VMAF, SI/TI values, hybrid model (hyn0) scores, and no-reference (nofu) scores. The research examines how different encoding conditions impact perceived video quality and investigates whether source content appeal influences quality perception and vice versa.

This dataset is part of the broader AVT-VQDB-UHD-1 series from TU Ilmenau's Audiovisual Technology Group, extending the original database with explicit appeal assessment alongside traditional quality evaluation.
