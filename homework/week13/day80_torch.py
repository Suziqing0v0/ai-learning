# Day 80 · PyTorch：用 backward() 重写手推的反向传播
import os
import numpy as np
import torch

X_np = np.array([[0.,0.], [0.,1.], [1.,0.], [1.,1.]])
y_np = np.array([[0.], [1.], [1.], [0.]])

rng = np.random.default_rng(0)
W1_np = rng.normal(size=(2, 3))
b1_np = rng.normal(size=(3,))
W2_np = rng.normal(size=(3, 1))
b2_np = rng.normal(size=(1,))

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0,z)

def forward(X,W1,b1,W2,b2):
    z1 = X @ W1 + b1
    h = relu(z1)
    z2 = h @ W2 + b2
    out = sigmoid(z2)
    return z1,h,out

def loss_numpy(X,y,W1,b1,W2,b2):
    z1,h,out = forward(X,W1,b1,W2,b2)
    return ((out - y)**2).mean() 

z1,h,out = forward(X_np,W1_np,b1_np,W2_np,b2_np)
n = 4

d_out = ((out - y_np)*2) / n
d_z2 = d_out*out*(1 - out)
dW2 = h.T @ d_z2
db2 = d_z2.sum(axis=0)
d_h = d_z2 @ W2_np.T
d_z1 = d_h * (z1 > 0)
dW1 = X_np.T @ d_z1
d_b1 = d_z1.sum(axis=0)

#torch
X = torch.tensor(X_np)
y = torch.tensor(y_np)
W1 = torch.tensor(W1_np, requires_grad=True)
W2 = torch.tensor(W2_np, requires_grad=True)
b1 = torch.tensor(b1_np, requires_grad=True)
b2 = torch.tensor(b2_np, requires_grad=True)

out_t = torch.sigmoid(torch.relu(X @ W1 + b1) @ W2 + b2)
loss_init = ((out_t - y) ** 2).mean()
loss_init.backward()

print(f"loss numpy {loss_numpy(X_np, y_np, W1_np, b1_np, W2_np, b2_np):.8f}  torch {loss_init.item():.8f}")                                  # 和 numpy 比
print(np.abs(W2.grad.numpy() - dW2).max())
print(np.abs(W1.grad.numpy() - dW1).max())

optimizer = torch.optim.SGD([W1,b1,W2,b2],lr = 0.5)

for i in range(3000):
    optimizer.zero_grad()
    out = torch.sigmoid(torch.relu(X @ W1 + b1) @ W2 + b2)
    loss_torch = ((out - y) **2).mean()
    loss_torch.backward()
    optimizer.step()



with torch.no_grad():
    out = torch.sigmoid(torch.relu(X @ W1 + b1) @ W2 + b2)
    acc = ((out > 0.5) == (y > 0.5)).float().mean()
    print(f"训练后：acc ={acc} out={out}" )

