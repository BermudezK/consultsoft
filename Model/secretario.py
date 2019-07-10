from Model.connection import mydb
from Model.secretario_query import (insertarPaciente, pacienteExiste, 
									obtenerMedicos, obtenerMedico, 
									obtenerPacientes, existe,existe2, 
									agregar_turno, existe_turno, 
									EliminarTurno, editarTurnoSeleccionado, 
									getPaciente, modificar_paciente, 
									modificar_usuario,modificar_secretario
									)
from Model.personal import Personal

class Secretario(Personal):
	def __init__(self, dni=None, nombre=None, apellido= None, telefono=None, id_usuario=None, usuario=None, password=None):
		super(Secretario,self).__init__(dni,nombre,apellido,telefono,id_usuario,usuario,password)

	def agregar_paciente(dni,nombre,apellido,telefono):
		insertarPaciente(dni,nombre,apellido,telefono)

	def existe_paciente(dni):
		resultado = pacienteExiste(dni)
		return resultado
	
	def obtener_paciente(self, dni):
		resultado = getPaciente(dni)
		return resultado
	
	def modificar_paciente(self, dni, nombre, apellido, telefono):
		modificar_paciente(dni, nombre, apellido, telefono)


	def existe_secretario(self,dni):
		if existe(dni) > 0:
			resultado= True
		else:
			resultado= False
		return resultado


	def existe_medico(self,dni):
		if existe2(dni) > 0:
			resultado= True
		else:
			resultado= False
		return resultado
	
	

		
	def obtener_medicos():
		return obtenerMedicos()

	def obtener_medico(dni):
		return obtenerMedico(dni)
	
	#este metodo va a obtener todos los pacientes
	def obtener_pacientes(self):
		return obtenerPacientes()

	def nuevo_Turno(self,medicodni,secretariodni,fechayhora,pacientedni,estado=True):
		agregar_turno(medicodni,secretariodni,fechayhora,pacientedni,estado)

	def verificar_turno(self,medico_ID,fecha_Hora):
		return int( existe_turno(medico_ID,fecha_Hora)) > 0

	def Borrar_Secretario(self,secretario):
		eliminar_Secretario(secretario)


	def editar_secretario(self,dni,nombre,apellido,telefono,nombreusuario,contraseña,userID):
		modificar_secretario(nombre,apellido,telefono,dni)
		modificar_usuario(nombreusuario,contraseña,userID)

# ------ Modificaciones de prueba -----
	
	def borrarTurno(self,turno):
		EliminarTurno(turno)

	def editarTurno(self,medico,secretario,fecha,turno):
		editarTurnoSeleccionado(medico,secretario,fecha,turno)
