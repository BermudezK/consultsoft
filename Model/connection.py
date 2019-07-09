import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(  
  host='127.0.0.1',
  user='root',
  passwd='38382454',
  port='3306',
  auth_plugin='mysql_native_password',
  database='clinica'
)

def select_personal(rol):
    try:
        if mydb.is_connected():
            cursor = mydb.cursor()
            consulta = 'SELECT personal_DNI,nombre, apellido, telefono FROM personal WHERE rol_id = {rol};'
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            cursor.close()
