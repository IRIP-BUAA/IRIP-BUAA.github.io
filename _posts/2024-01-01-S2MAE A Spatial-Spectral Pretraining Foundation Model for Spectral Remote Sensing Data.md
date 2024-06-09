---
title: S2MAE A Spatial-Spectral Pretraining Foundation Model for Spectral Remote Sensing Data
author: Zack
date: 2024-04-16 00:00:00 +0800
categories: [CVPR]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: S2MAE: A Spatial-Spectral Pretraining Foundation Model for Spectral Remote Sensing Data
- Link: https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models/blob/main
- Published in: CVPR 2024
- Type: Pretrain
- Backbone: ConvNext
- 下游任务: Object Detection, Semantic Segmentation, Change Detection
- Short Summary: GeoSense的大型数据集，设计了一个稀疏建模和低频重建（SMLFR）框架，用于ConvNet基础模型的自监督表示学习。具体而言，在遮罩图像建模（MIM）中提出了一种稀疏建模策略，使ConvNet能够通过将未遮罩的补丁视为体素并对编码器进行稀疏化来处理可变长度序列。此外，我们设计了一个低频重建目标，引导模型关注遥感图像中的重要地物特征，同时减轻不必要的细节干扰。
