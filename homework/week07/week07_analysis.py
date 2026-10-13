import os
folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(folder, "scores.csv")

import pandas as pd
pd.set_option("display.unicode.east_asian_width",True)
df=pd.read_csv(data_path)

import numpy as np
np.random.seed(42)
n=len(df)

df["性别"]=np.random.choice(["男","女"],n)
df["期中"]=np.round(np.clip(np.random.normal(73,8,n),0,100),1)
df["期末"]=np.round(np.clip(df["期中"]+np.random.normal(3,8,n),0,100),1)
df["作业"]=np.round(np.clip(np.random.normal(85,8,n),0,100),1)

df.loc[[3,17,42,88,105],"物理"]=np.nan

print(df.isna().sum())
print(df.dropna())
print(df.fillna(0))

print(df.groupby("性别")["物理"].mean())

进步=df["期末"]-df["期中"]
print(进步.mean())
print(进步.max(),进步.min())

偏科=df[abs(df["物理"]-df["数学"])>=40]
print(偏科)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False
folder = os.path.dirname(os.path.abspath(__file__))

fig,axes=plt.subplots(1,2)
#1
性别平均=df.groupby("性别")["物理"].mean()
axes[0].bar(性别平均.index,性别平均.values)
axes[0].set_title("男女生物理平均分")
axes[0].set_xlabel("性别")
axes[0].set_ylabel("物理平均分")

#2
axes[1].scatter(df["期中"],df["期末"], s=10) 
axes[1].set_title("期中vs期末")
axes[1].set_xlabel("期中成绩")
axes[1].set_ylabel("期末成绩")

axes[1].set_xlim(50,100)
axes[1].set_ylim(50,100)

axes[1].plot([50,100],[50,100],"r--",label="不进步也不退步")
axes[1].legend()

plt.tight_layout()
plt.savefig(os.path.join(folder, "week07_charts.png"))  


