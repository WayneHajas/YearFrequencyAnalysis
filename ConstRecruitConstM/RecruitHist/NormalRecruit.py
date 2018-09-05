import sys
sys.path.append('..\\..\\')
from WriteNormalRecruit import WriteNormalRecruit

sys.path.append( '..\\'  ) 
from hdf5file import hdf5file,burn

NewFile='../NormRecruit.csv'
WriteNormalRecruit(hdf5file,burn=0,NewFile=NewFile,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980)