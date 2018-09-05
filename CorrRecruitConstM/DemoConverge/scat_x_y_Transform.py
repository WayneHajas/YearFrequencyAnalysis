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

xTransform=GetParamValues(hdf5file, 'xTransform',burn=burn,nthin=nthin)
yTransform=GetParamValues(hdf5file, 'yTransform',burn=burn,nthin=nthin)

plt.close()
plt.plot(xTransform,yTransform,'k*')
plt.xlabel('xTransform')
plt.ylabel('yTransform')
plt.savefig('scat_x_y_Transform.png', format="png")
plt.show()
