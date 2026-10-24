# 第 5 周任务卡 · Matplotlib 画图

**本周目标**：把一组数据变成一张能放进报告里的图。

**为什么学这个**：物理里"看一眼图"往往比看一百个数字有用——曲线是不是直线、有没有峰、分布偏不偏，图上一目了然。这也是你以后写论文、做报告最常用的技能。

**本周的统一约定**：图都**存成 PNG 文件**，不依赖弹窗。这样出问题好排查，也方便你直接看。

---

## Day 28 · 第一条曲线

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.savefig("sin.png")
plt.show()
```

### 逐行解释

**`import matplotlib.pyplot as plt`**
- `matplotlib` = 画图库（**mat**h + **plot** + **lib**rary，"画数学图的库"）
- `pyplot` = 它最常用的那一块（py + plot，"Python 画图"）
- `as plt` = 起个短名字 `plt`，社区里所有人都这么写

**`x = np.linspace(0, 10, 100)`**
- 从 0 到 10 之间**等距取 100 个点**（Day 21 学过）
- 画曲线要取很多点才平滑，100 个够用了

**`y = np.sin(x)`**
- `np.sin` = **sin**e，正弦
- 这里是**向量化**：一次算出 100 个点的正弦值（Day 23 学过）

**`plt.plot(x, y)`**
- plot = 画线。x 当横坐标，y 当纵坐标

**`plt.savefig("sin.png")`**
- save + fig = 保存 + 图 → "把图存起来"

**`plt.show()`**
- 弹出一个窗口显示图

> **顺序很重要**：`savefig` 必须在 `show` **之前**。`show` 之后画布会被清空，再存会是空图。

### 中文字体的坑（一定会踩）

Matplotlib 默认字体**不支持中文**，标题写成中文会显示成一串方框。开头加这两行就好：

```python
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 用微软雅黑（原写的 SimHei 缺负号，2026-10 修订）
plt.rcParams['axes.unicode_minus'] = False      # 让负号正常显示
```

- `rcParams` = **r**un **c**ommand **params**，"运行参数"，图的全局设置
- `font.sans-serif` = 无衬线字体（sans 是法语"没有"，sans-serif = 没有衬线的字体）
- 第二行是修一个小 bug：换字体后负号会变成方框，这句让负号正常显示

**产出**：`day28_plot.py` + 生成的 `sin.png`

---

## Day 29 · 散点图和柱状图

三种最基本的图：

```python
plt.plot(x, y)              # 折线图：适合"随时间变化"
plt.scatter(x, y)           # 散点图：适合"一堆测量点"
plt.bar(names, values)      # 柱状图：适合"几类东西比较"
```

| 名字 | 英文意思 | 什么时候用 |
|---|---|---|
| `plot` | 画（线） | 连续变化，比如温度随时间 |
| `scatter` | 散开、撒 | 离散的测量点，看有没有相关性 |
| `bar` | 柱子 | 几类东西比大小，比如各科平均分 |

**产出**：`day29_charts.py` —— 三种图各画一张，分别存成 PNG。

---

## Day 30 · 直方图：看分布

```python
scores = np.array([53, 87, 39, 98, 69, 75, 58, 40])
plt.hist(scores, bins=5)
```

- `hist` = **hist**ogram，直方图
- `bins` = 箱子、区间。"把数据分成几个区间来数"
- 它回答的问题不是"每个数是多少"，而是"**数据集中在哪个范围**"

**产出**：`day30_hist.py` —— 造 1000 个随机数（`np.random.randn`），画直方图，看看是不是"中间高两边低"。

---

## Day 31 · 把图讲清楚

一张合格的图必须有这些：

```python
plt.plot(x, y, label="正弦曲线")     # label：给这条线起名
plt.title("正弦函数")                # title：图的标题
plt.xlabel("x")                     # xlabel：横轴叫什么
plt.ylabel("sin(x)")                # ylabel：纵轴叫什么
plt.legend()                        # legend：显示图例（哪条线叫什么）
plt.grid(True)                      # grid：显示网格
plt.xlim(0, 10)                     # xlim：横轴范围
plt.ylim(-1.5, 1.5)                 # ylim：纵轴范围
```

**验收标准**：把图拿给别人看，他不用问你也能看懂——这是唯一的判断标准。

**产出**：`day31_labels.py`

---

## Day 32 · 多子图与样式

```python
fig, axes = plt.subplots(2, 2)      # 2 行 2 列，一共 4 张子图

axes[0, 0].plot(x, y1)
axes[0, 1].plot(x, y2)
axes[1, 0].plot(x, y3)
axes[1, 1].plot(x, y4)

plt.tight_layout()                  # 自动调整间距，别让标签挤在一起
plt.savefig("four.png")
```

- `subplots` = sub + plots，子图。`plt.subplots(2, 2)` 造一张 2×2 的画布
- `axes` = axis 的复数，"一堆坐标轴"。用 `axes[行, 列]` 选其中一格
- 这里会看到**点号可以连着用**：`axes[0, 0].plot(...)` 读作"第 0 行第 0 列那张子图的 plot"

**产出**：`day32_subplots.py`

---

## Day 33–34 · 项目：一组物理数据的完整可视化

**要做什么**：造一组"看起来像真实实验数据"的数据，画成一张 2×2 的图。

**内容**：

1. **左上**：一条带噪声的正弦曲线（`np.sin(x) + 噪声`），散点画
2. **右上**：同样数据的直方图，看噪声分布
3. **左下**：把散点按 x 分区间求平均（或者画一条拟合线）
4. **右下**：柱状图，比较几个"类别"的数值

**要求**：

- 每张子图都有标题、轴标签
- 最后存成 `物理数据可视化.png`
- 分清哪些是"原始数据"、哪些是"处理结果"，在图例里标出来

**产出**：`week05_plot.py` + `物理数据可视化.png`

---

## 提交方式

文件放进 `homework/week05/`，然后说：**「第 5 周提交」**。
