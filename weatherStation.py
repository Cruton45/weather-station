import bme280
import smbus2
from time import sleep
import datetime
from datetime import date
from dataBaseHandler import *

import os
import sys



port = 1
address = 0x77
bus = smbus2.SMBus(port)
    
bme280.load_calibration_params(bus, address)
    

def receiveData():
    
    bme280_data = bme280.sample(bus, address)
    dataTable = [0,0,0]
    temp = bme280_data.temperature
    
    rhp = bme280_data.humidity
    mb = bme280_data.pressure
    
    dataTable[0] = temp
    dataTable[1] = rhp
    dataTable[2] = mb
    
    return dataTable

def submitData( d, lt, at, ht, lrhp, arhp, hrhp, lmb, amb, hmb):
    
    addData( d, lt, at, ht, lrhp, arhp, hrhp, lmb, amb, hmb)
    python = sys.executable
    os.execl(python, python, *sys.argv)    
    


def analyze(lpin):
    
    bme280_data = bme280.sample(bus, address)
    
    loopInit = lpin
    # Temp Vars
    LOWTEMP = bme280_data.temperature
    AVGTEMP = 0
    HIGHTEMP = bme280_data.temperature
        
    # Humidity Vars (RHP stands for relative humidity percentage)
    LOWRHP = bme280_data.humidity
    AVGRHP = 0
    HIGHRHP = bme280_data.humidity
        
    # Atmospheric Presure Vars(mb means millibars)
    LOWMB = bme280_data.pressure
    AVGMB = 0
    HIGHMB = bme280_data.pressure
    
    
    runTime = datetime.datetime.now()
    
    today = runTime.today()
    
    date = today.strftime("%b-%d-%Y")    
    
    print("Today is: ", today)    
    
    runDay = runTime.day
    curDay = runTime.day    
    
    while( loopInit == 1 and runDay == curDay ):
        
        curTime = datetime.datetime.now()
        curDay = curTime.day    
        
        dataTable = receiveData()
        
        if( dataTable[0] < LOWTEMP ):
            
            LOWTEMP = dataTable[0]
        
        elif( dataTable[0] > HIGHTEMP):
            
            HIGHTEMP = dataTable[0]
            
        
        if ( dataTable[1] < LOWRHP ):
            
            LOWRHP = dataTable[1]
            
            
        elif ( dataTable[1] > HIGHRHP):
            
            HIGHRHP = dataTable[1]
            
        
        if ( dataTable[2] < LOWMB ):
            
            LOWMB = dataTable[2]
            
        
        elif ( dataTable[2] > HIGHMB ):
            
            HIGHMB = dataTable[2]
        
        print(LOWTEMP, HIGHTEMP, LOWRHP, HIGHRHP, LOWMB, HIGHMB)
        
        sleep(1)
        
        AVGTEMP = ((LOWTEMP + HIGHTEMP) / 2)
        
        AVGRHP = ((LOWRHP + HIGHRHP) / 2)
        
        AVGMB = ((LOWMB + HIGHMB) / 2 )
        
    submitData(date, LOWTEMP, AVGTEMP, HIGHTEMP, LOWRHP, AVGRHP, HIGHRHP, LOWMB, AVGMB, HIGHMB)


analyze(1)




    

   
