# Day 65 · 阈值与权衡：精确率-召回率曲线
# Day 64 · 混淆矩阵：准确率、精确率、召回率
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

precisions = []
recalls = []

for th in np.arange(0.1,1.0,0.1):
    p = sigmoid(w*x + b)
    pred = (p >= th).astype(float)

    TP = ((pred == 1) & (y == 1)).sum()
    FP = ((pred == 1) & (y == 0)).sum()
    FN = ((pred == 0) & (y == 1)).sum()
    TN = ((pred == 0) & (y == 0)).sum()
    if TP+FP == 0:
        continue

    准确率 = (TP + TN) / (TP + TN + FP + FN)
    精确率 = TP / (TP + FP)
    召回率 = TP / (TP + FN)
    print(f"th={th} 精确率={精确率} 召回率={召回率}")
    precisions.append(精确率)
    recalls.append(召回率)

x = recalls
y = precisions
plt.plot(x, y, "o-")   
plt.title("PR曲线")
plt.xlabel("召回率")    
plt.ylabel("精确率")
plt.legend()       
plt.grid(True)

plt.tight_layout()                                  
plt.savefig(os.path.join(folder, "pr_curve.png")) 

