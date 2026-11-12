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

def mse(w,b):
    y_pred = w*x+b
    return ((y-y_pred)**2).mean()

plt.scatter(x, y, s=10)  
for w,b in [(2,1),(1,0),(3,2)]:
    plt.plot(x,w*x + b,label=f"w={w},b={b}")
    print(f"w={w},b={b} → MSE{mse(w,b):.4f}")
plt.title("散点")
plt.xlabel("x")    
plt.ylabel("y")
plt.legend()       
plt.grid(True)
plt.xlim(0, 10)    

plt.tight_layout()
plt.savefig(os.path.join(folder, "figure.png")) 
