import os                                                  

folder = os.path.dirname(os.path.abspath(__file__))        
path = os.path.join(folder, "data.txt")                   

with open(path,"r",encoding="utf-8") as f:
    a=f.readlines()
n=[]
for i in a:
    n.append(int(i))
b=sum(n)/len(n)
c=max(n)
d=min(n)
print(b,c,d)
