# Day 83 · 训练循环：epoch / batch / 准确率曲线
import os
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import torch.optim as optim

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 让中文正常显示
plt.rcParams['axes.unicode_minus'] = False      # 让负号正常显示

folder = os.path.dirname(os.path.abspath(__file__))  

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

Xtr = torch.tensor(Xtr, dtype=torch.float32)
Xte = torch.tensor(Xte, dtype=torch.float32)
ytr = torch.tensor(ytr, dtype=torch.long)
yte = torch.tensor(yte, dtype=torch.long)

loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=1e-3)

def evaluate():
    net.eval()
    with torch.no_grad():
        pred = net(Xte).argmax(dim=1)
        return (pred == yte).float().mean().item()

def evaluate_train():
    net.eval()
    with torch.no_grad():
        pred = net(Xtr).argmax(dim=1)
        return (pred == ytr).float().mean().item()

acc_train_list = []
acc_test_list = []
loss_history = []

n = (len(Xtr) + 63) // 64

for epoch in range(50):
    net.train()
    perm = torch.randperm(len(Xtr))
    epoch_loss = 0
    for i in range(0,len(Xtr),64):
        idx = perm[i:i+64]
        optimizer.zero_grad()
        loss = loss_fn(net(Xtr[idx]),ytr[idx])
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()

    acc_train = evaluate_train()
    acc_test = evaluate()
    acc_train_list.append(acc_train)
    acc_test_list.append(acc_test)
    loss_history.append(epoch_loss / n)
    
    
    if epoch % 10 == 0:
        print(f"epoch={epoch} 训练准确率={acc_train} 测试准确率={acc_test}")

fig, axes = plt.subplots(1,2, figsize=(11, 4))

axes[0].plot(loss_history)
axes[0].set_title("训练损失")

axes[1].plot(acc_train_list, label="训练")
axes[1].plot(acc_test_list, label="测试")
axes[1].legend()
axes[1].set_title("准确率")

plt.tight_layout()
plt.savefig(os.path.join(folder, "train_curves.png"))

