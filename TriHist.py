import matplotlib.pyplot as plt
from scipy.stats.mstats import mquantiles
from numpy import exp

import sys
sys.path.append('..\\..\\')
from GetParamStats import GetParamValues2 as GetParamValues
#Function to get recruit-values from .csv vile
from nGetParamStats import nGetParamValues 
sys.path.append('..\\')
from hdf5file import *
nthin=2000
lnM=GetParamValues(hdf5file, 'lnM',nthin=nthin)

lnM.sort()
n=len(lnM)
lowM=[exp(lnM[i]) for i in range(int(  n/3))   ]
medM=[exp(lnM[i]) for i in range(int(  n/3),int(2*n/3))  ]
uppM=[exp(lnM[i]) for i in range(int(2*n/3),n)   ]
bins=[0.004*i  for i in range(1+int(0.16/0.004))]
plt.close()

plt.hist(lowM,bins=bins,edgecolor='r',alpha=0.75,hatch='x',facecolor='none',linewidth=3)
plt.hist(medM,bins=bins,color='k'          ,alpha=0.25,                     linewidth=3)
plt.hist(uppM,bins=bins,edgecolor='b',alpha=0.75,hatch='*',facecolor='none',linewidth=3)



plt.title('FA3 Mortality Levels')
plt.xlabel('Natural Mortality Rate (year'+r'$-1$'+')')
plt.ylabel('Frequency')

import matplotlib.patches as mpatches
upppatch=mpatches.Patch(edgecolor='b',alpha=0.75,hatch='*',facecolor='white',linewidth=3,label='High')
midpatch=mpatches.Patch(color='k'          ,alpha=0.25,                                 label='Medium')
lowpatch=mpatches.Patch(edgecolor='r',alpha=0.75,hatch='x',facecolor='white',linewidth=3,label='Low')
plt.legend(handles=[upppatch,midpatch,lowpatch],title='Mortality Level')
plt.xlim(0,0.16)

plt.savefig('FA3_TriHist.png', format="png")
plt.show()