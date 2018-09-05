import csv
import numpy as np

def nGetNames(ChainFile):
    if isinstance(ChainFile,(list,np.ndarray)):
        result=GetNames(ChainFile[0])
        return(result)
    with open(ChainFile, newline='') as csvfile:
        NameReader=csv.reader(csvfile)
        result=next(NameReader)
    return(result)


def nGetParamValues(FileName, ParamName,burn=0,nthin=None):
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
           x=np.append(x,GetParamValues(fname, ParamName,burn=burn,nthin=None))
         
         result=thin(x,nthin)
         return(result)
     
     #Single node, single file
     with open(FileName, newline='') as csvfile:
        NameReader=csv.reader(csvfile)
        AllNames=next(NameReader)
        index=AllNames.index(ParamName)
        x=[float(row[index]) for row in NameReader]
        
        #Apply the burn-in     
        x=x[burn:]    
        
        #thin results
        result=thin(x,nthin)
        return(result)
def thin(x,nthin):
	if nthin==None:return(x)
	n=len(x)
	if nthin>=n:return(x)
	ithin=range(nthin)
	idelta=float(n)/float(nthin)
	iuse=list(map(lambda i:int(i*idelta),ithin))
	result=list(map(lambda i:x[i],iuse))
	return(result)	
 
def GetParamStats(FileName, ParamName,burn=0):
	"Generate statistics for a parameter saved in a hdf5 file"
	
	xarray=GetParamValues(FileName, ParamName,burn=burn)
	n = len(xarray)
	if not n:
	    print ('Cannot generate statistics for zero-length xarray in', ParamName)
	    return
	 

	try:
	    xquantiles=mquantile(xarray,qlist=[.025,.52,.5,.75,.975])
	    #xhpd=hpd(xarray, .05)
	    return {
		'n': n,
		'standard deviation': xarray.std(0),
		'mean': xarray.mean(0) ,
		#'%s%s HPD interval' % (int(100*(.95)),'%'): xhpd,
		'mc error': xarray.std(0) / sqrt(n)  ,
		'quantiles': xquantiles
	    }
	except:
	    print ('Could not generate output statistics for', ParamName)   
if __name__ == "__main__":
    
    ChainFile='D:\Analyses\Long-Lived-pymc3\TreeNob1875XDate\MCMC.20180510\chain-0.csv'  
    ParamNames=GetNames(ChainFile)
    LogRecruit__90=GetParamValues(ChainFile, 'LogRecruit__90',burn=0,nthin=None)
    ChainFile=[ChainFile,'D:\Analyses\Long-Lived-pymc3\TreeNob1875XDate\MCMC.20180511\chain-0.csv']
    ParamName=['LogRecruit__4','LogRecruit__100']
    test1=GetParamValues(ChainFile, ParamName,burn=0,nthin=None)    
    test2=GetParamValues(ChainFile, ParamName,burn=500,nthin=None)
    test3=GetParamValues(ChainFile, ParamName,burn=500,nthin=1000)
    print(len(test1))
    print(len(test1[0]))
    print(len(test2[1]))
    print(len(test3[1]))