import os 
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

folder = os.path.dirname(os.path.abspath(__file__))

x=np.linspace(0,10,100)
y=np.sin(x)

plt.plot(x,y,label="正弦曲线")
plt.title("正弦函数")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.ylim(-1.5,1.5)

plt.savefig(os.path.join(folder,"sin_labelled.png"))
