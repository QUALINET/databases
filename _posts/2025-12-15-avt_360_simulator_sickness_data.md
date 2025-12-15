---
title: AVT 360-SimulatorSickness-Data - Assessment of the Simulator Sickness Questionnaire for Omnidirectional Videos
database: AVT 360-SimulatorSickness-Data
categories:
- video
author: Ashutosh Singla, Steve Göring, Dominik Keller, Rakesh Rao Ramachandra Rao, Stephan Fremerey, Alexander Raake (Audiovisual Technology Group, Technische Universität Ilmenau)
external_link: https://github.com/Telecommunication-Telemedia-Assessment/360-SimulatorSickness-Data
access: Openly available for download from Zenodo (5.9 MB) and GitHub repository with evaluation tools
publicly_available: true
doi: 10.1109/VR50410.2021.00041
citation: 'Singla, A., Göring, S., Keller, D., Rao, R. R. R., Fremerey, S., & Raake, A. (2021). Assessment of the Simulator Sickness Questionnaire for Omnidirectional Videos. In 2021 IEEE Virtual Reality and 3D User Interfaces (VR), 198-206. https://doi.org/10.1109/VR50410.2021.00041'
license: Creative Commons Attribution 4.0 International
subjective_scores: true
total: 48
tags:
- 360-degree video
- omnidirectional video
- simulator sickness
- cybersickness
- ssq
- vrsq
- csq
- htc vive
- hmd
- virtual reality
---

This dataset addresses the important challenge of evaluating simulator sickness (also known as cybersickness) in 360-degree video experiences viewed through head-mounted displays (HMDs). The research was presented at IEEE VR 2021 in Lisboa, Portugal, and examines whether the standard 16-question Simulator Sickness Questionnaire (SSQ) can be simplified for more efficient testing in 360° video studies.

The dataset contains head rotation data and Simulator Sickness Questionnaire (SSQ) results from 48 participants who watched 20 different omnidirectional videos, each 30 seconds long, using the HTC Vive HMD. The research hypothesis was that since the SSQ was not originally designed for 360° video-related studies, it might be simplified while maintaining validity for assessing simulator sickness in this specific context.

Using Principal Component Analysis (PCA) across data from six previous studies, the researchers identified that a reduced questionnaire with only 9 out of 16 questions (less than 44% of the original) yields the best agreement with the complete SSQ. Exploratory Factor Analysis (EFA) confirmed that these nine symptom-related attributes sufficiently represent three key dimensions: Uneasiness, Visual Discomfort, and Loss of Balance. The study also compared the original SSQ with the Virtual Reality Sickness Questionnaire (VRSQ) and Cybersickness Questionnaire (CSQ).

The GitHub repository provides tools for evaluating both the SSQ and head rotation data, enabling researchers to apply the simplified questionnaire methodology to their own 360° video studies. The dataset is also available on Zenodo (DOI: 10.5281/zenodo.4472672) with open access under Creative Commons Attribution 4.0 International License.

This research has been influential with 15 citations and over 1,099 downloads, contributing to standardized and efficient assessment of simulator sickness in immersive 360° video experiences. The simplified questionnaire reduces participant burden while maintaining measurement validity, making it particularly valuable for large-scale quality of experience studies involving omnidirectional video content viewed through HMDs.
