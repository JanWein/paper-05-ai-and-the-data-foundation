"""Finite adaptive benchmark. All examples synthetic; expected, not hard capacity."""
from dataclasses import dataclass, replace
from itertools import product
from pathlib import Path
import json, csv
import numpy as np
from scipy.optimize import linprog

@dataclass(frozen=True)
class Parameters:
    q: float=.5
    gamma: float=.5
    Ls: float=10.
    k: float=1.
    tm: float=1.
    ta: float=2.
    dm: float=4.
    da: float=8.
    c: float=10.
    S: float=2.
    B: float=2.2
    h: float=.1
    F: float=1.7

def policies(p, access, repair):
    acts=list(product(range(2 if access else 1), range(2)))
    plans=[('R',(a,)) for a in acts] if repair else (
        [('N',(a,)) for a in acts]+[(s,(a,b)) for s in ('C2','C1N','C1P','C1C') for a,b in product(acts,repeat=2)])
    out=[]
    for mode, actions in plans:
        load=cost=adopt=first=prop=0.
        # Event-tree evaluation: branch costs, information, irreversible first loss.
        for z,prob in ((0,1-p.q),(1,p.q)):
            u=p.h if repair else 0.; loss=0.
            if mode=='N': loss=2*z*p.Ls
            elif mode=='C2': u+=1; loss=z*p.Ls
            elif mode.startswith('C1'):
                u+=1; first+=prob
                if z and mode=='C1N': loss+=p.Ls
                if z and mode=='C1P': u+=p.gamma; prop+=prob
                if z and mode=='C1C': u+=1
            a,r=actions[z] if len(actions)==2 else actions[0]
            t=p.ta if a else p.tm
            u+=r*t
            money=p.c-p.S*a+p.k*(u-(p.h if repair else 0.))+(p.F if repair else 0.)
            loss+=(p.da if a else p.dm)*(1-r)
            load+=prob*u; cost+=prob*(money+loss); adopt+=prob*a
        # Closed-form column construction, separate from the event-tree accumulation.
        source_load={'R':p.h,'N':0.,'C2':1.,'C1N':1.,'C1P':1+p.q*p.gamma,'C1C':1+p.q}[mode]
        source_loss={'R':0.,'N':2*p.q*p.Ls,'C2':p.q*p.Ls,'C1N':p.q*p.Ls,'C1P':0.,'C1C':0.}[mode]
        weights=[1.] if len(actions)==1 else [1-p.q,p.q]
        rec_load=sum(v*r*(p.ta if a else p.tm) for v,(a,r) in zip(weights,actions))
        rec_cost=sum(v*(p.c-p.S*a+p.k*r*(p.ta if a else p.tm)+(p.da if a else p.dm)*(1-r)) for v,(a,r) in zip(weights,actions))
        assert abs(load-source_load-rec_load)<1e-9
        source_money=p.F if repair else p.k*source_load
        assert abs(cost-source_money-source_loss-rec_cost)<1e-9
        out.append(dict(mode=mode,actions=str(actions),load=load,cost=cost,adoption=adopt,first=first,propagation=prop))
    return out

def solve(p,access,repair):
    cols=policies(p,access,repair); candidates=[]
    for i,x in enumerate(cols):
        if x['load']<=p.B+1e-12: candidates.append((x['cost'],[(i,1.)]))
    for i,x in enumerate(cols):
        for j,y in enumerate(cols[:i]):
            if (x['load']-p.B)*(y['load']-p.B)<0:
                alpha=(p.B-y['load'])/(x['load']-y['load'])
                candidates.append((alpha*x['cost']+(1-alpha)*y['cost'],[(i,alpha),(j,1-alpha)]))
    lp=linprog([x['cost'] for x in cols],A_ub=[[x['load'] for x in cols]],b_ub=[p.B],A_eq=[np.ones(len(cols))],b_eq=[1.],bounds=(0,None),method='highs')
    if not candidates:
        assert not lp.success
        return None
    value,mix=min(candidates,key=lambda x:x[0]); assert lp.success
    assert abs(value-lp.fun)<1e-8
    return dict(cost=value,load=sum(cols[i]['load']*a for i,a in mix),adoption=sum(cols[i]['adoption']*a for i,a in mix),first=sum(cols[i]['first']*a for i,a in mix),propagation=sum(cols[i]['propagation']*a for i,a in mix),mix=[dict(weight=a,**cols[i]) for i,a in mix],lp_error=abs(value-lp.fun))

