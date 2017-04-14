from __future__ import division
import math
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


for t in range(1,21):
    for n in range(1,1000):
        approx=math.exp(0.41)*(tpow(t,n+1)/fact(n+1))
        if approx<eps:
            print("t=",t," ","n=",n)
            break

