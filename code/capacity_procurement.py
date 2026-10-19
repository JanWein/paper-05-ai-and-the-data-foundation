"""R6 synthetic exact checks. Standalone: no imports of author model modules.
Enumerates raw source histories and convex recipient action allocations; no grids
or stochastic search. Fractions throughout. Run from any working directory.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[1]/'results'
count={'parameter_groups':0,'raw_source_columns':0,'recipient_allocations':0,'stock_tie_points':0,'fee_boundary_checks':0}
def enc(v):
    if isinstance(v,Q): return str(v)
    if isinstance(v,dict): return {str(k):enc(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [enc(x) for x in v]
    return v

def actions(a,j):return [(Q(0),Q(4)),(Q(1),Q(1))]+([(Q(0),7-a),(Q(2),1-a)] if j else [])
def raw_rec(x,a,j):
    """Vertices of the one-constraint allocation simplex, not closed-form hull."""
    pts=actions(a,j);cand=[]
    for i,(t,c) in enumerate(pts):
        if t<=x:cand.append((c,[(i,Q(1))]))
    for (i,(t,c)),(ii,(tt,cc)) in combinations(enumerate(pts),2):
        if t!=tt and min(t,tt)<=x<=max(t,tt):
            w=(x-tt)/(t-tt)
            cand.append((w*c+(1-w)*cc,[(i,w),(ii,1-w)]))
    count['recipient_allocations']+=1
    return min(cand,key=lambda z:z[0])
def g(x,a,j):return 4-3*min(x,1)-(a*min(max(x-1,0),1) if j else 0)
def source_menu(q,y):
    """Every source plan: no check, check second, first then N/P/C on fault,
    and omit/redundantly check on clean. (prob, service, residual source loss).
    No hidden-Z contingency is admitted before the first check.
    """
    z=[('N',[(1-q,Q(0),Q(0)),(q,Q(0),Q(20))]),
       ('C2',[(1-q,Q(1),Q(0)),(q,Q(1),Q(10))])]
    for clean,fault in product((0,1),('N','P','C')):
        t=Q(1)+(y if fault=='P' else Q(1) if fault=='C' else 0)
        z.append((f'C1_clean{clean}_fault{fault}',[(1-q,Q(1+clean),Q(0)),(q,t,Q(10) if fault=='N' else Q(0))]))
    return z

def hard_raw(hist,a,j,rho):
    d=max(t for p,t,l in hist if p);breaks=sorted({d}|{t+x for p,t,l in hist for x,c in actions(a,j) if t+x>=d})
    vals=[];witnesses={}
    for b in breaks:
        vv=10+rho*b;ww=[]
        for p,t,l in hist:
            cost,alloc=raw_rec(b-t,a,j);vv+=p*(t+l+cost)
            load=t+sum(w*actions(a,j)[i][0] for i,w in alloc)
            assert load<=b
            ww.append({'prob':p,'source_service':t,'source_loss':l,'allocation':alloc,'load':load})
        vals.append((vv,b));witnesses[b]=ww
    best=min(v for v,b in vals);mins=[b for v,b in vals if v==best]
    lo,hi=min(mins),max(mins)
    # Last segment has slope rho: zero price is an unbounded optimal ray.
    assert rho>=0
    return best,lo,None if rho==0 else hi,witnesses[lo],breaks

def expected_raw(hist,a,j,rho):
    # Pure occupation columns per observed history suffice for this linear root objective.
    vals=[]
    for choices in product(actions(a,j),repeat=len(hist)):
        load=sum(p*(t+x) for (p,t,l),(x,c) in zip(hist,choices))
        val=10+sum(p*(t+l+c) for (p,t,l),(x,c) in zip(hist,choices))+rho*load
        vals.append((val,load))
    v=min(v for v,b in vals);bs=[b for vv,b in vals if vv==v]
    return v,min(bs),None if rho==0 else max(bs)

def expected_x(a,j,r):
    pts=actions(a,j);v=min(c+r*t for t,c in pts);xs=[t for t,c in pts if c+r*t==v]
    return v,min(xs),None if r==0 else max(xs)
def stock_formula(a,j,r,q,y):
    d=1+y
    if not j or a==0:
        return (2+y,None) if r==0 else (2+y,2+y) if r<3*q else (2,2+y) if r==3*q else (2,2) if r<3 else (d,Q(2))
    if a==3:
        return (3+y,None) if r==0 else (3+y,3+y) if r<3*q else (3,3+y) if r==3*q else (3,3) if r<3 else (d,Q(3))
    H=a+q*(3-a)
    if r==0:return 3+y,None
    if r<q*a:return 3+y,3+y
    if r==q*a:return Q(3),3+y
    if r<a:return Q(3),Q(3)
    if r==a:return 2+y,Q(3)
    if r<H:return 2+y,2+y
    if r==H:return Q(2),2+y
    if r<3:return Q(2),Q(2)
    return d,Q(2)
def premium(a,j,r,q,y):
    if not j:return y*min((1-q)*r,q*(3-r))
    return y*min((1-q)*r,q*(a-r)) if r<=a else y*min((1-q)*(r-a),q*(3-r))

def run_group(a,r,q,y,export=False):
    count['parameter_groups']+=1;ell=1+q*y;h=Q(1,10);data={}
    assert y*(q+r)<10*q and ell+r*(1+y)<20*q
    for j in (0,1):
        menu=source_menu(q,y);raw=[];exp=[]
        for name,hist in menu:
            v,lo,hi,w,bs=hard_raw(hist,a,j,r);count['raw_source_columns']+=1
            raw.append((v,name,lo,hi,w))
            exp.append((expected_raw(hist,a,j,r)[0],name))
        cp=next(z for z in raw if z[1]=='C1_clean0_faultP')
        M,xlo,xhi=expected_x(a,j,r)
        assert M==1+r+(min(0,r-a) if j else 0)
        e=10+ell+r*ell+M;repair=10+r*h+M;P=premium(a,j,r,q,y)
        assert min(v for v,*_ in raw)==cp[0]==e+P
        assert min(v for v,n in exp)==e
        assert (cp[2],cp[3])==stock_formula(a,j,r,q,y)
        ex=next(expected_raw(hist,a,j,r) for n,hist in menu if n=='C1_clean0_faultP')
        assert ex==(e,ell+xlo,None if xhi is None else ell+xhi)
        # Check endpoints, midpoints of flat stock intervals and a point on zero-price rays.
        lo,hi=cp[2:4]
        for b in {lo,lo+1 if hi is None else hi,lo+Q(1,2) if hi is None else (lo+hi)/2}:
            val=10+ell+r*b+(1-q)*raw_rec(b-1,a,j)[0]+q*raw_rec(b-1-y,a,j)[0]
            assert val==cp[0];count['stock_tie_points']+=1
        T=e+P-repair;TE=ell+(ell-h)*r
        assert T==TE+P
        for f in [T-Q(1,100),T,T+Q(1,100)]:
            assert (cp[0]>f+repair)-(cp[0]<f+repair)==(T>f)-(T<f)
            count['fee_boundary_checks']+=1
        # Verify raw hull separately at every residual breakpoint and midpoint.
        xs=[Q(0),Q(1,2),Q(1),Q(3,2),Q(2),Q(5,2)]
        for x in xs:assert raw_rec(x,a,j)[0]==g(x,a,j)
        data[j]={'hard':cp[0],'expected':e,'repaired_pre_fee':repair,'threshold_hard':T,'threshold_expected':TE,'premium':P,'stock':[lo,hi],'expected_stock':[ex[1],ex[2]],'repaired_stock':[h+xlo,None if xhi is None else h+xhi],'raw_histories':cp[4],'all_source_minima':[(v,n,l,h) for v,n,l,h,w in raw]}
    diff=data[1]['premium']-data[0]['premium']
    assert diff<=0
    assert (diff<0)==(0<a<3 and q*a<r<a+q*(3-a))
    return data

# Predetermined breakpoint/midpoint checks, not random parameter sweeps.
records=[]
for q,y in [(Q(1,2),Q(1,2)),(Q(2,5),Q(2,5)),(Q(2,5),Q(3,5)),(Q(3,5),Q(2,5)),(Q(3,5),Q(3,5))]:
    for a in [Q(0),Q(1),Q(2),Q(3)]:
        cuts=sorted({Q(0),Q(3),q*a,a,a+q*(3-a),3*q})
        prices=sorted(set(cuts+[(x+y)/2 for x,y in zip(cuts,cuts[1:])]))
        for r in prices:
            z=run_group(a,r,q,y)
            records.append({'a':a,'rho':r,'q':q,'gamma':y,'cells':z})
w=run_group(Q(1),Q(1),Q(1,2),Q(1,2))
assert [w[j]['hard'] for j in (0,1)]==[Q(59,4),Q(29,2)]
assert all(w[j]['repaired_pre_fee']==Q(121,10) for j in (0,1))
assert [w[j]['threshold_hard'] for j in (0,1)]==[Q(53,20),Q(12,5)]
assert w[1]['stock']==[Q(5,2),Q(3)]
assert [min(w[j]['hard'],Q(5,2)+w[j]['repaired_pre_fee']) for j in (0,1)]==[Q(73,5),Q(29,2)]
openw=run_group(Q(1),Q(11,10),Q(1,2),Q(1,2))
assert openw[1]['threshold_hard']==Q(127,50)<Q(13,5)<openw[0]['threshold_hard']==Q(279,100)
assert all(openw[j]['stock']==[Q(5,2),Q(5,2)] for j in (0,1))
# Fixed B witnesses: direct history allocations, with procurement charged equally.
b=Q(11,5);r=Q(1);a=Q(1);F=Q(5,2)
fixed=[]
for j in (0,1):
    u=Q(45,4)+sum(raw_rec(b-x,a,j)[0]/2 for x in (Q(1),Q(3,2)))+r*b
    rr=10+F+raw_rec(b-Q(1,10),a,j)[0]+r*b
    fixed.append((u,rr))
assert fixed==[(Q(149,10),Q(157,10)),(Q(74,5),Q(147,10))]
assert (fixed[1][0]-fixed[1][1])-(fixed[0][0]-fixed[0][1])==Q(9,10)
OUT.mkdir(exist_ok=True)
(OUT/'capacity_procurement.json').write_text(json.dumps(enc({'status':'synthetic exact validation','counters':count,'benchmark_witness':w,'unique_stock_open_witness':openw,'fixed_stock_witness':fixed,'groups':records}),indent=2)+'\n')
print(json.dumps(count,sort_keys=True));print('R6 exact procurement checks PASS; all previous suites remain separate.')
