# Day 16 · Git 操作记录

## 我做了什么
1. 把 day2_bmi.py 里的 round(bmi, 1) 改成 round(bmi,)
2. git status → day2_bmi.py 显示成红色，标着 M
3. git diff → 看到改动，红色是删掉的、绿色是新加的
4. git restore homework/week01/day2_bmi.py
5. 打开文件，改坏的地方恢复回来了

## 四个命令分别干什么
- git status：查看有哪些改动
- git diff：查看具体改动哪几行
- git log：查看提交历史
- git restore：恢复成修改前的样子

## 一句话总结
如果以后代码改错了需要返回可以用这些代码找到原来的版本