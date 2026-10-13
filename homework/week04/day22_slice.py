import numpy as np
scores=np.array([85, 92, 78, 90, 66, 88, 95, 73])
print(scores[0])
print(scores[-1])
print(scores[:3])
print(scores[2:5])
print(scores[::2])
print(scores[::-1])
scores[1:5]=0
print(scores)
