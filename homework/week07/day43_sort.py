import os
folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(folder, "scores.csv")

import pandas as pd
pd.set_option("display.unicode.east_asian_width",True)
df=pd.read_csv(data_path)

print(df.sort_values("物理").head(10))
print(df.sort_values("物理",ascending=False).head(10))
df["总分"]=df["物理"]+df["数学"]
print(df["总分"])
df["平均分"]=df["总分"]/2
print(df["平均分"])
print(df.sort_values("总分",ascending=False))
print(df[df["总分"]>=180])
a=df[df["总分"]>=180]
print(a.shape[0])
