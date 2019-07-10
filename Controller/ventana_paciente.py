#from Model.connection import mydb
import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from Model.secretario import Secretario
from Model.paciente import Paciente
#from databaseclinica import *

class VentanaPaciente(QDialog):
	def __init__(self,usuario, paciente = None):
		QDialog.__init__(self)
		uic.loadUi("View/ventanaPaciente.ui",self)

		self.usuario=usuario
		self.paciente = paciente
		if isinstance(self.paciente, Paciente):
			self.labelNuevoPaciente.setText('Editar paciente')
			self.campoDNI.setDisabled(True)
			self.campoDNI.setText(str(self.paciente.dni))
			self.campoNombre.setText(str(self.paciente.nombre))
			self.campoApellido.setText(str(self.paciente.apellido))
			self.campoTelefono.setText(str(self.paciente.telefono))


		#Al hacer focus en el campo ejecuta la funcion
		self.campoNombre.textChanged.connect(self.validar_nombre)
		self.campoApellido.textChanged.connect(self.validar_apellido)
		self.campoDNI.textChanged.connect(self.validar_DNI)
		self.campoTelefono.textChanged.connect(self.validar_telefono)
		#Al hacer click en el boton ejecuta la funcion
		self.botonAceptar.clicked.connect(self.validar)
		self.botonCancelar.clicked.connect(self.closeEvent)

	#Guarda el DNI en la clase persona y lo va validando
	def validar_DNI(self):
		self.campoDNI.setMaxLength(8)
		dni=self.campoDNI.text()
		validar = re.match("^[0-9]{8,8}$", dni, re.I)
		if dni == "":
			return False
		elif not validar:
			return False
		else:
			return True

	#Guarda el Nombre en la clase persona y lo va validando
	def validar_nombre(self):
		self.campoNombre.setMaxLength(45)
		nombre=self.campoNombre.text()
		validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{1,45}$", nombre, re.I)
		if nombre == "":
			return False
		elif not validar:
			return False
		else:
			return True

	#Guarda el Apellido en la clase persona y lo va validando
	def validar_apellido(self):
		self.campoApellido.setMaxLength(45)
		apellido=self.campoApellido.text()
		validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{1,45}$", apellido, re.I)
		if apellido == "":
			return False
		elif not validar:
			return False
		else:
			return True

	#Guarda el Telefono en la clase persona y lo va validando
	def validar_telefono(self):
		self.campoTelefono.setMaxLength(13)
		telefono = self.campoTelefono.text()
		validar = re.match("^[0-9]{10,13}$", telefono, re.I)
		if telefono == "":
			return False
		elif not validar:
			return False
		else:
			return True

	# Guarda los datos correctos en la Base de Datos
	def validar(self):
		if self.validar_DNI() and self.validar_nombre() and self.validar_apellido() and self.validar_telefono():
			if isinstance(self.paciente, Paciente):
					nuevosDatos = {
						'dni': self.campoDNI.text(),
						'nombre': self.campoNombre.text(),
						'apellido': self.campoApellido.text(),
						'telefono': self.campoTelefono.text()
					}
					Secretario().modificar_paciente(self.paciente.dni, nuevosDatos['nombre'], nuevosDatos['apellido'], nuevosDatos['telefono'])
					QMessageBox.information(self, "Carga completada.", "Se actualizo un Paciente correctamente.", QMessageBox.Discard)
					self.close()

			elif self.usuario.existe_paciente(self.campoDNI.text()):
				QMessageBox.warning(self,"Carga Erronea!!","El paciente ya existe")
				
			else:
				self.usuario.agregar_paciente(self.campoDNI.text(),self.campoNombre.text(),self.campoApellido.text(),self.campoTelefono.text())
				QMessageBox.information(self,"Carga completada.","Se creo un paciente correctamente.",QMessageBox.Ok)
				self.campoDNI.setText("")
				self.campoApellido.setText("")
				self.campoNombre.setText("")
				self.campoTelefono.setText("")
				self.campoDNI.setStyleSheet("border: 1px solid black")
				self.campoApellido.setStyleSheet("border: 1px solid black")
				self.campoNombre.setStyleSheet("border: 1px solid black")
				self.campoTelefono.setStyleSheet("border: 1px solid black")
			
		else:
			QMessageBox.warning(self,"Carga Erronea!!","Valor incorrecto o campo vacio.",QMessageBox.Ok)
			if not self.validar_DNI():
				self.campoDNI.setStyleSheet("border: 1px solid red;")
			else: 
				self.campoDNI.setStyleSheet("border: 1px solid green;")
			if not self.validar_nombre():
				self.campoNombre.setStyleSheet("border: 1px solid red;")
			else: 
				self.campoNombre.setStyleSheet("border: 1px solid green;")
			if not self.validar_apellido():
				self.campoApellido.setStyleSheet("border: 1px solid red;")
			else:
				self.campoApellido.setStyleSheet("border: 1px solid green;")
			if not self.validar_telefono():
				self.campoTelefono.setStyleSheet("border: 1px solid red;")
			else:
				self.campoTelefono.setStyleSheet("border: 1px solid green;")

	#Cierra la ventana
	def closeEvent(self,event):
		self.close()


if __name__== '__main__':
	app = QApplication(sys.argv)
	dialogo=VentanaPaciente()
	dialogo.show()
	app.exec_()