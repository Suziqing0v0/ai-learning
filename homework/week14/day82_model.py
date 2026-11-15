# Day 82 · 搭 MLP：64 个像素 → 128 个隐藏单元 → 10 个类别
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

net = nn.Sequential(
    nn.Linear(64,128),
    nn.ReLU(),
    nn.Linear(128,10),
)

d = load_digits()
X = d.data / 16.0
y = d.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      random_state=0, stratify=y)

x = torch.tensor(Xtr[:4], dtype=torch.float32)
y_batch = torch.tensor(ytr[:4],)
logits = net(x)

print(x.shape, logits.shape)

probs = torch.softmax(logits, dim=1)
print(probs.shape, probs.sum(dim=1))

total = sum(p.numel() for p in net.parameters())
print(total)

loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(logits, y_batch)
print(loss)
