"""Explicitly synthetic software fixture; NOT an experimental estimate."""
from field_estimator import analyze
from itertools import product
from pathlib import Path
import json
rows=[]
for j,(a,d) in enumerate(list(product((0,1),repeat=2))*2):
 rows.append(dict(pool_id=f'SYNTHETIC_{j}',block='b0',A=a,D=d,
                  task_count=12,total_Y=-100+3*j+5*a+8*d+4*a*d,frame_frozen=1))
r=analyze(rows);assert r['pools']==8 and r['assignment_space']==2520
assert 0<=r['global_sharp_null_p']<=1
assert abs(r['ITT_interaction']-4/12)<1e-12
for bad in ([],rows+rows[:1]):
 try:analyze(bad)
 except ValueError:pass
 else:raise AssertionError('Invalid input accepted')
r['evidence_status']='SYNTHETIC SOFTWARE TEST ONLY'
out=Path(__file__).resolve().parents[1]/'results'
(out/'synthetic_estimator_test.json').write_text(json.dumps(r,indent=2))
print('Pool estimator synthetic test PASS; exact assignment enumeration 2520.')
