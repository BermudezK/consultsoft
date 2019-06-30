import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='1234',
  database='clinica'
)