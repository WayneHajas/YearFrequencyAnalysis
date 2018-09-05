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


CaseName='..\\NormRecruit.csv'
MinYear=1875
MaxYear=1980
year=range(MinYear,1+MaxYear)

pname=['NormRecruit_'+str(y)   for y in range(MinYear,1+MaxYear)]
quantile=[.025,.5,.975]


def GenCB(p,M):
    x=nGetParamValues(CaseName, p,nthin=nthin)
    n=len(x)
    z=(M,x)
    z2=zip(*z)
    z3=list(z2)
    z3.sort()
    
    r0=[z3[i][-1]  for i in range(int(  n/3)) ]
    r1=[z3[i][-1]  for i in range(int(  n/3),int(2*n/3)) ]
    r2=[z3[i][-1]  for i in range(int(2*n/3),n) ]
    
    cb=[mquantiles(r0,prob=quantile), mquantiles(r1,prob=quantile), mquantiles(r2,prob=quantile)]
    return(cb)
CB=[ GenCB(p,lnM)  for p in pname]

uppbnd0=[t[0][-1]  for t in CB]
lowbnd0=[t[0][ 0]  for t in CB]
uppbnd1=[t[1][-1]  for t in CB]
lowbnd1=[t[1][ 0]  for t in CB]
uppbnd2=[t[2][-1]  for t in CB]
lowbnd2=[t[2][ 0]  for t in CB]

lowM=plt.fill_between(year,lowbnd0,uppbnd0,  edgecolor='r',alpha=0.75,hatch='x',facecolor='none',linewidth=3)
midM=plt.fill_between(year,lowbnd1,uppbnd1,  color='k'          ,alpha=0.25,                     linewidth=3)
uppM=plt.fill_between(year,lowbnd2,uppbnd2,  edgecolor='b',alpha=0.75,hatch='*',facecolor='none',linewidth=3)
plt.yscale('log')
plt.xlim(MinYear-5,MaxYear+5)
plt.plot([MinYear,MaxYear],[1,1],'k-')
plt.title('Recruitment History Estimated from FA3')
plt.xlabel('Year Class')
plt.ylabel('Normalized Recruitment Rate')
plt.ylim(1/500,500)

import matplotlib.patches as mpatches
upppatch=mpatches.Patch(edgecolor='b',alpha=0.75,hatch='*',facecolor='white',linewidth=3,label='High')
midpatch=mpatches.Patch(color='k'          ,alpha=0.25,                      linewidth=3,label='Medium')
lowpatch=mpatches.Patch(edgecolor='r',alpha=0.75,hatch='x',facecolor='white',linewidth=3,label='Low')
plt.legend(handles=[upppatch,midpatch,lowpatch],title='Mortality Level')

plt.savefig('FA3_TriPlot.png', format="png")
plt.show()