# Day 87 · 看卷积核与特征图
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import os
import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import torch.optim as optim
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 让中文正常显示
plt.rcParams['axes.unicode_minus'] = False      # 让负号正常显示

folder = os.path.dirname(os.path.abspath(__file__))   # 图存在脚本旁边

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

w = net[0].weight.detach().numpy()
print(w.shape)

img, lab = test_ds[0]

feat = net[:3](img.unsqueeze(0)).detach().numpy()
print(feat.shape)

fig, axes = plt.subplots(2,8,figsize=(14,4))

for i in range(8):
    axes[0,i].imshow(w[i,0], cmap="gray")
    axes[0,i].set_title(f"核{i}")
    axes[0,i].axis("off")

    axes[1,i].imshow(feat[0,i], cmap="gray")
    axes[1,i].axis("off")

plt.tight_layout()                                  # 排版别挤在一起
plt.savefig(os.path.join(folder, "filters.png")) 
