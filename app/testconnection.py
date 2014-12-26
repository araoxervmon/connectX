__author__ = 'Abhilash'
import MySQLdb
import pymongo
import connections
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test
#cursor = conn.cursor()
#print cursor
#cursor.execute("SELECT * FROM users")
#row = cursor.fetchone()
print db
#client.close()
