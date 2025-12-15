---
title: AVT-ECoClass-VR - An Open-Source Audiovisual 360° Video and Immersive CGI Multi-Talker Dataset
database: AVT-ECoClass-VR
categories:
- audiovisual
author: Stephan Fremerey (Audiovisual Technology Group, Technische Universität Ilmenau), Carolin Breuer, Janina Fels (Institute for Hearing Technology and Acoustics, RWTH Aachen University), Larissa Leist, Maria Klatte (Center for Cognitive Science, RPTU Kaiserslautern), Alexander Raake (Audiovisual Technology Group, Technische Universität Ilmenau)
external_link: https://github.com/Telecommunication-Telemedia-Assessment/AVT-ECoClass-VR
access: Openly available for download from https://avtshare01.rz.tu-ilmenau.de/avt-ecoclass-vr/ (approximately 3.7 TB)
publicly_available: true
doi: 10.1109/QoMEX61742.2024.10598262
citation: 'Fremerey, S., Breuer, C., Leist, L., Klatte, M., Fels, J., & Raake, A. (2024). AVT-ECoClass-VR: An open-source audiovisual 360° video and immersive CGI multi-talker dataset to evaluate cognitive performance. In 2024 16th International Conference on Quality of Multimedia Experience (QoMEX), 207-213. https://doi.org/10.1109/QoMEX61742.2024.10598262'
license: Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
subjective_scores: true
total: 220
src: 20
tags:
- 360-degree video
- virtual reality
- cognitive performance
- multi-talker
- binaural audio
- cgi
---

This comprehensive audiovisual dataset examines how complex visual and acoustic scenes affect cognitive performance in virtual classroom scenarios. Presented at QoMEX 2024, the dataset was developed as part of the DFG-funded ECoClass-VR project (DFG-444697733) to investigate audiovisual scene analysis across age groups from children to adults using a speaker-story mapping task paradigm.

The dataset contains 220 video recordings (MOV format, 7680x3840 resolution) and 200 single-channel audio recordings (WAV format, 48000 Hz) of 20 native German speakers arranged in a circular classroom configuration. Each speaker read ten different stories, plus recordings of speakers in silence. The dataset includes 65 pre-rendered sample videos (MP4 format) and example subjective data from participants.

Two distinct audiovisual scenarios are provided: 360° omnidirectional video and computer-generated imagery (CGI). The implementations support both binaural audio synthesis using the Virtual Acoustics auralization framework and diotic presentations. The CGI version is built in Unity and supports HTC Vive controller interaction, while both scenarios enable investigation of how acoustic representation (diotic vs. binaural) and visual representation (360° video vs. CGI) impact cognitive performance and audiovisual scene analysis.

The companion repository AVT-ECoClass-VR-dataset (DOI: 10.5281/zenodo.14019040) provides subjective experiment data from three studies with 94 total participants (36, 24, and 34 respectively), including head/controller tracking with timestamps, speaker-story mappings, and questionnaire responses covering simulator sickness (SSQ), presence (IPQ), workload (NASA RTLX), listening effort, and noise sensitivity assessments. The subjective results were published in Frontiers in Psychology, Volume 16, 2025 (DOI: 10.3389/fpsyg.2025.1520630).

This collaborative work between TU Ilmenau, RWTH Aachen University, and RPTU Kaiserslautern provides valuable resources for research on immersive audiovisual quality, cognitive performance assessment in virtual environments, classroom acoustics, multi-talker scenarios, and the effects of different rendering approaches on user experience and task performance.
