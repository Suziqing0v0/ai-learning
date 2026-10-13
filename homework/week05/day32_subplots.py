import os 
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

folder = os.path.dirname(os.path.abspath(__file__))

x=np.linspace(0,10,100)

fig,axes=plt.subplots(2,2)

axes[0,0].plot(x,np.sin(x))
axes[0,1].plot(x,np.cos(x))
axes[1,0].plot(x,np.sin(x)*np.cos(x))
axes[1,1].plot(x,np.sin(x)+np.cos(x))

axes[0,0].set_title("sin(x)")
axes[0,1].set_title("cos(x)")
axes[1,0].set_title("sin(x)*cos(x)")
axes[1,1].set_title("sin(x)+cos(x)")

plt.tight_layout()

plt.savefig(os.path.join(folder,"four.png"))