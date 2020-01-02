---
access: 'Images used in the experiment are available at: Links: http://www.mpi-inf.mpg.de/resources/hdr/iqm-evaluation/dataset.html
  Download SIGGRAPH Asia 12 dataset (including experimental study results, 195MB zip
  file): Link: http://www.mpi-inf.mpg.de/resources/hdr/iqm-evaluation/loccg_sa12.zip
  Browse SIGGRAPH Asia 12 dataset: Link: http://www.mpi-inf.mpg.de/resources/hdr/iqm-evaluation/loccg_sa12/
  Download EG 12 dataset (including experimental study results, 113MB zip file): Link:
  http://www.mpi-inf.mpg.de/resources/hdr/iqm-evaluation/loccg_eg12.zip Browse EG
  12 dataset: Link: http://www.mpi-inf.mpg.de/resources/hdr/iqm-evaluation/loccg_eg12/'
author: Max-Planck-Institut Informatik
categories:
- Image
citation: Please refer to the paper entitled [CHM12] for additional information.
contact_email: null
contact_name: Martin Cadik (mcadik@mpi-inf.mpg.de)
database: Image dataset for evaluation of graphics artifacts
excerpt: ''
external_link: http://www.mpi-inf.mpg.de/resources/hdr/iqm-evaluation/
hrc: 15.0
license: ''
method: Custom
other: ''
partner: false
publicly_available: true
ratings: 35.0
references:
  CHM12: Martin Cadik, Robert Herzog, Rafal Mantiuk, Karol Myszkowski, Hans-Peter
    Seidel, New Measurements Reveal Weaknesses of Image Quality Metrics in Evaluating
    Graphics Artifacts, ACM Transactions on Graphics (Proc. of SIGGRAPH Asia), 2012.
resolution: ''
src: 37.0
subjective_scores: true
tags:
- HDR
- Image
title: Image dataset for evaluation of graphics artifacts
total: ''
---

Reliable detection of global illumination and rendering artifacts in the form of localized distortion maps is important for many graphics applications. Two experiments were run where observers use a brush-painting interface to directly mark image regions with noticeable/objectionable distortions in the presence/absence of a high-quality reference image, respectively. The collected data shows a relatively high correlation between the with-reference and no-reference observer markings. The demanding perpixel image-quality datasets reveal weaknesses of both simple (PSNR, MSE, sCIE-Lab) and advanced (SSIM, MS-SSIM, HDRVDP-2) quality metrics. The datasets have further potential in improving existing quality metrics, but also in analyzing the saliency of rendering distortions, and investigating visual equivalence given our with- and no-reference data. Stimuli #1 - #10 come from EG 12 dataset, for the dataset SIGGRAPH Asia 12 a similar but more extensive experiment has been performed (stimuli #11 - #37) in a more rigorous setup. All scenes were rendered into high-dynamic-range images and tone mapped for display.