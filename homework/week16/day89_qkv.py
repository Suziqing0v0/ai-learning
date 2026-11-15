# Day 89 · Q / K / V：把输入投影成三个不同角色
import numpy as np

X = np.array([[1., 0.],
              [0., 1.],
              [1., 1.]])

Wq = np.array([[1., 0.5],
               [0., 1.]])

Wk = np.array([[1., 0.],
               [0.5, 1.]])

Wv = np.array([[1., 2.],
               [3., 1.]])

Q = X @ Wq
K = X @ Wk
V = X @ Wv

scores = Q @ K.T
scaled = scores / np.sqrt(2)

weights = np.exp(scaled)
weights = weights / weights.sum(axis = 1, keepdims=True)

out = weights @ V
print(Q)
print(K)
print(V)
print(weights)
print(out)