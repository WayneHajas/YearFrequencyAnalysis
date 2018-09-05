import matplotlib.pyplot as plt
from scipy.stats.mstats import mquantiles

import sys
sys.path.append('..\\..\\')
from GetParamStats import GetParamValues
#Function to get recruit-values from .csv vile
from nGetParamStats import nGetParamValues 
sys.path.append('..\\')
from hdf5file import *
lnM=GetParamValues(hdf5file, 'lnM',nthin=nthin)
del(GetParamValues)



def GenCB(CaseName,p):
    x=nGetParamValues(CaseName, p,nthin=nthin)
    cb=mquantiles(x,prob=quantile)
    return(cb)
    
MinYear=1875
MaxYear=1980
year=range(MinYear,1+MaxYear)

pname=['NormRecruit_'+str(y)   for y in range(MinYear,1+MaxYear)]
quantile=[.025,.5,.975]

CaseName='..\\NormRecruit_lowM.csv'
CB=[ GenCB(CaseName,p)  for p in pname]
uppbnd=[t[-1]  for t in CB]
lowbnd=[t[ 0]  for t in CB]
medrec=[t[ 1]  for t in CB]
lowM=plt.fill_between(year,lowbnd,uppbnd,  edgecolor='r',alpha=0.75,hatch='x',facecolor='none',linewidth=3)

CaseName='..\\NormRecruit_midM.csv'
CB=[ GenCB(CaseName,p)  for p in pname]
uppbnd=[t[-1]  for t in CB]
lowbnd=[t[ 0]  for t in CB]
medrec=[t[ 1]  for t in CB]
midM=plt.fill_between(year,lowbnd,uppbnd,  color='k'          ,alpha=0.25,                     linewidth=3)

CaseName='..\\NormRecruit_uppM.csv'
CB=[ GenCB(CaseName,p)  for p in pname]
uppbnd=[t[-1]  for t in CB]
lowbnd=[t[ 0]  for t in CB]
medrec=[t[ 1]  for t in CB]
uppM=plt.fill_between(year,lowbnd,uppbnd,  edgecolor='b',alpha=0.75,hatch='*',facecolor='none',linewidth=3)
plt.yscale('log')
plt.xlim(MinYear-5,MaxYear+5)
plt.plot([-MinYear,2*MaxYear],[1,1],'k-')
plt.title('Recruitment History Estimated from FA3')
plt.xlabel('Year Class')
plt.ylabel('Normalized Recruitment Rate')
plt.ylim(1/1000,1000)

import matplotlib.patches as mpatches
upppatch=mpatches.Patch(edgecolor='b',alpha=0.75,hatch='*',facecolor='white',linewidth=3,label='High')
midpatch=mpatches.Patch(color='k'          ,alpha=0.25,                      linewidth=3,label='Medium')
lowpatch=mpatches.Patch(edgecolor='r',alpha=0.75,hatch='x',facecolor='white',linewidth=3,label='Low')
plt.legend(handles=[upppatch,midpatch,lowpatch],title='Mortality Level')

plt.savefig('FA3_TriPlot.png', format="png")
plt.show()