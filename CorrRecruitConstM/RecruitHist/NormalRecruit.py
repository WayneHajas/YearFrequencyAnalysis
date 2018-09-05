
from scipy.stats.mstats import mquantiles
import sys
sys.path.append('..\\..\\')
from WriteNormalRecruit import WriteNormalRecruit
from GetParamStats import GetParamValues

sys.path.append( '..\\'  ) 
from hdf5file import hdf5file,burn,nthin

NewFile='../NormRecruit.csv'
WriteNormalRecruit(hdf5file,burn=burn,NewFile=NewFile,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980)


lnM=GetParamValues(hdf5file, 'lnM',burn=burn)
lnMq=mquantiles(lnM,prob=[1/3,2/3])

NewFile='../NormRecruit_lowM.csv'
WriteNormalRecruit(hdf5file,burn=burn,NewFile=NewFile,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980,lnMupp=lnMq[0])

NewFile='../NormRecruit_midM.csv'
WriteNormalRecruit(hdf5file,burn=burn,NewFile=NewFile,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980,lnMlow=lnMq[0],lnMupp=lnMq[1])

NewFile='../NormRecruit_uppM.csv'
WriteNormalRecruit(hdf5file,burn=burn,NewFile=NewFile,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980,lnMlow=lnMq[1])
