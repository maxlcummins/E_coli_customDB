#!/Users/maxcummins/miniconda2/envs/py36ipy/bin/python

#used to edit headers of customDB_Feb_2018.fasta to make them compatible with ARIBAlord

import re
with open('../E_coli_customDB/EC_customDB.fasta', 'r+' ) as f:
    f = f.read()
f = re.sub('(>[^:]+):(.*)', r'\1_\2', f)
f = re.sub('insertion_', '', f)

print(f)
