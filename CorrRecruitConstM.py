'''
20180509
Model for estimating mortality rate and recruitment history from year-class-frequency
* Mortality rate is constant
* Annual recruitment is lognormally distributed with auto-correlation
* Multinomial distribution is used to simulate sampling
'''

from pymc import  *
from pylab import *
from tables import *
import tables
import warnings
warnings.filterwarnings('ignore', category=tables.NaturalNameWarning)

#This is where submodels are specified.  Mix and match as you see fit.
from ConstantMortality import Mortality
from AutoCorrelatedRecruit import Recruit
from Multinomial import SurveySampling

class CorrRecruitConstM(Mortality,Recruit,SurveySampling):
    
    def __init__(self, yearbornfrequency,MinYear=1875):	
      '''CorrRecruitConstM(yearbornfrequency,MinYear=1875)
      * yearbornfrequency is a list giving the number of animals from each year-class.  Oldest to youngest.
      MinYear is the year-born for the oldest year-class
      '''
      self.yearbornfrequency= yearbornfrequency
      self.MinYear=MinYear
    	#Number of years and animals
      self.nyear=len(yearbornfrequency)
      self.nanimal=sum(yearbornfrequency)
 
      #The values of yearborn
      self.YearBorn=[MinYear+i   for i in range(self.nyear)]
      self.MidYear=MinYear+.5*self.nyear
 
     #Inherited from Mortality-class
     #Generate array of ProbSurv-nodes to represent probability of survival until the survey for each of year-class
      self.Mortality()
     
     #Inherited from Recruitment-class
     #Generate array of LogRecruit-nodes to represent log of recruitment for each year-class
      self.Recruitment()
     
     #Inherited from SurveySampling-class
     #Generate array of LogProb-nodes to represent the log of the probability of appearing in the sample for each year-class
      self.CalcProbYearClass()
     
     #Inherited from SurveySampling-class
     #Assess data against the LogProb-nodes
      self.SampleAnimals()
     


#Test the function
if __name__ == "__main__":
    from  GetAgeFreq import GetAgeFreq
    csvfile='TreeNobXdate.csv'    
    yearbornfrequency=GetAgeFreq(csvfile,col=0,SurveyYear=2005,MaxYear=1980,MinYear=1875)
    test=CorrRecruitConstM(yearbornfrequency)