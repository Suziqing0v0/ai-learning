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
