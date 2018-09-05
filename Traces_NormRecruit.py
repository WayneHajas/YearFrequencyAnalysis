import sys
import matplotlib.pyplot as plt

sys.path.append('D:\\Analyses\\Long-Lived-pymc3\\TreeNob1875XDate')
from GetParamStats import GetParamValues,GetNames
from RunningQuantiles import pltRunningQuantile
sys.path.append( '../')   
sys.path.append( '../../')   


from HistoByHalf import HistoByHalf
CaseName='..\\NormRecruit.csv'

nthin=1000
burn=0

pname=GetNames(CaseName)


for p in pname:
      x=GetParamValues(CaseName, p,burn=burn,nthin=nthin)
      print (p,len(x))
      plt.close()
      HistoByHalf(plt,x, ParamName=p,LowCol='r',UppCol='b',alpha=0.25)
      if p[:7]=='Rel_Abu':
          plt.xlim(-.05,1.05)
      plt.xlabel('Number of Iterations')
      plt.ylabel('Confidence Bounds')
      fname='trace_'+p+'.png'
      plt.savefig(fname, format="png")

