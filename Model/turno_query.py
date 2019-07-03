from Model.connection import mydb
from mysql.connector import Error

def cargar_turnos():
	cursor = mydb.cursor()
	consulta = """SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true"""
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
	where T.estado = true and T.turno_ID ={id_Turno} """)
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
	where T.estado = true and concat(PS.nombre,', ', PS.apellido) like "%{nombre_paciente}%" """)
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
	where T.estado = true and concat(P.nombre,', ', P.apellido) like "%{nombre_medico}%"
	order by concat(P.nombre,', ', P.apellido) ASC""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado