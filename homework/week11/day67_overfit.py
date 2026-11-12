# Day 67 · 过拟合：训练集完美，测试集崩了
import os
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   
plt.rcParams['axes.unicode_minus'] = False  

folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(folder, "data.txt")

rng = np.random.default_rng(42)
x = np.linspace(0,10,50)
y = 2*x + 1 + rng.normal(0,1,50)

np.savetxt(data_path,np.column_stack([x,y]),fmt="%.4f",delimiter=",")

data = np.loadtxt(data_path,delimiter=",")
x = data[:,0]
y = data[:,1]

rng = np.random.default_rng(0)
idx = rng.permutation(len(x))
tr = idx[:20]
te = idx[20:]
x_tr,y_tr = x[tr],y[tr]
x_te,y_te = x[te],y[te]

xs = np.linspace(0,10,400)

for degree in [1,3,9,15]:
    coef = np.polyfit(x_tr, y_tr,degree)
    y_pred_tr = np.polyval(coef, x_tr)
    y_pred_te = np.polyval(coef, x_te)
    mse_tr = ((y_pred_tr - y_tr)**2).mean()
    mse_te = ((y_pred_te - y_te)**2).mean() 
    print(f"degree={degree} 训练={mse_tr:.3f} 测试={mse_te:.3f}")
    y_pred_te = np.polyval(coef, xs)
    plt.plot(xs, y_pred_te, label=f"{degree}次")

plt.scatter(x_tr, y_tr, s=12,label="训练集") 
plt.scatter(x_te, y_te, s=12,label="测试集") 

plt.title("拟合")
plt.xlabel("x")    
plt.ylabel("y")
plt.legend()       
plt.grid(True)
plt.xlim(0, 10)    
plt.ylim(0, 25)

plt.tight_layout()                                  # 排版别挤在一起
plt.savefig(os.path.join(folder, "overfit.png"))