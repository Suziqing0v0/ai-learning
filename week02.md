# 第 2 周任务卡 · 函数进阶与文件读写

**本周目标**：把代码从"一坨"变成"有结构"，学会真正读写磁盘上的文件。
**每天投入**：1.5–2 小时。

**本周开始要守的两条规范**（第 1 周评审里指出的）：

1. **变量名要有含义**：用 `avg`、`hi`、`lo`，不用 `a`、`b`、`c`
2. **运算符两边留空格**：`avg = sum(scores) / len(scores)`

---

## Day 8 · 函数返回多个值

你已经会用 `return "优秀"` 交回一个值。今天学一次交回好几个：

```python
def get_stats(scores):
    avg = sum(scores) / len(scores)
    hi = max(scores)
    lo = min(scores)
    return avg, hi, lo

scores = [85, 92, 78, 90, 66, 88]
avg, hi, lo = get_stats(scores)     # 三个变量一次接住三个值
print(avg, hi, lo)
```

要点：
- `return avg, hi, lo` 用逗号隔开，一次交回三个
- 接的时候也要三个变量，用逗号隔开

**产出**：`day8_stats.py` —— 把 Day 3 那四个统计打包成 `get_stats(scores)`，返回平均分、最高分、最低分、排序后的列表，外面一次接住并打印。

---

## Day 9 · 写文件

```python
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
```

- `open()` 打开文件，`"w"` 表示**写入**（会清空原内容）
- `with ... as f` 是固定写法，用完自动关闭文件
- `f.write("文字")` 写入内容，`\n` 是换行符
- `encoding="utf-8"` 处理中文

**产出**：`day9_write.py` —— 新建 `result.txt`，写入三行内容（可以写你自己想写的），然后到文件夹里确认文件真的生成了。

---

## Day 10 · 读文件

```python
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

- `"r"` 表示**读取**
- `readlines()` 一次读出所有行，得到一个列表，每行末尾带 `\n`
- `.strip()` 去掉行末的换行符
- 字符串转数字用 `int()` 或 `float()`

**产出**：`day10_read.py` + `data.txt`

先自己造一个 `data.txt`，**每行一个分数**（8 行）。然后写程序读进来，算平均分、最高分、最低分。

---

## Day 11 · 读写结合 + 异常处理

```python
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        ...
except FileNotFoundError:
    print("文件不存在，检查一下路径")
```

**产出**：`day11_report.py`

读 `data.txt` 算统计，把结果写进 `report.txt`。文件不存在时给出友好提示，而不是崩溃。

---

## Day 12 · 列表推导式与常用技巧

```python
nums = [int(x) for x in lines]    # 列表推导式
for i, v in enumerate(nums):      # 同时拿到序号和值
    print(i, v)
sorted(scores, reverse=True)      # 从大到小排序
```

**产出**：`day12_tricks.py` —— 用这三种写法各做一个小练习。

---

## Day 13–14 · 项目：文件统计器

写 `week02_stats.py`：

- 读入 `data.txt`（每行一个数字）
- 算出**平均值、中位数、标准差、最大值、最小值、个数**
- 把结果整齐地写进 `result.txt`
- 文件不存在时友好提示
- **至少 4 个函数**，主逻辑不超过 15 行

两个新统计量的算法：

- **中位数**：排序后取中间那个；个数是偶数时，取中间两个的平均
- **标准差**：每个数与平均值的差，平方，求平均，再开方（用 `** 0.5`）

**产出**：`week02_stats.py`

---

## 验收标准

- [ ] Day 8–12 的程序都能跑通
- [ ] `week02_stats.py` 能读文件、算 6 个统计量、写结果文件
- [ ] 文件不存在时不崩溃，而是给出提示
- [ ] 代码里至少有 4 个函数
- [ ] 变量名有含义，运算符两边有空格

---

## 提交方式

文件放进 `homework/week02/`，然后说：**「第 2 周提交」**。
