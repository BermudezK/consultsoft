import sys, re
import datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic, QtCore

class VentanaTurno(QDialog):

	def __init__(self, usuario, fechaHora=None):
		self.usuario=usuario
		QDialog.__init__(self)
		uic.loadUi("View/Ventana_Turnos.ui",self)
		
		if fechaHora != None:
			data = QtCore.QDateTime.fromString(fechaHora, "yyyy-MM-dd h:mm:ss")
			self.campo_hora_fecha.setDateTime(data)

		self.Campo_DNI_Medico.textChanged.connect(self.validar_dni_medico)
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
		if self.validar_dni_medico() and self.validar_dni_paciente() and self.validar_fecha():
			
			if self.usuario.existe_personal(self.Campo_DNI_Medico.text(),3):
				self.Campo_DNI_Medico.setStyleSheet("border: 1px solid green;")
			else:
				self.Campo_DNI_Medico.setStyleSheet("border: 1px solid red;")
				QMessageBox.information(self,"Carga incompleta","El Medico no existe.",QMessageBox.Discard)

			if self.usuario.existe_paciente(self.Campo_DNI_paciente.text()):
				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid green;")
			else:
				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid red;")
				QMessageBox.information(self,"Carga incompleta","El Paciente no existe.",QMessageBox.Discard)

			if not self.usuario.verificar_turno(self.Campo_DNI_Medico.text(), self.campo_hora_fecha.text()):
				self.campo_hora_fecha.setStyleSheet("border: 1px solid green;")
			else:
				self.campo_hora_fecha.setStyleSheet("border: 1px solid red;")
				QMessageBox.information(self,"Carga incompleta","El turno ya existe",QMessageBox.Discard)

			if self.usuario.existe_paciente(self.Campo_DNI_paciente.text()) and self.usuario.existe_personal(self.Campo_DNI_Medico.text(), 3) and not self.usuario.verificar_turno(self.Campo_DNI_Medico.text(), self.campo_hora_fecha.text()):
				self.usuario.nuevo_Turno(self.Campo_DNI_Medico.text(),self.usuario.dni,self.campo_hora_fecha.text(),self.Campo_DNI_paciente.text())
				
				QMessageBox.information(self,"Carga completa","Se creo un turno correctamente.",QMessageBox.Discard)
				self.Campo_DNI_paciente.setText("")
				self.Campo_DNI_Medico.setText("")

				self.Campo_DNI_paciente.setStyleSheet("border: 1px solid black")
				self.Campo_DNI_Medico.setStyleSheet("border: 1px solid black")

				self.campo_hora_fecha.setStyleSheet("border: 1px solid black")
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
			if not self.validar_fecha():
				self.campo_hora_fecha.setStyleSheet("border: 1px solid red;")
			else: 
				self.campo_hora_fecha.setStyleSheet("border: 1px solid green;")


	def closeEvent(self,event):
		self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	_ventana = VentanaTurno()
	_ventana.show()
	app.exec_()
