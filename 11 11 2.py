import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

fig=plt.figure()
ax=plt.axis(projection='3d')

d=0.05

n=10
xmin=0.
xmax=10.

h=(xmax-xmin)/n

tmin=0.
tmax=10.

#граничные условия слева и справа на концах
t1=0
t2=0

dt=h**2/2./d/2.
r=d*dt/h**2

x=np.arrange(xmin, xmax+h, h)
t=np.arrange(tmin, tmax+dt)

n=len(x)
m=len(t)

u=np.zeros((n,m))
u=np.array(u)

#граничные условия
u[0,:]=t1
u[n-1,:]=t2
#что это за синтаксис такой ужос
#заданние начального уровня при т равно 0
u[0:n,0]=-5.*x*(x-xmax)

for i in range(1, n-1):
    for j in range(m-1):
        u[i,j+1]=r*u[i-1,j]+(1-2*r)*u[i, j]+r*u[i+1,j]
        
        
        
        
        