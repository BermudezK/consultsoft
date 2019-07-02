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

def filtrar_por_turno(serch):
	cursor = mydb.cursor()
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true and T.turno_ID = {serch}
	order by T.turno_ID ASC""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

def filtrar_por_paciente(serch):
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true and nombrePaciente like '%{serch}%'
	order by nombrePaciente ASC""")
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado

def filtrar_por_medico():
	consulta = """SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true
	order by nombreMedico ASC"""
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	cursor.close()
	return resultado