# Day 61 · sigmoid：把任意数压到 0~1
import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

folder = os.path.dirname(os.path.abspath(__file__))

z = np.linspace(-10,10,200)
sigma = 1 / (1 + np.exp(-z))

plt.plot(z,sigma)
plt.title("sigmoid 函数")
plt.xlabel("z")
plt.ylabel("sigma")
plt.grid(True)

plt.tight_layout()
plt.savefig(os.path.join(folder, "sigmoid.png"))

print(f"z=-10,sigma[0].:4f")
print(f"z=-10,sigma[100].:4f")
print(f"z=-10,sigma[-1].:4f")