# Day 86 · 训练 CNN：两层卷积 + 池化
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import os
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import torch.optim as optim

tf = transforms.ToTensor()
train_ds = datasets.MNIST(r"D:\ai-learning\data", train=True,
                       download=False, transform=tf)
test_ds = datasets.MNIST(r"D:\ai-learning\data", train=False,
                       download=False, transform=tf)

train_dl = DataLoader(train_ds, batch_size=64, shuffle=True)
test_dl = DataLoader(test_ds, batch_size=64, shuffle=False)

net = nn.Sequential(
    nn.Conv2d(1, 8, 3), nn.ReLU(), nn.MaxPool2d(2),
    nn.Conv2d(8, 16, 3), nn.ReLU(), nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(16 * 5 * 5, 10),
)

print("参数量：", sum(p.numel() for p in net.parameters()))

loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=1e-3)
    
for epoch in range(2):
    net.train()
    for xb, yb in train_dl:
        optimizer.zero_grad()
        loss = loss_fn(net(xb),yb)
        loss.backward()
        optimizer.step()
    
    correct = 0
    net.eval()
    with torch.no_grad():
        for xb, yb in test_dl:   
            correct += (net(xb).argmax(1) == yb).sum().item()
    print(f"epoch {epoch}: acc={correct / len(test_ds):.4f}")