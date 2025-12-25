---
title: WebRTC-QoE - A Dataset of Quality of Experience in Audio-Video Communications
database: WebRTC-QoE Dataset
categories:
- audiovisual
author: Gulnaziye Bingol, Simone Porcu, Alessandro Floris, Luigi Atzori (University of Cagliari)
external_link: https://zenodo.org/records/15836614
access: Openly available for download from Zenodo and IEEE DataPort
publicly_available: true
doi: 10.21227/mb47-hf44
citation: 'Bingol, G., Porcu, S., Floris, A., & Atzori, L. (2024). WebRTC-QoE dataset of subjective scores, network impairments, and facial & speech features. Computer Networks, 244, 110356. https://doi.org/10.1016/j.comnet.2024.110356'
license: Creative Commons Attribution 4.0 International (CC-BY-4.0)
subjective_scores: true
total: 300
ratings: 300
method: ACR (Absolute Category Rating)
tags:
- webrtc
- qoe
- video calls
- audiovisual
- network impairments
- facial expression
- speech features
- openface
- opensmile
---

This comprehensive dataset examines user satisfaction in WebRTC video calls under various network conditions. It captures subjective evaluations from 20 subjects across 15 different test conditions with controlled network impairments including delay (0/500/1000 ms), jitter (0/500 ms), and packet loss (0/15/30%).

The 613.0 MB dataset combines objective metrics with subjective quality ratings using the Absolute Category Rating scale (1-5, Bad to Excellent), resulting in 300 ACR scores. The dataset includes four main components: subjective results (CSV, 4 KB), WebRTC internals session statistics (28.7 MB, 300 JSON files), facial expression features extracted using OpenFace (547 MB with gaze vectors, eye landmarks, and 35 action units), and speech features from the OpenSMILE toolkit (18.9 MB with 6,373 features per subject per condition).

The research was conducted at the University of Cagliari and published in Computer Networks (2024).
