scores = [85, 92, 58, 90, 66, 45, 95, 73]
b=0
for i in scores:
    if i >=90:
        print(i,"优秀")
    elif i >=80:
            print(i,"良好")
    elif i >=70:
            print(i,"中等")
    elif i >=60:
            print(i,"及格")
    else :
            print(i,"不及格")
            b=b+1
a=len(scores)
print("总人数",a)
print("不及格人数",b)
