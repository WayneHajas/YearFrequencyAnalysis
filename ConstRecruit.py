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
20180518
    Modified to give constant recruitment rates
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
        '''Log of Relative annual Recruitment.  Constant value for this model'''
        
        self.LogRecruit=numpy.empty(self.nyear,dtype=object)
        #Fix the first value in order to make the others more stable.  Everything will get normalized anyways.
        for y in range(self.nyear):
            self.LogRecruit[y]=Lambda('LogRecruit_'+str(self.MinYear+y),lambda t=0:0 )
    