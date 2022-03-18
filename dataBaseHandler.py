import sqlite3
from sqlite3 import Error

def dataBaseConnect():
    
    db_file = "WeatherDB.db"
    
    conn = sqlite3.connect(db_file) 
    return conn
    
def addData(d, lt, at, ht, lrhp, arhp, hrhp, lmb, amb, hmd):
    
    conn = dataBaseConnect()
    
    query = ''' INSERT INTO WEATHERDATA(Date,LOWTEMP,AVGTEMP,HIGHTEMP,LOWRHP,AVGRHP,HIGHRHP,LOWMB,AVGMB,HIGHMB) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    
    data = (d, lt, at, ht, lrhp, arhp, hrhp, lmb, amb, hmd)
    
    cur = conn.cursor()
    cur.execute(query, data)
    conn.commit()    

def getAllEntries():
    
    conn = dataBaseConnect()
    
    cur = conn.cursor()
    
    cur.execute('''SELECT * FROM WEATHERDATA''')
    
    rows = cur.fetchall()
    
    dataList = []
    
    i = 0
    
    for row in rows:
        
        dataList.insert(i, row)
        
        i = i + 1
        
    return dataList
