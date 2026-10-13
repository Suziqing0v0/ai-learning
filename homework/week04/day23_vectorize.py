import numpy as np
a=np.array([1, 2, 3, 4])
b=np.array([10, 20, 30, 40])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**2)
print(np.sqrt(a))


import time
start=time.time()
c=list(range(1000000))
for i in range(len(c)):
    c[i]=c[i]**2
print(c[:5])
end=time.time()
print("花了",end - start,"秒")


start=time.time()
d=np.arange(1000000)
print(d**2)
end=time.time()
print("花了",end - start,"秒")
