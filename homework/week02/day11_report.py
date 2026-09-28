import os                                                  

folder = os.path.dirname(os.path.abspath(__file__)) 
data_path=os.path.join(folder,"data.txt")       
report_path=os.path.join(folder,"report.txt")                 

try:
    with open(data_path,"r",encoding="utf-8") as f:
        a=f.readlines()
    n=[]
    for i in a:
        n.append(int(i))
    b=sum(n)/len(n)
    c=max(n)
    d=min(n)
    print(b,c,d)



    with open(report_path,"w",encoding="utf-8") as f:
        f.write(f"平均分:{b}\n")
        f.write(f"最高分:{c}\n")
        f.write(f"最低分:{d}\n")
    print("报告已生成")

except FileNotFoundError:
    print("文件不存在，检查一下路径")