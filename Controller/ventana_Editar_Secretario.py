import sys, re
import datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic, QtCore
from Model.turno import Turno
from Model.secretario import Secretario
from Model.administrador import Administrador
from Model.personal import Personal

class VentanaEditarsecretario(QDialog):

	def __init__(self,secretario,datossecretario):
		self.usuario=secretario
		QDialog.__init__(self)
		uic.loadUi("View/VentanaEditarSecretario.ui",self)
		print(datossecretario)
		#Cargar todos los datos del turno para luego editarlo
		self.secretario = Secretario(datossecretario[0][0],datossecretario[0][2],datossecretario[0][1],datossecretario[0][3],None,datossecretario[0][4],datossecretario[0][5])
		self.Campo_Nombre_2.setText(str(self.secretario.getNombre()))
		self.Campo_Apellido_2.setText(self.secretario.getApellido())
		self.Campo_Usuario_2.setText(str(self.secretario.getUsuario()))
		self.Campo_Password_2.setText(str(self.secretario.getPassword()))
		self.Campo_Telefono_2.setText(str(self.secretario.getTelefono()))

		self.Campo_Nombre_2.textChanged.connect(self.validar_nombre)
		self.Campo_Apellido_2.textChanged.connect(self.validar_apellido)
		self.Campo_Usuario_2.textChanged.connect(self.validar_usuario)
		self.Campo_Password_2.textChanged.connect(self.validar_password)
		self.Campo_Telefono_2.textChanged.connect(self.validar_telefono)
		self.BotonAceptar_2.clicked.connect(self.botonAceptar)
		self.BotonCancelar_2.clicked.connect(self.closeEvent)



	def validar_nombre(self):
		self.Campo_Nombre.setMaxLength(45)
		nombre=self.Campo_Nombre.text()
		validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{1,45}$", nombre, re.I)
		if nombre == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def validar_apellido(self):
		self.Campo_Apellido.setMaxLength(45)
		apellido=self.Campo_Apellido.text()
		validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{1,45}$", apellido, re.I)
		if apellido == "":
			return False
		elif not validar:
			return False
		else:
			return True



	def validar_usuario(self):
		self.Campo_Usuario.setMaxLength(45)
		usuario=self.Campo_Usuario.text()
		validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{1,45}$", usuario, re.I)
		if usuario == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def validar_password(self):
		self.Campo_Password.setMaxLength(8)
		password=self.Campo_Password.text()
		validar = re.match("^[0-9A-Z]{8,8}$", password, re.I)
		if password == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def validar_telefono(self):
		self.Campo_Telefono.setMaxLength(13)
		telefono = self.Campo_Telefono.text()
		validar = re.match("^[0-9]{10,13}$", telefono, re.I)
		if telefono == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def botonAceptar(self):
		if self.validar_telefono() and self.validar_password() and self.validar_usuario() and self.validar_nombre() and self.validar_apellido():

			self.secretario = Secretario(self.Campo_Nombre.text(),self.Campo_Apellido.text(),self.Campo_Usuario.text(),self.Campo_Password.text(),self.Campo_Telefono.text())
			#Verifica que el medico ingresado exista
			#resultado = Secretario().existe_medico(self.Campo_DNI_Medico.text())
			if not Personal().comprobar_existencia(self.Campo_Usuario.text()):
				Secretario().Editar_Secretario(self.getNombre(),self.getApellido(),self.getUsuario(),self.getPassword(),self.getTelefono())
				QMessageBox.information(self, "Turno editado", "Turno editado exitosamente.   ",QMessageBox.Ok)
			else:
				print("Error de edicion")

	def closeEvent(self,event):
		self.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	_ventana = VentanaTurno()
	_ventana.show()
	app.exec_()