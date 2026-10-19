"""Reproduce all R1 calculations and independently validate the constrained optimum.
All values are synthetic; no firm data or estimated causal effects.
"""
from model import Task,solve,demand,b,bp
from dataclasses import replace
from pathlib import Path
from itertools import product
import csv,json,sys,platform
import numpy as np
import scipy
from scipy.optimize import minimize
OUT=Path(__file__).resolve().parents[1]/'results';OUT.mkdir(exist_ok=True)
def write(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def numerical(ts,B,k):
 # Independent primal optimization in residual-error coordinates, not a root or KKT solver.
 if B==0:return sum(t.n*(t.c+t.L*t.p) for t in ts)
 pp=np.array([t.p for t in ts]);nn=np.array([t.n for t in ts]);LL=np.array([t.L for t in ts])
 def load(v):return np.array([b(t,t.p)-b(t,x) for t,x in zip(ts,v)])
 def jacload(v):return np.array([bp(t,x) for t,x in zip(ts,v)])
 scale=max(1.,sum(nn*LL*pp))
 def fun(v):return (sum(nn*(k*load(v)+LL*v))+sum(t.n*t.c for t in ts))/scale
 def jac(v):return nn*(-k*jacload(v)+LL)/scale
 cons={'type':'ineq','fun':lambda v:B-sum(nn*load(v)),
       'jac':lambda v:nn*jacload(v)}
 candidates=[]
 for fraction in (1.,.8,.5):
  res=minimize(fun,pp*fraction,jac=jac,bounds=[(1e-12,p) for p in pp],
   constraints=cons,method='SLSQP',options={'ftol':2e-13,'maxiter':1500})
  if res.success and cons['fun'](res.x)>=-1e-7:candidates.append(res.fun*scale)
 if not candidates:raise AssertionError('Independent optimizer failed')
 return min(candidates)
# Main finite choice: reusable class 1 source, optional AI in class 2.
B=7.;k=1.;h=.1;F=10.;S=14.;cells=[];solutions={}
for a,d in product((0,1),repeat=2):
 ts=[Task(.1 if d else .5,1,100,.5,n=2,c=20),
     Task(.3 if a else .2,.25 if a else 1,100,.5,c=20-S*a)]
 z=solve(ts,B-h*d,k);ind=numerical(ts,B-h*d,k)
 assert abs(z['cost']-ind)<1e-6
 solutions[a,d]=z
 cells.append(dict(A_workflow=a,D=d,cost=z['cost']+F*d,net_value=-z['cost']-F*d,
   eta=z['eta'],load=z['load'],reference_reserve=h*d,
   residual1=z['v'][0],residual2=z['v'][1],load1=2*z['z'][0],load2=z['z'][1],
   own_cost1=z['class_cost'][0],cost2=z['class_cost'][1],independent_cost=ind+F*d))
write('workflow_cells.csv',cells)
access=[]
for A,d in product((0,1),repeat=2):
 opts=[r for r in cells if r['D']==d and (A or not r['A_workflow'])]
 best=min(opts,key=lambda r:r['cost'])
 access.append(dict(A_access=A,D=d,adopted_AI=best['A_workflow'],cost=best['cost'],Y=-best['cost']))
write('access_cells.csv',access)
# Global optimum over every binary choice is distinct from conditional allocation.
best=min(cells,key=lambda r:r['cost']);assert (best['A_workflow'],best['D'])==(1,1)
# Capacity-regime counterexamples and zero effect at slack capacity.
regimes=[]
for B0 in (0.,.1,1.,2.,3.,4.,5.,6.,7.,8.,10.,20.,100.):
 vals={}
 for a,d in product((0,1),repeat=2):
  ts=[Task(.1 if d else .5,1,100,.5,n=2),Task(.3 if a else .2,.25 if a else 1,100,.5)]
  vals[a,d]=solve(ts,B0)
 H0=vals[1,0]['cost']-vals[0,0]['cost'];H1=vals[1,1]['cost']-vals[0,1]['cost']
 regimes.append(dict(B=B0,H_weak=H0,H_repaired=H1,committed_interaction=H0-H1,
  eta_manual_weak=vals[0,0]['eta'],eta_AI_weak=vals[1,0]['eta']))
write('capacity_regimes.csv',regimes)
accuracy=[]
for bb in (4.,6.,8.,10.,20.):
 zz={(aa,dd):solve([Task(.1 if dd else .5,1,100,.5,n=2),
      Task(.15 if aa else .2,.25 if aa else 1,100,.5)],bb) for aa,dd in product((0,1),repeat=2)}
 hh=[zz[1,dd]['cost']-zz[0,dd]['cost'] for dd in (0,1)]
 accuracy.append(dict(B=bb,AI_raw_error=.15,manual_raw_error=.2,interaction=hh[0]-hh[1]))
assert any(r['interaction']>0 for r in accuracy)
write('accuracy_improvement.csv',accuracy)
# Reuse, source repair and easier drafting; finite-scale global enumeration.
reuse=[]
for n in range(1,13):
 v0=solve([Task(.5,1,100,.5,n=n),Task(.2,1,100,.5)],7)
 v1=solve([Task(.1,1,100,.5,n=n),Task(.2,1,100,.5)],7)
 reuse.append(dict(reuse_count=n,source_value=v0['cost']-v1['cost']))
assert all(reuse[i+1]['source_value']>=reuse[i]['source_value'] for i in range(len(reuse)-1))
write('reuse.csv',reuse)
scale=[]
for c in (34.,28.,24.,22.,20.,15.,10.,5.,0.):
 opts=[]
 for n,d in product(range(0,13),(0,1)):
  ts=([Task(.1 if d else .5,1,100,.5,n=n)] if n else [])+[Task(.2,1,100,.5)]
  z=solve(ts,7.)
  value=35*n-1.5*n*n-c*n-z['cost']-10*d
  opts.append((value,n,d))
 val,n,d=max(opts);scale.append(dict(drafting_cost=c,optimal_scale=n,source_repair=d,value=val))
write('endogenous_scale.csv',scale)
# Own task and recipient effects, evaluated along fixed-A policies.
spill=[]
for a in (0,1):
 x,y=solutions[a,0],solutions[a,1]
 spill.append(dict(A_workflow=a,own_class1_saving=x['class_cost'][0]-y['class_cost'][0],
  recipient_class2_saving=x['class_cost'][1]-y['class_cost'][1],
  total_before_F=x['cost']-y['cost']))
write('spillovers.csv',spill)
# Fixed quotas: a deliberately different decentralized institution.
base=solutions[0,0];quotas=[2*base['z'][0],base['z'][1]]
local0=solve([Task(.5,1,100,.5,n=2,c=20)],quotas[0])
local1=solve([Task(.1,1,100,.5,n=2,c=20)],max(0,quotas[0]-h))
write('fixed_quota.csv',[dict(class1_quota=quotas[0],local_source_benefit=local0['cost']-local1['cost'],F=F,
                           local_repair=int(local0['cost']-local1['cost']>F))])
# Analytic allocation-share reversal, distinct from the all-in investment example.
account=[]
for aa in (0,1):
 vv=[]
 for pp in (.5,.3):
  tt=[Task(pp,1,100,0,n=2),Task(.3 if aa else .2,.25 if aa else 1,100,0)]
  zz=solve(tt,7);assert abs(zz['cost']-numerical(tt,7,1))<1e-6
  vv.append(zz)
 account.append(dict(A_workflow=aa,own_source_benefit=vv[0]['class_cost'][0]-vv[1]['class_cost'][0],
                     system_source_benefit=vv[0]['cost']-vv[1]['cost'],eta_low=vv[1]['eta']))
assert account[1]['own_source_benefit']<account[0]['own_source_benefit']
assert account[1]['system_source_benefit']>account[0]['system_source_benefit']
assert 1<account[1]['eta_low']/account[0]['eta_low']<2
write('account_reversal.csv',account)
# Independent constrained optimization across all finite options for heterogeneous tasks.
rng=np.random.default_rng(5102026);maxerr=0.;count=0;binding=0;slack=0;corners=0
for draw in range(40):
 J=2+(draw%2);kk=float(rng.uniform(.5,2));B0=float(rng.uniform(.3,9))
 base=[Task(float(rng.uniform(.02,.7)),float(rng.uniform(.3,2)),float(rng.uniform(20,150)),
            float(rng.uniform(0,1)),float(rng.integers(1,4)),float(rng.uniform(5,20)),
            'power' if draw%3==0 else 'log') for _ in range(J)]
 for options in product((0,1),repeat=J+1):
  a=options[:-1];d=options[-1]
  ts=[replace(t,p=t.p*(.55 if d and i==0 else 1)*(.8 if a[i] else 1),
       lam=t.lam*(.6 if a[i] else 1),c=t.c-2*a[i]) for i,t in enumerate(base)]
  bb=max(.01,B0-.05*d)
  z=solve(ts,bb,kk);vnum=numerical(ts,bb,kk)
  err=abs(z['cost']-vnum);maxerr=max(maxerr,err);count+=1
  assert err<2e-5,(draw,options,err)
  assert z['load']<=bb+1e-8
  binding+=z['eta']>1e-8;slack+=z['eta']<=1e-8
  for t,v,e,load in zip(ts,z['v'],z['e'],z['z']):
   marginal=t.L/bp(t,v)
   if e>1e-8:assert abs(marginal-z['w'])<1e-8
   else:assert marginal<=z['w']+1e-8;corners+=1
# Explicit zero-error, zero-capacity, all-zero-effort and slack tests.
assert solve([Task(0,1,100),Task(.2,1,100)],0)['load']==0
assert solve([Task(.001,1,1)],1)['e']==[0.]
assert solve([Task(.2,1,100)],100)['eta']==0
# False-alarm boundary: checking raises residual error for sufficiently reliable drafts.
from math import exp
pbad=.01;alpha=.05
r0=pbad
r1=alpha*(1-pbad)+(pbad-alpha*(1-pbad))*exp(-1.)
assert pbad<alpha/(1+alpha) and r1>r0
# Full source repair is a valid finite option, without using log(0).
full=solve([Task(0,1,100,.5,n=2),Task(.2,1,100,.5)],7)
assert full['v'][0]==0 and full['z'][0]==0
# Envelope shadow price and own/recipient derivative checks at binding interior.
ts=[Task(.5,1,100,.5,n=2),Task(.2,1,100,.5)]
z=solve(ts,7);eps=1e-5
fd=(solve(ts,7+eps)['cost']-solve(ts,7-eps)['cost'])/(2*eps)
assert abs(fd+z['eta'])<1e-6
pp=(solve([replace(ts[0],p=.5+eps),ts[1]],7)['cost']-solve([replace(ts[0],p=.5-eps),ts[1]],7)['cost'])/(2*eps)
assert abs(pp-2*z['w']*bp(ts[0],.5))<1e-6
# Sufficient demand order checked at upper endpoint; proof establishes whole interval.
wbar=4.8
m=Task(.2,1,100,.5);a=Task(.3,.25,100,.5)
assert demand(a,wbar)[2]>demand(m,wbar)[2]
assert sum(t.n*demand(t,wbar)[2] for t in [Task(.5,1,100,.5,n=2),a])<7
assert sum(t.n*demand(t,1)[2] for t in [Task(.1,1,100,.5,n=2),m])>7
summary=dict(synthetic_only=True,seed=5102026,independent_constrained_comparisons=count,
 max_cost_discrepancy=maxerr,binding_cases=int(binding),slack_cases=int(slack),
 zero_effort_class_cases=int(corners),global_policy=[best['A_workflow'],best['D']],
 own_recipient_and_shadow_derivatives='PASS',finite_choice_checks='PASS',
 python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__)
(OUT/'validation.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2));print('ACCESS CELLS',access);print('SCALE',scale)
