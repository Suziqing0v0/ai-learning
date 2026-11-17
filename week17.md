# 第 17 周任务卡 · HuggingFace 微调与模型选择

**本周目标**：理解预训练模型怎样接收文本、输出向量，完成一次小型文本分类微调，
并能判断一个任务应该“微调、换模型，还是只改 prompt”。

**本周原则**：重点是会加载、会微调、会判断，不手写 Transformer，也不追大模型指标。
模型缓存固定在 `D:\ai-learning\hf-cache`，镜像地址为 `https://hf-mirror.com`。

| 天 | 内容 | 产出 |
|---|---|---|
| Day 91 | 分词器、特殊 token、BERT 输出形状 | `day91_hf_basics.py` |
| Day 92 | 用小型情感数据微调 `bert-tiny` | `day92_finetune.py` |
| Day 93 | 评估本地微调模型，并做模型选择决策 | `day93_model_choice.py` |
| 收尾 | 助手整理（不占天数） | 周总结 + Git 收尾 |

---

## Day 91 · 认识 HuggingFace 模型与分词器

**要做什么**：加载 `prajjwal1/bert-tiny` 的分词器和基础模型，
查看一句话怎样变成 token、整数 ID、注意力掩码，以及模型输出的形状。

**输入文本**：`I love learning AI`

**固定版本**：

```text
模型名：prajjwal1/bert-tiny
revision：6f75de8b60a9f8a2fdf7b69cbd86d9e64bcb3837
```

**必须打印**：

- tokenizer 的完整返回结果
- 整数 ID 对应的 token 列表
- `input_ids`、`attention_mask` 的形状
- `last_hidden_state`、`pooler_output` 的形状
- `last_hidden_state` 中 `[CLS]` 位置的前 5 个数值

**期望结果**：

```text
tokens:
['[CLS]', 'i', 'love', 'learning', 'ai', '[SEP]']

input_ids:
[101, 1045, 2293, 4083, 9932, 102]

attention_mask:
[1, 1, 1, 1, 1, 1]

input_ids 形状: torch.Size([1, 6])
attention_mask 形状: torch.Size([1, 6])
last_hidden_state 形状: torch.Size([1, 6, 128])
pooler_output 形状: torch.Size([1, 128])

[CLS] 前 5 个数值:
[-0.9839, 0.2701, -3.6263, -1.9761, -0.6285]
```

**验收**：

- 能解释 `[CLS]`、`[SEP]`、`attention_mask`
- 能解释 `(1, 6, 128)` 中三个维度
- 知道为什么推理时要写 `model.eval()` 和 `torch.no_grad()`

---

## Day 92 · 小型情感分类微调

**要做什么**：使用 `BertForSequenceClassification`，把 `bert-tiny` 微调成二分类器。

**数据**：自己录入 20 条简单英文情感句子，正负类各 10 条；
预留 6 条没参与训练的测试句。

**训练要求**：

- 固定随机种子，保证结果可复现
- tokenizer 使用 `padding=True`、`truncation=True`、`return_tensors="pt"`
- 批大小 `5`，优化器用 `AdamW`，学习率 `3e-4`
- 训练 5 轮，每轮打印平均 loss
- 训练后打印训练集和测试集准确率
- 把模型和 tokenizer 保存到 `homework/week17/tiny_sentiment/`

**验收**：

- loss 总体下降；参考值约为
  `0.7012 → 0.6974 → 0.6728 → 0.6202 → 0.6037`
- 训练集和测试集准确率参考值均为 `1.0`
- 模型能输出二分类 logits，形状为 `(样本数, 2)`
- 能说明“预训练”和“微调”的区别

---

## Day 93 · 评估与模型选择

**要做什么**：给本地微调分类器设计 12 条新的困难测试句，
记录准确率、单条平均延迟、错误样例，并完成选择决策表。

**实际测试集**：使用下面 12 条带有更强换词、否定和隐含表达的句子。

```python
test_texts = [
    "I absolutely love this movie",
    "I really hate waiting this long",
    "The result exceeded my expectations",
    "This experience left me disappointed",
    "I do not like this product",
    "The film was not good at all",
    "The food was not bad",
    "The staff were friendly and helpful",
    "I regret buying this item",
    "What a delightful surprise",
    "This is exactly what I wanted",
    "I would never recommend this service",
]

test_labels = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0]
```

**必须打印**：

- 每句话的真实标签、预测标签、积极类概率
- 单句推理延迟（毫秒）
- 总准确率和平均延迟

**参考结果**：

```text
预测正确：5 / 12
准确率：约 0.4167
错误数：7
平均单句延迟：约 0.8–1.2 ms（CPU，仅作量级参考）
```

错误包括 `I absolutely love this movie`、`The food was not bad`、
`The staff were friendly and helpful` 等训练集没见过的表达。

**必须比较三条路线**：

| 路线 | 适合的情况 | 主要代价 |
|---|---|---|
| 改 prompt，调用现成大模型 | 规则变化快、开放式语言任务 | API 费、延迟、外部依赖 |
| 直接换一个现成预训练模型 | 任务与已有模型能力接近 | 适配成本、模型体积、许可证 |
| 在自己的数据上微调 | 标签稳定、领域特殊、样例足够 | 标注、训练、维护、过拟合风险 |

**验收**：

- 给出本地微调模型的准确率和错误样例
- 对 Super PPT 的“版式分类”给出明确选择及理由
- 能判断什么时候不值得微调

---

## 收尾（助手负责，不占天数）

**第 17 周总结**

| 环节 | 结论 |
|---|---|
| 分词 | 文本先变成 token 和词表 ID，并加入 `[CLS]`、`[SEP]` |
| 预训练推理 | `BertModel` 输出上下文向量，不更新参数 |
| 微调 | 增加二分类头，使用带标签数据更新 BERT 和分类头 |
| 可复现 | 模型 revision、PyTorch 种子和 DataLoader 随机生成器都要固定 |
| 简单测试 | 20 条训练、6 条相近测试，最终训练/测试准确率均为 1.0 |
| 困难测试 | 12 条新表达只答对 5 条，准确率约 41.7% |
| 延迟 | CPU 单句前向计算约 0.8–1.2 ms，不含加载和分词 |
| 泛化 | 小数据上训练分数高，不代表能处理新表达和否定句 |

**Super PPT 决策**：暂不替换现有轻量版式分类器，也不接情感模型。
先积累真实页面标注；类别稳定、数据足够、轻量模型持续失败后，再考虑中文模型微调。


