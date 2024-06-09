---
title: SpectralGPT Spectral Foundation Model
author: Zack
date: 2024-01-01 00:00:00 +0800
categories: [TPAMI]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: SpectralGPT: Spectral Foundation Model
- Link: https://arxiv.org/pdf/2311.07113
- Published in: TPAMI 2024
- Type: Pretrain
- Code/Project: https://github.com/danfenghong/IEEE_TPAMI_SpectralGPT
- 备注: 自监督MAE，以渐进式训练方式在多个数据集上进行训练
- Backbone: Transformer
- 下游任务: Classification, Semantic Segmentation, Change Detection
- Short Summary: 虽然大多数基础模型都是为了有效地处理各种视觉任务的RGB图像而定制的，但在光谱数据方面的研究存在明显的差距。采用MAE架构构建，多目标重建策略；generative pretrained transformer(GPT)
