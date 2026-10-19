"""R8 synthetic finite-state verification. Standard library, no author imports.
Raw exhaustive policy enumeration and separately formed conditional minimization.
Physical actions, costs, latent states and resource stock are identical across
information regimes. No policy may use a hidden identity or unaudited fault.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[1]/'results'
MASKS=(0,1,2,3)
COUNTS={'operating_groups':0,'cell_comparisons':0,'full_policies_evaluated':0,'positive_history_resource_checks':0,'root_patterns':0,'forbidden_policies_rejected':0,'matched_state_pairs':0,'adoption_boundary_checks':0}
def enc(z):
    if isinstance(z,Q):return str(z)
    if isinstance(z,dict):return {str(k):enc(v) for k,v in z.items()}
    if isinstance(z,(list,tuple)):return [enc(v) for v in z]
    return z

def worlds(p,r):
    return [(j,z1,z2,(Q(1,2)*(p if z1 else 1-p)*(p if z2 else 1-p)),(0 if r and j==0 else z1 if j==0 else z2)) for j,z1,z2 in product((0,1),repeat=3) if (p if z1 else 1-p)*(p if z2 else 1-p)>0]
def pre(w,mode):return w[0] if mode=='early' else None
def post(w,mode,checked):
    if mode in ('early','late'):return (w[0],w[4] if checked else None)
    return w[4] if checked else None

def term(w,mask,W,d):return d*mask.bit_count()+W*w[4]*(not bool(mask & (1<<w[0])))
def all_policies(p,r,mode,W,v,d):
    ws=worlds(p,r);keys=sorted(set(pre(w,mode) for w in ws),key=str);best=None;minpol=[];n=0
    # First enumerate all checking decisions at their actual pre-signal nodes.
    for bits in product((0,1),repeat=len(keys)):
        checks=dict(zip(keys,bits))
        nodes=sorted({(pre(w,mode),checks[pre(w,mode)],post(w,mode,checks[pre(w,mode)])) for w in ws},key=str)
        for actions in product(MASKS,repeat=len(nodes)):
            rule=dict(zip(nodes,actions));cost=Q(0);loads=[]
            for w in ws:
                b=checks[pre(w,mode)];m=rule[(pre(w,mode),b,post(w,mode,b))]
                load=Q(r,10)+b+m.bit_count();assert load<=4
                cost+=w[3]*(v*b+term(w,m,W,d));loads.append(load)
                COUNTS['positive_history_resource_checks']+=1
            n+=1
            if best is None or cost<best:best=cost;minpol=[(checks,rule)]
            elif cost==best:minpol.append((checks,rule))
    COUNTS['full_policies_evaluated']+=n
    checks,rule=minpol[0];witness=[]
    for w in ws:
        b=checks[pre(w,mode)];m=rule[(pre(w,mode),b,post(w,mode,b))]
        witness.append({'J':w[0]+1,'Z1':w[1],'Z2':w[2],'prob':w[3],'potential_Y':w[4],'check':b,'repair_mask':m,'load':Q(r,10)+b+m.bit_count(),'residual_error':int(w[4] and not (m&(1<<w[0])))})
    return best,len(minpol),n,witness

def conditional_value(p,r,mode,W,v,d):
    ws=worlds(p,r);value=Q(0)
    for key in set(pre(w,mode) for w in ws):
        group=[w for w in ws if pre(w,mode)==key];options=[]
        for b in (0,1):
            z=sum(w[3]*v*b for w in group)
            for obs in set(post(w,mode,b) for w in group):
                block=[w for w in group if post(w,mode,b)==obs]
                z+=min(sum(w[3]*term(w,m,W,d) for w in block) for m in MASKS)
            options.append(z)
        value+=min(options)
    return value

def general_formula(p,r,mode,W,v,d):
    known=min(p*W,d,v+p*min(W,d))
    if r==0:return known if mode!='opaque' else min(p*W,2*d,v+p*min(W,2*d))
    if mode=='early':return known/2
    return min(p*W/2,d/(2 if mode=='late' else 1),v+p*min(W,d)/2)
def raw_feasible(witness,mode):
    # No hidden state can enter checking or terminal decisions.
    ck={};rp={}
    for row in witness:
        w=(row['J']-1,row['Z1'],row['Z2'],row['prob'],row['potential_Y'])
        k=pre(w,mode);b=row['check'];t=(k,b,post(w,mode,b))
        if k in ck and ck[k]!=b:return False
        if t in rp and rp[t]!=row['repair_mask']:return False
        ck[k]=b;rp[t]=row['repair_mask']
    return True

def check_group(p,v,d,W):
    COUNTS['operating_groups']+=1;cells={}
    for r,mode in product((0,1),('opaque','late','early')):
        raw,n,pols,w=all_policies(p,r,mode,W,v,d)
        assert raw==conditional_value(p,r,mode,W,v,d)==general_formula(p,r,mode,W,v,d)
        assert raw_feasible(w,mode)
        COUNTS['cell_comparisons']+=1
        cells[f'{r}_{mode}']={'cost':raw,'optimal_policy_count':n,'policies_enumerated':pols,'witness':w}
    for r in (0,1):
        ws=worlds(p,r)
        for w in ws:
            # Pair the same repair/workflow cell state-by-state across institutions.
            for mode in ('late','early'):
                assert w[4]==(0 if r and w[0]==0 else (w[1] if w[0]==0 else w[2]))
                COUNTS['matched_state_pairs']+=1
    if 0<p<1 and 0<v<(1-p)*d/2 and W>=2*d:
        x=p*W;t=v+p*d;u=v+2*p*d;z=2*v+p*d
        want=[min(x,u),min(x,t),min(x,t),min(x,z)/2,min(x,z)/2,min(x,t)/2]
        assert [cells[f'{r}_{m}']['cost'] for r,m in product((0,1),('opaque','late','early'))]==want
        y=max(x-t,0);G0=min(y,p*d);GR=min(y,v)/2;J=GR-G0
        assert cells['0_opaque']['cost']-cells['0_early']['cost']==G0
        assert cells['1_opaque']['cost']-cells['1_early']['cost']==GR
        assert (J>0)==(v>2*p*d and x>v+3*p*d)
        assert (cells['1_late']['cost']-cells['1_early']['cost'])==GR
    return cells

records=[]
# Targeted switch/tie/null cases, not random draws.
for p,v in ((Q(1,10),Q(3,10)),(Q(1,10),Q(1,5)),(Q(1,10),Q(1,10)),(Q(1,4),Q(1,5))):
    d=Q(1);t=v+p*d;u=v+2*p*d;z=2*v+p*d
    cuts=sorted({2*d,t/p,u/p,z/p,(t+2*p*d)/p})
    cuts=sorted(set(cuts+[(a+b)/2 for a,b in zip(cuts,cuts[1:])]+[max(cuts)+1]))
    for W in cuts:
        cells=check_group(p,v,d,W);records.append({'p':p,'v':v,'d':d,'W':W,'cells':cells})
# Outside the simplified region: original full formulas and no mandatory checking.
for p,v,d,W in [(Q(0),Q(1,2),Q(1),Q(4)),(Q(1),Q(1,2),Q(1),Q(4)),(Q(1,2),Q(0),Q(1),Q(3)),(Q(1,2),Q(1),Q(0),Q(3)),(Q(1,3),Q(2),Q(1),Q(1,2)),(Q(1,10),Q(7,10),Q(1),Q(20))]:
    records.append({'p':p,'v':v,'d':d,'W':W,'cells':check_group(p,v,d,W)})
# Explicitly rejected hidden-identity / hidden-fault policies.
ws=worlds(Q(1,10),0)
for mode,kind in [('opaque','target'),('late','check_identity'),('early','check_fault')]:
    w=[]
    for z in ws:
        w.append({'J':z[0]+1,'Z1':z[1],'Z2':z[2],'prob':z[3],'potential_Y':z[4],
        'check':z[0] if kind=='check_identity' else z[4] if kind=='check_fault' else 0,
        'repair_mask':(1<<z[0]) if kind=='target' else 0})
    assert not raw_feasible(w,mode);COUNTS['forbidden_policies_rejected']+=1
# The exact joint-investment witness, including EVERY root alternative.
p=Q(1,10);v=Q(3,10);d=Q(1);F=Q(9,50);K=Q(21,200);S=Q(9,100);Ws=[Q(9,2),Q(8)]
cc=[check_group(p,v,d,W) for W in Ws];roots=[]
for A,r,P in product((0,1),repeat=3):
    op=cc[A][f"{r}_{'early' if P else 'opaque'}"]['cost']
    roots.append({'A':A,'r':r,'P':P,'operating':op,'total':op+r*F+P*K-A*S})
assert min(roots,key=lambda z:z['total'])==next(z for z in roots if (z['A'],z['r'],z['P'])==(1,1,1))
assert min(z['total'] for z in roots)==Q(79,200)
assert min(z['total'] for z in roots if z['P']==0)==Q(81,200)
assert min(z['total'] for z in roots if z['A']==0)==Q(81,200)
# All fee boundaries of each four-foundation problem, checked by pairwise region inequalities.
root_checks=[]
for W,cs in zip(Ws,cc):
    O=cs['0_opaque']['cost'];L=cs['0_early']['cost'];R=2*cs['1_opaque']['cost']
    Fs={Q(0),O-R/2,L/2,F};Ks={Q(0),O-L,(R-L)/2,K}
    for ff,kk in product(sorted(Fs),sorted(Ks)):
        costs=[O,kk+L,ff+R/2,ff+kk+L/2]
        a=[kk>=O-L and ff>=O-R/2 and ff+kk>=O-L/2,
           kk<=O-L and ff>=L/2 and ff-kk>=L-R/2,
           ff<=O-R/2 and kk>=(R-L)/2 and kk-ff>=R/2-L,
           ff<=L/2 and kk<=(R-L)/2 and ff+kk<=O-L/2]
        assert a==[z==min(costs) for z in costs]
        COUNTS['root_patterns']+=1;root_checks.append({'W':W,'F':ff,'K':kk,'minimizers':[i for i,b in enumerate(a) if b]})
# Global optional-AI ties after reoptimizing all foundation roots.
for ff,kk in product((Q(0),F,Q(1,5)),(Q(0),K,Q(3,20))):
    costs=[]
    for cs in cc:
        costs.append([cs['0_opaque']['cost'],kk+cs['0_early']['cost'],ff+cs['1_opaque']['cost'],ff+kk+cs['1_early']['cost']])
    entry=min(costs[1])-min(costs[0])
    for saving in (entry-Q(1,1000),entry,entry+Q(1,1000)):
        allcost=costs[0]+[z-saving for z in costs[1]]
        manual=min(costs[0]);ai=min(costs[1])-saving
        assert (ai<manual)==(saving>entry)
        assert (ai==manual)==(saving==entry)
        assert min(allcost)==min(manual,ai)
        COUNTS['adoption_boundary_checks']+=1
# Exposure partition is exact: aggregate residual loss has no rounding term.
for n in (1,2,7,100):
    for c in cc:
        for entry in c.values():
            for row in entry['witness']:
                residual=row['residual_error'];W=Ws[cc.index(c)]
                assert sum(W*residual/n for _ in range(n))==W*residual
# Strict open-region inequalities behind the example.
x0=p*Ws[0];x1=p*Ws[1];t=v+p*d;u=v+2*p*d;z=2*v+p*d
assert 2*p*d<v<(1-p)*d/2 and t<x0<u<z<x1
assert 3*p*d/2<F<t/2
assert (x0-t)/2<K<u-F-t/2
assert K-(x0-t)/2<S<u-F-x0/2
# Full-price root replacements of either source, and both, are not omitted.
root_coverage=[];symmetric=[]
for a,c in enumerate(cc):
    for P in (0,1):
        mode='early' if P else 'opaque';base=c[f'1_{mode}']['cost']
        named=F+P*K+base
        other=d+P*K+base
        both=F+d+P*K
        assert named<other and named<both
        root_coverage.append({'A':a,'P':P,'named_programme':named,'other_source_full_price':other,'both_sources':both})
    # Counterfactual extension: BOTH sources can be pre-repaired at fee F each.
    # No strictly optimal provenance-plus-single-repair policy then exists.
    L=c['0_early']['cost'];O=c['0_opaque']['cost'];R=2*c['1_opaque']['cost']
    for ff in (Q(1,20),L/2,F,Q(3,10)):
        for kk in (Q(0),Q(1,100),K):
            target=ff+kk+L/2
            assert min(kk+L,2*ff)<=target
            if ff!=L/2 or kk>0:assert min(kk+L,2*ff)<target
            symmetric.append({'A':a,'F':ff,'K':kk,'single_repair_plus_lineage':target,'best_of_no_repair_lineage_and_both_repaired':min(kk+L,2*ff)})

OUT.mkdir(exist_ok=True)
result={'status':'synthetic exact validation','counts':COUNTS,'operating_groups':records,'root_witness':{'p':p,'v':v,'d':d,'F':F,'K':K,'S':S,'W':Ws,'all_eight_alternatives':roots,'cells':cc},'root_boundary_tests':root_checks,'replication_n':[1,2,7,100],'full_price_root_alternatives':root_coverage,'symmetric_cheap_repair_boundary':symmetric}
(OUT/'lineage_information.json').write_text(json.dumps(enc(result),indent=2)+'\n')
print(json.dumps(COUNTS,sort_keys=True));print('R8 exhaustive information-feasible policies, joint choices and matched histories PASS')
