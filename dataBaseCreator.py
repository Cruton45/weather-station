import sqlite3

conn = sqlite3.connect('WeatherDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved


c.execute('''CREATE TABLE WEATHERDATA
             ([generated_id] INTEGER PRIMARY KEY, [Date] text, [LOWTEMP] integer, [AVGTEMP] integer, [HIGHTEMP] integer, [LOWRHP] integer, [AVGRHP] integer, [HIGHRHP] integer, [LOWMB] integer, [AVGMB] integer, [HIGHMB] integer)''')
          
                 
conn.commit()

# Note that the syntax to create new tables should only be used once in the code (unless you dropped the table/s at the end of the code). 
# The [generated_id] column is used to set an auto-increment ID for each record
# When creating a new table, you can add both the field names as well as the field formats (e.g., Text)