---
title: One for All Toward Unified Foundation Models for Earth Vision
author: Zack
date: 2024-04-07 00:00:00 +0800
categories: [Arxiv]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: One for All: Toward Unified Foundation Models for Earth Vision
- Link: https://arxiv.org/abs/2401.07527
- Published in: Arxiv 2024
- Type: Pretrain
- Code/Project: ---
- 备注: 掩码，在主干前加了不同模态的编码器，解码器也是各个模态独立的
- 数据类型: RGB, SAR, 多光谱, NIR
- Backbone: Transformer
- 下游任务: Classification, Semantic Segmentation
- Short Summary: 目前的遥感基础模型通常专注于单一模态或特定的空间分辨率范围，这限制了它们在下游数据集中的通用性。尽管已经有开发多模态遥感基础模型的尝试，但它们通常为每种模态或空间分辨率采用单独的视觉编码器，需根据输入数据切换不同的骨干网络。为了解决这一问题，我们提出了一种简单而有效的方法，称为OFA-Net（One-For-All网络）：使用单一的共享Transformer骨干网络来处理不同空间分辨率的多种数据模态。通过使用掩码图像建模机制，我们在一个精心策划的多模态数据集上预训练单一的Transformer骨干网络。
