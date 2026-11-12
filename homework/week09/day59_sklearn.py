import os
import numpy as np
from sklearn.linear_model import LinearRegression

folder = os.path.dirname(os.path.abspath(__file__))
data = np.loadtxt(os.path.join(folder, "data.txt"), delimiter=",")

x = data[:,0]
y = data[:,1]
x2 = x.reshape(-1,1)
model = LinearRegression()
model.fit(x2,y)

print(model.coef_)
print(model.intercept_)