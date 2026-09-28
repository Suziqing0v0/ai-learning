scores=[85,92,58,90,66,45,95,73]
fail=0
for s in scores:
    if s >=90:
        print(s,"优秀")
    elif s >=80:
        print(s,"良好")
    elif s >=70:
        print(s,"中等")
    elif s >=60:
        print(s,"合格")
    else:
        print(s,"不及格")
        fail=fail+1
a=len(scores)
print("总人数：",a)
print("不及格人数：",fail)