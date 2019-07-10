import sys, re
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic

#Clase heredada de QMainWindow (Constructor de ventanas)
class VentanaSecretario(QDialog):
	#Metodo constructor del a clase
	def __init__(self, usuario):
		self.usuario=usuario #deberian de pasarle un administrador
		#Iniciar el objeto QMainWindow
		QDialog.__init__(self)
		#Cargar la configuracio del archivo .ui en el objeto
		uic.loadUi("./View/ventanaSecretario.ui",self)
		self.Campo_DNI.textChanged.connect(self.validar_dni)
		self.Campo_Nombre.textChanged.connect(self.validar_nombre)
		self.Campo_Apellido.textChanged.connect(self.validar_apellido)
		self.Campo_Usuario.textChanged.connect(self.validar_usuario)
		self.Campo_Password.textChanged.connect(self.validar_password)
		self.Campo_Telefono.textChanged.connect(self.validar_telefono)
		#Al hacer click en el boton ejecuta la funcion
		self.BotonAceptar.clicked.connect(self.cargarSecretario)
		self.BotonCancelar.clicked.connect(self.closeEvent)


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

	def validar_dni(self):
		self.Campo_DNI.setMaxLength(8)
		dni=self.Campo_DNI.text()
		validar = re.match("^[0-9]{8,8}$", dni, re.I)
		if dni == "":
			return False
		elif not validar:
			return False
		else:
			return True


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

	def cargarSecretario(self):
		if self.validar_telefono() and self.validar_password() and self.validar_usuario() and self.validar_nombre() and self.validar_apellido() and self.validar_dni():
			if self.usuario.existe_personal(self.Campo_DNI.text(),2):
				QMessageBox.warning(self,"Carga Erronea!!","El Secretario ya existe")
			elif self.usuario.existe_usuario(self.Campo_Usuario.text()):
				QMessageBox.warning(self,"Carga Erronea!!","Nombre de Usuario ya existe")
			else:
				self.usuario.agregar_secretario(self.Campo_DNI.text(), self.Campo_Nombre.text(), self.Campo_Apellido.text(),self.Campo_Usuario.text(),self.Campo_Password.text(), self.Campo_Telefono.text())
				QMessageBox.information(self,"Carga completada.","Se creo un Secretario correctamente.",QMessageBox.Discard)
				self.Campo_DNI.setText("")
				self.Campo_Apellido.setText("")
				self.Campo_Nombre.setText("")
				self.Campo_Telefono.setText("")
				self.Campo_Usuario.setText("")
				self.Campo_Password.setText("")


				self.Campo_DNI.setStyleSheet("border: 1px solid black")
				self.Campo_Apellido.setStyleSheet("border: 1px solid black")
				self.Campo_Nombre.setStyleSheet("border: 1px solid black")
				self.Campo_Telefono.setStyleSheet("border: 1px solid black")
				self.Campo_Usuario.setStyleSheet("border: 1px solid black")
				self.Campo_Password.setStyleSheet("border: 1px solid black")

		else:
			QMessageBox.warning(self,"Carga Erronea!!","Valor incorrecto o campo vacio.",QMessageBox.Discard)
			if not self.validar_dni():
				self.Campo_DNI.setStyleSheet("border: 1px solid red;")
			else: 
				self.Campo_DNI.setStyleSheet("border: 1px solid green;")
			if not self.validar_nombre():
				self.Campo_Nombre.setStyleSheet("border: 1px solid red;")
			else: 
				self.Campo_Nombre.setStyleSheet("border: 1px solid green;")
			if not self.validar_apellido():
				self.Campo_Apellido.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Apellido.setStyleSheet("border: 1px solid green;")
			if not self.validar_telefono():
				self.Campo_Telefono.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Telefono.setStyleSheet("border: 1px solid green;")
			if not self.validar_usuario():
				self.Campo_Usuario.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Usuario.setStyleSheet("border: 1px solid green;")
			if not self.validar_password():
				self.Campo_Password.setStyleSheet("border: 1px solid red;")
			else:
				self.Campo_Password.setStyleSheet("border: 1px solid green;")


	def closeEvent(self,event):
		self.close()


if __name__=='__main__':
#Instancia para iniciar una aplicacion
	app = QApplication(sys.argv)
#Crear un objeto de la clase
	_ventana = VentanaSecretario()
#Mostrar la ventana
	_ventana.show()
#Ejecuta la aplicaion
	app.exec_()