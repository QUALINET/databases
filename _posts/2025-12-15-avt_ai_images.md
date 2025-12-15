---
title: AVT-AI-Image-Dataset - Appeal and Quality Assessment for AI-Generated Images
database: AVT-AI-Image-Dataset
categories:
- image
author: Steve Göring, Rakesh Rao Ramachandra Rao, Rasmus Merten, Alexander Raake (Audiovisual Technology Group, Technische Universität Ilmenau)
external_link: https://github.com/Telecommunication-Telemedia-Assessment/avt_ai_images
access: Openly available for download from GitHub repository
publicly_available: true
doi: 10.1109/ACCESS.2023.3267968
citation: 'Göring, S., Rao, R. R. R., Merten, R., & Raake, A. (2023). Analysis of Appeal for Realistic AI-Generated Photos. IEEE Access, 11, 38999-39012. https://doi.org/10.1109/ACCESS.2023.3267968'
license: GNU General Public License v3.0
subjective_scores: true
total: 135
tags:
- ai-generated images
- text-to-image
- image appeal
- dall-e
- midjourney
- craiyon
- synthetic media
- crowdsourcing
---

This dataset examines the appeal and quality of AI-generated images, addressing the critical question of to what extent AI-generated images are realistic or of high appeal from a photographic point of view and how users perceive them. Published alongside research in IEEE Access (2023) and at QoMEX 2023, the dataset was developed as part of the Deutsche Forschungsgemeinschaft (DFG) funded research (DFG-437543412).

The dataset comprises 135 images generated using five different AI text-to-image generators (including DALL-E-2, Midjourney, and Craiyon) based on 27 different text prompts. Some prompts were derived from the DrawBench benchmark, ensuring diversity in scene complexity and description specificity. The generated images were combined with real photographs for comparison in subjective evaluation studies.

An online crowdsourcing test was conducted to collect subjective ratings on appeal, realism, and text prompt matching from participants. The raw annotation data is stored in the repository's evaluation/subjective/ directories, along with evaluation scripts to reproduce the research results. Subjective ratings were compared with state-of-the-art image quality models and features to assess the validity of objective quality metrics for AI-generated content.

The primary finding indicates that some AI generators can produce realistic and highly appealing images, with Midjourney achieving particularly strong performance with appeal ratings of 4.5. However, image quality and appeal depend significantly on both the specific generator used and the text prompt provided. AI-generated images may appear artificial, exhibit low quality, or have low appeal compared to real images, with these limitations varying by generator and prompt complexity.

A companion paper at QoMEX 2023 (DOI: 10.1109/QoMEX58391.2023.10178486) extends this analysis by evaluating quality and appeal through crowdsourcing tests and correlating subjective ratings with objective quality assessment models. The research has been highly influential with 13 citations and over 1,100 downloads, contributing to understanding synthetic media quality assessment and informing the development of improved AI image generation systems. The dataset and evaluation methodology are made publicly available following an Open Science approach, enabling reproducible research on AI-generated image quality and appeal.
