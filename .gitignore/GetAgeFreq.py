'''
20180509 library to read age values from .csv file and convert them to a year-class-frequency
'''

import csv

def GetAgeFreq(csvfile,col=0,SurveyYear=2005,MaxYear=1980,MinYear=1875):
    '''
    csvfile is the name of the file
    col is the column to look at in the file
    SurveyYear is the date the shells were collected
    MaxYear and MinYear indicate the range of year-classes to create
    '''
    #open the file    
    reader=csv.reader(open(csvfile))
    
    #extract the age-values from the correct column
    age=[t[col] for t in reader]

    #Convert age to year-born 
    yb=[SurveyYear-int(t) for t in age[1:]]
    
    #Create list to contain values
    result=[0 for t in range(MinYear,MaxYear+1) ]
    
    #If year-born is withing the range, increment the number of animals for the corresponding year-class
    for t in yb:
        if(t>=MinYear) and (t<=MaxYear):
          result[t-MinYear]+=1
    
    return(result)

#Test the function
if __name__ == "__main__":
    
    csvfile='TreeNobXdate.csv'    
    test=GetAgeFreq(csvfile,col=0,SurveyYear=2005,MaxYear=1980,MinYear=1875)
    print(test)
    