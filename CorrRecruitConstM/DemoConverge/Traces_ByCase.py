import sys
import matplotlib.pyplot as plt
sys.path.append( '../')   
sys.path.append( '../../')   




from GetParamStats import GetParamValues2 as GetParamValues
from GetParamStats import GetNames
from HistoByHalf import HistoByHalf

from hdf5file import hdf5file,burn,nthin
nthin=None

pname=['deviance','yTransform','Omega','LogRecruit1880','LogRecruit1893','lnSigmaRecruit','T']

for hf in hdf5file:
    rs=hf[-13:-5]

    for p in pname:
      try:
        x=GetParamValues(hf, p,burn=burn,nthin=nthin)
      except:
        print('Traces_ByCase 25 ',hf,p)
        x=GetParamValues(hf, p,burn=burn,nthin=nthin)
      print (p,len(x))
      if len(x)>0:
          plt.close()
          HistoByHalf(plt,x, ParamName=p,LowCol='r',UppCol='b',alpha=0.25)
          if p[:7]=='Rel_Abu':
              plt.xlim(-.05,1.05)
          plt.xlabel('Number of Iterations')
          plt.ylabel('Confidence Bounds')
          fname='trace_ByCase_'+p+'_'+rs+'.png'
          plt.savefig(fname, format="png")


for p in pname:
  try:
    x=GetParamValues(hdf5file, p,burn=burn,nthin=nthin)
  except:
    print('Traces_ByCase 25 ',hf,p)
    x=GetParamValues(hf, p,burn=burn,nthin=nthin)
  print (p,len(x))
  plt.close()
  HistoByHalf(plt,x, ParamName=p,LowCol='r',UppCol='b',alpha=0.25)
  if p[:7]=='Rel_Abu':
      plt.xlim(-.05,1.05)
  plt.xlabel('Number of Iterations')
  plt.ylabel('Confidence Bounds')
  fname='trace_ByCase_'+p+'.png'
  plt.savefig(fname, format="png")