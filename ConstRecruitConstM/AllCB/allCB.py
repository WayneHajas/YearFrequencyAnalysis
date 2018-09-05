import os
import sys
sys.path.append( '../')   
sys.path.append( '../../')   

import csv
from numpy import average,var
from GetParamStats import GetParamValues2 as GetParamValues
from GetParamStats import GetNames

from scipy.stats.mstats import mquantiles

from hdf5file import hdf5file,burn,nthin
pname=GetNames(hdf5file)


quantile=[.025,.5,.975]


outfile=csv.writer(open('allCB.csv','w'),lineterminator='\n')


for p in pname:
	x=GetParamValues(hdf5file, p,burn=burn,nthin=nthin)
	print (p,len(x),max(x))
	outfile.writerow(list([p]+list(mquantiles(x,prob=quantile))+[len(x)]))

D=GetParamValues(hdf5file, 'deviance',burn=burn,nthin=nthin)
pD=1/2*var(D)
DIC=pD + average(D)
outfile.writerow(['pD',pD])
outfile.writerow(['DIC',DIC])



del(outfile)