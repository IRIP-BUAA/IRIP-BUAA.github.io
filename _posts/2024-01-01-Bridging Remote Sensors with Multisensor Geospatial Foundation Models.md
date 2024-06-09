---
title: Bridging Remote Sensors with Multisensor Geospatial Foundation Models
author: Zack
date: 2024-01-16 00:00:00 +0800
categories: [CVPR]
tags: [paper, Other]
math: true
pin: false
---
- 论文名称: Bridging Remote Sensors with Multisensor Geospatial Foundation Models
- Link: https://arxiv.org/abs/2404.01260
- Published in: CVPR 2024
- Type: Other
- 备注: 跨传感器的掩码方式。每个传感器有独立的embedding提取器，为每个传感器设置单独的解码器和跨传感器预测。例如，当模型被馈送来自DSM的遮罩图像时，它可以预测自身的遮罩补丁或RGB对应的图像
- 数据类型: SAR, RGB, DSM
- Backbone: Swin Transformer
- 下游任务: Classification, Semantic Segmentation, cloud removal, pan-sharpening
- Short Summary: 通过使用遮罩图像建模技术可以学习到对应传感器之间的联合表示吗？针对该问题提出了msGFM（多传感器地理空间基础模型），该模型有效整合了四种关键传感器模式的数据。msGFM特别擅长处理配对和非配对的传感器数据。
