# 报错记录

---

## 错误 1 · NameError

**代码：**

```python
print(abc)
```

**报错：**

```
Traceback (most recent call last):
  File "xxx.py", line 1, in <module>
    print(abc)
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
```

**原因：** abc 这个变量没有定义过，Python 不认识这个名字。

**改法：** 先定义它，比如 `abc = 1`，再 print。

---

## 错误 2 · IndexError


IndexError: list index out of range


原因：这是列表的索引，没有第五号
改法：可以把5换成2

## 错误 3 · KeyError

原因：没有小王对应的量
改法：换成字典里有的人名
