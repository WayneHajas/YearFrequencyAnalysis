import matplotlib.pyplot as plt
from scipy.stats.mstats import mquantiles
import csv 

import sys
sys.path.append('..\\..\\')
from nGetParamStats import nGetParamValues as GetParamValues

OutFileName='NormRecuritCB.csv'
CaseName='..\\NormRecruit.csv'
MinYear=1875
MaxYear=1980
year=range(MinYear,1+MaxYear)

sys.path.append( '..\\'  ) 
nthin=200000
pname=['NormRecruit_'+str(y)   for y in range(MinYear,1+MaxYear)]
quantile=[.025,.5,.975]



outfile=csv.writer(open(OutFileName,'w'),lineterminator='\n')

for i in range(MaxYear-MinYear+1):
  pname='NormRecruit_'+str(MinYear+i)
  x=GetParamValues(CaseName, pname,nthin=nthin)
  curCB=list(mquantiles(x,prob=quantile))
  print(i,pname,curCB)
  outfile.writerow([pname]+curCB)
del(outfile)