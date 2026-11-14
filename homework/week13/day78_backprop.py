# Day 78 · 反向传播：链式法则手推两层网络
import os
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(5, 2))
y = np.array([[1.], [0.], [1.], [0.], [0.]])

W1 = rng.normal(size=(2, 3))
b1 = rng.normal(size=(3,))
W2 = rng.normal(size=(3, 1))
b2 = rng.normal(size=(1,))

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

def loss(X,y,W1,b1,W2,b2):
    z1,h,out = forward(X,W1,b1,W2,b2)
    return ((out - y)**2).mean() 

z1,h,out = forward(X,W1,b1,W2,b2)
n = 5

d_out = ((out - y)*2) / n
d_z2 = d_out*out*(1 - out)
dW2 = h.T @ d_z2
db2 = d_z2.sum(axis=0)
d_h = d_z2 @ W2.T
d_z1 = d_h * (z1 > 0)
dW1 = X.T @ d_z1
d_b1 = d_z1.sum(axis=0)

print(loss(X,y,W1,b1,W2,b2))
print(dW2)
print(db2)
print(dW1)
print(d_b1)

eps = 1e-6

W2p = W2.copy()
W2p[0,0] += eps
W2m = W2.copy()
W2m[0,0] -= eps

loss_plus2 = loss(X,y,W1,b1,W2p,b2)
loss_minus2 = loss(X,y,W1,b1,W2m,b2)

num2 = (loss_plus2 - loss_minus2) / (eps * 2)

W1p = W1.copy()
W1p[0,0] += eps
W1m = W1.copy()
W1m[0,0] -= eps

loss_plus1 = loss(X,y,W1p,b1,W2,b2)
loss_minus1 = loss(X,y,W1m,b1,W2,b2)

num1 = (loss_plus1 - loss_minus1) / (eps * 2)

print(f"W2[0,0] 解析 {dW2[0,0]} 数值 {num2} 差 {abs(dW2[0,0]-num2)}")
print(f"W1[0,0] 解析 {dW1[0,0]} 数值 {num1} 差 {abs(dW1[0,0]-num1)}")






