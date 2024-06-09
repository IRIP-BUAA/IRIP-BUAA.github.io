---
title: EarthGPT A Universal Multi-modal Large Language Model for Multi-sensor Image Comprehension in Remote Sensing Domain
author: Zack
date: 2024-05-10 00:00:00 +0800
categories: [Arxiv]
tags: [paper, MLLM]
math: true
pin: false
---
- 论文名称: EarthGPT: A Universal Multi-modal Large Language Model for Multi-sensor Image Comprehension in Remote Sensing Domain
- 模型架构: MLLM
- Visual Encoder: CNN, Transformer
- Text Encoder: Transformer
- Model Details: Vision Encoder：DINOv2 ViT-L/14、CLIP ConvNeXt-LText Encoder：LLaMA-2
- Task: Scene Classification, Image Caption, Visual Grounding, RS VQA, Object Detection
- Link: https://arxiv.org/abs/2401.16822
- Code/Project: https://github.com/wivizhang/EarthGPT
- Short Summary: 1. 提出了一种同一集成各种多传感器遥感解释任务的MLLM，EarthGPT，提出了视觉增强感知机制和跨模态相互理解的方法，最后提出了一种遥感领域的多传感器多任务的统一指令微调方法 2. 构建了最大的多模态多传感器的遥感指令跟随数据集MMRS-1M，由超过100万个图像文本对组成，包括有光学、合成孔径雷达（SAR）和红外图像
- Published in: Arxiv 2024
