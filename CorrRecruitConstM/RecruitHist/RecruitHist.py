import matplotlib.pyplot as plt
from scipy.stats.mstats import mquantiles

import sys
sys.path.append('..//..//')
from nGetParamStats import nGetParamValues,nGetNames


CaseName='..\\NormRecruit.csv'
MinYear=1875
MaxYear=1980
year=range(MinYear,1+MaxYear)

sys.path.append( '..\\'  ) 
from hdf5file import hdf5file,burn
nthin=200000
pname=['NormRecruit_'+str(y)   for y in range(MinYear,1+MaxYear)]
quantile=[.025,.5,.975]

def GenCB(p):
    x=nGetParamValues(CaseName, p,nthin=nthin)
    cb=mquantiles(x,prob=quantile)
    return(cb)
CB=[ GenCB(p)  for p in pname]

uppbnd=[t[-1]  for t in CB]
lowbnd=[t[ 0]  for t in CB]
medrec=[t[ 1]  for t in CB]

plt.fill_between(year,lowbnd,uppbnd, color='r',alpha=0.25)
plt.plot(year,medrec,'r-',alpha=0.25,linewidth=3)
plt.yscale('log')
plt.xlim(MinYear-5,MaxYear+5)
plt.plot([MinYear,MaxYear],[1,1],'k-')
plt.title('Recruitment History Estimated from FA3')
plt.xlabel('Year Class')
plt.ylabel('Normalized Recruitment Rate')
plt.ylim(1/500,500)

plt.savefig('FA3_RecruitHistoryl.png', format="png")
plt.show()