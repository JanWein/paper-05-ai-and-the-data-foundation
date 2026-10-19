"""Prospective pool-randomized estimator. Runnable, no empirical observations supplied.
Input is one JSON row per independent reference pool with its fixed task count
and complete operational net-value total. The randomization test is for the
GLOBAL SHARP NULL of no effect on any pool, not the weak null of zero interaction.
"""
import argparse,json,itertools,math,random
from pathlib import Path
from scipy.stats import t as student_t
LABELS=((0,0),(1,0),(0,1),(1,1));SIGNS=(1,-1,-1,1)
def analyze(rows,seed=505,draws=9999,exact_limit=20000):
 if not rows:raise ValueError('No authorized pool data supplied')
 needed={'pool_id','block','A','D','task_count','total_Y','frame_frozen'}
 if any(not needed<=set(r) for r in rows):raise ValueError('Missing pool fields')
 if len({r['pool_id'] for r in rows})!=len(rows):raise ValueError('Duplicated pools')
 if any(r['frame_frozen']!=1 or not math.isfinite(r['total_Y']) or r['task_count']<=0
        or (r['A'],r['D']) not in LABELS for r in rows):raise ValueError('Invalid or incomplete frame')
 blocks={b:[r for r in rows if r['block']==b] for b in sorted(set(r['block'] for r in rows))}
 for rr in blocks.values():
  counts=[sum((r['A'],r['D'])==c for r in rr) for c in LABELS]
  if min(counts)<2 or len(set(counts))!=1:raise ValueError('Requires balanced blocks with >=2 pools per cell')
 N=sum(r['task_count'] for r in rows)
 means=[sum(4*r['total_Y'] for r in rows if (r['A'],r['D'])==c)/N for c in LABELS]
 delta=sum(s*m for s,m in zip(SIGNS,means));variance=0.
 for rr in blocks.values():
  K=len(rr)
  for c in LABELS:
   yy=[r['total_Y'] for r in rr if (r['A'],r['D'])==c];m=len(yy);av=sum(yy)/m
   sample_var=sum((y-av)**2 for y in yy)/(m-1)
   variance+=(K/N)**2*sample_var/m
 se=math.sqrt(variance);df=len(rows)-4*len(blocks)
 crit=float(student_t.ppf(.975,df));ci=[delta-crit*se,delta+crit*se]
 # Restricted assignment space: equal cell counts in every block.
 assignments_count=math.prod(math.factorial(len(rr))//math.factorial(len(rr)//4)**4 for rr in blocks.values())
 def assignments(rr):
  ids=tuple(range(len(rr)));m=len(rr)//4
  for a in itertools.combinations(ids,m):
   rem1=tuple(x for x in ids if x not in a)
   for bb in itertools.combinations(rem1,m):
    rem2=tuple(x for x in rem1 if x not in bb)
    for cc in itertools.combinations(rem2,m):
     dd=tuple(x for x in rem2 if x not in cc)
     yield (a,bb,cc,dd)
 def stat(rr,groups):
  return 4*sum(sign*sum(rr[i]['total_Y'] for i in gg) for sign,gg in zip(SIGNS,groups))/N
 if assignments_count<=exact_limit:
  stats=[0.]
  for rr in blocks.values():
   one=[stat(rr,g) for g in assignments(rr)]
   stats=[x+y for x in stats for y in one]
  pval=sum(abs(x)>=abs(delta)-1e-12 for x in stats)/len(stats);method='exhaustive global-sharp-null'
 else:
  rng=random.Random(seed);extreme=0
  for _ in range(draws):
   val=0.
   for rr in blocks.values():
    ids=list(range(len(rr)));rng.shuffle(ids);m=len(rr)//4
    val+=stat(rr,[ids[j*m:(j+1)*m] for j in range(4)])
   extreme+=abs(val)>=abs(delta)-1e-12
  pval=(extreme+1)/(draws+1);method='Monte Carlo global-sharp-null with plus-one correction'
 return dict(task_count=N,pools=len(rows),cell_means=dict(zip(['00','10','01','11'],means)),
  ITT_interaction=delta,conservative_Neyman_SE=se,approximate_t95=ci,approximate_df=df,
  global_sharp_null_p=pval,randomization_method=method,assignment_space=assignments_count,
  warning='Randomization p is NOT an exact test of zero factorial interaction allowing main effects.')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('pool_json');ap.add_argument('--seed',type=int,default=505)
 args=ap.parse_args();print(json.dumps(analyze(json.loads(Path(args.pool_json).read_text()),seed=args.seed),indent=2))
