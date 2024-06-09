---
title: H2RSVLM: Towards Helpful and Honest Remote Sensing Large Vision Language Model
author: Zack
date: 2024-01-01 00:00:00 +0800
categories: [Arxiv]
tags: [paper, MLLM]
math: true
pin: false
---
- 论文名称: H2RSVLM: Towards Helpful and Honest Remote Sensing Large Vision Language Model
- 模型架构: MLLM
- Visual Encoder: Transformer
- Text Encoder: Transformer
- Model Details: Vision Encoder：CLIP ViT-LText Encoder：Vicuna-v1.5
- Task: Scene Classification, RS VQA, Visual Grounding
- Link: https://arxiv.org/abs/2403.20213
- Code/Project: https://github.com/opendatalab/H2RSVLM
- Short Summary: 1. 创建了HqDC-1.4M数据集，还构建了两个指令微调数据集HqDC-Instruct和RS-Specialized-Instruct    2. 针对幻觉问题，构建了第一个遥感self-awareness数据集，RSSA。包含一系列可回答和不可回答的任务    3. 基于上述数据，通过预训练和监督微调两个步骤，基于LLaVA模型训练了H2RSVLM模型（helpfulness 和 honesty）
- Published in: Arxiv 2024
