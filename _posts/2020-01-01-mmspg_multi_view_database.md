---
access: 'Python scripts to automaticaly generate the multi-view content from Blender
  are available from HTTP: Script using Add-On in Blender Link: https://documents.epfl.ch/groups/g/gr/gr-eb-unit/public/multiview-generation-add-on.zip
  Scripts using command line Link: https://documents.epfl.ch/groups/g/gr/gr-eb-unit/public/multiview-generation-command-line.zip
  Manual how to use scripts Link: https://documents.epfl.ch/groups/g/gr/gr-eb-unit/public/User-Manual.pdf
  Link to ftp server with multi-view database (under construction...) In order to
  obtain the password to access ftp server please contact Martin Rerabek (martin.rerabek@epfl.ch).'
author: EPFL
categories:
- Image
citation: If you use this database or scripts to generate the multi-view content in
  your research we kindly ask you to reference the website (http://mmspg.epfl.ch/MultiviewDatabase).
contact_email: null
contact_name: If you have any questions regarding this research please contact Martin
  Rerabek (martin.rerabek@epfl.ch).
database: MMSPG Multi-view database
excerpt: ''
external_link: http://mmspg.epfl.ch/MultiviewDatabase
hrc: ''
license: "Permission is hereby granted, without written agreement and without license\
  \ or royalty fees, to use, copy, modify, and distribute the data provided and its\
  \ documentation for research purpose only. The data provided may not be commercially\
  \ distributed. In no event shall the Ecole Polytechnique F\xE9d\xE9rale de Lausanne\
  \ (EPFL) be liable to any party for direct, indirect, special, incidental, or consequential\
  \ damages arising out of the use of the data and its documentation. The Ecole Polytechnique\
  \ F\xE9d\xE9rale de Lausanne (EPFL) specifically disclaims any warranties. The data\
  \ provided hereunder is on an \"as is\" basis and the Ecole Polytechnique F\xE9\
  d\xE9rale de Lausanne (EPFL) has no obligation to provide maintenance, support,\
  \ updates, enhancements, or modifications."
method: ''
other: Multiview
partner: true
publicly_available: true
ratings: ''
resolution: ''
src: ''
subjective_scores: false
tags:
- 3D
- Image
title: MMSPG Multi-view database
total: ''
---

One of the alternative methods to display 3D content on the conventional 2D screen is based on the monocular cue called motion parallax. One of the ways how to employ motion parallax based method is to use multi-view image or video content and then to display relevant view for each position of viewer face. In general, there is not sufficient amount of multi-view image data available due to the difficult multi-view acquisition proces which needs specific hardware and software solution. We came up with the solution to render multi-view content using open source software called Blender (http://www.blender.org/). The biggest advantage of this software is the availability of production repository and the posibility to use scripting in order to automate required tasks. So, the python scripts which allows the user to generate set of cameras in different setup (1D parallel, circular, grid) and render the scene from Blender with each of them has been developed and are available.