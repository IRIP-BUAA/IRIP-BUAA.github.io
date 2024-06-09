---
title: Change-Aware Sampling and Contrastive Learning for Satellite Images
author: Zack
date: 2023-01-01 00:00:00 +0800
categories: [CVPR]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: Change-Aware Sampling and Contrastive Learning for Satellite Images
- Link: https://openaccess.thecvf.com/content/CVPR2023/html/Mall_Change-Aware_Sampling_and_Contrastive_Learning_for_Satellite_Images_CVPR_2023_paper.html
- Published in: CVPR 2023
- Type: Pretrain
- Code/Project: https://github.com/utkarshmall13/CACo
- 备注: 自监督，对比学习
- Backbone: Resnet
- Backbone 1: CNN（ResNet-18, ResNet-50）
- 下游任务: Classification, Change Detection, Semantic Segmentation
- 下游任务 1: Classification（Landcover classification），Change detection，Semantic segmentation，Change Events
- Short Summary: 季节变化损失与SeCo相同，使用同一地点几个月时间内的图片作为正样本，其他地点的图片作为负样本。长时间变化用几个月内的做正样本，长时间后的图片做负样本。
