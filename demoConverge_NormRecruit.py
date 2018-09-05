import os
import sys

import csv
import sys
import matplotlib.pyplot as plt

sys.path.append('D:\\Analyses\\Long-Lived-pymc3\\TreeNob1875XDate')
from GetParamStats import GetParamValues,GetNames
from RunningQuantiles import pltRunningQuantile

from scipy.stats.mstats import mquantiles

CaseName='..\\NormRecruit.csv'
MinYear=1875
MaxYear=1980

sys.path.append( '..\\'  ) 
nthin=2000
pname=['NormRecruit_'+str(y)   for y in range(MinYear,1+MaxYear)]
quantile=[.025,.5,.975]



for p in pname:
      x=GetParamValues(CaseName, p,nthin=nthin)
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

