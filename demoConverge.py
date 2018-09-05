import os
import sys

import csv
import sys
import matplotlib.pyplot as plt

sys.path.append('..\\..\\')
from GetParamStats import GetParamValues,GetNames
from RunningQuantiles import pltRunningQuantile

from scipy.stats.mstats import mquantiles

sys.path.append( '..\\'  ) 
from hdf5file import hdf5file,burn,nthin
nthin=2000
pname=GetNames(hdf5file)
quantile=[.025,.5,.975]



for p in pname:
      x=GetParamValues(hdf5file, p,burn=burn,nthin=nthin)
      print (p,len(x))
      plt.close()
      pltRunningQuantile(plt,x, prob=[.025,.975],LowCol='r',UppCol='b',alpha=0.25)
      plt.title(p)
      plt.xlabel('Number of Iterations')
      plt.ylabel('Confidence Bounds')
      if p[:9]=='Rel_Abund':
          plt.ylim(-.05,1.05)
      fname=p+'.png'
      plt.savefig(fname, format="png")

