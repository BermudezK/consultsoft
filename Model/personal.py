from Model.persona import Persona
from Model.connection import logIn,  existe_personal, existe_usuario

class Personal (Persona):
	def __init__(self, dni=None,nombre=None,apellido=None,telefono=None,id_usuario=None,usuario=None,password=None):
		super(Personal,self).__init__(dni,nombre,apellido,telefono)
		self.setId_Usuario(id_usuario)
		self.setUsuario(usuario)
		self.setPassword(password)

	def setId_Usuario(self,id_usuario):
		self._id_usuario = id_usuario
	def setUsuario(self,usuario):
		self._usuario = usuario
	def setPassword(self,password):
		self._password = password
	
	def getId_Usuario(self):
		return self._id_usuario
	def getUsuario(self):
		return self._usuario
	def getPassword(self):
		return self._password
	
	id_usuario = property(fget=getId_Usuario, fset=setId_Usuario)
	usuario = property(fget=getUsuario, fset=setUsuario)
	password = property(fget=getPassword, fset=setPassword)
	
	def existe_usuario(self, usuario):
		if existe_usuario(usuario)>0:
			resultado = True
		else:
			resultado = False
		return resultado
	
	def existe_personal(self,dni,rol):
		if existe_personal(dni,rol) > 0:
			resultado= True
		else:
			resultado= False
		return resultado    
	
	def logIn(userName, password):
		return logIn(userName, password)