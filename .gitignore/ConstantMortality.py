'''
20180510
Class to represent a constant mortality rate.
The mortality model will be incorporated into a larger model through multiple inheritiance.

Requirements from some other contributing class:
    *self.MidYear
    *self.YearBorn
Required variable that must be generated:
    *self.ProbSurv
        From oldest to youngest, the probability an animals from a year-class will survive until the survey
'''


from pymc import  *
from pylab import *
from tables import *
import tables
import warnings
warnings.filterwarnings('ignore', category=tables.NaturalNameWarning)
import numpy as np

class Mortality():
     
    def Mortality(self):	
        #The instantaneous mortality rate
        self.lnM=Normal('lnM',-3.8,1 )
        self.M=Lambda('M',lambda t=self.lnM:np.exp(t))
        
        #The probablility an animal from a year-class survives to the survey
        #Values only have to be proportional.
        #Use MidYear to keep values near one
        self.ProbSurv=[ Lambda('ProbSurv_'+str(y),lambda y=y,M=self.M,MidYear=self.MidYear:np.exp(M*(y-MidYear)),trace=False)  for y in self.YearBorn]