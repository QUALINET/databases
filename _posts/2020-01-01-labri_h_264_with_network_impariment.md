---
access: 'Download information for the database may be obtained by contacting Karel
  Fliegel (fliegek@fel.cvut.cz). The FTP access will be provided to the users registered
  in Qualinet Databases. The data volume is 102.6GB in total, including: H.264/AVC
  video sequences, 135 sequences, 2.6GB YUV video sequences, 135 sequences, 100GB
  Experimental data, 3 files, 179kB'
author: LaBRI
categories:
- Video
citation: In publications using the database, the following paper should be cited
  [BBH11].
contact_email: null
contact_name: Jenny Benois-Pineau (jenny.benois@labri.fr) - research related information
  Karel Fliegel (fliegek@fel.cvut.cz) - download information
database: LaBRI H.264 with Network Impariment
excerpt: ''
external_link: http://www.labri.fr/
hrc: 8.0
license: To make it available to Qualinet an agreement has been signed with LaBRI.
  Other users will have to sign similar agreement to use the data.
method: ''
other: ''
partner: true
publicly_available: true
ratings: ''
references:
  BBH11: Boujut, H.; Benois-Pineau, J.; Hadar, O.; Ahmed, T.; Bonnet, P. Weighted-MSE
    based on saliency map for assessing video quality of H.264 video streams, Image
    Quality and System Performance VIII. Edited by Farnand, Susan P.; Gaykema, Frans.
    Proceedings of the SPIE, Volume 7867, pp. 78670X-78670X-8 (2011).
resolution: 1920x1080
src: 15.0
subjective_scores: true
tags:
- Video
title: LaBRI H.264 with Network Impariment
total: 120
---

This database is a result of joint effort of Laboratoire Bordelais de Recherche en Informatique LaBRI (University of Bordeaux) and Communication Systems Engineering Dept. (Ben Gurion University of the Negev (BGU)). The database is composed of 15 video sources (SRC) from OpenVideo.org, TUM/Taurus Media and NTIA/ITS databases. The SRC videos were encoded in H.264/AVC with the x264 encoder at 6000kb/s. The resolution of the 15 SRC videos is 1920x1080 pixels progressive and the frame-rate is 25 frames per second. The 15 SRC videos were decoded with the FFMPEG 0.5.1 H.264/AVC decoder to produce YUV 4:2:0 raw file, presented to the subjects during the experiment. According to recommendation ITU-R BT500.11, the length of each video sequence is equal to 10 seconds (250 frames). Two network models, IP and RF, were applied on the 15 SRC. The IP model is composed of 5 different loss profiles which are defined in ITU-T G.1050. The RF model is composed of 3 loss different profiles. Thus (5 + 3) * 15 = 120 PVS sequences are present in this database. Subjective and objective metrics were computed on this video database. The metrics values for each SRC and PVS sequences are stored in a table available in Microsoft Excel and CSV file formats. Subjective metrics are MOS (Mean Opinion Score) and DMOS (Differential Mean Opinion Score). Objective metrics are PSNR and SSIM. The settings of each HRC are also available in a table in CSV format. Tables with the offsets of the first frame in the H.264 streams (tables of sections 1 and 2.2) are stored in file LaBRI-exp-offsets.csv.