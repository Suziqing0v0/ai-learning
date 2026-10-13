# 第 4 周任务卡 · NumPy 入门

**本周目标**：学会用 NumPy 处理一整组数据，不用再写循环。

**为什么学这个**：物理里到处是"对一整组数据做同样的运算"——一万个粒子、一千个时间点、一张图像的几百万个像素。用列表得写循环，用数组一行就够。**这是从"通用 Python"走向"科学计算"的第一道门。**

---

## Day 21 · 为什么用数组

### 先看差别

**用列表**（前两周的做法）：

```python
scores = [53, 87, 39, 98]
doubled = []
for s in scores:
    doubled.append(s * 2)
print(doubled)
```

**用数组**：

```python
import numpy as np

scores = np.array([53, 87, 39, 98])
doubled = scores * 2
print(doubled)
```

两个都得到 `[106, 174, 78, 196]`。但第二个**没写循环**——一句 `* 2` 就全部乘好了。

这个能力叫**向量化**（vectorization）：把"一个算完再算下一个"变成"整体一起算"。

### 逐行解释

```python
import numpy as np
```

- `import` = 导入，把 numpy 这个工具箱搬进来
- `numpy` = **num**erical **py**thon（数值 Python）的缩写，科学计算的基础库
- `as np` = as 是"**作为**"的意思，给它起个短名字叫 `np`
- 以后写 `np.array` 比写 `numpy.array` 省事，社区里所有人都用 `np`

```python
scores = np.array([53, 87, 39, 98])
```

- `np.array` = array 是"**数组**"，长得像列表，但能力强得多
- `([53, 87, 39, 98])` = 括号里给一个列表，它把列表变成数组

```python
doubled = scores * 2
```

- **关键**：`scores` 是数组，`* 2` 会**自动作用到每一个元素**
- 如果 `scores` 是列表，这句话不会出错但结果不一样（列表乘 2 = 复制两份）

### 怎么造数组

```python
np.array([53, 87, 39])      # 从列表创建
np.zeros(5)                 # 5 个 0
np.ones(3)                  # 3 个 1
np.arange(0, 10, 2)         # 0, 2, 4, 6, 8
np.linspace(0, 1, 5)        # 0 到 1 之间等距取 5 个点
```

| 名字 | 拆开看 | 意思 |
|---|---|---|
| `array` | array | 数组 |
| `zeros` / `ones` | zero / one + s | 全是 0 / 全是 1 |
| `arange` | a + range | 像 `range`，但返回数组 |
| `linspace` | line + space | 线性等距地取点 |

### 数组的三个属性

```python
a = np.array([53, 87, 39])
print(a.shape)     # (3,)   形状：有 3 个元素
print(a.dtype)     # int64  元素类型
print(a.size)      # 3      元素个数
```

### 验收标准

- [ ] 建一个数组存你那 8 个分数
- [ ] 打印出 `shape`、`dtype`、`size`
- [ ] 试 `* 2`、`+ 10`、`/ 2`，看结果是不是每个元素都变了
- [ ] 用 `np.arange` 和 `np.linspace` 各造一个数组，打印看看

**产出**：`day21_numpy.py`

---

## Day 22 · 索引与切片

数组取值和列表**几乎一样**，但多了一个本事：**一次能改一片**。

```python
a = np.array([53, 87, 39, 98, 69])

a[0]          # 53           第一个
a[-1]         # 69           最后一个
a[1:3]        # [87 39]      索引 1 到 3（不含 3）
a[:2]         # [53 87]      前两个
a[::2]        # [53 39 69]   每隔一个取
```

**数组独有的**：

```python
a[0] = 100          # 改一个
a[1:3] = 0          # 一次改一片 → [53 0 0 98 69]
```

**产出**：`day22_slice.py`

---

## Day 23 · 向量化：为什么数组快

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)        # [11 22 33 44]     对应位置相加
print(a * b)        # [10 40 90 160]    对应位置相乘
print(a ** 2)       # [1 4 9 16]
print(np.sqrt(a))   # [1. 1.41 1.73 2.]  开方
```

**要点**：两个数组运算时，是**对应位置的元素**在算，不是数学里的矩阵乘法。

**顺便感觉一下快多少**：用列表写循环和用数组直接算，各处理 100 万个数，比一比时间。

**产出**：`day23_vectorize.py`

---

## Day 24 · 条件筛选

**这是 NumPy 最爽的功能**——不写循环就能挑出符合条件的元素。

```python
scores = np.array([53, 87, 39, 98, 69, 75, 58, 40])

mask = scores >= 60          # 得到一个"真假数组"
print(mask)                  # [False  True False  True  True  True False False]

print(scores[mask])          # [87 98 69 75]  只留下 True 的位置
print(scores[scores >= 60])  # 一步写完，效果一样
print(scores[scores < 60])   # 不及格的
```

- `mask` = 面具、掩码。它是一串 True/False，True 的位置会被留下
- `scores >= 60` 会**对每个元素分别判断**，返回一串真假

**产出**：`day24_filter.py` —— 从分数数组里分别挑出优秀（≥90）、及格、不及格三组。

---

## Day 25 · 统计函数

```python
scores = np.array([53, 87, 39, 98, 69, 75, 58, 40])

scores.mean()     # 平均值
scores.max()      # 最大
scores.min()      # 最小
scores.sum()      # 总和
scores.std()      # 标准差
np.median(scores) # 中位数
```

**对比一下**：前两周你为了算这些写了四个函数，现在**一行一个**。

**二维数组和 `axis`**：

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])

m.sum()            # 21       全部加起来
m.sum(axis=0)      # [5 7 9]  按列（竖着）加
m.sum(axis=1)      # [6 15]   按行（横着）加
```

- `axis` = 轴。`axis=0` 是"沿着第 0 维"，也就是**往下竖着**加

**产出**：`day25_stats.py`

---

## Day 26–27 · 项目：用 NumPy 重写统计器

**要做什么**：把 `week02_stats.py` 里手写的那四个统计函数全换成 NumPy，再做一次数据探索。

**任务**

1. 读 `data.txt`（每行一个分数）
2. 用 NumPy 算：个数、平均值、中位数、标准差、最大值、最小值
3. **额外算三个**：
   - 及格率（≥60 的比例）
   - 最高分和最低分差多少
   - 每个分数偏离平均值多少（用 `scores - scores.mean()`）
4. 结果写进 `result_numpy.txt`

**对比要求**：把 NumPy 版和 Week 2 手写版的结果并排贴进 `week04_对比.md`，写一句话说感受。

**产出**：`week04_stats_numpy.py` + `result_numpy.txt` + `week04_对比.md`

---

## 提交方式

文件放进 `homework/week04/`，然后说：**「第 4 周提交」**。
