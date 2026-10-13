import numpy as np
scores=np.array([53, 87, 39, 98, 69, 75, 58, 40])
print(scores.mean())
print(scores.max())
print(scores.min())
print(scores.sum())
print(scores.std())
print(np.median(scores))

m=np.array([[1,2,3],
            [4,5,6]])
print(m.sum())
print(m.sum(axis=0))
print(m.sum(axis=1))
print(m.sum().shape)
print(m.sum(axis=0).shape)
print(m.sum(axis=1).shape)

grade=np.array([[85,92,78,90],
                [66,88,95,73],
                [70,65,80,85]])
print(grade.sum(axis=1))
print(grade.mean(axis=0))