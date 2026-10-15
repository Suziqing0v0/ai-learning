import os
import matplotlib.pyplot as plt
import numpy as np

folder = os.path.dirname(os.path.abspath(__file__)) 

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False   

#1
rng = np.random.default_rng(42)

fig,axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].hist(rng.normal(0,1,10000),bins=30)
axes[1].hist(rng.normal(5,1,10000),bins=30)

axes[0].set_title("均值=0的正态分布")
axes[0].set_xlabel("x")
axes[0].set_ylabel("落在这个区间的个数")

axes[1].set_title("均值=5的正态分布")
axes[1].set_xlabel("x")
axes[1].set_ylabel("落在这个区间的个数")

plt.tight_layout()                                
plt.savefig(os.path.join(folder, "day48_hist.png")) 

#2
for n in [10,100,1000,10000,100000]:
    data = rng.normal(0,1,n)
    print(f"样本量：{n}:平均值：{ data.mean():.6f}")