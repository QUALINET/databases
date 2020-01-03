---
access: 'The files are available for download via HTTP. Link: https://jpeg.org/plenodb/pc/microsoft/'
author: Microsoft
categories:
- image
contact_name: Microsoft (Charles Loop, Qin Cai, Sergio Orts Escolano, and Philip A.
  Chou)
database: 'JPEG Pleno Database: Microsoft Voxelized Upper Bodies - A Voxelized Point
  Cloud Dataset'
deprecated: false
excerpt: ''
external_link: https://jpeg.org/plenodb/pc/microsoft/
license: Microsoft hereby makes available dynamic voxelized point cloud data sequences
  as potential test material for MPEG and/or JPEG standardization efforts, as well
  as non-commercial use subject to the accompanying license agreement (https://jpeg.org/plenodb/pc/microsoft/license.pdf)
  by the wider research community.
partner: false
publicly_available: true
src: 10
subjective_scores: false
tags:
- point cloud
- image
title: 'JPEG Pleno Database: Microsoft Voxelized Upper Bodies - A Voxelized Point
  Cloud Dataset'
total: 10
---

The voxelized point cloud is a set of points (x, y, z) constrained to lie on a regular 3D grid, which without loss of generality may be assume to be the integer lattice. The (x, y, z) coordinates may be interpreted as the address of a volumetric element, or voxel. A voxel whose address is in the set is said to be occupied; otherwise it is unoccupied. Each occupied voxel may have attributes, such as color, transparency, normals, curvature, and specularity. A voxelized point cloud captured at one instant of time is a frame. A dynamic voxelized point cloud is represented as a sequence of frames. The dynamic voxelized point cloud sequences in this dataset are known as the Microsoft Voxelized Upper Bodies (MVUB). There are five subjects in the dataset, known as Andrew, David, Phil, Ricardo, and Sara. The upper bodies of these subjects are captured by four frontal RGBD cameras, at 30 fps, over a 7-10s period for each. Two spatial resolutions are provided for each sequence: a cube of 512x512x512 voxels and a cube of 1024x1024x1024 voxels, respectively known as depth 9 and depth 10. In each cube, only voxels near the surface of the subjects are occupied. The attributes of a voxel are the red, green, and blue components of the surface color. Voxels at depth 9 are approximately 1.5mm cubed, while voxels at depth 10 are approximately 0.75mm cubed.