import os
import numpy as np

folder = os.path.dirname(os.path.abspath(__file__))
data = np.loadtxt(os.path.join(folder, "data.txt"), delimiter=",")

x = data[:,0]
y = data[:,1]

def mse(w,b):
    y_pred = w*x+b
    return ((y-y_pred)**2).mean()

w=0
b=0
lr=0.01

for i in range(500):
    y_pred = w*x+b
    dw = (((y_pred-y)*x).mean())*2
    db = ((y_pred-y).mean())*2
    w = w-dw*lr
    b = b-db*lr
    if i %50 == 0:
        print (f"第{i:3d}轮：w={w:.3f},b={b:.3f},loss={mse(w,b):.4f}")
    
print (f"最终：w={w:.3f},b={b:.3f},loss={mse(w,b):.4f}")

