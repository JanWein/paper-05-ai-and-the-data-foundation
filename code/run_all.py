"""Run the complete synthetic reproduction suite without external services."""
import subprocess
import sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for script in ('lineage_information.py','check_lineage_raw.py','capacity_supply.py','capacity_procurement.py','granularity.py','pathwise.py','adaptive.py','reproduce.py','test_field_estimator.py'):
    subprocess.run([sys.executable,str(root/'code'/script)],cwd=root,check=True)
