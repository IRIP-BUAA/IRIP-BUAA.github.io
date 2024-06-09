---
title: CMID: A Unified Self-Supervised Learning Framework for Remote Sensing Image Understanding
author: Zack
date: 2023-01-01 00:00:00 +0800
categories: [TGRS]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: CMID: A Unified Self-Supervised Learning Framework for Remote Sensing Image Understanding
- Link: https://arxiv.org/abs/2304.09670
- Published in: TGRS 2023
- Type: Pretrain
- Code/Project: https://github.com/NJU-LHRS/official-CMID
- 备注: 自监督，通过蒸馏将对比学习和掩码结合在一起
- Backbone: Transformer, CNN
- Backbone 1: architecture-agnostic(CNN/Transformer)
- 下游任务: Classification, Semantic Segmentation, Object Detection, Change Detection
- 下游任务 1: scene classification, semantic segmentation, object detection, and change detection
- Short Summary: 对图片一个做增强一个做mask，经过网络后同时计算两个分支的contrastive loss和mask分支的regression loss。
