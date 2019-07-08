from Model.connection import mydb
from mysql.connector import Error
import time

fechaActual = time.strftime("%Y-%m-%d %H:%M:%S")

def cargar_turnos():
	cursor = mydb.cursor()
	consulta = """SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true
	order by T.fecha_hora"""
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

def filtrar_por_turno(id_Turno):
	cursor = mydb.cursor()
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true and T.turno_ID ={id_Turno} and T.fecha_hora >= "{fechaActual}" """)
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

def filtrar_por_paciente(nombre_paciente):
	cursor = mydb.cursor()
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true and concat(PS.nombre,', ', PS.apellido) like "%{nombre_paciente}%" and T.fecha_hora >= "{fechaActual}"
	order by T.fecha_hora""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

def filtrar_por_medico(nombre_medico):
	cursor = mydb.cursor()
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true and concat(P.nombre,', ', P.apellido) like "%{nombre_medico}%" and T.fecha_hora >= "{fechaActual}"
	order by concat(P.nombre,', ', P.apellido), T.fecha_hora ASC""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

def filtrar_por_fecha(fechabuscada):
	cursor = mydb.cursor()
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where fecha_Hora between "{fechabuscada}" and "{fechabuscada}" + interval 1 day
	order by T.fecha_hora ASC""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

def filtrar_por_fechaHora(fechaHora):
	cursor = mydb.cursor()
	consulta = (f"""
					SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
					from turno T 
					inner join personal P on T.medico_ID = P.personal_DNI
					inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
					where fecha_Hora between '{fechaHora}' AND '{fechaHora}' + interval  59 minute
					order by T.fecha_hora ASC""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

def obtenerTurnos(desde, hasta):
	try:
		if mydb.is_connected():
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

def filtrar_para_medico(dniMedico):
	cursor = mydb.cursor()
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(PS.nombre,', ', PS.apellido), PS.paciente_DNI
					from turno T 
					inner join personal P on T.medico_ID = P.personal_DNI
					inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
					where T.estado = true and P.personal_DNI = {dniMedico} and T.fecha_hora >= "{fechaActual}"
					order by T.fecha_hora ASC
				""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

# ------- MODIFICAR TURNO -------

def Traer_turno_de_una_fila(paciente):
	cursor = mydb.cursor()
	consulta = (f"""SELECT turno_ID, medico_ID, secretario_ID, fecha_Hora, paciente_DNI
					from turno
					where turno_ID = {paciente}""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado