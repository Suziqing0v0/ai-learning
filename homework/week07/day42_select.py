import os
folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(folder, "scores.csv")

import pandas as pd
pd.set_option("display.unicode.east_asian_width",True)
df=pd.read_csv(data_path)

print(df["物理"])
print(df[["学号","物理"]])
print(df[df["物理"]>=90])
print(df[(df["物理"]>=90) & (df["数学"]>=90)])
结果1=df[df["物理"]>=90]
print(结果1.shape[0])
结果2=df[(df["物理"]>=90) & (df["数学"]>=90)]
print(结果2.shape[0])