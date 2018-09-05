import sys
import matplotlib.pyplot as plt
sys.path.append( '../')   
sys.path.append( '../../')   




from GetParamStats import GetParamValues2 as GetParamValues
from GetParamStats import GetNames
from HistoByHalf import HistoByHalf
from hdf5file import hdf5file,burn,nthin

from hdf5file import hdf5file,burn,nthin
nthin=1000

pname=GetNames(hdf5file)


for p in pname:
      x=GetParamValues(hdf5file, p,burn=burn,nthin=nthin)
      print (p,len(x))
      plt.close()
      HistoByHalf(plt,x, ParamName=p,LowCol='r',UppCol='b',alpha=0.25)
      if p[:7]=='Rel_Abu':
          plt.xlim(-.05,1.05)
      plt.xlabel('Number of Iterations')
      plt.ylabel('Confidence Bounds')
      fname='trace_'+p+'.png'
      plt.savefig(fname, format="png")

