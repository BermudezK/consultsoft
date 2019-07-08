from Model.connection import existe_personal, obtenerPacientes
from Model.personal import Personal
from Model.secretario import obtenerPacientes
class medico(Personal):
	def __init__(self, dni=None, nombre=None, apellido= None, telefono=None, id_usuario=None, 
	usuario=None, password=None):
		super(medico,self).__init__(dni,nombre,apellido,telefono,id_usuario,usuario,password)
    
	def existe_medico(self,dni):
		return existe_personal(dni,3)>0

	def obtener_pacientes(self):
		return obtenerPacientes()

