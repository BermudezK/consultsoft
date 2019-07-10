import sys, re
import datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic, QtCore
from Model.turno import Turno
from Model.secretario import Secretario
from Model.administrador import Administrador
from Model.personal import Personal

class VentanaEditarsecretario(QDialog):

	def __init__(self,usuario,secretario):
		self.usuario=usuario
		self.secretario = secretario
		QDialog.__init__(self)
		uic.loadUi("View/VentanaEditarSecretario.ui",self)
		
		#Cargar todos los datos del turno para luego editarlo
		self.Campo_Nombre_2.setText(str(self.secretario.nombre))
		self.Campo_Apellido_2.setText(self.secretario.apellido)
		self.Campo_Telefono_2.setText(str(self.secretario.telefono))
		self.Campo_Usuario_2.setText(str(self.secretario.usuario))
		self.Campo_Password_2.setText(str(self.secretario.password))

		self.Campo_Nombre_2.textChanged.connect(self.validar_nombre)
		self.Campo_Apellido_2.textChanged.connect(self.validar_apellido)
		self.Campo_Usuario_2.textChanged.connect(self.validar_usuario)
		self.Campo_Password_2.textChanged.connect(self.validar_password)
		self.Campo_Telefono_2.textChanged.connect(self.validar_telefono)
		self.BotonAceptar_2.clicked.connect(self.botonAceptar)
		self.BotonCancelar_2.clicked.connect(self.closeEvent)



	def validar_nombre(self):
		self.Campo_Nombre_2.setMaxLength(45)
		nombre=self.Campo_Nombre_2.text()
		validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{1,45}$", nombre, re.I)
		if nombre == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def validar_apellido(self):
		self.Campo_Apellido_2.setMaxLength(45)
		apellido=self.Campo_Apellido_2.text()
		validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{1,45}$", apellido, re.I)
		if apellido == "":
			return False
		elif not validar:
			return False
		else:
			return True



	def validar_usuario(self):
		self.Campo_Usuario_2.setMaxLength(45)
		usuario=self.Campo_Usuario_2.text()
		validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{1,45}$", usuario, re.I)
		if usuario == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def validar_password(self):
		self.Campo_Password_2.setMaxLength(8)
		password=self.Campo_Password_2.text()
		validar = re.match("^[0-9A-Z]{8,8}$", password, re.I)
		if password == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def validar_telefono(self):
		self.Campo_Telefono_2.setMaxLength(13)
		telefono = self.Campo_Telefono_2.text()
		validar = re.match("^[0-9]{10,13}$", telefono, re.I)
		if telefono == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def botonAceptar(self):
		if self.validar_telefono() and self.validar_password() and self.validar_usuario() and self.validar_nombre() and self.validar_apellido():
			if (self.secretario.usuario != self.Campo_Usuario_2.text()) and Secretario().comprobar_existencia(self.Campo_Usuario_2.text()):	
				QMessageBox.information(self, "Error al Editar", "El usuario ya se encuentra registrado",QMessageBox.Ok)
			else:
				# dni,nombre,apellido,telefono,nombreusuario,contraseña,userID
				Secretario().editar_secretario(self.secretario.dni,self.Campo_Nombre_2.text(),self.Campo_Apellido_2.text(),self.secretario.getTelefono(),self.Campo_Usuario_2.text(),self.Campo_Password_2.text(), self.secretario.id_usuario)
				QMessageBox.information(self, "Secretario editado", "Secretario editado exitosamente.   ",QMessageBox.Ok)
				self.close()
		else: 
			if not self.validar_telefono():
				self.Campo_Telefono_2.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Telefono_2.setStyleSheet("border: 1px solid green;")
			
			if not self.validar_password():
				self.Campo_Password_2.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Password_2.setStyleSheet("border: 1px solid green;")
			
			if not self.validar_nombre():
				self.Campo_Nombre_2.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Nombre_2.setStyleSheet("border: 1px solid green;")
			
			if not self.validar_apellido():
				self.Campo_Apellido_2.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Apellido_2.setStyleSheet("border: 1px solid green;")
			if not self.validar_usuario():
				self.Campo_Usuario_2.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Usuario_2.setStyleSheet("border: 1px solid green;")
			
	def closeEvent(self,event):
		self.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	_ventana = VentanaTurno()
	_ventana.show()
	app.exec_()