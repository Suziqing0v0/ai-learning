import os 
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

folder = os.path.dirname(os.path.abspath(__file__))

x=np.linspace(1,10,100)
y_true=np.sin(x)
fig,axes=plt.subplots(2,2)
#1
noise=np.random.randn(100)*0.2
y_data=y_true + noise
axes[0,0].scatter(x,y_data,s=10,label="测量数据")
axes[0,0].plot(x,y_true,color="red",label="真实曲线")
axes[0,0].legend()
axes[0,0].set_xlabel("x")
axes[0,0].set_ylabel("sin(x)")
#2
axes[0,1].hist(noise,bins=20)
axes[0,1].set_xlabel("x")
axes[0,1].set_ylabel("noise")
#3
grouped=y_data.reshape(10,10).mean(axis=1)
x_grouped=x.reshape(10,10).mean(axis=1)
axes[1,0].plot(x_grouped,grouped,"o-")
axes[1,0].set_xlabel("x")
axes[1,0].set_ylabel("sin(x)")
#4
labels=["原始数据","分段平均","真实曲线"]
values=[y_data.std(),grouped.std(),y_true.std()]
axes[1,1].bar(labels,values)
axes[1,1].set_xlabel("数据来源")
axes[1,1].set_ylabel("标准差")

axes[0,0].set_title("带噪声的散点 + 真实曲线")
axes[0,1].set_title("噪声直方图")
axes[1,0].set_title("分区间求平均（降噪）")
axes[1,1].set_title("三种数据标准差对比")

plt.tight_layout()
plt.savefig(os.path.join(folder,"物理数据可视化.png"))