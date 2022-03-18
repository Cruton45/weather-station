from dataBaseHandler import *


def logData():
    allEntry = getAllEntries()

    numbOfEntries = len(allEntry)

    i = 0

    dataFile = open("weatherData","w+")

    dataFile.write("ID, DATE, LOWTEMP, AVGTEMP, HIGHTEMP, LOWRHP, AVGRHP, HIGHRHP, LOWMB, AVGMB, HIGHMB\n")

    while( i <= (numbOfEntries - 1) ):
    
        stringData = str(allEntry[i])
    
        dataFile.write( "%s\n" % stringData )
    
        i = i + 1
    
    
    dataFile.close()
    
logData()