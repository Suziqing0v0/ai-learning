import os
import numpy as np
import pandas as pd

pd.set_option("display.unicode.east_asian_width",True)

folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(folder, "scores.csv")

np.random.seed(42)
n=120
df=pd.DataFrame({
    "学号":range(1,n+1),
    "班级":np.random.choice(["一班","二班","三班"],n),
    "物理":np.round(np.clip(np.random.normal(75,12,n),0,100),1),
    "数学":np.round(np.clip(np.random.normal(78,15,n),0,100),1),
})

df.to_csv(data_path,index=False,encoding="utf-8-sig")
print("数据已生成:",data_path)

df=pd.read_csv(data_path)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)