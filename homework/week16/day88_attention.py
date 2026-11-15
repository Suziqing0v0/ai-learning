# Day 88 · 注意力最小版本：点积 → softmax → 加权平均
import numpy as np

X = np.array([[1., 0.],
             [0., 1.],
             [1., 1.]])

scores = X @ X.T
scaled = scores / np.sqrt(X.shape[1])
weights = np.exp(scaled)
weights = weights / weights.sum(axis = 1, keepdims=True)
out = weights @ X

print(np.round(scores,3))
print(np.round(weights,3))
print(np.round(out,3))
