---
title: Multi Modal Multi Objective Contrastive Learning for Sentinel 1-2 Imagery
author: Zack
date: 2023-12-01 00:00:00 +0800
categories: [CVPRW]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: Multi Modal Multi Objective Contrastive Learning for Sentinel 1-2 Imagery
- Link: https://openaccess.thecvf.com/content/CVPR2023W/EarthVision/html/Prexl_Multi-Modal_Multi-Objective_Contrastive_Learning_for_Sentinel-12_Imagery_CVPRW_2023_paper.html
- Published in: CVPRW 2023
- Type: Pretrain
- Code/Project: ---
- 备注: 自监督，对比学习，多模态
- Backbone: Resnet
- Backbone 1: CNN(ResNet18)
- 下游任务: Classification, Regression
- 下游任务 1: Classification(Land-cover,Crop type mapping,), Regression (Biomass estimation)
- Short Summary: 构建模态内和模态间相似度损失函数，通过地理编码获取更难的对比学习负样本对
