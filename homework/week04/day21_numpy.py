import numpy as np
scores=np.array([85,92,78,90,66,88,95,73])

print(scores.shape)
print(scores.dtype)
print(scores.size)

a=scores*2
b=scores+10
c=scores/2
print(a)
print(b)
print(c)

d=np.arange(0,10,2)
e=np.linspace(0,1,5)
print(d)
print(e)