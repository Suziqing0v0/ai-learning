# Day 73 · 评估：混淆矩阵、每类指标、错例分析
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from scipy.sparse import hstack

decks = [
    ("伪随机数", ["计算机没有骰子", "种子决定一切", "常见生成器", "线性同余法"]),
    ("贝叶斯定理", ["先验与后验", "似然函数", "经典例子"]),
    ("梯度下降", ["损失函数", "学习率", "收敛过程"]),
    ("决策树", ["信息增益", "分裂规则", "剪枝"]),
    ("聚类", ["K 怎么选", "中心点", "无监督的特点"]),
    ("神经网络", ["神经元", "激活函数", "反向传播"]),
    ("电动力学", ["麦克斯韦方程组", "电磁波", "边界条件", "矢量势"]),
    ("短视频脚本", ["前三秒抓人", "钩子怎么写", "节奏控制", "结尾引导"]),
    ("RAG", ["文档切分", "向量检索", "上下文拼接"]),
]

titles,pages,labels = [],[],[]

for name,points in decks:
    titles.append(name)
    pages.append(1)
    labels.append("标题页")
    for i,p in enumerate(points,start=2):
        titles.append(p)
        pages.append(i)
        labels.append("要点页")
    titles.append("总结与回顾")
    pages.append(len(points)+2)
    labels.append("总结页")

titles_arr = np.array(titles)

vec = TfidfVectorizer(analyzer="char", ngram_range=(1,2))
Xtxt = vec.fit_transform(titles)

Xpage = np.array(pages,dtype=float).reshape(-1,1)
X = hstack([Xtxt, Xpage]).tocsr()
y = np.array(labels)

Xtr, Xte, ytr, yte, t_tr, t_te = train_test_split(
    Xtxt, y, titles_arr, test_size=0.3, random_state=0, stratify=y
)

model = LogisticRegression(max_iter=2000)
model.fit(Xtr, ytr)
pred = model.predict(Xte)

cm = confusion_matrix(yte, pred, labels=["标题页", "要点页", "总结页"])
print(cm)
print(classification_report(yte, pred, zero_division=0))

wrong = yte != pred
for t, actual, guess in zip(t_te[wrong], yte[wrong], pred[wrong]):
    print(f"「{t}」 实际={actual} 猜={guess}")