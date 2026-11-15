# Day 84 · 训练技巧：学习率与批大小对比
import time
import os
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import torch.optim as optim

d = load_digits()
X = d.data / 16.0
y = d.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      random_state=0, stratify=y)

Xtr = torch.tensor(Xtr, dtype=torch.float32)
Xte = torch.tensor(Xte, dtype=torch.float32)
ytr = torch.tensor(ytr, dtype=torch.long)
yte = torch.tensor(yte, dtype=torch.long)

def run(lr=1e-3, bs=64, epochs=20, seed=0):   
    torch.manual_seed(seed)
    net = nn.Sequential(
        nn.Linear(64,128),
        nn.ReLU(),
        nn.Linear(128,10),
    )

    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(net.parameters(), lr=lr)
    
    t0 = time.time()
    for epoch in range(epochs):
        net.train()
        perm = torch.randperm(len(Xtr))
        for i in range(0,len(Xtr),bs):
            idx = perm[i:i+bs]
            optimizer.zero_grad()
            loss = loss_fn(net(Xtr[idx]),ytr[idx])
            loss.backward()
            optimizer.step()

    with torch.no_grad():
        net.eval()
        pred = net(Xte).argmax(dim=1)
        acc = (pred == yte).float().mean().item()


    return acc, time.time() - t0

print("学习率对比")
for lr in (1e-4,1e-3,1e-2,1e-1):
    acc, t = run(lr=lr)
    print(f"lr={lr:<7} test={acc:.3f} t={t:.1f}s")

print("批大小对比")
for bs in (16,64,256):
    acc, t = run(bs=bs)
    print(f"batch={bs:<4} test={acc:.3f} t={t:.1f}s")
    
    
