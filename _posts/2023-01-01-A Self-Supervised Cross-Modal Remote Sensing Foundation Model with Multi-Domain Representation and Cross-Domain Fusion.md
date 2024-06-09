---
title: A Self-Supervised Cross-Modal Remote Sensing Foundation Model with Multi-Domain Representation and Cross-Domain Fusion
author: Zack
date: 2023-03-12 00:00:00 +0800
categories: [IGARSS]
tags: [paper, Pretrain]
math: true
pin: false
---
- 论文名称: A Self-Supervised Cross-Modal Remote Sensing Foundation Model with Multi-Domain Representation and Cross-Domain Fusion
- Link: https://ieeexplore.ieee.org/abstract/document/10282433
- Published in: IGARSS 2023
- Type: Pretrain
- Code/Project: ---
- 备注: 多模态，对比学习+重建
- 数据类型: 多光谱
- Backbone: Transformer
- 下游任务: single-modal interpretation/multi-modal interpretation
- Short Summary: 然而，多模态数据在传感器种类、成像机制、分辨率和光谱信息上具有独特性。现有方法主要针对单一模态数据，特别是光学遥感图像，直接将其应用于多模态数据很难平衡提取各模态特征，并突破单一模态数据的性能上限。一种基于多域表示和跨域融合概念的模型架构.对于多模态遥感输入数据，MSFE首先在相应的特征空间中学习各种特征，即在欧几里得空间中学习光学和红外数据，在双曲空间中学习高光谱数据，在复数空间中学习SAR数据。然后，基于自监督损失，MMFH通过多模态特征对齐和交互学习跨模态互补信息，从而提高基础模型对多模态遥感数据的解释性能。
