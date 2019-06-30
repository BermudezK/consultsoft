import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host='localhost',
  user='jessica',
  passwd='morena2019',
  port='3306',
  auth_plugin='mysql_native_password',
  database='clinica'
)