---
title: TOV The original vision model for optical remote sensing image understanding via self-supervised learning
author: Zack
date: 2023-04-09 00:00:00 +0800
categories: [IEEE]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: TOV: The original vision model for optical remote sensing image understanding via self-supervised learning
- Link: https://arxiv.org/abs/2204.04716
- Published in: IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2023
- Type: Pretrain
- Code/Project: https://github.com/GeoX-Lab/G-RSIM/tree/main/TOV_v1
- 备注: 自监督
- Backbone: Resnet
- Backbone 1: CNN(Resnet-50)
- 下游任务: Classification, Semantic Segmentation, Object Detection
- 下游任务 1: scene classification, object detection and semantic segmentation
- Short Summary: 先学习网络上的自然图片，然后学习未标记RSI图片，
