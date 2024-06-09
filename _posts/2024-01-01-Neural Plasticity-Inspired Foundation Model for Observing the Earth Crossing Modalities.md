---
title: Neural Plasticity-Inspired Foundation Model for Observing the Earth Crossing Modalities
author: Zack
date: 2024-11-15 00:00:00 +0800
categories: [Arxiv]
tags: [paper, Other]
math: true
pin: false
---
- 论文名称: Neural Plasticity-Inspired Foundation Model for Observing the Earth Crossing Modalities
- Link: https://arxiv.org/abs/2403.15356
- Published in: Arxiv 2024
- Type: Other
- 备注: 将各种数据模态自适应地集成到一个单一框架中，这种动态超网络，能够调整到不同的波长，使得一个多功能Transformer能够在来自五个传感器的数据上进行联合训练
- 数据类型: RGB, NIR, 多光谱, SAR
- Backbone: Transformer
- 下游任务: Classification, Semantic Segmentation
- Short Summary: 这是通过设计的基于超网络的动态权重生成器实现的，该生成器适应每个通道的光谱波长。通过将具有不同通道数量的图像嵌入到统一的特征空间中，模型利用共享Transformer块来学习模态共享表示。
