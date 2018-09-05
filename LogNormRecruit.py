'''
20180510
Class to represent lognormal,recruitment. No Autocorrelation
The mortality model will be incorporated into a larger model through multiple inheritiance.

Requirements from some other contributing class:
    *self.nyear
    *self.MinYear
Required variable that must be generated:
    *self.LogRecruit
        From oldest to youngest, the log of the relative amount of recruitment that happened for each year-class
2018-08-15
    Fix first LogRecruit to zero.  To help manage the range of LogRecruit values
    Adjust the prior for lnSigmaRecruit so it is approximately equivalent to autocorrelated lognormal.
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
                
        #Standard deviation of recruitment rate
        self.lnSigmaRecruit=Normal('lnSigmaRecruit',3.0000078167376,0.20387959628544947)
        self.tauRecruit=Lambda('tauRecruit',lambda t=self.lnSigmaRecruit:np.exp(-2*t))
        
        #Fix first LogRecruit to zero.
        self.LogRecruit   =[Lambda('LogRecruit_'+str(self.MinYear),lambda t=self.lnSigmaRecruit:0,trace=True)]
        self.LogRecruit+=[  Normal('LogRecruit_'+str(self.MinYear+y),0,self.tauRecruit ) for y in range(1,self.nyear)]
    