---
title: Popeye A Unified Visual-Language Model for Multi-Source Ship Detection from Remote Sensing Imagery
author: Zack
date: 2024-02-12 00:00:00 +0800
categories: [Arxiv]
tags: [paper, MLLM]
math: true
pin: false
---
- 论文名称: Popeye: A Unified Visual-Language Model for Multi-Source Ship Detection from Remote Sensing Imagery
- 模型架构: MLLM
- Visual Encoder: Transformer
- Text Encoder: Transformer
- Model Details: Vision Encoder：CLIP ViT-L、DINOv2 ViT-LText Encoder：LLaMA
- Task: Ship Detection
- Link: https://arxiv.org/abs/2403.03790
- Code/Project: -
- Short Summary: 1. 设计了一种image-to-caption的方法来统一各种船只检测数据集，基于现有的公开数据集构建了一个多模态多源指令跟随数据集MMShip（统一标记范式）  2. 提出Popeye架构，主要包括四个部分，统一标记范式、跨模态图像解释方法（通过多尺度多模态特征融合模块和视觉-语言对齐调整模块实现视觉-语言对齐，在 COCO Caption 数据集上对齐）、knowledge adaption paradigm（在 MMShip 数据集上进行船只领域适应阶段的训练）、与 SAM（Segment Anything Model）的集成
- Published in: Arxiv 2024
