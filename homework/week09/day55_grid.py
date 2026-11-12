import os
import numpy as np
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.abspath(__file__))
data = np.loadtxt(os.path.join(folder,"data.txt"),delimiter=",")

x = data[:,0]
y = data[:,1]

def mse(w,b):
    y_pred = w*x + b
    return((y-y_pred)**2).mean()

best_w = None
best_b = None
best_loss = 1e9

for w in np.arange(0,4,0.1):
    for b in np.arange(0,2,0.1):
        loss = mse(w,b)
        if loss < best_loss:
            best_w = w
            best_b = b
            best_loss = loss

print(f"最优 w={best_w:.2f},b={best_b:.2f},MSE={best_loss:.4f}")
