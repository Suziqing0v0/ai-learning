import pandas as pd
pd.set_option("display.unicode.east_asian_width",True)

df=pd.DataFrame({
    "姓名":["小明","小红","小刚"],
    "班级":["一班","一班","二班"],
    "物理":[85,92,78],
    "数学":[90,88,95],
})

print(df)