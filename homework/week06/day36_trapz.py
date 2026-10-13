import numpy as np

def f(x):
    return x**2

a,b=0,1
exact=1/3
for n in [10,100,1000]:
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    y=f(x)
    area=np.sum(y[:-1]*h)
    print(f"矩形法 n={n} 计算值={area:.6f} 误差={area-exact:.2e}")

    y=f(x).copy()
    y[0]=y[0]/2
    y[n]=y[n]/2
    area=np.sum(y*h)
    print(f"梯形法 n={n} 计算值={area:.6f} 误差={area-exact:.2e}")