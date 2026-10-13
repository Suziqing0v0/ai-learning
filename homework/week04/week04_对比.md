week2:
import os
folder=os.path.dirname(os.path.abspath(__file__))
data_path=os.path.join(folder,"data.txt")

def read_number(data_path):
    with open(data_path,"r",encoding="utf-8") as f:
        lines=f.readlines()
        nums=[int(i) for i in lines]
    return nums

def get_mean(n):
    b=sum(n)/len(n)
    return b

def get_median(n):
    c=sorted(n)
    d=len(c)
    if d%2!=0:
        e=d//2+1
        return c[e-1]
    else:
        f=d//2
        g=d//2+1
        h=c[f-1:g]
        j=(h[0]+h[1])/2
        return j

def get_stdev(n):
    k=get_mean(n)
    p=0
    for m in n:
        p=p+(m-k)**2
    q=p/len(n)
    r=q**0.5
    return r

try:
    n=read_number(data_path)
    s=max(n)
    t=min(n)

    result_path=os.path.join(folder,"result.txt")
    with open(result_path,"w",encoding="utf-8") as f:
        f.write(f"个数：{len(n)}\n")
        f.write(f"平均值：{round(get_mean(n),2)}\n")
        f.write(f"中位数：{get_median(n)}\n")
        f.write(f"标准差：{round(get_stdev(n),2)}\n")
        f.write(f"最大值：{s}\n")
        f.write(f"最小值：{t}\n")
        f.write(f"\n")
    print("正常运行")
except FileNotFoundError:
    print("文件不存在")

week4：
import os
import numpy as np

folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(folder, "data.txt")
result_path = os.path.join(folder, "result_numpy.txt")

scores = np.loadtxt(data_path)

print(scores.size)
print(scores.mean())
print(np.median(scores))
print(scores.std())
print(scores.max())
print(scores.min())
print((scores>=60).mean())
print(scores.max()-scores.min())
print(scores-scores.mean())

with open(result_path, "w", encoding="utf-8") as f:
    f.write(f"个数：{scores.size}\n")
    f.write(f"平均值：{scores.mean()}\n")
    f.write(f"中位数：{np.median(scores)}\n")
    f.write(f"标准差：{scores.std()}\n")
    f.write(f"最大值：{scores.max()}\n")
    f.write(f"最小值：{scores.min()}\n")
    f.write(f"及格率：{(scores>=60).mean()}\n")
    f.write(f"极差：{scores.max()-scores.min()}\n")
    f.write(f"与平均值的差：{scores-scores.mean()}\n")

week4代码简洁了很多，而且不用自己设计函数，不容易算错