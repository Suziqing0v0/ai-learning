import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

plt.figure()
x=np.linspace(0,10,50)
y=np.sin(x)

plt.plot(x,y)
plt.savefig("line.png")
plt.show()

plt.figure()
x=np.linspace(0,10,50)
y=np.sin(x)

plt.scatter(x,y)
plt.savefig("scatter.png")
plt.show()

plt.figure()
names=["语文","数学","英语"]
values=[85,92,78]

plt.bar(names,values)
plt.savefig("bar.png")
plt.show()