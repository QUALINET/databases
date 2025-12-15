---
title: AVT 360° Streaming Video Quality Dataset - Subjective Test Dataset and Meta-data-based Models
database: AVT 360° Streaming Video Quality Dataset
categories:
- video
author: Stephan Fremerey, Steve Göring, Rakesh Rao Ramachandra Rao (Audio Visual Technology Group, Technische Universität Ilmenau), Rachel Huang (Huawei Technologies Co. Ltd.), Alexander Raake (Audio Visual Technology Group, Technische Universität Ilmenau)
external_link: https://github.com/Telecommunication-Telemedia-Assessment/360_streaming_video_quality_dataset
access: Openly available for download from Zenodo (534.3 MB compressed, 93.0 GB total)
publicly_available: true
doi: 10.1109/MMSP48831.2020.9287065
citation: 'Fremerey, S., Göring, S., Rao, R. R. R., Huang, R., & Raake, A. (2020). Subjective Test Dataset and Meta-data-based Models for 360° Streaming Video Quality. In 2020 IEEE 22nd International Workshop on Multimedia Signal Processing (MMSP), 1-6. https://doi.org/10.1109/MMSP48831.2020.9287065'
license: Creative Commons Attribution 4.0 International (CC-BY-4.0)
subjective_scores: true
total: 191
resolution: 4K, 6K, 8K
method: 5-point Absolute Category Rating (ACR)
tags:
- 360-degree video
- adaptive streaming
- 4k
- 6k
- 8k
- htc vive
- htc vive pro
- vmaf
- omnidirectional video
---

This comprehensive dataset examines 360-degree video streaming quality under real-world conditions, presented at IEEE MMSP 2020 in Tampere, Finland. The research addresses the challenge of quality assessment for adaptive streaming of omnidirectional video content, which is critical for virtual reality and immersive media applications.

The dataset comprises three subjective test rounds with a total of 191 stimuli (64 stimuli in tests 1 and 2, 63 stimuli in test 3) at resolutions of 4K, 6K, and 8K using real-world streaming bitrates. Testing was conducted using HTC Vive for the initial test and HTC Vive Pro for subsequent tests, with quality assessments collected using the 5-point Absolute Category Rating (ACR) scale.

The dataset provides comprehensive information for each stimulus including source video links, subjective quality scores, video metadata, head rotation tracking data, and Simulator Sickness Questionnaire (SSQ) responses per stimulus and participant. This rich multimodal data enables research on the relationship between user behavior (head movements), physiological responses (simulator sickness), and perceived video quality in 360-degree streaming scenarios.

Multiple quality metrics were evaluated including VMAF, PSNR, SSIM, ADM2, WS-PSNR, and WS-SSIM. The key finding showed that VMAF demonstrated the highest correlation with subjective scores among all tested metrics. A center-cropped VMAF variant achieved comparable performance while enabling significantly faster computation, making it more practical for real-time streaming applications.

The research developed two lightweight quality prediction models: a bitstream metadata-based approach using only encoding parameters, and a hybrid no-reference model utilizing bitrate, resolution, and pixel data. Both models achieved performance levels similar to full-reference approaches while requiring substantially less computational resources, making them suitable for integration into adaptive streaming systems.

This work, conducted in collaboration with Huawei Technologies, has been influential with 16 citations and 112 dataset downloads. The dataset is hosted on Zenodo (DOI: 10.5281/zenodo.4090961) under Creative Commons Attribution 4.0 International License, supporting reproducible research on 360-degree video quality assessment, adaptive streaming optimization, and the development of efficient quality metrics for immersive video content.
