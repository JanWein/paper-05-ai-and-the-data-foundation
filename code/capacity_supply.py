"""R7 synthetic exact raw-history/occupation-hull checks, no author imports.
Standard library Fraction enumeration; a small Decimal smooth-cost diagnostic.
All nonlinear procurement is charged once on the deterministic root stock.
"""
from fractions import Fraction as Q
from itertools import product,combinations
from pathlib import Path
from decimal import Decimal as D,localcontext
import json
OUT=Path(__file__).resolve().parents[1]/'results'
counts={'parameter_groups':0,'hard_source_minima':0,'expected_raw_columns':0,'cell_identities':0,'optimal_stock_points':0,'fee_comparisons':0,'chords_crossing_tier':0}
def encode(v):
    if isinstance(v,(Q,D)):return str(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return v

def acts(j,S=Q(2)):
    return [(Q(0),Q(4)),(Q(1),Q(1))]+([(Q(0),8-S),(Q(2),2-S)] if j else [])
def raw_rec(x,j):
    pp=acts(j);z=[]
    for i,(t,c) in enumerate(pp):
        if t<=x:z.append((c,[(i,Q(1))]))
    for (i,(t,c)),(ii,(tt,cc)) in combinations(enumerate(pp),2):
        if t!=tt and min(t,tt)<=x<=max(t,tt):
            w=(x-tt)/(t-tt);z.append((w*c+(1-w)*cc,[(i,w),(ii,1-w)]))
    return min(z,key=lambda v:v[0])
def menu():
    # N has no finding: recipient cannot condition on its hidden fault state.
    m=[('N',[(Q(1),Q(0),Q(10))]),('C2',[(Q(1,2),Q(1),Q(0)),(Q(1,2),Q(1),Q(10))])]
    for clean,fault in product((0,1),('N','P','C')):
        t=Q(1)+(Q(1,2) if fault=='P' else Q(1) if fault=='C' else Q(0))
        m.append((f'C1_clean{clean}_fault{fault}',[(Q(1,2),Q(1+clean),Q(0)),(Q(1,2),t,Q(10) if fault=='N' else Q(0))]))
    return m
CP='C1_clean0_faultP'
def C(B,r,k,b):return r*B+k*max(B-b,0)
def hard(hist,j,r,k,b):
    low=max(t for p,t,l in hist);cuts=sorted({low,b}|{t+x for p,t,l in hist for x,c in acts(j) if t+x>=low})
    cuts=[B for B in cuts if B>=low]
    vals=[]
    for B in cuts:
        val=10+C(B,r,k,b);w=[]
        for p,t,l in hist:
            v,alloc=raw_rec(B-t,j);load=t+sum(ww*acts(j)[i][0] for i,ww in alloc)
            assert load<=B
            val+=p*(t+l+v);w.append({'p':p,'source':t,'loss':l,'allocation':alloc,'load':load})
        vals.append((val,B,w))
    v=min(z[0] for z in vals);best=[z for z in vals if z[0]==v]
    return v,min(z[1] for z in best),max(z[1] for z in best),best[0][2]
def columns(j):
    z=[]
    for name,hist in menu():
        for choices in product(acts(j),repeat=len(hist)):
            t=sum(p*(ss+x) for (p,ss,l),(x,c) in zip(hist,choices))
            v=10+sum(p*(ss+l+c) for (p,ss,l),(x,c) in zip(hist,choices))
            z.append((t,v,name,choices))
    return z

def occupation(j,r,k,b):
    """Independent global convexification, including cross-source chords.
    A 2D lower-boundary point has at most two columns; convex C is linear on
    either side of b, so endpoint columns and chord intersections at b suffice.
    """
    z=columns(j);counts['expected_raw_columns']+=len(z)
    cand=[(v+C(t,r,k,b),t,[(i,Q(1))]) for i,(t,v,*_) in enumerate(z)]
    for (i,(t,v,*_)),(ii,(tt,vv,*_)) in combinations(enumerate(z),2):
        if min(t,tt)<b<max(t,tt):
            w=(b-tt)/(t-tt);cand.append((w*v+(1-w)*vv+C(b,r,k,b),b,[(i,w),(ii,1-w)]));counts['chords_crossing_tier']+=1
    v=min(v for v,t,w in cand);best=[zz for zz in cand if zz[0]==v]
    return v,min(z[1] for z in best),max(z[1] for z in best),best[0][2],z

def closed(r,k,b):
    v=r+k
    R=[11+Q(11,10)*r,10+Q(21,10)*r]
    U0=Q(49,4)+Q(5,2)*r+k*(Q(5,2)-b) if v<=Q(3,2) else 16-Q(3,2)*b+r*b
    U1=Q(23,2)+3*r+k*(3-b) if v<=1 else 12+Q(5,2)*r+k*(Q(5,2)-b) if v<=2 else 17-2*b+r*b
    E0=Q(49,4)+Q(9,4)*r+k*(Q(9,4)-b)
    E1=Q(45,4)+Q(13,4)*r+k*(Q(13,4)-b) if v<=1 else E0
    IH=(k-r+Q(1,2))/2 if v<=1 else Q(3,4)-r if v<=Q(3,2) else Q(3,4)-r+(v-Q(3,2))*(Q(5,2)-b) if v<=2 else 2-b/2-r
    return R,[U0,U1],[E0,E1],IH,min(k,1-r)
def stocks(j,r,k,b):
    v=r+k
    if not j:return (Q(5,2),Q(5,2)) if v<Q(3,2) else (b,Q(5,2)) if v==Q(3,2) else (b,b)
    return (Q(3),Q(3)) if v<1 else (Q(5,2),Q(3)) if v==1 else (Q(5,2),Q(5,2)) if v<2 else (b,Q(5,2)) if v==2 else (b,b)
def estocks(j,r,k,b):
    v=r+k
    if v==3:return b,Q(9,4)
    if not j or v>1:return Q(9,4),Q(9,4)
    return (Q(13,4),Q(13,4)) if v<1 else (Q(9,4),Q(13,4))

def group(r,k,b):
    counts['parameter_groups']+=1;assert Q(1,2)<r<1 and Q(21,10)<b<Q(9,4) and 0<=k<=3-r
    R,U,E,IH,IE=closed(r,k,b);rows={}
    for j in (0,1):
        hs=[]
        for name,hist in menu():
            h=hard(hist,j,r,k,b);hs.append((name,h));counts['hard_source_minima']+=1
        cp=next(z for name,z in hs if name==CP)
        assert cp[0]==min(z[0] for name,z in hs)==U[j];counts['cell_identities']+=1
        assert cp[1:3]==stocks(j,r,k,b)
        oo=occupation(j,r,k,b);assert oo[0]==E[j];counts['cell_identities']+=1
        assert oo[1:3]==estocks(j,r,k,b)
        # Prior validation has no loss or extra source-service cost beyond all-in F.
        rcuts=sorted({Q(1,10),b}|{Q(1,10)+t for t,c in acts(j)})
        rv=[(10+raw_rec(B-Q(1,10),j)[0]+C(B,r,k,b),B) for B in rcuts]
        assert min(v for v,B in rv)==R[j];counts['cell_identities']+=1
        assert [B for v,B in rv if v==R[j]]==[Q(21,10) if j else Q(11,10)]
        for lo,hi,hist,sourcebase in [(cp[1],cp[2],next(h for n,h in menu() if n==CP),Q(45,4))]:
            for B in {lo,hi,(lo+hi)/2}:
                vv=10+C(B,r,k,b)+sum(p*(t+l+raw_rec(B-t,j)[0]) for p,t,l in hist)
                assert vv==U[j];counts['optimal_stock_points']+=1
        elo,ehi=oo[1:3]
        for B in {elo,ehi,(elo+ehi)/2}:
            assert Q(45,4)+raw_rec(B-Q(5,4),j)[0]+C(B,r,k,b)==E[j];counts['optimal_stock_points']+=1
        for T in (U[j]-R[j],E[j]-R[j]):
            for F in (T-Q(1,100),T,T+Q(1,100)):
                assert ((T>F)-(T<F))==(((T+R[j])>(F+R[j]))-((T+R[j])<(F+R[j])))
                counts['fee_comparisons']+=1
        rows[j]={'U':U[j],'R_pre_fee':R[j],'E':E[j],'TH':U[j]-R[j],'TE':E[j]-R[j],'hard_stocks':cp[1:3],'expected_stocks':oo[1:3],'repaired_stock':Q(21,10) if j else Q(11,10),'hard_raw_witness':cp[3],'all_hard_source_minima':[(n,z[0],z[1:3]) for n,z in hs],'expected_witness':[(oo[4][i],w) for i,w in oo[3]]}
    assert IH==(U[1]-R[1])-(U[0]-R[0]);assert IE==(E[1]-R[1])-(E[0]-R[0])
    assert U[1]<=U[0] and E[1]<=E[0] and R[1]<R[0]
    # Complete sign classification, including both zero plateaus.
    v=r+k;rc=2-b/2
    if r<Q(3,4):sg=(k>r-Q(1,2))-(k<r-Q(1,2))
    elif r==Q(3,4):sg=-1 if v<1 else 0 if v<=Q(3,2) else 1
    elif r<rc:
        vz=Q(3,2)+(r-Q(3,4))/(Q(5,2)-b);sg=(v>vz)-(v<vz)
    elif r==rc:sg=-1 if v<2 else 0
    else:sg=-1
    assert (IH>0)-(IH<0)==sg
    return {'rho':r,'kappa':k,'b':b,'IH':IH,'IE':IE,'cells':rows}

records=[]
# Fixed finite boundary set, not a random campaign: all price/sign kinks plus
# between-kink midpoints, at three tier positions and four diagnostic prices.
for b in (Q(43,20),Q(11,5),Q(89,40)):
    rc=2-b/2
    for r in (Q(3,5),Q(3,4),(Q(3,4)+rc)/2,rc,(rc+1)/2):
        cuts={Q(0),1-r,Q(3,2)-r,2-r,3-r,r-Q(1,2)}
        cuts.add(Q(3,2)+(r-Q(3,4))/(Q(5,2)-b)-r)
        cuts=sorted(x for x in cuts if 0<=x<=3-r)
        for k in sorted(set(cuts+[(x+y)/2 for x,y in zip(cuts,cuts[1:])])):records.append(group(r,k,b))
seeds=[group(Q(3,5),k,Q(11,5)) for k in (Q(0),Q(1,10),Q(1,5))]
assert [(z['IH'],z['IE']) for z in seeds]==[(Q(-1,20),Q(0)),(Q(0),Q(1,10)),(Q(1,20),Q(1,5))]
assert [seeds[0]['cells'][j]['TH'] for j in (0,1)]==[Q(209,100),Q(51,25)]
assert [seeds[2]['cells'][j]['TH'] for j in (0,1)]==[Q(43,20),Q(11,5)]
assert Q(43,20)<Q(87,40)<Q(11,5)
for z in seeds:
    assert z['cells'][0]['hard_stocks']==(Q(5,2),Q(5,2)) and z['cells'][1]['hard_stocks']==(Q(3),Q(3))
# Small smooth diagnostic using Decimal, independent raw hulls/source plans.
def dec(x):return D(x.numerator)/D(x.denominator) if isinstance(x,Q) else D(x)
def smooth(z,r,k,b,delta):
    def H(x):return (x+(x*x+delta*delta).sqrt())/2
    return r*z+k*(H(z-b)-H(-b))
def smoothprime(z,r,k,b,delta):
    x=z-b;return r+k*(1+x/(x*x+delta*delta).sqrt())/2

def smooth_min(knots,operation,r,k,b,delta):
    # Each operation segment is linear; zero total slope is solved by bisection.
    vals=[(operation(x)+smooth(x,r,k,b,delta),x) for x in knots]
    for l,h in zip(knots,knots[1:]):
        slope=(operation(h)-operation(l))/(h-l)
        if slope+smoothprime(l,r,k,b,delta)<0<slope+smoothprime(h,r,k,b,delta):
            lo,hi=l,h
            for _ in range(150):
                mid=(lo+hi)/2
                if slope+smoothprime(mid,r,k,b,delta)<0:lo=mid
                else:hi=mid
            x=(lo+hi)/2;vals.append((operation(x)+smooth(x,r,k,b,delta),x))
    return min(vals)
sm=[]
with localcontext() as ctx:
    ctx.prec=65
    r,k,b=map(dec,(Q(3,5),Q(1,5),Q(11,5)))
    for dq in (Q(1,100),Q(1,10)):
        delta=dec(dq);eps=k*delta/2;vals=[]
        for j in (0,1):
            hardvals=[]
            for name,hist in menu():
                knots=sorted({max(t for p,t,l in hist)}|{t+x for p,t,l in hist for x,c in acts(j) if t+x>=max(t for p,t,l in hist)})
                def op(B):return D(10)+sum(dec(p)*(dec(t+l)+dec(raw_rec(Q(B)-t,j)[0])) for p,t,l in hist)
                zz=smooth_min(list(map(dec,knots)),op,r,k,b,delta);hardvals.append((zz[0],name,zz[1]))
            hardbest=min(hardvals)
            assert hardbest[1]==CP
            def rop(B):return D(10)+dec(raw_rec(Q(B)-Q(1,10),j)[0])
            repair=smooth_min(list(map(dec,[Q(1,10),Q(11,10),Q(21,10)])),rop,r,k,b,delta)[0]
            # Expected lower hull of all raw columns, including cross-source chords.
            zz=sorted(set((t,v) for t,v,*_ in columns(j)));hull=[]
            for z in zz:
                if hull and z[0]==hull[-1][0]:continue
                while len(hull)>=2 and (hull[-1][0]-hull[-2][0])*(z[1]-hull[-1][1]) <= (hull[-1][1]-hull[-2][1])*(z[0]-hull[-1][0]):hull.pop()
                hull.append(z)
            ex=[]
            for (t,v),(tt,vv) in zip(hull,hull[1:]):
                def eo(B):return dec(v)+(B-dec(t))*dec((vv-v)/(tt-t))
                ex.append(smooth_min([dec(t),dec(tt)],eo,r,k,b,delta)[0])
            expected=min(ex)
            closedvals=[dec(seeds[2]['cells'][j][key]) for key in ('U','R_pre_fee','E')]
            for z,z0 in zip((hardbest[0],repair,expected),closedvals):assert abs(z-z0)<=eps+D('1e-40')
            vals.append({'hard':hardbest[0],'hard_stock':hardbest[2],'repair':repair,'expected':expected})
        ih=vals[1]['hard']-vals[1]['repair']-vals[0]['hard']+vals[0]['repair']
        assert ih>0 and abs(ih-D('0.05'))<=2*k*delta
        fee=D(87)/40;assert vals[0]['hard']-vals[0]['repair']<fee<vals[1]['hard']-vals[1]['repair']
        # Independent checks of uniform error and slope bounds at designated points.
        for Bq in (Q(0),Q(1,10),Q(11,10),Q(21,10),Q(11,5),Q(5,2),Q(3),Q(10)):
            B=dec(Bq);err=smooth(B,r,k,b,delta)-dec(C(Bq,Q(3,5),Q(1,5),Q(11,5)))
            assert abs(err)<=eps and r<smoothprime(B,r,k,b,delta)<r+k
        assert smooth(D(0),r,k,b,delta)==0
        ie=vals[1]['expected']-vals[1]['repair']-vals[0]['expected']+vals[0]['repair']
        assert abs(ie-D('0.2'))<=2*k*delta
        for j in (0,1):
            for name,key in [('hard','TH'),('expected','TE')]:
                assert abs(vals[j][name]-vals[j]['repair']-dec(seeds[2]['cells'][j][key]))<=k*delta
        sm.append({'delta':dq,'epsilon':eps,'IH_smooth':ih,'IE_smooth':ie,'cells':vals})
# Eight closed-box primitive corners diagnose the analytic open neighborhood.
primitive=[]
for q,y,a in product((Q(49,100),Q(51,100)),(Q(49,100),Q(51,100)),(Q(99,100),Q(101,100))):
    r,k,b,h=Q(3,5),Q(1,5),Q(11,5),Q(1,10)
    assert y*(q+3)<10*q and 1+q*y+3*(1+y)<20*q
    vals=[]
    for j in (0,1):
        pp=acts(j,a+1)
        def rc(x):
            zz=[c for t,c in pp if t<=x]
            for (t,c),(tt,cc) in combinations(pp,2):
                if t!=tt and min(t,tt)<=x<=max(t,tt):
                    w=(x-tt)/(t-tt);zz.append(w*c+(1-w)*cc)
            return min(zz)
        plans=[('N',[(Q(1),Q(0),20*q)]),('C2',[(1-q,Q(1),Q(0)),(q,Q(1),Q(10))])]
        for clean,fault in product((0,1),('N','P','C')):
            t=1+(y if fault=='P' else 1 if fault=='C' else 0)
            plans.append((f'C1_clean{clean}_fault{fault}',[(1-q,Q(1+clean),Q(0)),(q,t,Q(10) if fault=='N' else Q(0))]))
        vv=[]
        for name,hist in plans:
            low=max(t for p,t,l in hist)
            cuts={low,b}|{t+x for p,t,l in hist for x,c in pp if t+x>=low}
            choices=[(10+C(B,r,k,b)+sum(p*(t+l+rc(B-t)) for p,t,l in hist),B) for B in cuts if B>=low]
            v=min(x[0] for x in choices);bs=sorted(B for x,B in choices if x==v);vv.append((v,name,bs))
        v,name,bs=min(vv);assert name==CP and bs==[Q(3) if j else 2+y]
        rep=10+(1-a if j else 1)+C(h+(2 if j else 1),r,k,b)
        vals.append(v-rep)
    assert vals[0]<Q(87,40)<vals[1]
    assert vals[1]-vals[0]==q*a*y-r*y+k*(1-y)>0
    primitive.append({'q':q,'gamma':y,'S':a+1,'TH':vals})

OUT.mkdir(exist_ok=True)
(OUT/'capacity_supply.json').write_text(json.dumps(encode({'status':'synthetic exact targeted validation','counts':counts,'groups':records,'selected_witnesses':seeds,'smooth_diagnostics':sm,'primitive_box_corner_checks':primitive,'smooth_status':'Decimal 65-digit diagnostics, not exact algebra or empirical data'}),indent=2)+'\n')
print(json.dumps(counts,sort_keys=True));print('R7 raw-history/occupation-hull and smooth-cost checks PASS')
