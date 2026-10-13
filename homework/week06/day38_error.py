import os 
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False

folder = os.path.dirname(os.path.abspath(__file__))

def f(x):
    return np.exp(-x**2)

a,b=0,1
exact=0.7468241328

n_list=[10, 20, 40, 80, 160, 320, 640]
err_rect=[]
err_trap=[]
err_simp=[]

for n in n_list:
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    y=f(x)
    area_rect=np.sum(y[:-1]*h)
    err_rect.append(abs(area_rect-exact))

    y=f(x).copy()
    y[0]=y[0]/2
    y[n]=y[n]/2
    area_trap=np.sum(y*h)
    err_trap.append(abs(area_trap-exact))

    y=f(x).copy()
    coef=np.ones(n+1)
    coef[1:-1:2]=4
    coef[2:-1:2]=2
    area_simp=np.sum(coef*y)*h/3
    err_simp.append(abs(area_simp-exact))
    
plt.figure()

plt.loglog(n_list,err_rect,"o-",label="矩形法")
plt.loglog(n_list,err_trap,"o-",label="梯形法")
plt.loglog(n_list,err_simp,"o-",label="辛普森法")
plt.title("误差随步长变化（对数图）")
plt.xlabel("n")
plt.ylabel("error")
plt.legend()
plt.grid(True,which="both")

plt.savefig(os.path.join(folder,"error_plot.png"))