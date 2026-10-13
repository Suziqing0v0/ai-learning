import numpy as np
scores=np.array([53, 87, 39, 98, 69, 75, 58, 40])
mask=scores >=60
print(mask)
print((scores>=60).sum())
print((scores<60).sum())
print((scores>=60).mean())
print(scores[scores>=60])
print(scores[scores<60])
print(scores[scores>=90])
