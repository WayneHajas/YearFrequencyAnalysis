

import sys
from numpy.random import seed
seed(756)
sys.path.append('..\\')
from  GetAgeFreq import GetAgeFreq

from numpy import log,ndarray,array

import statsmodels.api as sm
from scipy import stats
csvfile='..\\TreeNobXdate.csv'
col=0#Use first column from file
SurveyYear=2005
MaxYear=1980
MinYear=1875

#Generate an age-frequency.  Oldest-ages first
data=GetAgeFreq(csvfile,col=col,SurveyYear=SurveyYear,MaxYear=MaxYear,MinYear=MinYear)
nyear=len(data)

#Add a column of ones to represent the constant
yb=array([array([int(1),int(t)]) for t in range(nyear)])

glm=sm.GLM(data,yb,family=sm.families.Poisson(),links=sm.families.links.Log())
print(glm.fit().summary())
print('#############')
groups=[t for t in range(nyear)]
MLM=sm.MixedLM(data,yb,groups=groups,family=sm.families.Poisson(),links=sm.families.links.Log())
print(MLM.fit().summary())
print('#############')