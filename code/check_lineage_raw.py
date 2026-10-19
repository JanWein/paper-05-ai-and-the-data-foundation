"""Second standalone R8 checker. No imports of any model/verifier modules.
Independent raw-state conditional minimization of every root source mask,
including both full-price prior replacements and symmetric cheap coverage.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
out=Path(__file__).resolve().parents[1]/'results'
p=F(1,10);v=F(3,10);d=F(1);fee=F(9,50);K=F(21,200);saving=F(9,100)
count=0;rows=[]
def value(mask,info,W,p1=p,p2=p,pi=F(1,2)):
    global count
    states=[]
    for j,a,b in product((0,1),repeat=3):
        prob=(pi if j==0 else 1-pi)*(p1 if a else 1-p1)*(p2 if b else 1-p2)
        bad=(a if j==0 else b) if not (mask&(1<<j)) else 0
        states.append((j,a,b,bad,prob))
    before=lambda s:s[0] if info=='early' else -1
    after=lambda s,yes:(s[0] if info!='opaque' else -1,s[3] if yes else -1)
    val=F(0)
    for first in set(before(s) for s in states):
        block=[s for s in states if before(s)==first];c=[]
        for yes in (False,True):
            t=sum(s[-1]*v*yes for s in block)
            for observed in set(after(s,yes) for s in block):
                at=[s for s in block if after(s,yes)==observed]
                t+=min(sum(s[-1]*(d*m.bit_count()+W*s[3]*(not(m&(1<<s[0])))) for s in at) for m in range(4))
                count+=1
            c.append(t)
        val+=min(c)
    return val
for A,W in enumerate((F(9,2),F(8))):
    for mask,info in product(range(4),('opaque','late','early')):
        z=value(mask,info,W)
        root=(fee if mask&1 else 0)+(d if mask&2 else 0)
        assert mask.bit_count()+1+2<=5<6
        rows.append({'A':A,'mask':mask,'information':info,'operating':str(z),'full_price_root_total':str(root+z+(K if info=='early' else 0)-A*saving)})
    assert value(2,'early',W)==value(1,'early',W)
    assert value(3,'opaque',W)==0
    for info in ('opaque','late','early'):
        assert fee+value(1,info,W)<fee+d+value(3,info,W)
# Independent perturbations of the two priors and routing, not a new fitted model.
perturb=[]
for p1,p2,pi in product((F(999,10000),F(1001,10000)),(F(999,10000),F(1001,10000)),(F(4999,10000),F(5001,10000))):
    candidates=[]
    for A,mask,P in product(range(2),range(4),range(2)):
        W=(F(9,2),F(8))[A];op=value(mask,'early' if P else 'opaque',W,p1,p2,pi)
        root=(fee if mask&1 else 0)+(d if mask&2 else 0)
        candidates.append((root+P*K+op-A*saving,A,mask,P))
    assert min(candidates)[1:]==(1,1,1)
    assert min(x for x in candidates if x[3]==0)[1:]==(0,1,0)
    perturb.append([str(p1),str(p2),str(pi)])
# All early/late/opaque operating cells of the independent main witness must match.
data=json.loads((out/'lineage_information.json').read_text())
for row in rows:
    if row['mask'] in (0,1):
        assert F(row['operating'])==F(data['root_witness']['cells'][row['A']][f"{row['mask']}_{row['information']}"]['cost'])
result={'status':'synthetic second-checker PASS','conditional_terminal_minima':count,'root_mask_information_cells':len(rows),'asymmetric_prior_routing_cases':len(perturb),'rows':rows,'perturbations':perturb}
(out/'lineage_raw_check.json').write_text(json.dumps(result,indent=2)+'\n')
print('Second independent raw-state information/root-mask checker PASS:',count,'conditional minima;',len(perturb),'asymmetry cases')
