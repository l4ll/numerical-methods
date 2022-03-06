import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

n=40
xmin=0.
xmax=1.
h=(xmax-xmin)/n

x=np.linspace(xmin, xmax, n)

diag0=[0]*n
b=[0]*n

#for i in range(n):
#    b[i]=1200.*h**2*x[i]**2*10


#граничные условия
q1=-10
t2=10

b[0]=h*q1
b[n-1]=t2

diag0=[2]*(n)
diag0[0]=-1
diag0[n-1]=1

diag1=[-1]*(n-1)
diag1[0]=1


diag2=[-1]*(n-1)
diag2[n-2]=0

    
ds=[diag0,diag2,diag1]
a=sparse.diags(ds, [0,-1,1]).toarray()
print('a=',a)
y=np.linalg.solve(a,b)
print('y=',y)

fig=plt.plot(x, y)

plt.show()