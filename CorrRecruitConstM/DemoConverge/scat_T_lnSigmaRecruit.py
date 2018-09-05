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

T=GetParamValues(hdf5file, 'T',burn=burn,nthin=nthin)
lnSigmaRecruit=GetParamValues(hdf5file, 'lnSigmaRecruit',burn=burn,nthin=nthin)

plt.close()
plt.plot(T,lnSigmaRecruit,'k*')
plt.xlabel('T')
plt.ylabel('lnSigmaRecruit')
plt.savefig('scat_T_lnSigmaRecruit.png', format="png")
plt.show()