def main():
    dest=Path(__file__).resolve().parents[1]/'results'; dest.mkdir(exist_ok=True)
    p=Parameters(); results={}; count=0; maxerr=0.
    for A,d in product(range(2),repeat=2):
        x=solve(p,A,d); results[f'A{A}D{d}']=x; count+=1; maxerr=max(maxerr,x['lp_error'])
        cols=policies(p,A,d)
        with (dest/f'adaptive_policies_A{A}D{d}.csv').open('w') as f:
            w=csv.DictWriter(f,fieldnames=list(cols[0])); w.writeheader(); w.writerows(cols)
    assert np.allclose([results[k]['cost'] for k in ('A0D0','A1D0','A0D1','A1D1')],[12.4,12.4,12.7,11.7])
    # Independent closed-form theorem checks on strict, open parameter regions.
    rng=np.random.default_rng(5017)
    candidates=accepted=skipped=0
    main_cells=count
    for _ in range(100):
        candidates+=1
        q=rng.uniform(.2,.8); g=rng.uniform(.1,.8); ell=1+q*g
        tm=rng.uniform(1.,2.); delta=rng.uniform(.1,.5); ta=tm+delta
        w0=rng.uniform(3.,6.); dm=w0*tm; S=(1+w0)*delta/2
        B=ell+tm*rng.uniform(.6,.95); h=.05
        if h+ta>=B:
            skipped+=1  # Outside the sufficient feasibility region, not a failed check.
            continue
        accepted+=1
        y=(B-ell)/tm; R=ell+(dm-tm)*(1-y)
        r=Parameters(q=q,gamma=g,Ls=10*w0,tm=tm,ta=ta,dm=dm,da=S+dm+2,S=S,B=B,h=h,F=R+(S-delta)/2)
        expected=[r.c+r.k*B+dm*(1-y)]*2+[r.F+r.c+tm,r.F+r.c-S+ta]
        for (A,d),v in zip(((0,0),(1,0),(0,1),(1,1)),expected):
            z=solve(r,A,d); assert abs(z['cost']-v)<1e-8
            assert abs(z['adoption']-(A*d))<1e-8
            count+=1; maxerr=max(maxerr,z['lp_error'])
    theorem_cells=count-main_cells
    boundaries={}
    for label,r in [('slack_null',replace(p,B=10)),('zero_capacity',replace(p,B=0)),('certain_clean',replace(p,q=0)),('certain_fault',replace(p,q=1)),('equivalent_resource',replace(p,B=10,h=1.25,F=1.25))]:
        cells={}
        for A,d in product(range(2),repeat=2):
            z=solve(r,A,d); cells[f'A{A}D{d}']=z; count+=1
            if z: maxerr=max(maxerr,z['lp_error'])
        boundaries[label]=cells
    for label in ('slack_null','equivalent_resource'):
        c=boundaries[label]; interaction=c['A0D1']['cost']-c['A1D1']['cost']-c['A0D0']['cost']+c['A1D0']['cost']; assert abs(interaction)<1e-8
    boundary_cells=count-main_cells-theorem_cells
    thresholds=[]
    for S in np.linspace(0,6,61):
        r=replace(p,S=float(S)); row={'S':float(S)}
        for d in (0,1):
            z=solve(r,1,d); row[f'cost_d{d}']=z['cost']; row[f'adoption_d{d}']=z['adoption'];count+=1; maxerr=max(maxerr,z['lp_error'])
            if S< (1 if d else 4)-1e-9: assert z['adoption']<1e-8
            if S> (1 if d else 4)+1e-9: assert z['adoption']>1e-8
        thresholds.append(row)
    entry_grid_cells=count-main_cells-theorem_cells-boundary_cells
    assert candidates==accepted+skipped==100
    assert (accepted,skipped)==(98,2)
    assert theorem_cells==4*accepted==392
    assert (main_cells,boundary_cells,entry_grid_cells)==(4,20,122)
    assert count==main_cells+theorem_cells+boundary_cells+entry_grid_cells==538
    decomposition=dict(main_cells=main_cells,accepted_draw_cells=theorem_cells,boundary_cells=boundary_cells,entry_grid_cells=entry_grid_cells)
    output=dict(parameters=p.__dict__,cells=results,boundaries=boundaries,validation=dict(lp_comparisons=count,max_abs_error=maxerr,theorem_draws=accepted,theorem_candidates=candidates,theorem_accepted=accepted,theorem_skipped=skipped,comparison_decomposition=decomposition,skipped_candidates_are_failed_checks=False,policy_counts_noaccess=18,policy_counts_access=68,capacity='expected only'),adoption_thresholds=dict(unrepaired=4,repaired=1))
    (dest/'adaptive_results.json').write_text(json.dumps(output,indent=2))
    with (dest/'adaptive_adoption.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(thresholds[0])); w.writeheader();w.writerows(thresholds)
    print(json.dumps(output['validation'],indent=2))
if __name__=='__main__': main()
