from __future__ import division

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

print("values according to other researchers")

for t in range(1,11):
    approx=1
    for n in range(1,1000):
        if (n+2-t)>0:
            approx=(tpow(t,n+1)*(n+2))/(fact(n+1)*(n+2-t))
        if approx<eps:
            print("t=",t," ","n=",n)
            break
