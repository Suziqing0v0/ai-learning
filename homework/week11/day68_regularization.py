# Day 68 · 正则化：给"太复杂"加个价钱
import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.pipeline import make_pipeline

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   
plt.rcParams['axes.unicode_minus'] = False  

folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(folder, "data.txt")
data = np.loadtxt(data_path,delimiter=",")
x = data[:,0]
y = data[:,1]

rng = np.random.default_rng(0)
idx = rng.permutation(len(x))
tr = idx[:20]
te = idx[20:]
x_tr,y_tr = x[tr],y[tr]
x_te,y_te = x[te],y[te]

X_tr = x_tr.reshape(-1,1)
X_te = x_te.reshape(-1,1)

a_list = []
mse_tr_list = []
mse_te_list = []
for a in [0.0001,0.001,0.01,0.1,1,10,100,1000]:
    model = make_pipeline(
    StandardScaler(),
    PolynomialFeatures(9,include_bias=False),
    Ridge(alpha=a),
    )
    model.fit(X_tr,y_tr)
    y_pred_tr = model.predict(X_tr)
    mse_tr = np.mean((y_pred_tr-y_tr)**2)
    y_pred_te = model.predict(X_te)
    mse_te = np.mean((y_pred_te-y_te)**2)
    print(f"alpha={a} 训练MSE={mse_tr:.3f} 测试MSE={mse_te:.3f}")
    a_list.append(a)
    mse_tr_list.append(mse_tr)
    mse_te_list.append(mse_te)

plt.plot(a_list,mse_tr_list,"o-",label="训练曲线")
plt.plot(a_list,mse_te_list,"o-",label="测试曲线")
plt.xscale("log")
plt.title("正则化")
plt.xlabel("alpha")    
plt.ylabel("MSE")
plt.legend()       
plt.grid(True)
plt.tight_layout()                                 
plt.savefig(os.path.join(folder, "reg_curve.png"))