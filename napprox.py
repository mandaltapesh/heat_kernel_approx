from __future__ import division
import igraph as ig
import numpy as np


g =ig.Graph()

g=g.Read_GML("football.gml")

def degree_matrix(A):
    D=[]
    for le in A:
        l=len(le)
    for r in range(0, l):
        s=0
        for c in range(0, l):
            s=s+A[r][c]
        d=[]
        for i in range(0,l):
            if i==r:
                d.append(s)
            else:
                d.append(0)
        D.append(d)

    return D

def identity_matrix(A):
    D=[]
    for le in A:
        l=len(le)
    for r in range(0, l):
        d=[]
        for c in range(0, l):
            if r==c:
                d.append(1)
            else:
                d.append(0)
        D.append(d)

    return D

def d_inverse(DI):
    for le in DI:
        l=len(le)
    for r in DI:
        for c in range(0,l):
            if r[c]!=0:
                r[c]=1/r[c]

    return DI

def typical_mat(A):
    Ad=[]
    for le in A:
        l=len(le)
    for i in range(0,l):
        r=[]
        for j in range(0,l):
            r.append(A[i][j])
        Ad.append(r)

    return Ad

def Ppower(P,n):
    pro=P
    for i in range(1,n):
        pro=(np.dot(pro,P))

    return pro

def Tpower(t,n):
    pro=t
    for i in range(1,n):
        pro=pro*t

    return pro

def nfact(n):
    pro=1
    for i in range(1,n+1):
        pro=pro*i

    return pro

def TNZ(n,I,P,t):
    s=I
    if n==0:
        return I
    else:
        for i in range(1,n+1):
            pros=Tpower(1,i)*(1/nfact(i))
            pro=np.dot(Ppower(P,i),pros)
            s=np.array(s)+np.array(pro)

    return s

def chebyshev(A):
    for le in A:
        l=len(le)
    v=[]
    for i in range(0,l):
        s=0
        for j in range(0,l):
           s=s+A[i][j] 
        v.append(s)

    return max(v)
        
A=typical_mat(g.get_adjacency())
D=degree_matrix(A)
DI=d_inverse(D)
I=identity_matrix(A)
P=typical_mat(np.dot(DI,A))

eps=0.05

print("values according to my method")
for t in range(1,11):
    for n in range(1,1000):
        pn=Ppower(P,n+1)
        tn=Tpower(t,n+1)
        approx=typical_mat(np.dot(pn,tn/nfact(n+1)))
        approxf=chebyshev(approx)
        if approxf<=eps/2:
            print("t=",t,"n=",n)
            break
        
        
