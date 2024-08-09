import sqlite3
import re

db = sqlite3.connect('userBirth.db')
c = db.cursor()
#creating table
#c.execute("""CREATE TABLE dates (
#           date text
#          )""")

#inserting date
#c.execute("INSERT INTO dates VALUES ('26052011')")
#c.execute("UPDATE dates SET date = '26.05.2011'")
def getBirthDate(tableName, columnName):
    c.execute("SELECT " + columnName + " FROM " + tableName)

    print(c.fetchall())

def createBirthDate(tableName, newDate):
    c.execute("INSERT INTO " +  tableName + " VALUES ('" + newDate + "')")
    c.execute("SELECT date FROM " + tableName)
    print("Successfully did - now you have: " + str(c.fetchall()))
    
    
print("Hello, I am database controller, what do you need?")
print("Print '1' to get Birth date or '2' to create Birth date")
chose = int(input())
if chose == 1:
    tableName = str(input("What table do you need? "))
    columnName = str(input("What column do you need? "))
    getBirthDate(tableName, columnName)
elif chose == 2:
    tableName = str(input("What table do you need? "))
    newDate = str(input("What date do you want to insert? "))
    createBirthDate(tableName, str(newDate))





db.commit()
db.close()