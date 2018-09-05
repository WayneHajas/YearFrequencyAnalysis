import os
import sys
sys.path.append( '../../'  ) 

import csv
import sys
import matplotlib.pyplot as plt
from numpy import array
from pymc import  *

import pickle

from GetParamStats import GetParamValues as GetParamValues
from GetParamStats import GetNames

sys.path.append( '..\\'  ) 
from hdf5file import hdf5file,burn,nthin


pname=GetNames(hdf5file)

def apply_gr(hdf5file,p,burn=0,nthin=None):
    x=[GetParamValues(h, p,burn=burn,nthin=nthin)  for h in hdf5file]
    x=[t for t in x if len(t)>1000]
    n=min([len(t) for t in x])
    x=[t[:n] for t in x]
    result=gelman_rubin(x)
    return(result)


outfile=csv.writer(open('gelman_rubin.csv','w'),lineterminator='\n')
outfile.writerow(['Parameter','R-hat'])

for p in pname:
      if p[:10]!='Rel_Abund_':
          gr=apply_gr(hdf5file, p,burn=burn,nthin=nthin)
          print (p,gr)
          outfile.writerow([p,gr])

del (outfile)