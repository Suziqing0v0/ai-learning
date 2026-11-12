# Day 69 · 交叉验证：一次划分不够，换着考
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   
plt.rcParams['axes.unicode_minus'] = False  

folder = os.path.dirname(os.path.abspath(__file__))

rng = np.random.default_rng(42)
n = 100

x=np.concatenate([rng.normal(-1,1,n),rng.normal(1,1,n)])
y=np.concatenate([np.zeros(n),np.ones(n)])
X = x.reshape(-1,1)

model = LogisticRegression()
scores = cross_val_score(model,X,y,cv=5)
print(scores)
print(f"平均{scores.mean():.4f} 标准差{scores.std():.4f}")

X_tr,X_te,y_tr,y_te = train_test_split(X,y,test_size=0.3,random_state=0)
model.fit(X_tr,y_tr)
print(f"单次划分准确率{model.score(X_te,y_te):.4f}")


