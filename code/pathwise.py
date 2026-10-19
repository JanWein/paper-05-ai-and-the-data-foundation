"""Exact synthetic raw-history checks, standalone: no imports from author models."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,csv

BASE=dict(q=Q(1,2),g=Q(1,2),Ls=Q(10),k=Q(1),tm=Q(1),ta=Q(2),dm=Q(4),da=Q(8),c=Q(10),h=Q(1,10),F=Q(29,10),S=Q(2))

def raw(p,A,d):
    acts=list(product(range(1+A),range(2)))
    # First action and second action rules are chosen before the hidden fault.
    specs=[('repair',None,(a,)) for a in acts] if d else (
      [('no_check',None,(a,)) for a in acts]+
      [('second',None,(a,b)) for a,b in product(acts,repeat=2)]+
      [('first',(clean,fault),(a,b)) for clean,fault,a,b in product(('leave','check'),('leave','propagate','check'),acts,acts)])
    out=[]
    for mode,rule,actions in specs:
        loads=[];losses=[];branchcosts=[];cost=adopt=Q(0)
        for z,prob in ((0,1-p['q']),(1,p['q'])):
            u=Q(0);wrong1=wrong2=z
            if d: u+=p['h'];wrong1=wrong2=0
            elif mode=='second':u+=1;wrong2=0
            elif mode=='first':
                u+=1;wrong1=0
                action=rule[z]
                if action=='check':u+=1;wrong2=0
                elif action=='propagate':u+=p['g'];wrong2=0
            a,r=actions[z] if len(actions)==2 else actions[0]
            u+=r*(p['ta'] if a else p['tm'])
            loss=(wrong1+wrong2)*p['Ls']+(p['da'] if a else p['dm'])*(1-r)
            money=p['c']-p['S']*a+p['k']*(u-(p['h'] if d else 0))+(p['F'] if d else 0)
            loads.append(u);losses.append(loss);branchcosts.append(money+loss);cost+=prob*(money+loss);adopt+=prob*a
        out.append(dict(mode=mode,rule=str(rule),actions=str(actions),load0=loads[0],load1=loads[1],cost0=branchcosts[0],cost1=branchcosts[1],cost=cost,adoption=adopt))
    return out

def hard(p,A,d,B):
    cols=raw(p,A,d);feas=[x for x in cols if max(x['load0'],x['load1'])<=B]
    if not feas:return None,[]
    v=min(x['cost'] for x in feas)
    return v,[x for x in feas if x['cost']==v]

def expected(p,A,d,B):
    cols=raw(p,A,d); pts=[((1-p['q'])*x['load0']+p['q']*x['load1'],x['cost']) for x in cols]
    vals=[c for u,c in pts if u<=B]
    for i,(u,c) in enumerate(pts):
        for v,e in pts[:i]:
            if (u-B)*(v-B)<0:
                t=(B-v)/(u-v);vals.append(t*c+(1-t)*e)
    return min(vals) if vals else None

def G(p,A,x):
    if x<0:return None
    v=[p['dm']]
    if x>=p['tm']:v.append(p['k']*p['tm'])
    if A:
        v.append(p['da']-p['S'])
        if x>=p['ta']:v.append(p['k']*p['ta']-p['S'])
    return min(v)

def frontier(p,A,d,B):
    if d:
        v=G(p,A,B-p['h']);return None if v is None else p['c']+p['F']+v
    v=[2*p['q']*p['Ls']+G(p,A,B)]
    if B>=1:v.append(p['k']+p['q']*p['Ls']+G(p,A,B-1))
    if B>=1+p['g']:v.append(p['k']*(1+p['q']*p['g'])+(1-p['q'])*G(p,A,B-1)+p['q']*G(p,A,B-1-p['g']))
    return p['c']+min(v)

def main():
    dest=Path(__file__).resolve().parents[1]/'results';p=BASE.copy();B=Q(11,5);n=0
    cells={};allrows=[]
    for A,d in product(range(2),repeat=2):
        h,win=hard(p,A,d,B);e=expected(p,A,d,B);cells[f'A{A}D{d}']=dict(hard=h,expected=e,winners=win)
        for row in raw(p,A,d):allrows.append(dict(A=A,d=d,**row,feasible=max(row['load0'],row['load1'])<=B))
    assert [cells[k]['hard'] for k in ('A0D0','A1D0','A0D1','A1D1')]==[Q(55,4),Q(55,4),Q(139,10),Q(129,10)]
    assert [cells[k]['expected'] for k in ('A0D0','A1D0','A0D1','A1D1')]==[Q(62,5),Q(62,5),Q(139,10),Q(129,10)]
    breaks=sorted({max(x['load0'],x['load1']) for A,d in product(range(2),repeat=2) for x in raw(p,A,d)})
    # Include redundant clean rechecks: they create no break beyond the useful set.
    assert breaks==list(map(Q,[0,Q(1,10),1,Q(11,10),Q(3,2),2,Q(21,10),Q(5,2),3,Q(7,2),4]))
    budgets=sorted(set(breaks+[(a+b)/2 for a,b in zip(breaks,breaks[1:])]))
    tiecases=[]
    for b,S,A,d in product(budgets,map(Q,[0,1,2,4,5,7,8]),range(2),range(2)):
        r=dict(p,S=S);v,w=hard(r,A,d,b);assert v==frontier(r,A,d,b);n+=1
        if len(w)>1:tiecases.append(dict(B=b,S=S,A=A,d=d,cost=v,winner_count=len(w),winners=w))
    # Entire decisive strip has a proven formula; exact interior and boundary witnesses.
    regions=[]
    for S in map(Q,[0,1,2,4,5,7,8]):
        r=dict(p,S=S);u=Q(55,4) if S<=4 else (Q(63,4)-S/2 if S<=7 else Q(77,4)-S)
        v,w=hard(r,1,0,B);assert v==u
        adoptions=set(x['adoption'] for x in w)
        expected_adoptions=({Q(0),Q(1,2)} if S==4 else {Q(1,2),Q(1)} if S==7 else {Q(0)} if S<4 else {Q(1,2)} if S<7 else {Q(1)})
        assert adoptions==expected_adoptions
        _,repaired_winners=hard(r,1,1,B)
        assert set(x['adoption'] for x in repaired_winners)==({Q(0),Q(1)} if S==1 else {Q(0)} if S<1 else {Q(1)})
        fee=u-(10+min(Q(1),2-S))
        for F in (fee-Q(1,10),fee,fee+Q(1,10)):
            rr=dict(r,F=F);a,_=hard(rr,1,0,B);b,_=hard(rr,1,1,B);assert (a==b)==(F==fee)
        regions.append(dict(S=S,unrepaired=u,repair_threshold=fee,adoption_probabilities=sorted(set(x['adoption'] for x in w))))
    assert hard(p,1,0,Q(5,2))[0]==Q(49,4)
    assert hard(p,1,1,Q(21,10))[0]==p['F']+10
    assert hard(p,1,1,Q(209,100))[0]==p['F']+11
    eq=dict(p,h=Q(5,4),F=Q(5,4));nulls=[]
    for b in (Q(2),Q(11,5),Q(9,4),Q(12,5),Q(5,2)):
        hs=[hard(eq,0,d,b)[0] for d in (0,1)];es=[expected(eq,0,d,b) for d in (0,1)]
        assert es[0]==es[1]
        if b<Q(9,4):assert hs==[Q(55,4),Q(61,4)]
        elif b<Q(5,2):assert hs==[Q(55,4),Q(49,4)]
        else:assert hs==[Q(49,4),Q(49,4)]
        nulls.append(dict(B=b,hard=hs,expected=es))
    # Primitive generalization witness, distinct exact rational primitives, no random campaign.
    g=dict(p,q=Q(1,3),g=Q(3,5),tm=Q(1),dm=Q(5),h=Q(6,5),F=Q(6,5))
    b=Q(21,10);hc=[hard(g,0,d,b)[0] for d in (0,1)];ec=[expected(g,0,d,b) for d in (0,1)]
    assert ec[0]==ec[1];assert hc[1]-hc[0]==(1-g['q'])*(g['dm']-g['k']*g['tm'])
    result=dict(synthetic_only=True,exact_rational=True,main_cells=cells,load_breakpoints=breaks,frontier_cell_checks=n,tie_cases=tiecases,strip_frontier=regions,equal_expected_resource=nulls,primitive_witness=dict(hard=hc,expected=ec))
    (dest/'pathwise_results.json').write_text(json.dumps(result,default=str,indent=2))
    with (dest/'pathwise_raw_histories.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(allrows[0]));w.writeheader();w.writerows(allrows)
    print(json.dumps(dict(frontier_cell_checks=n,raw_seed_columns=len(allrows),seed_hard=[str(cells[k]['hard']) for k in ('A0D0','A1D0','A0D1','A1D1')],exact_checks='PASS'),indent=2))
if __name__=='__main__':main()
