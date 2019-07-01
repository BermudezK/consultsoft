from Model.connection import mydb
from Model.secretario_query import insertarPaciente, pacienteExiste, obtenerMedicos, obtenerPacientes, existe, agregar_turno
from Model.personal import Personal

class Secretario(Personal):
	def __init__(self, dni=None, nombre=None, apellido= None, telefono=None, id_usuario=None, usuario=None, password=None):
		super(Secretario,self).__init__(dni,nombre,apellido,telefono,id_usuario,usuario,password)

	def agregar_paciente(dni,nombre,apellido,telefono):
		insertarPaciente(dni,nombre,apellido,telefono)

	def existe_paciente(dni):
		resultado = pacienteExiste(dni)
		return resultado

	def existe_secretario(self,dni):
		print(existe(dni))
		if existe(dni) > 0:
			resultado= True
		else:
			resultado= False
		return resultado
		
	def obtener_medicos():
		return obtenerMedicos()
	
	#este metodo va a obtener todos los pacientes
	def obtener_pacientes(self):
		return obtenerPacientes()

	def nuevo_Turno(self,medicodni,secretariodni,fechayhora,pacientedni):
		agregar_turno(medicodni,secretariodni,fechayhora,pacientedni)
