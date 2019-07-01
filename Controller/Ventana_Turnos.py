import sys, re
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic
from Model.administrador import Administrador
from Model.secretario import Secretario



class VentanaTurno(QDialog):

	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("./Ventana_Turnos.ui",self)

		self.Campo_DNI_paciente.textChanged.connect(self.validar_dni_paciente)
		self.Campo_DNI_medico.textChanged.connect(self.validar_dni_medico)
		#self.Campo_Fecha_Hora.textChanged.connect(self.validar_fehca)
		self.BotonAceptar.clicked.connect(self.cargarTurno)
		self.BotonCancelar.clicked.connect(self.closeEvent)


	def validar_dni_paciente(self):
		self.Campo_DNI_paciente.setMaxLength(8)
		dni=self.Campo_DNI_paciente.text()
		validar = re.match("^[0-9]{8,8}$", dni, re.I)
		if dni == "":
			return False
		elif not validar:
			return False
		else:
			return True

	def validar_dni_medico(self):
		self.Campo_DNI_medico.setMaxLength(8)
		dni2=self.Campo_DNI_medico.text()
		validar = re.match("^[0-9]{8,8}$", dni2, re.I)
		if dni2 == "":
			return False
		elif not validar:
			return False
		else:
			return True

	#def validar_fecha(self):



	def cargarTurno(self):
		if self.validar_dni_medico(),self.validar_dni_paciente():
			if Secretario().existe_paciente(self.Campo_DNI_paciente.text()) and Administrador().comprobar_existencia(self.Campo_DNI_medico.text()):
				QMessageBox.information(self,"Carga completa","Se creo un turno correctamente.",QMessageBox.Discard)
				self.Campo_DNI_paciente.setText("")
				self.Campo_DNI_medico.setText("")

				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid black")
				self.Campo_DNI_medico.setStyleSheet("border: 1px solid black")
			else:
				QMessageBox.warning(self,"Carga Erronea!!","El paciente o el medico no existe")



		else:
			QMessageBox.warning(self,"Carga Erronea!!","Valor incorrecto o campo vacio.",QMessageBox.Discard)
			if not self.validar_dni_paciente():
				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid red;")
			else: 
				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid green;")
			if not self.validar_dni_medico():
				self.Campo_DNI_medico.setStyleSheet("border: 1px solid red;")
			else: 
				self.Campo_DNI_medico.setStyleSheet("border: 1px solid green;")



	def closeEvent(self,event):
		self.close()



if __name__=='__main__':
	app = QApplication(sys.argv)
	_ventana = VentanaTurno()
	_ventana.show()
	app.exec_()