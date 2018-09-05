

import sys
sys.path.append('..\pyfunctions')
from numpy.random import seed
seed(756)
sys.path.append('..\\')
from  GetAgeFreq import GetAgeFreq

from numpy import log
from scipy.stats import linregress

csvfile='..\\TreeNobXdate.csv'
col=0#Use first column from file
SurveyYear=2005
MaxYear=1980
MinYear=1875


data=GetAgeFreq(csvfile,col=col,SurveyYear=SurveyYear,MaxYear=MaxYear,MinYear=MinYear)
nyear=len(data)
fudge=[.0001,.001,.01,.1,1]

year=[t for t in range(nyear)]

for t in fudge:
    lFA=[log(t+s) for s in data]
    print(t,linregress(year,lFA)[0],linregress(year,lFA)[-1] )
