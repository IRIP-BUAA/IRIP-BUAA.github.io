---
title: CROMA: Remote Sensing Representations with Contrastive Radar-Optical Masked Autoencoders
author: Zack
date: 2023-01-01 00:00:00 +0800
categories: [NeurIPS]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: CROMA: Remote Sensing Representations with Contrastive Radar-Optical Masked Autoencoders
- Link: https://arxiv.org/pdf/2311.00566
- Published in: NeurIPS 2023
- Type: Pretrain
- Code/Project: https://github.com/antofuller/CROMA
- 备注: 对比学习+重建，多光谱+孔径雷达
- Backbone: ViT
- Backbone 1: ViT-B/ViT-L
- 下游任务: Classification, Semantic Segmentation
- 下游任务 1: Classification,Segmentation
- Short Summary: 分别编码被遮盖的多光谱光学和合成孔径雷达样本，这些样本在空间和时间上是对齐的，并执行跨模态对比学习。另一个编码器融合这些传感器，生成联合多模态编码，然后通过一个轻量级解码器预测被遮盖的补丁。
