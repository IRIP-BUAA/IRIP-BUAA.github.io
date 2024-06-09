---
title: Scale-MAE A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning
author: Zack
date: 2023-12-16 00:00:00 +0800
categories: [ICCV]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning
- Link: https://arxiv.org/abs/2212.14532
- Published in: ICCV 2023
- Type: Pretrain
- Code/Project: https://github.com/bair-climate-initiative/scale-mae
- 备注: MAE，对位置编码和解码器进行了优化
- Backbone: ViT
- Backbone 1: ViT-Large
- 下游任务: Classification, Semantic Segmentation
- 下游任务 1: 基于KNN的分类，linear classi-fication，Semantic segmentation
- Short Summary: 原始ViT的位置编码与相机高度无关，Scale-MAE引入了基于地面采样距离（GSD）的位置编码，该编码与图像中土地面积成比例缩放，而不考虑图像的分辨率。此外，Scale-MAE还在MAE框架中引入了拉普拉斯金字塔解码器，以鼓励网络学习多尺度表示。来自ViT编码器的嵌入被解码为捕捉低频信息的低分辨率图像和捕捉高频信息的高分辨率图像。
