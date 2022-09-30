import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234567890", database="rec_unit") #establish connection with DBMS

mycursor = mydb.cursor()

'''
mycursor.execute("CREATE DATABASE rec_unit") #create database

mycursor.execute("SHOW DATABASES") # get the names of databases

for db in mycursor:
    print(db) # output names of databases
'''

'''
mycursor.execute("CREATE TABLE REC_OF_UNITS (rooms VARCHAR(10), jan_22 INTEGER(10))") #create a table in DB

mycursor.execute("SHOW TABLES") # get names of tables in DB
for tb in mycursor: # print names of tables in DB
    print(tb)
'''

'''
# insert a values in table using execute ony
sqlFormula = "INSERT INTO rec_of_units (rooms, jan_22) VALUES (%s, %s)"
room1 = ("room1", 0)
mycursor.execute(sqlFormula, room1)

mydb.commit()
'''

'''
# insert many values in table using array -> list & executemany
sqlFormula = "INSERT INTO rec_of_units (rooms, jan_22) VALUES (%s, %s)"
rooms = [("room2", 0),
         ("room3", 0),
         ("room4", 0),
         ("room5", 0)]
mycursor.executemany(sqlFormula, rooms)

mydb.commit()
'''
'''
# get and print all values form table
mycursor.execute("SELECT * FROM rec_of_units")

myresult = mycursor.fetchall() # <--- important

for row in myresult:
    print(row)
'''

'''
# get and print a column values form table
mycursor.execute("SELECT rooms FROM rec_of_units")

myresult = mycursor.fetchall() # <--- important

for row in myresult:
    print(row)
'''
'''
#get and print only one row
mycursor.execute("SELECT rooms FROM rec_of_units")

myresult = mycursor.fetchone() # <--- important

for row in myresult:
    print(row)
'''
'''#get and print only rows that satisfies the condition
mycursor.execute("SELECT * FROM rec_of_units WHERE rooms='room1'")

myresult = mycursor.fetchall() # <--- important

for row in myresult:
    print(row)
'''

'''
#get and print only rows in which rooms name is room1
sql = "SELECT * FROM rec_of_units WHERE rooms = %s"
mycursor.execute(sql, ("room1", ))  # secure way of applying value using %s

myresult = mycursor.fetchall()  # <--- important

for row in myresult:
    print(row)
'''

'''
# Update a data in table
sql = "UPDATE rec_of_units SET jan_22 = 1 WHERE rooms = 'room1'"
mycursor.execute(sql)  # secure way of applying value using %s
mydb.commit()

sql = "SELECT * FROM rec_of_units"
mycursor.execute(sql)
myresult = mycursor.fetchall()  # <--- important

for row in myresult:
    print(row)
'''
'''
# limit and off the output
sql = "SELECT * FROM rec_of_units LIMIT 2" # gets only 2 rows/ results
sql = "SELECT * FROM rec_of_units LIMIT 2 offset 2" # gets only 2 rows/ results after offsetting 2 results/ rows
mycursor.execute(sql)
myresult = mycursor.fetchall()  # <--- important

for result in myresult:
    print(result)
'''

sql = "SELECT * FROM rec_of_units ORDER BY rooms"
sql = "SELECT * FROM rec_of_units ORDER BY jan_22 DESC"
sql = "SELECT * FROM rec_of_units ORDER BY jan_22 ASC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)