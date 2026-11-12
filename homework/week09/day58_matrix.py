import os
import numpy as np

X = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,0],
])
w = np.array([1,2])
b=5
y = X@w+b
print(y)
print(y.shape)

y = X[:,0]*w[0]+X[:,1]*w[1]+b
print(y)
print(y.shape)
print(X.shape)
print(w.shape)

w = np.array([1,2,3])
print(y)
print(y.shape)