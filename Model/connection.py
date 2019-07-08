import mysql.connector
from mysql.connector import Error
from Model.mysqlScript import mydbCon
import time
fechaActual = time.strftime("%Y-%m-%d %H:%M:%S")

def querySelect(consulta):
	try:
		mydb= mysql.connector.connect(**mydbCon)
		cursor = mydb.cursor()
		cursor.execute(consulta)
		resultado = cursor.fetchall()
		return resultado
	except Error as e :
		print ("Error while connecting to MySQL", e)
	finally:
		#closing database connection.
		if(mydb.is_connected()):
			cursor.close()
			mydb.close()

def queryInsert(consulta, values):
	try:
		mydb= mysql.connector.connect(**mydbCon)		
		cursor = mydb.cursor()
		cursor.execute(consulta, values) 	
		mydb.commit()
	except Error as e :
		print ("Error while connecting to MySQL", e)
	finally:
		#closing database connection.
		if(mydb.is_connected()):
			cursor.close()
			mydb.close()


def select_personal(rol):
	consulta = (f"SELECT personal_DNI,nombre, apellido, telefono FROM personal WHERE rol_id = {rol}")
	return querySelect(consulta)

def select_secretarias():
	consulta = 'SELECT personal_DNI,nombre, apellido, telefono FROM personal WHERE rol_id = 2;'
	return querySelect(consulta)

def select_IDuser(user_name):
	consulta = (f'select usuario_ID from usuario where userName = "{user_name}";')
	return querySelect(consulta)

def insert_personal(dni, usuario, rol, nombre, apellido, telefono):
	consulta = "INSERT into personal(Personal_DNI, Usuario_ID, Rol_ID, Nombre, Apellido, Telefono)values(%s,%s,%s,%s,%s,%s)"
	values = (dni, usuario, rol, nombre, apellido, telefono)
	queryInsert(consulta, values)

def insert_usuario(user_name, password):
	consulta = "insert into usuario(userName, password)values(%s,%s)"
	values = (user_name, password)
	queryInsert(consulta, values)
	resultado_usuarioID = select_IDuser(user_name)
	return resultado_usuarioID[0][0]

def insert_paciente(dni,nombre,apellido,telefono):
	consulta ="insert into paciente(Paciente_DNI,Nombre,Apellido,Telefono)values(%s,%s,%s,%s)"
	values=(dni,nombre,apellido,telefono)
	queryInsert(consulta, values)

def pacienteExiste(dni):
	consulta = (f"SELECT COUNT(*) FROM paciente WHERE Paciente_DNI = {dni}")
	resultado = querySelect(consulta)
	if len(resultado)>0:
		res = resultado
	else:
		res=[resultado]
	return res[0][0]

def obtenerPacientes():
	consulta = " SELECT paciente_DNI, nombre, apellido, telefono from paciente"
	resultado=querySelect(consulta)
	return resultado

def existe_personal(dni, id):
	consulta= (f"select count(*) from personal where personal_DNI={dni} and rol_ID={id}")
	resultado = querySelect(consulta)
	return resultado[0][0]

def insert_turno(medico_ID,secretario_ID,fecha_Hora,paciente_DNI,estado):
	consulta = "insert into turno (medico_ID,secretario_ID,fecha_Hora,paciente_DNI,estado)values(%s,%s,%s,%s,%s)"
	values=(medico_ID,secretario_ID,fecha_Hora,paciente_DNI,estado)
	queryInsert(consulta,values)

def existe_turno(medico_ID,fecha_Hora):
	consulta=(f"select count(*) from turno where medico_ID={medico_ID} and fecha_Hora='{fecha_Hora}'")
	resultado=querySelect(consulta)
	if len(resultado)>0:
		res = resultado
	else:
		res=[resultado]
	return res[0][0]

