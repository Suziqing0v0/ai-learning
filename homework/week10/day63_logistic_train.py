# Day 63 · 训练逻辑回归：梯度下降 + 决策边界
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

w = 0
b = 0
lr = 0.5 
for i in range(1000):
    p = sigmoid(w*x + b)
    if i%200 == 0:
        print(f"w={w},b={b}时， cross_entropy(y,p) = {cross_entropy(y,p)}")
    dw = np.mean((p-y)*x)
    db = np.mean(p-y)
    w = w-lr*dw
    b = b-lr*db

plt.scatter(x[y == 0],y[y == 0],label = "类别0")
plt.scatter(x[y == 1],y[y == 1],label = "类别1")

plt.axvline(x=-b/w, color="red", linestyle="--", label="决策边界")

plt.title("决策边界")
plt.xlabel("x")    
plt.ylabel("y")
plt.legend()       
plt.grid(True)
plt.tight_layout()                                  # 排版别挤在一起
plt.savefig(os.path.join(folder, "logistic.png")) 
