from Model.personal import Personal
from Model.connection import (
	select_personal,
	insert_usuario,
	insert_personal,
	obtenerPacientes,
	obtener_personal, 
	existe_personal, 
	modificar_personal,
	modificar_usuario
)
class Administrador(Personal):
	def __init__(self, dni=None,nombre=None,apellido=None,telefono=None,id_usuario=None,usuario=None,password=None):
		super(Administrador, self).__init__(dni,nombre,apellido,telefono,id_usuario,usuario,password)


	# Este metodo permitirá al administrador obtener una lista de todos los secretarios cargados en el sistema
	# Retorno: lista de tuplas de secretarios
	def obtener_secretarios(self):
		secretarias = select_personal(2)
		return secretarias
	
	def obtener_medicos(self):
		return select_personal(3)
	
	def agregar_medico(self, dni,nombre,apellido,telefono,usuario,password):
		#Para agregar un medico antes tengo que agregar su usuario y obtener su id 
		id_usuario = insert_usuario(usuario, password)
		#aqui voy agregar un medico 
		#def insert_personal(dni, usuario, rol, nombre, apellido, telefono):
		insert_personal(dni, id_usuario, 3, nombre, apellido, telefono)
	
	def agregar_secretario(self,dni,nombre,apellido,nombre_usuario,contraseña,telefono):
		#aca va un try catch
		id_user=insert_usuario(nombre_usuario,contraseña)
		#personal_DNI, usuario_ID, rol_id, nombre, apellido, telefono
		insert_personal(dni,id_user, 2, nombre, apellido, telefono)
	
	def modificar_medico(self, dni, username, nuevosDatos):
		modificar_personal(dni, nuevosDatos)
		modificar_usuario(username, nuevosDatos)

	
	def editar_secretario(self,dni, username, nuevosDatos):
		modificar_personal(dni,nuevosDatos)
		modificar_usuario(username,nuevosDatos)

	def obtener_secretario(self,usuarioid):
		return select_personal(usuarioid) 
	  
