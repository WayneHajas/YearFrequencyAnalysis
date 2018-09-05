'''
20180510
Class to represent survey-sampling as a multi-nomial distribution.
The mortality model will be incorporated into a larger model through multiple inheritiance.

Requirements from some other contributing class:
    *self.nyear
    *self.MinYear
    *self.ProbSurv
    *self.LogRecruit
        From oldest to youngest, the log of the relative amount of recruitment that happened for each year-class
    *self.ProbSurv
        From oldest to youngest, the probability an animals from a year-class will survive until the survey
Required variable that must be generated:
    *none
'''


from pymc import  *
from pylab import *
from tables import *
import tables
import warnings
warnings.filterwarnings('ignore', category=tables.NaturalNameWarning)
import numpy as np
from scipy.special import expit
import WCHmultinomial 

class SurveySampling():    
    def CalcProbYearClass(self):	
        '''
        Use the recruitment rates and probability-of-survival-to-survey to calculate the probablity of a year-class in the sameple
        '''
        #Unnormalized probabilities
        self.UnnormalizedProb=[Lambda('UnnormalizedProb'+str(self.MinYear+i),lambda x=self.ProbSurv[i],y=self.LogRecruit[i]:x*np.exp(y),trace=False  )   \
                              for i in range(self.nyear)]
        
        self.LogSumUnnormalizedProb=Lambda('LogSumUnnormalizedProb',lambda x=self.UnnormalizedProb:np.log(sum(x)),trace=False)
        
        self.LogProb=[Lambda('LogProb_'+str(self.MinYear+i),\
            lambda s=self.UnnormalizedProb[i],t=self.LogSumUnnormalizedProb:np.log(s)-t,trace=False)   for i in range(self.nyear)]

    def SampleAnimals(self):	
        #Apply the multinomial distribution
        self.ObsVal=WCHmultinomial.WCHMulti('ObsVal',array(self.yearbornfrequency),self.LogProb)
