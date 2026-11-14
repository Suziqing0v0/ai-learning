# Day 77 · 前向传播：从一个神经元到两层网络
import os
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
X = rng.normal(size=(5,2))
w1 = rng.normal(size=(2,3))
b1 = rng.normal(size=(3,))
w2 = rng.normal(size=(3,1))
b2 = rng.normal(size=(1,))

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0,z)

h = relu(X @ w1 + b1)
out = sigmoid(h @ w2 + b2)

print(X.shape, h.shape, out.shape)
print(out)

out_no_relu = sigmoid((X @ w1 + b1) @ w2 + b2)

w_eff = w1 @ w2
b_eff = b1 @ w2 + b2
out_one = sigmoid(X @ w_eff + b_eff)

print("没有 ReLU == 压成一层 ？", np.allclose(out_no_relu,out_one))
print("有 ReLU == 压成一层 ？", np.allclose(out,out_one))



