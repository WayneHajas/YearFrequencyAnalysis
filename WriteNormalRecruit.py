import os
import sys
import csv
import  numpy as np
import tables
from copy import copy
#from utils import hpd, quantiles
from scipy.stats.mstats import mquantiles
from numpy import average,exp


def WriteNormalRecruit(hdf5file,burn=0,NewFile='..\\NormRecruit.csv',quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980,lnMlow=None,lnMupp=None):
    
    
    OutName=['NormRecruit_'+str(y)   for y in range(MinYear,1+MaxYear)]
    with open(NewFile,'w',newline='') as csvout:
            outwriter = csv.writer(csvout, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            outwriter.writerow(OutName)
            for FileName in hdf5file:
                f=tables.open_file(FileName,mode='r+')
                nTable=len(f.list_nodes('/'))
    	          #Names of tables
                curName='//chain0//PyMCsamples'
                try:
                  curTable=f.get_node(curName)
                except:
                  print('WriteNormalRecruit 28 ',FileName)
                  curTable=f.get_node(curName)
    
                i=0                
                for t in curTable.iterrows():
                    curTable.iterrows()
                    use=(i>=burn)
                
                    lnM=t['lnM']
                    if (lnMlow and (lnM<lnMlow)):
                        use=False
                    if (lnMupp and (lnM>lnMupp)):
                        use=False
                    if (use):
                            try:
                              LogRecruit=[t['LogRecruit_'+str(s)]  for s in range(MinYear,1+MaxYear)]
                              NormRecruit=[ exp(r-average(LogRecruit))     for r in LogRecruit ]
                              outwriter.writerow(NormRecruit)
                            except:
                              print('writenormalrecruit 39 ', FileName)
                              LogRecruit=[t['LogRecruit'+str(s)]  for s in range(MinYear,1+MaxYear)]
                              NormRecruit=[ exp(r-average(LogRecruit))     for r in LogRecruit ]
                              outwriter.writerow(NormRecruit)

                    i+=1


if __name__ == "__main__":
    

  hdf5file=['CorrRecruit_narrowConstM.01/MCMC_20180511.hdf5',\
			'CorrRecruit_narrowConstM.01/MCMC_20180512.hdf5',\
			'CorrRecruit_narrowConstM.01/MCMC_20180513.hdf5']

  NewFile='CorrRecruit_narrowConstM.01/NormRecruit.csv'
  WriteNormalRecruit(hdf5file,burn=0,NewFile=NewFile,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980)