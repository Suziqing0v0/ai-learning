import os
folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(folder, "scores.csv")

import pandas as pd
pd.set_option("display.unicode.east_asian_width",True)
df=pd.read_csv(data_path)

print(df.groupby("班级")["物理"].mean())
print(df.groupby("班级")[["物理","数学"]].mean())
print(df.groupby("班级").size())
print(df.groupby("班级")["物理"].agg(["max","min"]))

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False

plt.figure()
平均分=df.groupby("班级")["物理"].mean()
plt.bar(平均分.index,平均分.values)

plt.title("各班物理平均分")
plt.xlabel("班级")
plt.ylabel("平均分")

plt.savefig(os.path.join(folder,"物理平均分.png"))