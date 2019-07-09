from Model.connection import mydb
from Model.medico_query import (obtenerPacientes, existe)
from Model.personal import Personal
from Model.secretario import obtenerPacientes
class Medico(Personal):
	def __init__(self, dni=None, nombre=None, apellido= None, telefono=None, id_usuario=None, 
	usuario=None, password=None):
		super(Medico,self).__init__(dni,nombre,apellido,telefono,id_usuario,usuario,password)
    
	def existe_medico(self,dni):
		# print(existe(dni))
		#if existe(dni) > 0:
		#	resultado= True
		#else:
			#resultado= False
		#return resultado

		return existe(dni)>0

	def obtener_pacientes(self):

		return obtenerPacientes()

