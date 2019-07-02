import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  passwd='1234',
#  port='33061',
#  auth_plugin='mysql_native_password',
  database='clinica'
)