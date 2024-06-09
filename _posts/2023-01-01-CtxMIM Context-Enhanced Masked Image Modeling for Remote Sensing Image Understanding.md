---
title: CtxMIM Context-Enhanced Masked Image Modeling for Remote Sensing Image Understanding
author: Zack
date: 2023-01-01 00:00:00 +0800
categories: [Arxiv]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: CtxMIM: Context-Enhanced Masked Image Modeling for Remote Sensing Image Understanding
- Link: https://arxiv.org/abs/2310.00022
- Published in: Arxiv 2023
- Type: Pretrain
- Code/Project: ---
- 备注: 自监督，掩码
- Backbone: Swin Transformer
- Backbone 1: Swin-B
- 下游任务: Classification, Semantic Segmentation, Object Detection, Instance Segmentation
- 下游任务 1: classification, semantic segmentation, object detection, instance segmentation
- Short Summary: CtxMIM将原始图像块形式化为重建模板，并采用Siamese框架处理两组图像块。引入了一个上下文增强的生成分支，通过重建中的上下文一致性约束提供上下文信息。通过这种简单且优雅的设计，CtxMIM鼓励预训练模型在大规模数据集上学习对象级或像素级特征，而无需特定的时间或地理约束。
