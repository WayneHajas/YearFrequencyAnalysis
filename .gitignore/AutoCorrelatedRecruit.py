'''
20180510
Class to represent lognormal, auto-correlated recruitment.
The mortality model will be incorporated into a larger model through multiple inheritiance.

Requirements from some other contributing class:
    *self.nyear
    *self.MinYear
Required variable that must be generated:
    *self.LogRecruit
        From oldest to youngest, the log of the relative amount of recruitment that happened for each year-class
2018-05-18
  Linear transformed T and lnSigmaRecruit to x and y.  x and y should be orthogopnal
2018-08-13
    Changed definition of Omega to be consistent with documentation.
2018-08-15
    Adjust prior on  xTransform to widen effective prior on ro
'''


from pymc import  *
from pylab import *
from tables import *
import tables
import warnings
warnings.filterwarnings('ignore', category=tables.NaturalNameWarning)
import numpy as np
from scipy.special import expit

class Recruit():
    def Recruitment(self):	
        '''Log of Relative annual Recruitment'''
        
        #Dummy variables to help the convergence of T and lnSigmaRecruit
        self.xTransform=Normal('xTransform',0,0.05)
        self.yTransform=Normal('yTransform',0,0.057120)
        
        #Standard deviation of recruitment rate
        self.lnSigmaRecruit=Lambda('lnSigmaRecruit',lambda x=self.xTransform,y=self.yTransform:3+.36207*x-.36207*y)
		
        #Will be subjected to antiLogit transformation
        self.T=Lambda('T',lambda x=self.xTransform,y=self.yTransform:7+.84483*x+.15517*y)
        #Coefficient for autocorrelation
        self.Ro=Lambda('Ro',lambda t=self.T:expit(t))
		
	  #Between-year variability in log-Recruitment
        self.Omega=Lambda('Omega',lambda ro=self.Ro,lnSigmaRecruit=self.lnSigmaRecruit:np.exp(lnSigmaRecruit)*np.sqrt(1-ro*ro))
        self.tauOmega=Lambda('tauOmega',lambda t=self.Omega:1./t/t)
        
        
        self.LogRecruit=numpy.empty(self.nyear,dtype=object)
        #Fix the first value in order to make the others more stable.  Everything will get normalized anyways.
        self.LogRecruit[0]=Lambda('LogRecruit'+str(self.MinYear),lambda t=self.xTransform:0,trace=True)
        for y in range(1,self.nyear):
            self.LogRecruit[y]=Normal('LogRecruit'+str(self.MinYear+y),self.Ro*self.LogRecruit[y-1],self.tauOmega,trace=True )
    
    