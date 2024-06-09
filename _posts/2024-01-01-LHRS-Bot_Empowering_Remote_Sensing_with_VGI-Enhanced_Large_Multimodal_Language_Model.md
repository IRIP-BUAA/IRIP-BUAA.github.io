---
title: LHRS-Bot: Empowering Remote Sensing with VGI-Enhanced Large Multimodal Language Model
author: Zack
date: 2024-01-01 00:00:00 +0800
categories: [Arxiv]
tags: [paper, MLLM]
math: true
pin: false
---
- 论文名称: LHRS-Bot: Empowering Remote Sensing with VGI-Enhanced Large Multimodal Language Model
- 模型架构: MLLM
- Visual Encoder: Transformer
- Text Encoder: Transformer
- Model Details: Vision Encoder：CLIP ViT-LText Encoder：LLaMA-2
- Task: Scene Classification, RS VQA, Visual Grounding
- Link: https://arxiv.org/abs/2402.02544
- Code/Project: https://github.com/NJU-LHRS/LHRS-Bot
- Short Summary: 1. 提出LHRS-Align数据集：大规模遥感领域的图像文本数据集，使用开源的全球地理数据生成的。2. 提出了LHRS-Instruct数据集，是一个专门为遥感图像理解定制的多模态指令跟随数据集。3. 在此基础上，提出了LHRS-Bot模型，采用了新的bridging strategy，并利用课程学习的方法来充分挖掘数据集种的内在知识4. 提出LHRS-Bench，用于对遥感领域的MLLM进行评估，包含690个单选题
- Published in: Arxiv 2024
