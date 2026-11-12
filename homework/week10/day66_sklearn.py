# Day 66 · sklearn 对照：为什么默认的 w 更小
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

folder = os.path.dirname(os.path.abspath(__file__))

rng = np.random.default_rng(42)
n = 100
x=np.concatenate([rng.normal(-1,1,n),rng.normal(1,1,n)])
y=np.concatenate([np.zeros(n),np.ones(n)])

X = x.reshape(-1,1)
m1 = LogisticRegression()
m1.fit(X,y)
print(m1.coef_)
print(m1.intercept_)

m2 = LogisticRegression(C=np.inf)
m2.fit(X,y)
print(m2.coef_)
print(m2.intercept_)

