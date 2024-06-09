---
title: SkyEyeGPT Unifying Remote Sensing Vision-Language Tasks via Instruction Tuning with Large Language Model
author: Zack
date: 2024-01-01 00:00:00 +0800
categories: [Arxiv]
tags: [paper, MLLM]
math: true
pin: false
---
- 论文名称: SkyEyeGPT: Unifying Remote Sensing Vision-Language Tasks via Instruction Tuning with Large Language Model
- 模型架构: MLLM
- Visual Encoder: Transformer
- Text Encoder: Transformer
- Model Details: Vision Encoder：EVA-CLIPText Encoder：LLaMA2-chat
- Task: Image Caption, Visual Grounding, RS VQA
- Link: https://arxiv.org/abs/2401.09712
- Code/Project: https://github.com/ZhanYang-nwpu/SkyEyeGPT
- Short Summary: 1.遥感领域的视觉语言指令数据集（SkyEye968k），包括单任务和多任务对话指令，包括968k条样本的指令跟随数据集2. 提出SkyEyeGPT模型，通过一个对齐层将RS视觉特征投影到语言领域后，它们与任务特定的指令一起被馈送到基于LLM的RS解码器中；设计了一个两阶段微调方法，第一阶段是遥感图文对齐，第二阶段是多任务对话微调
- Published in: Arxiv 2024
