---
title: RingMo-lite A Remote Sensing Multi-task Lightweight Network with CNN-Transformer Hybrid Framework
author: Zack
date: 2023-09-26 00:00:00 +0800
categories: [Arxiv]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: RingMo-lite: A Remote Sensing Multi-task Lightweight Network with CNN-Transformer Hybrid Framework
- Link: https://arxiv.org/abs/2309.09003
- Published in: Arxiv 2023
- Type: Pretrain
- Code/Project: ---
- 备注: 掩码（FD-MIM），轻量化
- 数据类型: 多光谱, RGB
- Backbone: CNN-Transformer hybrid
- 下游任务: Classification, Object Detection, Semantic Segmentation, Change Detection
- Short Summary: RingMo-lite，这是一种具有CNN-Transformer混合框架的RS多任务轻量级网络，能够有效利用RS的频域特性来优化解释过程。它结合了变压器模块作为低通滤波器，通过双分支结构提取RS图像的全局特征，以及CNN模块作为堆叠的高通滤波器来有效提取细粒度细节。此外，在预训练阶段，设计的频域掩码图像建模（FD-MIM）结合了每个图像补丁的高频和低频特性，有效捕捉了RS数据中的潜在特征表示。
