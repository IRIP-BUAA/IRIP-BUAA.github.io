---
title: RS-LLaVA Large Vision Language Model for Joint Captioning and Question Answering in Remote Sensing Imagery
author: Zack
date: 2024-03-15 00:00:00 +0800
categories: [RS]
tags: [paper, MLLM]
math: true
pin: false
---
- 论文名称: RS-LLaVA: Large Vision Language Model for Joint Captioning and Question Answering in Remote Sensing Imagery
- 模型架构: MLLM
- Visual Encoder: Transformer
- Text Encoder: Transformer
- Model Details: Vision Encoder：CLIP ViT-LText Encoder：Vicuna-v1.5
- Task: Image Caption, RS VQA
- Link: https://www.mdpi.com/2072-4292/16/9/1477
- Code/Project: https://github.com/BigData-KSU/RS-LLaVA
- Short Summary: 1. 通过集成caption和VQA数据集，提出了一个遥感领域的指令微调数据集2. 基于LLaVA模型，通过使用遥感数据对模型进行预训练和lora微调得到了了RS-LLaVA
- Published in: RS 2024
