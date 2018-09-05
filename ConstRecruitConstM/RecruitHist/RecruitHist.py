import matplotlib.pyplot as plt
from scipy.stats.mstats import mquantiles

import sys
sys.path.append('D:\\Analyses\\Long-Lived-pymc3\\TreeNob1875XDate')
from GetParamStats import GetParamValues,GetNames


CaseName='..\\NormRecruit.csv'
MinYear=1875
MaxYear=1980
year=range(MinYear,1+MaxYear)

sys.path.append( '..\\'  ) 
nthin=200000
pname=['NormRecruit_'+str(y)   for y in range(MinYear,1+MaxYear)]
quantile=[.025,.5,.975]

def GenCB(p):
    x=GetParamValues(CaseName, p,nthin=nthin)
    cb=mquantiles(x,prob=quantile)
    return(cb)
CB=[ GenCB(p)  for p in pname]

uppbnd=[t[-1]  for t in CB]
lowbnd=[t[ 0]  for t in CB]

plt.fill_between(year,lowbnd,uppbnd, color='r',alpha=0.25)
plt.yscale('log')
plt.xlim(MinYear-5,MaxYear+5)
plt.plot([MinYear,MaxYear],[1,1],'k-')
plt.title('Recruitment History Estimated from FA3')
plt.xlabel('Year Class')
plt.ylabel('Normalized Recruitment Rate')
plt.ylim(1/150,150)

plt.savefig('FA3_RecruitHistoryl.png', format="png")
plt.show()