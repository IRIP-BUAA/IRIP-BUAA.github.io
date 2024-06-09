---
title: GeoChat Grounded Large Vision-Language Model for Remote Sensing
author: Zack
date: 2024-01-01 00:00:00 +0800
categories: [CVPR]
tags: [paper, MLLM]
math: true
pin: false
---
- 论文名称: GeoChat: Grounded Large Vision-Language Model for Remote Sensing
- 模型架构: MLLM
- Visual Encoder: Transformer
- Text Encoder: Transformer
- Model Details: Vision Encoder：CLIP-ViTText Encoder： Vicuna-v1.5
- Task: Scene Classification, RS VQA, Visual Grounding
- Link: https://arxiv.org/abs/2311.15826
- Code/Project: https://github.com/mbzuai-oryx/geochat
- Short Summary: 1. RS多模态数据集：多模态数据集，且提出了一个生成数据的pipeline2. GeoChat：利用已有的数据微调LLaVA-1.5，利用lora微调；除了能够处理自然语言问题之外，用户还可以提供视觉提示（bounding box），并且模型能够回答有关ROI（指定感兴趣区域）的问题
- Published in: CVPR 2024
