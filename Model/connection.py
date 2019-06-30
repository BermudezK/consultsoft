import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  passwd='147852',
  port='3306',
  auth_plugin='mysql_native_password',
  database='clinica'
)