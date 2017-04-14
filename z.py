from __future__ import division
import math
import numpy as np
eps=0.025

def tpow(t,n):
    pro=1
    for i in range(0,n):
        pro=pro*t

    return pro

def fact(n):
    f=1
    for i in range(2,n+1):
        f=f*i

    return f

print("values according to my research")

tn=[4,7,9,12,15,17,20,23,25,28,31,34,36,39,42,44,47,50,52,55]

for z in np.arange(0,2,0.01):
    ln=[]
    for t in range(1,21):
        for n in range(1,1000):
            approx=math.exp(z)*(tpow(t,n+1)/fact(n+1))
            if approx<eps:
                ln.append(n)
                break
    if ln==tn:
        print(z)
        break

