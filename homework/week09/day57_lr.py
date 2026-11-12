import os
import numpy as np
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.abspath(__file__))
data = np.loadtxt(os.path.join(folder, "data.txt"), delimiter=",")

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 让中文正常显示
plt.rcParams['axes.unicode_minus'] = False      # 让负号正常显示

x = data[:,0]
y = data[:,1]

def mse(w,b):
    y_pred = w*x+b
    return ((y-y_pred)**2).mean()

def train(lr,n=500):
    w=0.0
    b=0.0
    history = []

    for i in range(n):
        y_pred = w*x+b
        dw = (((y_pred-y)*x).mean())*2
        db = ((y_pred-y).mean())*2
        w = w-dw*lr
        b = b-db*lr
        history.append(mse(w,b))

    return history

for lr in [0.001,0.01,0.02,0.03]:
    h = train(lr)
    plt.plot(h,label=f"lr={lr}")

plt.yscale("log")
plt.xlim(0,100)
plt.ylim(0.5,1e8)
plt.xlabel("轮数")
plt.ylabel("loss(对数)")

plt.legend()
plt.tight_layout()                                  # 排版别挤在一起
plt.savefig(os.path.join(folder, "loss_curves.png"))  
