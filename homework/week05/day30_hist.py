import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

data=np.random.randn(1000)
plt.figure()
plt.hist(data,bins=5)
plt.savefig("hist5.png")

plt.figure()
plt.hist(data,bins=30)
plt.savefig("hist30.png")

plt.figure()
plt.hist(data,bins=100)
plt.savefig("hist100.png")
