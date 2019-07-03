from Model.connection import mydb

def obtenerTurnos(desde, hasta):
    try:
        if mydb.is_connected():
            print(mydb)
            cursor = mydb.cursor()
            consulta = (f"""SELECT CAST(fecha_Hora as date) AS 'Dia', HOUR(CAST(fecha_Hora as time)) AS 'Hora', count(*) 'Total' FROM turno
                            WHERE fecha_Hora BETWEEN '{desde}' AND '{hasta}' AND estado = true
                            GROUP BY CAST(fecha_Hora as date), HOUR(CAST(fecha_Hora as time))
                            ORDER BY CAST(fecha_Hora as date), HOUR(CAST(fecha_Hora as time));
                        """)
                        
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            cursor.close()