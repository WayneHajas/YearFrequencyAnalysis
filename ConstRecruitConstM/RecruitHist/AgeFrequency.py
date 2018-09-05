import sys
sys.path.append('..\\..\\')
from PredictAgeFreq import PredictAgeFreq
from  GetAgeFreq import GetAgeFreq



col=0
SurveyYear=2005
MaxYear=1980
MinYear=1875
yearborn=[y for y in range(MinYear,1+MaxYear)]
csvfile='../../TreeNobXdate.csv'     
yearbornfrequency=GetAgeFreq(csvfile,col=col,SurveyYear=SurveyYear,MaxYear=MaxYear,MinYear=MinYear)


nAnimal=sum(yearbornfrequency)
import matplotlib.pyplot as plt
plt.close()
plt.plot(yearborn,yearbornfrequency,'k*',0.25)
plt.title('Geoduck Age Frequency')
plt.xlabel('Year Class')
plt.ylabel('Number of Geoducks')
plt.xlim(1870,1985)
plt.ylim(-1,40)

plt.savefig('AgeFrequency.png', format="png")
plt.show()