import os
import sys
import csv
import  numpy as np
import tables
from copy import copy
#from utils import hpd, quantiles
from scipy.stats.mstats import mquantiles
from scipy.stats import multinomial
from numpy import average,exp


def PredictAgeFreq(hdf5file,nAnimal,burn=0,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980):
    
    nyear=MaxYear-MinYear+1
    PredAgeFreq=[]
    for FileName in hdf5file:
        print(FileName)
        f=tables.open_file(FileName,mode='r+')
        nTable=len(f.list_nodes('/'))
	          #Names of tables
        curName='//chain0//PyMCsamples'
        try:
          curTable=f.get_node(curName)
        except:
          print('PredictAgeFreq 28 ',FileName)
          curTable=f.get_node(curName)

        i=0
        for t in curTable.iterrows():
            if i>=burn:
                  try:
                      LogRecruit=[t['LogRecruit_'+str(s)]  for s in range(MinYear,1+MaxYear)]
                  except:
                      LogRecruit=[t['LogRecruit'+str(s)]  for s in range(MinYear,1+MaxYear)]
                  lnM=t['lnM']
                  M=exp(lnM)
                  
                  #UnNormalized probabilities
                  UnNorm=[ exp(t+M*(y-nyear/2)) for y,t in enumerate(LogRecruit)]
                  NormProb=[t/sum(UnNorm)  for t in UnNorm]
                  
                  #Random Age Frequency
                  CurAgeFreq=list(multinomial(nAnimal, NormProb).rvs()[0])
                  PredAgeFreq+=[CurAgeFreq]  
                  i+=1 
                  
    #Quantiles on number of animals for every age-class
    qanimal=[ mquantiles( [t[i]  for t in PredAgeFreq],prob=quantile)   for i in range(nyear)]
      
    result={}
    for i,t in enumerate(quantile):
          result[t]=[s[i]   for s in qanimal]
    return(result)



if __name__ == "__main__":
    
  from numpy.random import seed
  seed(20180814)
  
  
  hdf5file=['CorrRecruit_narrowConstM.01/MCMC_20180511.hdf5']
  nAnimal=410
  test=PredictAgeFreq(hdf5file,nAnimal,burn=0,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980)  
