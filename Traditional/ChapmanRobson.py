

from numpy import exp
import sys
from numpy import exp
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
na0=sum(data)
a0=0
abar=sum([ i*data[i]    for i in range(nyear)])/na0

sCR=(abar-a0)/  ( (abar-a0) +(na0-1)/na0    )
zCR=-log(sCR)
zCRc=zCR- (na0-1)*(na0-2) / na0 / ( na0*(na0*(abar-a0)+1) ) / (na0 + na0*(na0*(abar-a0)-1) )
zCRcSigma=((1-exp(-zCRc))**2)/na0/exp(-zCRc)
print(-2*zCRcSigma + zCRc  ,0*zCRcSigma + zCRc  ,+2*zCRcSigma + zCRc    )