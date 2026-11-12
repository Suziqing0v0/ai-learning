# Day 62 · 交叉熵：分类为什么不用 MSE
import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

folder = os.path.dirname(os.path.abspath(__file__))

rng = np.random.default_rng(42)
n = 100

x=np.concatenate([rng.normal(-1,1,n),rng.normal(1,1,n)])
y=np.concatenate([np.zeros(n),np.ones(n)])

def sigmoid(z):
    sigma = 1 / (1 + np.exp(-z))
    return sigma

def cross_entropy(y,p):
    return -np.mean( y*np.log(p) + (1-y)*np.log(1-p) )


for w,b in ([0,0],[2,0]):
    p = sigmoid(w*x + b)
    print(f"w={w},b={b}时， cross_entropy(y,p) = {cross_entropy(y,p)}")

