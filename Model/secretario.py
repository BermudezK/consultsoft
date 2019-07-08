from Model.connection import (select_personal, insert_paciente, pacienteExiste, 
							obtenerPacientes, existe_personal,insert_turno,existe_turno)
from Model.personal import Personal

class Secretario(Personal):
	def __init__(self, dni=None, nombre=None, apellido= None, telefono=None, id_usuario=None, usuario=None, password=None):
		super(Secretario,self).__init__(dni,nombre,apellido,telefono,id_usuario,usuario,password)

	def agregar_paciente(dni,nombre,apellido,telefono):
		insert_paciente(dni,nombre,apellido,telefono)

	def existe_paciente(dni):
		resultado = pacienteExiste(dni)
		return resultado

	def obtener_medicos():
		return select_personal(3)
	
	#este metodo va a obtener todos los pacientes
	def obtener_pacientes(self):
		return obtenerPacientes()

	def nuevo_Turno(self,medicodni,secretariodni,fechayhora,pacientedni,estado=True):
		insert_turno(medicodni,secretariodni,fechayhora,pacientedni,estado)

	def verificar_turno(self,medico_ID,fecha_Hora):
		return existe_turno(medico_ID,fecha_Hora) > 0
