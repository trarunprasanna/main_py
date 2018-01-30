import pyodbc
import numpy
import math
import time

connection = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                                'Server=LAPTOP;'
                                'Database=sample;'
                                'uid=user;pwd=Password')

cursor = connection.cursor()

cursor.execute("select * from stud")
data=cursor.fetchall()
print (data)