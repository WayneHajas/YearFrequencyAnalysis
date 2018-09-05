from datetime import datetime
from numpy import ndarray,append
from numpy.random import seed

from pymc import  *
from pylab import *
from tables import *
import tables
import warnings
warnings.filterwarnings('ignore', category=tables.NaturalNameWarning)

        
def ExecuteModel(Model,Niter=11000,burn=1000,thin=10,basename='MCMC',db='hdf5',verbose=2,maxSimplex=0,maxPowell=0,rseed=756):

    #Set the random seed
    seed(rseed)
    
    #create the database name
    dbname=basename+'_'+str(rseed)

    N=MAP(Model)
    
    #If requested, find MAP-state for the model
    if maxSimplex>0:
       print('start Simplex ')
       N.fit(iterlim=maxSimplex,tol=1.0,verbose=verbose)
    if maxPowell>0:
       print('start powell ')
       N.fit('fmin_powell',iterlim=maxPowell,verbose=verbose)
      

    
    # Create MCMC object
    M = MCMC(Model,db=db,name=dbname)

    # Sample
    M.sample(Niter,burn=burn,thin=thin,verbose=verbose)



  
