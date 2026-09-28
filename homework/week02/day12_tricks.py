import os
folder=os.path.dirname(os.path.abspath(__file__))
data_path=os.path.join(folder,"data.txt")

with open(data_path,"r",encoding="utf-8") as f:
    a=f.readlines()

n=[int(i) for i in a]
for b,c in enumerate(n):
    print(b,c)
print(sorted(n,reverse=True))
