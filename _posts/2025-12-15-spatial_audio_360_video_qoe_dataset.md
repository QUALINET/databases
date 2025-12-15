---
title: Multimodal Gaze, Physiology, and Pose Data for Evaluating Spatial Audio in 360° Videos
database: Spatial Audio 360° Video QoE Dataset
categories:
- video
author: Amit Hirway, Yuansong Qiao, Niall Murray (Technological University of the Shannon)
external_link: https://zenodo.org/records/17099830
access: Openly available for download from Zenodo
publicly_available: true
doi: 10.5281/zenodo.17099830
citation: 'Hirway, A., Qiao, Y., & Murray, N. (2024). A Quality of Experience and Visual Attention Evaluation for 360° Videos with Non-spatial and Spatial Audio. ACM Transactions on Multimedia Computing, Communications, and Applications, 20(9), 1-20. https://doi.org/10.1145/3650208'
license: Creative Commons Attribution 4.0 International (CC-BY-4.0)
contact_name: Amit Hirway
contact_email: a.hirway@research.ait.ie
subjective_scores: true
total: 73
method: Likert scale
tags:
- virtual reality
- 360-degree video
- spatial audio
- qoe
- eye tracking
- ambisonics
- visual attention
- physiological measurements
---

This comprehensive multimodal dataset examines how spatial sound affects participants' visual attention and Quality of Experience (QoE) in immersive 360° environments. The study involved 73 participants who experienced identical video content under four distinct audio conditions: silence, stereo, first-order Ambisonics, and third-order Ambisonics.

The dataset contains 288 gaze data files (eye gaze and pupil diameter), 288 pose data files (head pitch and yaw), and 72 heart rate files, sampled at 120 Hz for gaze/pose and 1 Hz for heart rate. Data was collected using head-mounted displays with integrated eye tracking, rotating chairs supporting 3 degrees of freedom, and the Empatica E4 wearable for physiological measurements. The dataset also includes subjective questionnaire responses using a 20-item assessment with a 5-point Likert scale.

The data is organized into eight folders by audio condition and environment type. A companion browser-based tool called JSAmbisonics is available on GitHub, featuring spatial audio playback and real-time gaze overlays built with Three.js and Omnitone. This work was published in ACM Transactions on Multimedia Computing, Communications, and Applications (2024).
