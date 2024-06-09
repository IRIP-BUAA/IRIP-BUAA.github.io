---
title: Predicting Gradient is Better Exploring Self-Supervised Learning for SAR ATR with a Joint-Embedding Predictive Architecture
author: Zack
date: 2023-06-20 00:00:00 +0800
categories: [Arxiv]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: Predicting Gradient is Better: Exploring Self-Supervised Learning for SAR ATR with a Joint-Embedding Predictive Architecture
- Link: https://arxiv.org/abs/2311.15153v4
- Published in: Arxiv 2023
- Type: Pretrain
- Code/Project: https://github.com/waterdisappear/SAR-JEPA
- 备注: 自监督，类似JEPA的框架，固定student生成梯度特征
- 数据类型: SAR
- Backbone: ViT
- 下游任务: Target Recognition
- Short Summary: 发现像素采样不适用于SAR图像，因为SAR图像的单个像素包含乘性噪声。因此更倾向于使用局部补丁进行遮挡，而不是整个图像或像素级别。工作旨在通过局部补丁在目标层次上挖掘语义信息，而不是场景层次，工作发现梯度比率比HOG的差分梯度在乘性斑点噪声下更适合目标形状信息提取。
