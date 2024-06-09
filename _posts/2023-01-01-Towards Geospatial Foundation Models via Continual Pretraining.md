---
title: Towards Geospatial Foundation Models via Continual Pretraining
author: Zack
date: 2023-10-24 00:00:00 +0800
categories: [ICCV]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: Towards Geospatial Foundation Models via Continual Pretraining
- Link: https://arxiv.org/abs/2302.04476
- Published in: ICCV 2023
- Type: Pretrain
- Code/Project: https://github.com/mmendiet/GFM
- 备注: 数据集，自监督掩码+蒸馏，持续预训练
- Backbone: Swin Transformer
- Backbone 1: Swin transformer
- 下游任务: Change Detection, Classification, Semantic Segmentation, Super-resolution
- 下游任务 1: change detection, classification, multi-label classification, semantic segmentation, and super-resolution
- Short Summary: 改论文注意到了地理空间数据集的多样性对MIM预训练十分重要。为了增加纹理细节，我们确保了各种地面采样距离（GSD），包括比Sentinel-2（GSD为10米）高得多分辨率的图像。此外，选择的标签数据集涵盖了广泛的通用遥感场景类，确保样本间的视觉多样性。通过蒸馏的方式让学生网络学习到ImageNet pretrain的特征。
