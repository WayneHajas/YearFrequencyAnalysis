'''
20180510  Library for taking values from pymc/hdf5 files.
Results from multiple hdf5 values can be combined
'''


import os
import sys
import  numpy as np
from pymc import  *
from pylab import *
import tables
from copy import copy
#from utils import hpd, quantiles
from scipy.stats.mstats import mquantiles



def GetParamValues(FileName, ParamName,burn=0,nthin=None):
     '''Get parameter values saved in a hdf5 file.  
     *FileName is the full name of the file.
     *ParamName is the name(s) of the node(s)
     *first burn of the iterations stored in the file are ignored
     *results to be reduced to nthin evenly spaced values'''
     
     #check for multiple nodes
     if isinstance(ParamName,(list,np.ndarray)):
         result=[ GetParamValues(FileName, p,burn=burn,nthin=nthin)  for p in ParamName]
         return(result)
         
     #Check for multiple input files
     if isinstance(FileName,(list,np.ndarray)):
         x=np.ndarray(0,dtype=float)
         for fname in FileName:
           #burn is applied to both chains
           x=append(x,GetParamValues(fname, ParamName,burn=burn,nthin=None))
         
         n=len(x)
     
         #No thinning to do     
         if not(nthin) or (nthin>=n):
           return(x)
     
         result=[ x[int(i*(n-1)/(nthin-1))]      for i in range(nthin)]     
         return(result)
     
     #Single node, single file
     #open file and get all values
     f=pymc.database.hdf5.load(FileName)
     x=f.trace(ParamName)[:]
     n=len(x)
     
     #burn-in not achieved
     if burn>n:
         return([])
     
    #Apply the burn-in     
     x=x[burn:]     
     n=len(x)
     #No thinning to do     
     if not(nthin) or (nthin>=n):
         return(x)
     
     result=[ x[int(i*(n-1)/(nthin-1))]      for i in range(nthin)]     
     return(result)
     
     
def GetParamValues2(FileName, ParamName,burn=0,nthin=None):
     '''Get parameter values saved in a hdf5 file.  
     Use Table-library directly and avoid pymc code.
     
     *FileName is the full name of the file.
     *ParamName is the name(s) of the node(s)
     *first burn of the iterations stored in the file are ignored
     *results to be reduced to nthin evenly spaced values'''
     
     #check for multiple nodes
     if isinstance(ParamName,(list,np.ndarray)):
         result=[ GetParamValues2(FileName, p,burn=burn,nthin=nthin)  for p in ParamName]
         return(result)
         
     #Check for multiple input files
     if isinstance(FileName,(list,np.ndarray)):
         x=np.ndarray(0,dtype=float)
         for fname in FileName:
           #burn is applied to both chains
           x=append(x,GetParamValues2(fname, ParamName,burn=burn,nthin=None))
         
         n=len(x)
     
         #No thinning to do     
         if not(nthin) or (nthin>=n):
           return(x)
     
         result=[ x[int(i*(n-1)/(nthin-1))]      for i in range(nthin)]     
         return(result)
     
     #Single node, single file
     #open file and get all values
     result=OldGetParamValues(FileName, ParamName,burn=burn,nthin=nthin)
     
     return(result)
     
def OldGetParamValues(FileName, ParamName,burn=0,nthin=None):
	'''Get parameter values saved in a hdf5 file.  Chains are appended one after the other.
       Use Table-library directly and avoid pymc code.'''
	
	f=tables.open_file(FileName,mode='r+')

	nTable=len(f.list_nodes('/'))
	
	#Names of tables
	curName='//chain0//PyMCsamples'

	curTable=f.get_node(curName)
	values=curTable.col(ParamName)

	f.close()
	xarray = np.array(values[burn:], float)
	result=thin(xarray,nthin)
	del (f)
	return (result)

    


def GetNames(FileName):
    
    #Check for multiple input files
    if isinstance(FileName,(list,np.ndarray)):
        result=GetNames(FileName[0])
        return(result)
    
    #open file
    db=pymc.database.hdf5.load(FileName)
    
    #Get the names
    AllName=[t for t in  db.trace_names[-1]   if t[:11]!= 'Metropolis_']   
    
    #Sort the names - ignoring case
    AllName.sort(key=lambda s: s.lower())
    del (db)
    return(AllName)




def thin(x,nthin):
	if nthin==None:return(x)
	n=len(x)
	if nthin>=n:return(x)
	result=[ x[int((i+.5)*n/nthin)]      for i in range(nthin)] 
	return(result)



def GetSumParamValues(FileName, PreFix,burn=0,nthin=None):
    nPrefix=len(PreFix)
    pname=GetNames(FileName)
    pname=list(filter(lambda p:p[:nPrefix]==PreFix,pname))
    AllValues=list(map(lambda p: GetParamValues(FileName, p,burn=burn,nthin=nthin)   ,pname))
    nparam=len(pname)
    niter=len(AllValues[0])
    result=list(map(lambda i:sum( list(map(lambda t:t[i],AllValues))) ,range(niter)))
    return(result)



if __name__ == "__main__":
    
    import os
    import sys
    os.chdir('Q:/analyses/CrossDating/ModelsAndFunctions')
    sys.path.append('Q:/analyses/CrossDating/ModelsAndFunctions')
    import tables
    
    FileName="Q:/analyses/CrossDating/Barkley/Ring/AutoCorrRecruit/4plus.140/MCMC.hdf5"
    FileName="Q:/analyses/CrossDating/Barkley/Ring/AutoCorrRecruit/4plus/MCMC.hdf5"
    ParamName="Mort"
    x=GetParamStats(FileName, ParamName)
    print (x)
    
    

