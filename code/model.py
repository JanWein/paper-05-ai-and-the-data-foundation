"""Independent-reference verification allocation. Synthetic primitives only."""
from dataclasses import dataclass,replace
from math import log
from scipy.optimize import brentq
import numpy as np
@dataclass(frozen=True)
class Task:
    p:float; lam:float; L:float; tau:float=0.; n:float=1.; c:float=0.; kind:str="log"
def b(t,v):
    return (log(v)/t.lam if t.kind=='log' else 2*np.sqrt(v)/t.lam)+t.tau*v
def bp(t,v):
    return (1/(t.lam*v) if t.kind=='log' else 1/(t.lam*np.sqrt(v)))+t.tau
def demand(t,w):
    if t.p==0: return 0.,0.,0.
    m=t.L/bp(t,t.p)
    if w>=m: return t.p,0.,0.
    v=w/(t.lam*(t.L-t.tau*w))
    if t.kind=='power':v=v*v
    e=(log(t.p/v) if t.kind=='log' else 2*(np.sqrt(t.p)-np.sqrt(v)))/t.lam
    z=e+t.tau*(t.p-v)
    return v,e,z
def solve(tasks,B,k=1.):
    assert B>=0 and k>0
    for t in tasks: assert 0<=t.p<=1 and t.lam>0 and t.L>0 and t.tau>=0 and t.n>0
    def Q(w):return sum(t.n*demand(t,w)[2] for t in tasks)
    if B==0:
        w=max([k]+[(t.L/bp(t,t.p) if t.p>0 else 0) for t in tasks])
    elif Q(k)<=B: w=k
    else:
        high=max((t.L/bp(t,t.p) if t.p>0 else 0) for t in tasks)
        w=brentq(lambda w:Q(w)-B,k,high,xtol=1e-13)
    out=[demand(t,w) for t in tasks]
    costs=[t.n*(t.c+k*z+t.L*v) for t,(v,e,z) in zip(tasks,out)]
    return dict(cost=sum(costs),w=w,eta=w-k,load=sum(t.n*q[2] for t,q in zip(tasks,out)),
                v=[q[0] for q in out],e=[q[1] for q in out],z=[q[2] for q in out],class_cost=costs)
if __name__=='__main__':
 for B in (2,3,4,5,6):
  vals={}
  for a in (0,1):
   for d in (0,1):
    ts=[Task(.1 if d else .5,1,100,.5),Task(.3 if a else .2,.25 if a else 1,100,.5)]
    vals[a,d]=solve(ts,B)
  H=[vals[1,d]['cost']-vals[0,d]['cost'] for d in (0,1)]
  benefits=[vals[a,0]['cost']-vals[a,1]['cost'] for a in (0,1)]
  print(B,'H',H,'repair',benefits,'w',[round(vals[a,d]['w'],3) for a,d in ((0,0),(1,0),(0,1),(1,1))])
