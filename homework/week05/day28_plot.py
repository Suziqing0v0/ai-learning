import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

x=np.linspace(0,10,100)
y=np.sin(x)

plt.plot(x,y)
plt.savefig("sin.png")
plt.show()