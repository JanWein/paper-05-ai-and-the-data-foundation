"""R5 exact synthetic checks. Standalone raw task allocations, no prior model imports."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,csv
P=dict(q=Q(1,2),g=Q(1,2),Ls=Q(10),k=Q(1),tm=Q(1),ta=Q(2),dm=Q(4),da=Q(8),c=Q(10),S=Q(2),h=Q(1,10),F=Q(5,2))
def f(n,x,p):return min(Q(1),Q(max(0,(n*x)//p['tm']),n))
def rec(n,x,A,p,raw=False):
    if x<0:return None
    acts=[(0,0),(0,1)]+([(1,0),(1,1)] if A else [])
    if raw:
        vals=[]
        for word in product(acts,repeat=n):
            load=sum((r*(p['ta'] if a else p['tm']) for a,r in word),Q(0))/n
            cost=sum(((p['da'] if a else p['dm'])*(1-r)+p['k']*r*(p['ta'] if a else p['tm'])-p['S']*a for a,r in word),Q(0))/n
            if load<=x:vals.append(cost)
        return min(vals)
    vals=[]
    # Counts of each of the full four actions, independent of their task labels.
    for ma in range(n+1):
      for au in range(n-ma+1) if A else (0,):
       for aa in range(n-ma-au+1) if A else (0,):
        mu=n-ma-au-aa
        load=(ma*p['tm']+aa*p['ta'])/n
        if load<=x:vals.append((mu*p['dm']+ma*p['k']*p['tm']+au*(p['da']-p['S'])+aa*(p['k']*p['ta']-p['S']))/n)
    return min(vals)
def fluid(x,A,p):
    if x<0:return None
    if not A:return p['dm']-(p['dm']-p['k']*p['tm'])*min(Q(1),x/p['tm'])
    assert p['tm']==1 and p['ta']==2 and 1<=p['S']<=4
    if x<=1:return 4-3*x
    if x<=2:return 1+(1-p['S'])*(x-1)
    return 2-p['S']
def source_histories(d,p):
    if d:return [('prior',[(p['h'],Q(0)),(p['h'],Q(0))])]
    out=[('neither',[(Q(0),Q(0)),(Q(0),2*p['Ls'])]),('second',[(Q(1),Q(0)),(Q(1),p['Ls'])])]
    # Include redundant clean rechecks. First action and contingent table are fixed ex ante.
    for clean,fault in product(('leave','check'),('leave','propagate','check')):
        hist=[]
        for z in (0,1):
            u=Q(1);wrong=z
            a=clean if not z else fault
            if a=='check':u+=1;wrong=0
            if a=='propagate':u+=p['g'];wrong=0
            hist.append((u,wrong*p['Ls']))
        out.append((f'first:{clean}/{fault}',hist))
    return out
def hard(n,A,d,B,p,raw=False,continuum=False):
    rows=[]
    for name,hist in source_histories(d,p):
        costs=[];loads=[]
        for z,(u,loss) in enumerate(hist):
            rc=fluid(B-u,A,p) if continuum else rec(n,B-u,A,p,raw)
            if rc is None:break
            # Recipient costs are net of common production c, source F includes k*h once.
            money=p['F'] if d else p['k']*u
            costs.append(p['c']+money+loss+rc);loads.append(u)
        if len(costs)==2:
            v=(1-p['q'])*costs[0]+p['q']*costs[1]
            rows.append(dict(source=name,cost=v,source_loads=loads,branch_costs=costs))
    return min(x['cost'] for x in rows),rows

def raw_witness(n,x,A,p):
    acts=[(0,0),(0,1)]+([(1,0),(1,1)] if A else [])
    options=[]
    for word in product(acts,repeat=n):
        load=sum((r*(p['ta'] if a else p['tm']) for a,r in word),Q(0))/n
        cost=sum(((p['da'] if a else p['dm'])*(1-r)+p['k']*r*(p['ta'] if a else p['tm'])-p['S']*a for a,r in word),Q(0))/n
        if load<=x:options.append(dict(actions=word,load=load,cost=cost))
    return min(options,key=lambda v:v['cost'])

def main():
    dest=Path(__file__).resolve().parents[1]/'results';B=Q(11,5);p=P.copy();eq=dict(p,h=Q(5,4),F=Q(5,4));matches=[]
    for n,expect in ((1,[Q(55,4),Q(61,4)]),(4,[Q(13),Q(13)]),(7,[Q(361,28),Q(355,28)])):
        costs=[hard(n,0,d,B,eq)[0] for d in (0,1)];assert costs==expect
        assert [hard(n,0,d,B,eq,True)[0] for d in (0,1)]==costs
        beta=eq['dm']-eq['k']*eq['tm'];gap=beta*((1-eq['q'])*f(n,B-1,eq)+eq['q']*f(n,B-1-eq['g'],eq)-f(n,B-Q(5,4),eq))
        assert costs[1]-costs[0]==gap
        matches.append(dict(n=n,costs=costs,gap=gap))
    fl=[hard(1,0,d,B,eq,continuum=True)[0] for d in (0,1)];assert fl==[Q(127,10),Q(62,5)]
    # Independent raw labeled allocations vs count solution at exact capacity boundaries.
    rawchecks=0;sourcechecks=0;rows=[]
    for n,A,S,d in product((1,2,3,4),(0,1),(Q(1),Q(2),Q(4)),(0,1)):
        r=dict(p,S=S)
        for x in (Q(0),Q(1,n),Q(3,5),Q(1),Q(6,5),Q(2)):
            v=rec(n,x,A,r,True);assert v==rec(n,x,A,r)
            if A:
                closed=(4-3*Q(min(n,int(n*x)),n) if x<=1 else 1+(1-S)*Q(min(n,int(n*(x-1))),n) if x<=2 else 2-S)
                assert v==closed
            rawchecks+=1
        a,competitors=hard(n,A,d,B,r,True);b,_=hard(n,A,d,B,r);assert a==b;sourcechecks+=1
        if not d:assert {v['source'] for v in competitors if v['cost']==a}=={'first:leave/propagate'}
        for v in competitors:rows.append(dict(n=n,A=A,S=S,d=d,**v))
    # Convergence and rounding bounds, deterministic witnesses rather than a campaign.
    convergence=[]
    for n in (1,4,7,20):
      for b,S in product((Q(21,10),Q(11,5),Q(9,4)),(Q(1),Q(2),Q(4))):
        r=dict(p,S=S);finite=[];limit=[]
        for A,d in product((0,1),repeat=2):
            v,plans=hard(n,A,d,b,r);l,_=hard(n,A,d,b,r,continuum=True)
            bound=Q(0) if d else (Q(3,2)/n if not A else (S+2)/(2*n))
            assert 0<=v-l<=bound
            finite.append(v);limit.append(l)
        mn=Q(int(n*(b-Q(3,2))),n);bn=Q(int(n*(b-2)),n)
        assert finite[0]==Q(55,4)-3*mn/2
        assert finite[2]==finite[0]-(S-1)*bn/2
        if S==1:assert finite[0]==finite[2]
        if S==4:assert (3-b+S*(2-b/2))==(7+S-3*b)
        assert limit==[16-3*b/2,p['F']+11,15-b-S*(b-2)/2,p['F']+12-S]
        convergence.append(dict(n=n,B=b,S=S,finite=finite,fluid=limit))
    # Fluid strict region, fee ties, and unchanged expected-capacity solution.
    U0=16-3*B/2;U1=15-B-p['S']*(B-2)/2;T0=5-3*B/2;TH=3-B+p['S']*(2-B/2);TE=7+p['S']-3*B
    assert TH-TE==(B-2)*(4-p['S'])/2 and TH-T0==(p['S']-1)*(2-B/2)
    seed=[hard(1,A,d,B,p,continuum=True)[0] for A,d in ((0,0),(1,0),(0,1),(1,1))]
    assert seed==[Q(127,10),Q(63,5),Q(27,2),Q(25,2)]
    expected=[19-3*B,19-3*B,p['F']+11,p['F']+12-p['S']];assert expected==[Q(62,5),Q(62,5),Q(27,2),Q(25,2)]
    feechecks=[]
    for F in (T0,TE,TH):
        r=dict(p,F=F);a0=hard(1,0,0,B,r,continuum=True)[0];a1=hard(1,1,0,B,r,continuum=True)[0];r0=hard(1,0,1,B,r,continuum=True)[0];r1=hard(1,1,1,B,r,continuum=True)[0]
        if F==T0:assert a0==r0
        if F==TE:assert 19-3*B==r1
        if F==TH:assert a1==r1
        feechecks.append(dict(F=F,hard=[a0,a1,r0,r1]))
    general=dict(eq,q=Q(1,3),g=Q(3,5),dm=Q(5),h=Q(6,5),F=Q(6,5))
    for n in (1,4,7):
        b=Q(21,10);beta=Q(4)
        vals=[hard(n,0,d,b,general)[0] for d in (0,1)]
        gap=beta*((1-general['q'])*f(n,b-1,general)+general['q']*f(n,b-1-general['g'],general)-f(n,b-general['h'],general))
        assert vals[1]-vals[0]==gap
    gaps=[]
    for n in (1,4,7,20):
      for b in (Q(2),Q(11,5),Q(9,4)):
        beta=Q(3);fn=lambda x:f(n,x,eq);fi=lambda x:min(Q(1),x)
        dn=beta*((fn(b-1)+fn(b-Q(3,2)))/2-fn(b-Q(5,4)))
        di=beta*((fi(b-1)+fi(b-Q(3,2)))/2-fi(b-Q(5,4)))
        assert di<=0 and abs(dn-di)<=beta/n and dn<=beta/n
        gaps.append(dict(n=n,B=b,gap=dn,fluid_gap=di))
    witnesses=[]
    for n,A,d in ((1,0,0),(1,0,1),(4,0,0),(4,0,1),(7,0,0),(7,0,1),(4,1,0),(4,1,1)):
        r=eq if not A else p
        value,plans=hard(n,A,d,B,r,True)
        winner=next(v for v in plans if v['cost']==value)
        hist=dict(source_histories(d,r))[winner['source']]
        shared=None
        if winner['source'] in ('neither','prior'):
            shared=raw_witness(n,B-hist[0][0],A,r)
        branches=[];expected_value=Q(0)
        for z,(source_load,source_loss) in enumerate(hist):
            recw=shared if shared is not None else raw_witness(n,B-source_load,A,r)
            assert source_load+recw['load']<=B
            cost=r['c']+(r['F'] if d else r['k']*source_load)+source_loss+recw['cost']
            expected_value+=((1-r['q']) if z==0 else r['q'])*cost
            branches.append(dict(z=z,source_load=source_load,total_load=source_load+recw['load'],recipient=recw,cost=cost))
        assert expected_value==value
        if shared is not None:assert branches[0]['recipient']['actions']==branches[1]['recipient']['actions']
        witnesses.append(dict(scenario='matched_mean_no_access' if not A else 'cheap_validation_access',parameters=r,B=B,n=n,A=A,d=d,source=winner['source'],cost=value,branches=branches))
    (dest/'granularity_raw_witnesses.json').write_text(json.dumps(witnesses,default=str,indent=2))
    out=dict(synthetic_only=True,exact_fractions=True,raw_allocation_checks=rawchecks,raw_global_source_checks=sourcechecks,matched_mean=matches,matched_mean_fluid=fl,fluid_seed_hard=seed,fluid_seed_expected=expected,thresholds=dict(T0=T0,TH=TH,TE=TE),fee_ties=feechecks,convergence=convergence,gap_bounds=gaps)
    (dest/'granularity_results.json').write_text(json.dumps(out,default=str,indent=2))
    with (dest/'granularity_source_competitors.csv').open('w') as fobj:
        w=csv.DictWriter(fobj,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(json.dumps(dict(raw_allocation_checks=rawchecks,raw_global_source_checks=sourcechecks,matched_mean=str(matches),fluid_seed=list(map(str,seed)),status='PASS'),indent=2))
if __name__=='__main__':main()
