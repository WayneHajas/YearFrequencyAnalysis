


import os
import sys
import csv
import  numpy as np
from pymc import  *
from pylab import *
import tables
from copy import copy
#from utils import hpd, quantiles
from scipy.stats.mstats import mquantiles
from numpy import average,exp


sys.path.append( '..\\'  ) 
from hdf5file import hdf5file
nthin=2000000
burn=0
quantile=[.025,.5,.975]

NewFile='..\\NormRecruit.csv'
MinYear=1875
MaxYear=1980
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
            curTable=f.get_node(curName)

            for i in range(burn):
                curTable.iterrows()
            for t in curTable.iterrows():
                    LogRecruit=[t['LogRecruit_'+str(s)]  for s in range(MinYear,1+MaxYear)]
                    NormRecruit=[ exp(r-average(LogRecruit))     for r in LogRecruit ]
                    outwriter.writerow(NormRecruit)