def logIn(userName, password):
	consulta = (f'SELECT u.usuario_id, u.username, p.personal_dni, r.rol_id, r.nombre_rol, p.nombre, p.apellido FROM usuario u inner join personal p on u.Usuario_ID = p.Usuario_ID inner join rol r on p.Rol_ID = r.Rol_ID WHERE u.userName = "{userName}" AND u.password = "{password}" AND u.Usuario_ID in (SELECT distinct (Usuario_ID) FROM personal )')
	resultado = querySelect(consulta)
	if len(resultado)>0:
		res = resultado
	else:
		res=[resultado]
	return res[0]

def existe_usuario(usuario):
	consulta = (f"""select count(*) from usuario where userName='{usuario}'""")
	resultado = querySelect(consulta)
	return resultado[0][0]


def select_turnos():
	consulta = """SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true
	order by T.fecha_hora"""
	resultado = querySelect(consulta)
	return resultado

def filtrar_por_turno(id_Turno):
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true and T.turno_ID ={id_Turno} and T.fecha_hora >= "{fechaActual}" """)
	resultado = querySelect(consulta)
	return resultado

def filtrar_por_paciente(nombre_paciente):
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where T.estado = true and concat(PS.nombre,', ', PS.apellido) like "%{nombre_paciente}%" and T.fecha_hora >= "{fechaActual}"
	order by T.fecha_hora""")
	resultado = querySelect(consulta)
	return resultado

def filtrar_por_medico(nombre_medico):
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico',concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
				from turno T 
				inner join personal P on T.medico_ID = P.personal_DNI
				inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
				where T.estado = true and concat(P.nombre,', ', P.apellido) like "%{nombre_medico}%" and T.fecha_hora >= "{fechaActual}"
				order by concat(P.nombre,', ', P.apellido), T.fecha_hora ASC""")
	resultado = querySelect(consulta)
	return resultado

def obtenerTurnos(desde,hasta):
	consulta = (f"""SELECT CAST(fecha_Hora as date) AS 'Dia', HOUR(CAST(fecha_Hora as time)) AS 'Hora', count(*) 'Total' FROM turno
							WHERE fecha_Hora BETWEEN '{desde}' AND '{hasta}' AND estado = true
							GROUP BY CAST(fecha_Hora as date), HOUR(CAST(fecha_Hora as time))
							ORDER BY CAST(fecha_Hora as date), HOUR(CAST(fecha_Hora as time));
						""")
	resultado = querySelect(consulta)
	return resultado

def filtrar_por_fecha(fechabuscada):
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
	from turno T 
	inner join personal P on T.medico_ID = P.personal_DNI
	inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
	where fecha_Hora between "{fechabuscada}" and "{fechabuscada}" + interval 1 day
	order by T.fecha_hora ASC""")
	resultado=querySelect(consulta)
	return resultado

def filtrar_para_medico(dniMedico):
	consulta = (f"""SELECT T.turno_ID, T.fecha_hora, concat(PS.nombre,', ', PS.apellido), PS.paciente_DNI
					from turno T 
					inner join personal P on T.medico_ID = P.personal_DNI
					inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
					where T.estado = true and P.personal_DNI = {dniMedico} and T.fecha_hora >= "{fechaActual}"
					order by T.fecha_hora ASC
				""")
	resultado=querySelect(consulta)
	return resultado

def filtrar_por_fechaHora(fechaHora):
	consulta = (f"""
					SELECT T.turno_ID, T.fecha_hora, concat(P.nombre,', ', P.apellido) as 'nombreMedico', concat(PS.nombre,', ', PS.apellido) as 'nombrePaciente'
					from turno T 
					inner join personal P on T.medico_ID = P.personal_DNI
					inner join paciente PS on T.paciente_DNI = PS.paciente_DNI
					where fecha_Hora between '{fechaHora}' AND '{fechaHora}' + interval  59 minute
					order by T.fecha_hora ASC""")
	resultado = querySelect(consulta)
	return resultado