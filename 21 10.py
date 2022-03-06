import numpy as np
from scipy import sparse

a=[[1,1,2],[2,-1,2],[-1,2,-1]]

print('a=',a)

b=[9,6,0]
b=np.array(b)
b=b.transpose()

x=np.linalg.solve(a,b)
print('x=',x)

d=[2,2,2,2]
off_diag=[-1,-1,-1]
ds=[d,off_diag, off_diag]
a=sparse.diags(ds, [0,-1,1]).toarray()
b=[3,0,1,1]
print('a=',a)
y=np.linalg.solve(a, b)
print('y=',y)