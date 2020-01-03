---
access: 'HDR images can be downloaded in one ZIP file (1.8GB): Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/HDR.zip
  Base images are also available (Divided into 15 parts, 1~2GB each), File Name: set_name
  + image_name + shutter_speed + aperture + iso + time: Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S00.zip
  Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S01.zip Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S02.zip
  Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S03.zip Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S04.zip
  Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S05.zip Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S06.zip
  Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S07a.zip Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S07b.zip
  Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S08.zip Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S09.zip
  Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S10.zip Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S11.zip
  Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S12.zip Link: http://www.cs.sfu.ca/~colour/data2/funt_hdr/PNG_S13.zip
  Measured Illumination: (White patch values of the 4 Colorcheckers of each set):
  Image Filelist:  http://www.cs.sfu.ca/~colour/data2/funt_hdr/real_illum.zip HDR
  image list: set names of 105 HDR images: http://www.cs.sfu.ca/~colour/data2/funt_hdr/Filelist_hdr.txt
  Base image list 1: filenames of 105 base images >= 10321: http://www.cs.sfu.ca/~colour/data2/funt_hdr/Filelist_base_unsaturated_10321_med5x5.txt
  Base image list 1: filenames of 105 base images >= 11000: http://www.cs.sfu.ca/~colour/data2/funt_hdr/Filelist_base_unsaturated_11000_med5x5.txt'
author: Simon Fraser University
categories:
- image
citation: Please cite the papers [FS10a], [FS10b] if you use the gallery.
contact_name: Briant Funt (http://www.cs.sfu.ca/~funt, funt@cs.sfu.ca)
database: Funt et al. HDR Dataset
deprecated: false
excerpt: ''
external_link: http://www.cs.sfu.ca/~colour/data/funt_hdr/
partner: false
publicly_available: true
references:
  FS10a: Funt, B. and Shi, L., The Rehabilitation of MaxRGB, Proc. IS&T Eighteenth
    Color Imaging Conference, San Antonio, Nov. 2010.
  FS10b: Funt, B. and Shi, L.,  The Effect of Exposure on MaxRGB Color Constancy,
    Proc. SPIE Volume 7527 Human Vision and Electronic Imaging XV, San Jose, Jan.
    2010.
resolution: 4256x2832
src: 105
subjective_scores: false
tags:
- hdr
- image
title: Funt et al. HDR Dataset
total: 105
---

The following is a data set of images of 105 scenes captured using a Nikon D700 digital still camera. The camera's auto-bracketing was used to capture up to 9 images of exposures with 1 EV (exposure value) difference between each in the sequence. The rate of capture was 5 frames per second. The exposure range was set to ensure that in each set there would be at least one image with maximum digital count less than 10321. During bracketing, the camera was set to allow it to adjust the shutter speed and/or the aperture setting automatically between frames in order to change the exposure by 1EV. In other words, the f-stop setting was not fixed. All images were recorded in Nikon's NEF raw data format. The raw images were then processed in two ways. The first was to create almost-raw 16-bit Portable Network Graphics (PNG) format (lossless compression) images from the NEF data, one image per exposure value. We will refer to these 16-bit PNGs as the 'base images'. The second was to create a set of HDR (high dynamic range) images from the base images. Two sets of base images were captured for each scene. One set includes 4 Gretag Macbeth mini Colorcheckers positioned at different angles with respect to one another. The second set contained images of the same scene, but without the Colorcheckers. Between taking the two image sets, the camera was refocused and possibly moved slightly. For the first set, the focus was adjusted so the Colorcheckers were in focus. For the second set, the focus was optimized for the scene overall. (In the cases when only the first set is available, the Colorcheckers are cropped out to form the second set). To create the base images, the raw NEF images were decoded using dcraw (more specifically Windows executable dcrawMS.exe). To preserve the original digital counts for each of the RGB channels, demosaicing was not enabled. The camera outputs 14-bit data per channel so the range of possible digital counts is 0 to 16383. The raw images contain 4284x2844 14-bit values in an RGGB pattern. To create a color image the two G values were averaged, but no further demosaicing was done. This results in a 2142x1422 RGB image. An HDR image was also constructed from each set of base images. The base images require alignment, which was done by the simple Median Threshold Bitmap approach (Ward 2003). After applying a 3x3 median filter to the base images, the Matlab function makehdr from the Matlab Image Processing Toolbox was used to combine them into one HDR image. To ensure the reliability of the pixel values, all base image pixels having values greater than 13004 or less than 30 were excluded. The final HDR images may vary slightly in size due to possible cropping at the boundaries of the images as they are aligned.