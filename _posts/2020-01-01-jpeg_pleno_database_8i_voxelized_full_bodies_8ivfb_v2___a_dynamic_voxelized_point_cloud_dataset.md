---
access: 'The files are available for download via HTTP. Link: https://jpeg.org/plenodb/pc/8ilabs/
  Direct Link (5.5GB): https://jpeg.org/plenodb/pc/8ilabs/8iVFBv2.7z'
author: 8i Labs
categories:
- video
citation: If you publish images or report performance results of these data, we request
  that you cite this document [DHM17] as Eugene d'Eon, Bob Harrison, Taos Myers, and
  Philip A. Chou, "8i Voxelized Full Bodies - A Voxelized Point Cloud Dataset," ISO/IEC
  JTC1/SC29 Joint WG11/WG1 (MPEG/JPEG) input document WG11M40059/WG1M74006, Geneva,
  January 2017.
contact_name: 8i Labs (hi@8i.com) Eugene d'Eon, Bob Harrison, Taos Myers and Philip
  A. Chou
database: 'JPEG Pleno Database: 8i Voxelized Full Bodies (8iVFB v2) - A Dynamic Voxelized
  Point Cloud Dataset'
broken_link: false
excerpt: ''
external_link: https://jpeg.org/plenodb/pc/8ilabs/
license: 8i Labs, Inc. hereby makes available dynamic voxelized point cloud data sequences
  as potential test material for MPEG and/or JPEG standardization efforts, as well
  as non-commercial use subject to the accompanying license agreement (https://jpeg.org/plenodb/pc/8ilabs/license.pdf)
  by the wider research community. The terms of use of the dataset are governed by
  the License Agreement, which is an integral part of the dataset and which must accompany
  any copy of the dataset.
publicly_available: true
references:
  DHM17: Eugene d'Eon, Bob Harrison, Taos Myers, and Philip A. Chou, "8i Voxelized
    Full Bodies - A Voxelized Point Cloud Dataset," ISO/IEC JTC1/SC29 Joint WG11/WG1
    (MPEG/JPEG) input document WG11M40059/WG1M74006, Geneva, January 2017.
src: 4
subjective_scores: false
tags:
- point cloud
- video
title: 'JPEG Pleno Database: 8i Voxelized Full Bodies (8iVFB v2) - A Dynamic Voxelized
  Point Cloud Dataset'
total: 4
---

A voxelized point cloud is a set of points (x, y, z) constrained to lie on a regular 3D grid, which without loss of generality, may be assumed to be the integer lattice. The (x, y, z) coordinates may be interpreted as the address of a volumetric element, or voxel. A voxel whose address is in the set is said to be occupied; otherwise it is unoccupied. Each occupied voxel may have attributes, such as color, transparency, normals, curvature, and specularity. A voxelized point cloud captured at one instant of time is a frame. A dynamic voxelized point cloud is represented as a sequence of frames. The dynamic voxelized point cloud sequences in this dataset are known as the 8i Voxelized Full Bodies (8iVFB). There are four sequences in the dataset, known as longdress, loot, redandblack, and soldier, pictured below. In each sequence, the full body of a human subject is captured by 42 RGB cameras configured in 14 clusters (each cluster acting as a logical RGBD camera), at 30 fps, over a 10 s period. One spatial resolution is provided for each sequence: a cube of 1024x1024x1024 voxels, known as depth 10. In each cube, only voxels near the surface of the subjects are occupied. The attributes of an occupied voxel are the red, green, and blue components of the surface color. For each sequence, the cube is scaled so that it is the smallest bounding cube that contains the entire sequence. Since the height of the subject is typically the longest dimension, for a subject 1.8 m high, a voxel at depth 10 would be approximately 1.8 m / 1024 voxels ≈ 1.75 mm per voxel on a side.