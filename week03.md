# 第 3 周任务卡 · Git、模块与类

**本周目标**：学会给代码存版本、把作业传上 GitHub、把代码拆成多个文件，最后接触一下"类"。

**本周重点不是写更多 Python，而是学会"管理代码"。** 这是从"写练习"走向"做项目"的第一步。

---

## Day 15 · Git 第一次提交

### 为什么需要 Git

回想 Day 5 那次——你把报错粘贴进了 `day5_dict.py`，代码被覆盖了，只能靠我帮你还原。

**如果有 Git，两条命令就能退回去。** 这就是版本管理。

### 第一步 · 配置身份

Git 每次提交都会记录"谁提交的"。在终端里运行这两条（把内容换成你自己的）：

```
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

> 名字会出现在每次提交记录里，中英文都行。邮箱先用你现在有的（QQ 邮箱也行），以后注册 GitHub 了可以再改。

验证：

```
git config --global --list
```

### 第二步 · 建仓库

先切到你的学习目录，再初始化：

```
cd C:\Users\15503\Desktop\opencode\ai-learning
git init
```

看到 `Initialized empty Git repository` 就成了。这时目录里会多一个隐藏文件夹 `.git`，你的所有版本历史都存在里面。

### 第三步 · 第一次提交

```
git add .
git commit -m "完成第1周和第2周的全部练习"
```

- `git add .` 把当前所有改动"放进待提交区"
- `git commit -m "说明"` 把这一批改动**存成一个版本**，引号里是这次改了什么

### 第四步 · 查看记录

```
git log --oneline
```

应该看到你刚才那次提交，前面有一串字母数字（那是版本号）。

### 验收标准

- [ ] `git config --global --list` 能看到你的名字和邮箱
- [ ] `ai-learning` 里出现了 `.git` 文件夹
- [ ] `git log --oneline` 能看到至少一条提交记录
- [ ] 能用自己的话说清 `add` 和 `commit` 各干了什么

---

## Day 16 · 看历史与回到过去

**要学的**：改坏了怎么退回去——这是 Git 最大的用处。

```
git status              查看当前有哪些改动
git diff                看具体改了哪几行
git log --oneline       看提交历史
git restore 文件名       把某个文件恢复到上次提交的样子
```

**练习**：随便找一个作业文件，故意改坏几行，用 `git diff` 看改动，再用 `git restore` 恢复。

**产出**：在 `day16_git.md` 里写下你做的操作和每步看到的结果。

---

## Day 17 · GitHub：把作业传上去

1. 注册 GitHub 账号
2. 新建一个仓库（Repository），名字建议 `ai-learning`
3. 把本地仓库连上去并推送：

```
git remote add origin 你的仓库地址
git branch -M main
git push -u origin main
```

**为什么值得做**：这个仓库以后就是你的作品集。两年后你去找实习或联系导师，别人点开就能看到你写过什么。

**验收标准**

- [ ] 浏览器打开你的 GitHub 仓库，能看到 week01 和 week02 的文件
- [ ] 能在网页上看到你的提交记录

---

## Day 18 · 模块与 import

**要学的**：把函数拆到另一个文件里，然后 import 进来用。

```python
# 文件 mystats.py
def get_mean(nums):
    return sum(nums) / len(nums)

# 文件 main.py
import mystats

print(mystats.get_mean([1, 2, 3]))
```

**产出**：把 `week02_stats.py` 拆成两个文件——`mystats.py`（放四个统计函数）+ `week02_main.py`（放主逻辑）。

---

## Day 19–20 · 类（class）入门

**要学的**：`class` 是什么，为什么 PyTorch 里到处都是 `model.forward()` 这种写法。

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say(self):
        print(f"{self.name} 的分数是 {self.score}")
```

这一节先"看得懂、能照着写"，不要求自己设计类。**能读懂别人的类，比会写更重要**——以后看 numpy、torch 的代码全靠这个。

**产出**：`day19_class.py`，写一个 `Student` 类，建三个学生，把他们的分数打印出来。

---

## 提交方式

文件放进 `homework/week03/`，然后说：**「第 3 周提交」**。
