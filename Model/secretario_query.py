from Model.connection import mydb

def insertarPaciente(dni,nombre,apellido,telefono):
	sqlInsertarPaciente = 'insert into paciente(Paciente_DNI,Nombre,Apellido,Telefono)value(%s,%s,%s,%s)'
	cursor = mydb.cursor()
	cursor.execute(sqlInsertarPaciente,(dni,nombre,apellido,telefono))
	# Guarda los valores ingresado en la tabla
	mydb.commit()
	# IMPORTANTE: Se quito esto porque cerraba la conexion y no me permitia guardar mas de un paciente a la vez.
	cursor.close()
	#mydb.close()

def pacienteExiste(dni):
	sqlPacienteExiste = (f"SELECT COUNT(*) FROM paciente WHERE Paciente_DNI = {dni}")
	cursor = mydb.cursor()
	cursor.execute(sqlPacienteExiste)
	#Guarda el resultado
	resultado = cursor.fetchone()
	return resultado

def getPaciente(dni):
	sqlGetPaciente = (f"SELECT * FROM paciente WHERE Paciente_DNI = {dni}")
	cursor = mydb.cursor()
	cursor.execute(sqlGetPaciente)
	#Guarda el resultado
	resultado = cursor.fetchone()
	return resultado

def modificar_paciente(dni,nombre,apellido,telefono):
  cursor = mydb.cursor()
  updatePaciente = f"""
      UPDATE paciente
          SET paciente_DNI = {dni},
              nombre = "{nombre}",
              apellido = "{apellido}",
              telefono = {telefono}
          WHERE paciente_DNI = {dni};
  """
  cursor.execute(updatePaciente)
  mydb.commit()
  cursor.close()


def obtenerMedicos():
  cursor = mydb.cursor()

  consulta = """SELECT p.personal_dni, p.nombre, p.apellido, p.telefono 
  FROM personal AS p 
  INNER JOIN usuario AS u ON p.usuario_id = u.usuario_id 
  INNER JOIN rol AS r ON p.rol_id = r.rol_id 
  WHERE r.rol_id = 3;"""
  cursor.execute(consulta)
  resultado = cursor.fetchall()
  cursor.close()
  return resultado

  
def obtenerPacientes():
	cursor =mydb.cursor()
	consulta = " SELECT paciente_DNI, nombre, apellido, telefono from paciente;"
	cursor.execute(consulta)
	resultado=cursor.fetchall()
	cursor.close()
	return resultado

def existe(dni):
    cursor= mydb.cursor()
    consulta= (f"select count(*) from personal where personal_DNI={dni} and rol_ID=2")
    cursor.execute(consulta)
    resultado=cursor.fetchone()
    cursor.close()
    return resultado[0]

def existe2(dni):
    cursor= mydb.cursor()
    consulta= (f"select count(*) from personal where personal_DNI={dni} and rol_ID=3")
    cursor.execute(consulta)
    resultado=cursor.fetchone()
    cursor.close()
    return resultado[0]

def agregar_turno(medico_ID,secretario_ID,fecha_Hora,paciente_DNI,estado):
    sqlconsulta = "insert into turno (medico_ID,secretario_ID,fecha_Hora,paciente_DNI,estado) values (%s,%s,%s,%s,%s)"
    cursor= mydb.cursor()
    cursor.execute(sqlconsulta,(medico_ID,secretario_ID,fecha_Hora,paciente_DNI,estado))
    mydb.commit()
    cursor.close()

def existe_turno(medico_ID,fecha_Hora):
	consultaTurno=(f"select count(*) from turno where medico_ID={medico_ID} and fecha_Hora='{fecha_Hora}';")
	cursor = mydb.cursor()
	cursor.execute(consultaTurno)
	resultado=cursor.fetchone()
	cursor.close()
	return resultado[0]


