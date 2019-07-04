import sys, re
import datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic
from Model.administrador import Administrador
from Model.secretario import Secretario



class VentanaTurno(QDialog):

	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("View/Ventana_Turnos.ui",self)

		self.Campo_DNI_Medico.textChanged.connect(self.validar_dni_medico)
		self.Campo_DNI_Secretario.textChanged.connect(self.validar_dni_secretario)
		self.campo_hora_fecha.dateTimeChanged.connect(self.validar_fecha)
		self.Campo_DNI_paciente.textChanged.connect(self.validar_dni_paciente)
		#print(self.campo_hora_fecha.toString()) #de momento vamos a impirmir la fecha
		self.BotonAceptar_2.clicked.connect(self.closeEvent)
		self.BotonAceptar.clicked.connect(self.cargarTurno)


	def validar_dni_medico(self):
		self.Campo_DNI_Medico.setMaxLength(8)
		dni2=self.Campo_DNI_Medico.text()
		validar = re.match("^[0-9]{8,8}$", dni2, re.I)
		if not validar:
			return False
		else:
			return True

	def validar_dni_secretario(self):
		self.Campo_DNI_Secretario.setMaxLength(8)
		dni3=self.Campo_DNI_Secretario.text()
		validar = re.match("^[0-9]{8,8}$", dni3, re.I)
		if not validar:
			return False
		else:
			return True


	def validar_fecha(self):
		datetime_object = datetime.datetime.now()
		fecha_text=self.campo_hora_fecha.text()
		fecha = datetime.datetime.strptime(fecha_text, '%Y/%m/%d %H:%M')
		if fecha >= datetime_object:
			return True
		else:
			return False

	def validar_dni_paciente(self):
		self.Campo_DNI_paciente.setMaxLength(8)
		dni=self.Campo_DNI_paciente.text()
		validar = re.match("^[0-9]{8,8}$", dni, re.I)
		if not validar:
			return False
		else:
			return True



	def cargarTurno(self):
		if self.validar_dni_medico() and self.validar_dni_paciente() and self.validar_dni_secretario() and self.validar_fecha():
			if Secretario.existe_paciente(self.Campo_DNI_paciente.text()) and Secretario().existe_medico(self.Campo_DNI_Medico.text()) and Secretario().existe_secretario(self.Campo_DNI_Secretario.text()):

				Secretario().nuevo_Turno(self.Campo_DNI_Medico.text(),self.Campo_DNI_Secretario.text(),self.campo_hora_fecha.text(),self.Campo_DNI_paciente.text())
				#crear turno con el estado 1 por defecto
				QMessageBox.information(self,"Carga completa","Se creo un turno correctamente.",QMessageBox.Discard)
				self.Campo_DNI_paciente.setText("")
				self.Campo_DNI_Medico.setText("")
				self.Campo_DNI_Secretario.setText("")
				#self.campo_hora_fecha("")

				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid black")
				self.Campo_DNI_Medico.setStyleSheet("border: 1px solid black")
				self.Campo_DNI_Secretario.setStyleSheet("border: 1px solid black")
				#self.campo_hora_fecha.setStyleSheet("border: 1px solid black")
			else:

				QMessageBox.warning(self,"Carga Erronea!!","Valor incorrecto o campo vacio.")



		else:
			QMessageBox.warning(self,"Carga Erronea!!","Valor incorrecto o campo vacio.",QMessageBox.Discard)
			if not self.validar_dni_paciente():
				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid red;")
			else: 
				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid green;")
			if not self.validar_dni_medico():
				self.Campo_DNI_Medico.setStyleSheet("border: 1px solid red;")
			else: 
				self.Campo_DNI_Medico.setStyleSheet("border: 1px solid green;")
			if not self.validar_dni_secretario():
				self.Campo_DNI_Secretario.setStyleSheet("border: 1px solid red;")
			else: 
				self.Campo_DNI_Secretario.setStyleSheet("border: 1px solid green;")
			if not self.validar_fecha():
				self.campo_hora_fecha.setStyleSheet("border: 1px solid red;")
			else: 
				self.campo_hora_fecha.setStyleSheet("border: 1px solid green;")



	def closeEvent(self,event):
		self.close()



#if __name__=='__main__':
app = QApplication(sys.argv)
_ventana = VentanaTurno()
_ventana.show()
app.exec_()