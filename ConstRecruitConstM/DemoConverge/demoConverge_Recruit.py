import os
import sys

import csv
import sys
import matplotlib.pyplot as plt
from numpy import average,exp

sys.path.append('..\\..\\')
from GetParamStats import GetParamValues,GetNames
from RunningQuantiles import pltRunningQuantile

from scipy.stats.mstats import mquantiles

sys.path.append( '..\\'  ) 
from hdf5file import hdf5file,burn,nthin
nthin=200
pname=GetNames(hdf5file)
quantile=[.025,.5,.975]

pname=['LogRecruit_'+str(y)  for y in range(1875,1981)]

LogRecruit=[ tuple(GetParamValues(hdf5file, pname,burn=burn,nthin=nthin)) for p in pname]

zlr=zip(*LogRecruit)

NormExp=[ [exp(s-average(r))  for s in r]     for r in zlr]

for y in range(1875,1981):
      x=NormExp[y-1875]
      print (y,len(x))
      plt.close()
      pltRunningQuantile(plt,x, prob=[.025,.975],LowCol='r',UppCol='b',alpha=0.25)
      plt.title('Recruit_'+str(y))
      plt.xlabel('Number of Iterations')
      plt.ylabel('Confidence Bounds')
      fname='Recruit_'+str(y)+'.png'
      plt.savefig(fname, format="png")

