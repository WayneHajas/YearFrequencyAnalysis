import sys
sys.path.append('..\\..\\')
from PredictAgeFreq import PredictAgeFreq
from  GetAgeFreq import GetAgeFreq

sys.path.append( '..\\'  ) 
from hdf5file import hdf5file,burn

from numpy.random import seed
seed(20180814)

col=0
SurveyYear=2005
MaxYear=1980
MinYear=1875
yearborn=[y for y in range(MinYear,1+MaxYear)]
csvfile='../../TreeNobXdate.csv'     
yearbornfrequency=GetAgeFreq(csvfile,col=col,SurveyYear=SurveyYear,MaxYear=MaxYear,MinYear=MinYear)


nAnimal=sum(yearbornfrequency)
CB=PredictAgeFreq(hdf5file,nAnimal,burn=0,quantile=[.025,.5,.975],MinYear=1875,MaxYear=1980)  

import matplotlib.pyplot as plt
plt.close()
plt.plot(yearborn,yearbornfrequency,'k*')
plt.fill_between(yearborn,CB[.025],CB[.975],color='r',alpha=0.25)
#plt.plot(yearborn,CB[.025],'r-',linewidth=3,alpha=0.25)
plt.plot(yearborn,CB[.5  ],'g-',linewidth=3,alpha=0.25)
#plt.plot(yearborn,CB[.975],'r-',linewidth=3,alpha=0.25)
plt.title('FA1 Model Predictions')
plt.xlabel('Year Class')
plt.ylabel('Number of Geoducks')
plt.xlim(1870,1985)
plt.ylim(-2,60)
star=plt.plot([0,0],[0,0],'k*')
shade=plt.plot([0,0],[0,0],'r-',linewidth=6,alpha=0.25)
plt.legend((star[0],shade[0]),('Data Values','Predicted Values\n(95% Credibility Interval)'),title=15*'-'+'Age Frequency'+15*'-',numpoints=1,loc=2)
plt.savefig('PredictData.png', format="png")
plt.show()