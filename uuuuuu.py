import numpy as np
import matplotlib.pyplot as plt

def normaldistr(x, mu, sigma):
    y=1/sigma/np.sqrt(2*np.pi)*np.exp(-((x-mu)/sigma)**2/2)
    
    return y

def derivative(x, mu, sigma):
    
    y=normaldistr(x, mu, sigma)/sigma**2*(mu-x)
    return y

def secondder(x, mu, sigma):
    
    y=1/sigma**2*(derivative(x, mu, sigma)*(mu-x)-normaldistr(x, mu, sigma))
    return y

mu=0
sigma=1.3
xmin=-5
xmax=5
n=100
step=(xmax-xmin)/(n-1)
x=[0]*n
for i in range(n):
    x[i]=xmin+i*step

x=np.array(x)


f=normaldistr(x, mu, sigma)
plt.plot(x,f, color='darkblue', linestyle='dashdot')

f=derivative(x, mu, sigma)
plt.plot(x,f, color='mediumvioletred', linestyle='--')

f=secondder(x, mu, sigma)
plt.plot(x,f, color='red')