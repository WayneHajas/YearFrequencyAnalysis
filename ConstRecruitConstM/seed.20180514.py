'''
20180514  Create Model and generate MCMC
'''

import sys
sys.path.append('../')
from  GetAgeFreq import GetAgeFreq
from ConstRecruitConstM import ConstRecruitConstM
from ExecuteModel import ExecuteModel   
   
#Get the YearBornFrequency as a list  
col=0
SurveyYear=2005
MaxYear=1980
MinYear=1875
csvfile='../TreeNobXdate.csv'     
yearbornfrequency=GetAgeFreq(csvfile,col=col,SurveyYear=SurveyYear,MaxYear=MaxYear,MinYear=MinYear)

#Create the model
Model=ConstRecruitConstM(yearbornfrequency,MinYear=MinYear)

#Generate the MCMC
ExecuteModel(Model,Niter=1100000,burn=100000,thin=100,basename='MCMC',db='hdf5',verbose=2,maxSimplex=0,maxPowell=0,rseed=20180514)