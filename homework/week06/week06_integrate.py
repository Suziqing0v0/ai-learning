import os 
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False

folder = os.path.dirname(os.path.abspath(__file__))

def f(x):
    return np.exp(-x ** 2)

exact=0.7468241328

n_list=[10, 20, 40, 80, 160, 320, 640]
err_rect=[]
err_trap=[]
err_simp=[]

def rect(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    y=f(x)
    area=np.sum(y[:-1]*h)
    return area

def trap(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    y=f(x)
    y[0]=y[0]/2
    y[n]=y[n]/2
    area=np.sum(y*h)
    return area

def simp(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    y=f(x)
    coef=np.ones(n+1)
    coef[1:-1:2]=4
    coef[2:-1:2]=2
    area=np.sum(coef*y)*h/3
    return area

for n in n_list:
    area_rect=rect(f,0,1,n)
    err_rect.append(abs(area_rect-exact))

    area_trap=trap(f,0,1,n)
    err_trap.append(abs(area_trap-exact))

    area_simp=simp(f,0,1,n)
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

plt.savefig(os.path.join(folder,"week06_error.png"))

for i in range(len(n_list)-1):
    ratio=err_rect[i]/err_rect[i+1]
    print(n_list[i],"→",n_list[i+1],ratio)

for i in range(len(n_list)-1):
    ratio=err_trap[i]/err_trap[i+1]
    print(n_list[i],"→",n_list[i+1],ratio)

for i in range(len(n_list)-1):
    ratio=err_simp[i]/err_simp[i+1]
    print(n_list[i],"→",n_list[i+1],ratio)