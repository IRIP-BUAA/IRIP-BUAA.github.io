---
title: SwiMDiff: Scene-wide Matching Contrastive Learning with Diffusion Constraint for Remote Sensing Image
author: Zack
date: 2024-01-01 00:00:00 +0800
categories: [Arxiv]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: SwiMDiff: Scene-wide Matching Contrastive Learning with Diffusion Constraint for Remote Sensing Image
- Link: https://arxiv.org/abs/2401.05093
- Published in: Arxiv 2024
- Type: Pretrain
- Code/Project: ---
- 备注: 对比学习，用同一场景下的图片构建了一个FNS，并用一个基于Diffussion的图像恢复任务做辅助任务
- Backbone: Resnet
- Short Summary: 以往的CL忽略了细粒度特征和负样本中的潜在联系，SwiMDiff采用场景范围的匹配方法，有效地重新校准标签，将来自同一场景的数据识别为假负样本。此调整使CL更适用于遥感的细微差别。此外，SwiMDiff将CL与扩散模型无缝集成。通过实施像素级别的扩散约束，我们增强了编码器捕捉图像的全局语义信息和细粒度特征的能力。
