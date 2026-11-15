# Day 81 · 数据：1797 张 8x8 手写数字
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 让中文正常显示
plt.rcParams['axes.unicode_minus'] = False      # 让负号正常显示

folder = os.path.dirname(os.path.abspath(__file__))  

d = load_digits()
X = d.data / 16.0
y = d.target

print(X.shape, y.shape)
print("像素范围", X.min(), X.max())
print(np.bincount(y))

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      random_state=0, stratify=y)

print(Xtr.shape, Xte.shape)

fig, axes = plt.subplots(1,5, figsize=(10, 2.5))
for ax, img, lab in zip(axes, d.images[:5], y[:5]):
    ax.imshow(img, cmap="gray")
    ax.set_title(str(lab))
    ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(folder, "digits.png"))