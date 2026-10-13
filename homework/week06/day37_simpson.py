import numpy as np
a,b=0,1
exact=1/3

def f(x):
    return x**2

for n in [10,100,1000]:
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    y=f(x)
    
    coef=np.ones(n+1)
    coef[1:-1:2]=4
    coef[2:-1:2]=2
    area=np.sum(coef*y)*h/3
    print(f"辛普森法 n={n} 计算值={area:.6f} 误差={area-exact:.2e}")
