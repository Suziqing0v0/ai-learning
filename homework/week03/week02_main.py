import mystats

import os
folder=os.path.dirname(os.path.abspath(__file__))
data_path=os.path.join(folder,"data.txt")

try:
    n=mystats.read_number(data_path)
    s=max(n)
    t=min(n)

    result_path=os.path.join(folder,"result.txt")
    with open(result_path,"w",encoding="utf-8") as f:
        f.write(f"个数：{len(n)}\n")
        f.write(f"平均值：{round(mystats.get_mean(n),2)}\n")
        f.write(f"中位数：{mystats.get_median(n)}\n")
        f.write(f"标准差：{round(mystats.get_stdev(n),2)}\n")
        f.write(f"最大值：{s}\n")
        f.write(f"最小值：{t}\n")
        f.write(f"\n")
    print("正常运行")
except FileNotFoundError:
    print("文件不存在")