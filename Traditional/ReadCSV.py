#run q:/analyses/mortalityestimates/pyfunctions/readcsv
from numpy import *
import csv

def GetCSV(filename,YearSurvey,MinYear=None,MaxYear=1980,NameRow=0,column=0):


    data=[]
    reader=csv.reader(open(filename))
      #read in the columnth column
    for row in reader:
        data+=[row[column]]
    
    #get rid of the column header
    data=data[NameRow:] 
      
    #convert ages to year-born   
    YearBorn=[YearSurvey-int(d) for d in data]
    YearBorn.sort()
      
     #Number of year-classes      
    nyear=MaxYear-MinYear+1
    
    YearBorn=[yb for yb in YearBorn if yb<=MaxYear] #Remove year-class that are too young
    if MinYear:
        YearBorn=[yb for yb in YearBorn if yb>=MinYear] #Remove year-class that are too old
        nyear=MaxYear-MinYear+1
        
      
    #Build age-frequency
    AF=nyear*[0]
    for yb in YearBorn:
          AF[yb-MinYear]+=1

    return(AF)  
    
if __name__ == "__main__":


 
    filename='D:\\Analyses\\Long-lived-mortality redux\\NeatMCMC\\TreeNobXdate.csv'
    column=0
    NameRow=1
    YearSurvey=2005
    MaxYear=1980
    MinYear=1875
    x1=GetCSV(filename,YearSurvey,MinYear=MinYear,MaxYear=MaxYear,NameRow=NameRow,column=0)
    x2=GetCSV(filename,YearSurvey,MinYear=MinYear,MaxYear=MaxYear,NameRow=NameRow,column=1)
