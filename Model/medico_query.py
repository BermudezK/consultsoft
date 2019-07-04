from Model.connection import mydb

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


def medicoExiste(dni):
	sqlmedicoExiste = (f"SELECT COUNT(*) FROM medico WHERE Medico_DNI = {dni}")
	cursor = mydb.cursor()
	cursor.execute(sqlmedicoExiste)
	#Guarda el resultado
	resultado = cursor.fetchone()
	return resultado

def existe(dni):
    cursor= mydb.cursor()
    consulta= (f"select count(*) from personal where personal_DNI={dni} and rol_ID=3")
    cursor.execute(consulta)
    resultado=cursor.fetchone()
    cursor.close()
    return resultado[0]