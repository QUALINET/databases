---
access: 'Dataset is available with image preview at: Link: http://vision.ucsd.edu/~nalldrin/research/cvpr08/datasets/
  HDR images of three objects are available for various illuminations: APPLE image,
  112 images, resolution: 646x696 Link: http://vision.ucsd.edu/~nalldrin/research/cvpr08/datasets/apple.tar.gz
  GOURD1 image, 102 images, resolution: 552x588 Link: http://vision.ucsd.edu/~nalldrin/research/cvpr08/datasets/gourd1.tar.gz
  GOURD2 image, 98 images, resolution: 601x501 Link: http://vision.ucsd.edu/~nalldrin/research/cvpr08/datasets/gourd2.tar.gz'
author: University of California
categories:
- image
citation: The images provided in these dataset are free to use so long as proper credit
  is attributed to the original authors. In particular, any publications utilizing
  this dataset should cite the following paper [AZK08].
contact_name: Neil Alldrin (http://vision.ucsd.edu/~nalldrin/, nalldrin@gmail.com)
database: HDR Image Dataset for Photometric Stereo
broken_link: true
excerpt: ''
external_link: http://vision.ucsd.edu/~nalldrin/research/cvpr08/datasets/
publicly_available: true
references:
  AZK08: N. Alldrin, T. Zickler, and D. Kriegman, Photometric Stereo With Non-Parametric
    and Spatially-Varying Reflectance, 2008 Conf. on Comp. Vision and Pattern Recognition
    (CVPR), Anchorage, AK, June 2008.
subjective_scores: false
tags:
- hdr
- image
title: HDR Image Dataset for Photometric Stereo
total: 312
---

The dataset contains 220 HDR images of 3 objects. Images were acquired in a dark room using an EOS-1Ds camera with a fixed zoom lens. The camera was placed roughly 1.5m from the test object (~10cm in diameter). All images were acquired with the camera and test object in the same position. Illumination consisted of a single incandescent light bulb placed roughly 1.5m from the test object (whose position was varied in each image). Light source directions were measured with a mirrored sphere placed in the scene and light source intensity was measured with a diffuse sphere placed in the scene. Each image in the dataset is actually the result of multiple RAW images captured by the camera. To prevent clipping of bright and dark regions of the scene, we combined multiple low dynamic range (LDR) images taken at different shutter speeds into a single high dynamic range (HDR) image. To eliminate ambient illumination (which is present even in a dark room to some degree), we acquired ambient images by occluding the light source relative to the test object (i.e., we blocked the light source so that the test object was in shadow, so that only ambient light illuminated the object). The images present in the dataset are the difference between normal images and their corresponding ambient images.