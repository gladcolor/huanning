---
title: "Pre-Disaster Imagery from Google Photorealistic 3D Tiles for Building Damage Assessment"
date: 2026-10-26T08:57:00-04:00
area: Disaster response, 3D geospatial data
summary: Recreating each post-tornado drone frame's camera view in Google Photorealistic 3D Tiles to obtain matching pre-disaster images for building damage assessment.
image: media/projects/pre-disaster-3d-tiles/before-after-pair.webp
tags:
- Disaster Response
- Drones
- 3D Reconstruction
- Change Detection
---

Change-detection models, such as Siamese neural networks, judge a building's damage by comparing an image taken before a disaster with one taken after it. Satellites make such pairs easy: they look straight down from a fixed perspective, so the before and after images line up almost pixel for pixel. Drone footage shows roofs and facades in much richer detail, but nobody flies a drone over a neighborhood before a tornado arrives, and the camera position and angle change from flight to flight. For drone-based damage assessment, the missing piece is a pre-disaster image taken from the same viewpoint as each post-disaster drone frame.

My part of this tornado damage assessment study builds those pre-disaster images from Google's Photorealistic 3D Tiles. The core idea is to use Google's 3D model of the neighborhood as the record of how the buildings looked before the disaster, and to render perspective images from that model with the same viewport as each drone image.

> **Note:** The illustrations marked "simulated" on this page were generated with an AI image model to explain the method. Images from the study will be added soon.

## Reconstructing the camera for every drone frame

To reconstruct the tornado footage, the video is turned into a sequence of image frames, which are then fed into 3D reconstruction software (RealityScan). The frames are aligned and georeferenced using drone telemetry data and ground control points (GCPs). RealityScan computes the orientation and location of each frame and creates a dense point cloud and mesh of the scene. The orientation and location tell us where the camera was in geographic space and which direction it was pointing when it captured each video frame.

![Simulated: a dense 3D point cloud of a tornado-damaged neighborhood, with camera positions along the drone flight path and ground control points](media/projects/pre-disaster-3d-tiles/camera-poses.webp)

*Simulated illustration of the reconstruction: camera positions recovered along the drone flight path above the damaged neighborhood, with ground control points on the ground.*

## Recreating the same view in Photorealistic 3D Tiles

We use the camera direction and position to replicate each drone frame's viewpoint in Photorealistic 3D Tiles provided by Google Maps. Photorealistic 3D Tiles is a data service for accessing high-resolution, textured 3D mesh models of the real world, the same 3D models shown in Google Earth.

![Google Photorealistic 3D Tiles: a textured 3D model of the Statue of Liberty and Liberty Island](media/projects/pre-disaster-3d-tiles/google-3d-tiles-example.webp)

*An example of Google Photorealistic 3D Tiles. Image: [Google Maps Platform documentation](https://developers.google.com/maps/documentation/tile/3d-tiles-overview), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

We take screenshots from Photorealistic 3D Tiles at each replicated viewpoint. Because the 3D buildings in Google Earth were captured before the tornado, these screenshots are pre-disaster images rendered from the 3D building models, with viewports close to the post-disaster drone frames. Each drone frame thus gains a matching before image, and the pairs can be used to train change-detection models that compare the same buildings before and after the disaster.

![Simulated: the same street before the tornado, rendered from 3D Tiles, and after the tornado, in a drone frame](media/projects/pre-disaster-3d-tiles/before-after-pair.webp)

*Simulated illustration of a before-and-after pair: a pre-disaster view from 3D Tiles (left) and a post-disaster drone frame (right). In the study, both images of a pair share the same camera position and direction.*

## From image pairs to 3D change detection

The same reconstruction also opens a second path. Once the post-disaster 3D model is built from the drone footage, it can be compared directly with Google's pre-disaster 3D model to detect changes in 3D: a missing roof, a collapsed wall, or a building that is gone. Google's 3D models are a good reference for the building structure before the disaster, and current 3D reconstruction technology makes it fast to build the post-disaster model for assessment.

## New value from historical data

This project combines archived data, new technology, and AI to create an application that none of them supports alone. The 3D city models were not built for disaster response, but they hold a record of buildings that no one thought to survey before the tornado. My [street tree diameter growth monitoring](../street-tree-diameter/) project follows the same idea: it turns more than a decade of historical street view imagery into a growth record for every street tree. Both projects use AI to create new value from historical data.
