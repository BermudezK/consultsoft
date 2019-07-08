import sys, re
import datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5 import uic, QtCore
from Model.turno import Turno
from Model.secretario import Secretario

class VentanaEditarTurno(QDialog):

	def __init__(self, usuario,datosTurno, fechaHora=None):
		self.usuario = usuario
		QDialog.__init__(self)
		uic.loadUi("View/VentanaEditarTurno.ui",self)
		self.turno = Turno()
		#Cargar todos los datos del turno para luego editarlo
		print(datosTurno)
		self.turno.setNro_Turno(datosTurno[0][0])
		self.turno.setMedico(datosTurno[0][1])
		self.turno.setFechayHora(datosTurno[0][3])
		self.turno.setPaciente(datosTurno[0][4])
		#self.turno.setEstado(datosTurno[0][5])
		self.Campo_DNI_Medico.setText(str(self.turno.getMedico()))
		self.campo_hora_fecha.setDateTime(self.turno.getFechayHora())
		self.Campo_DNI_paciente.setText(str(self.turno.getPaciente()))
		self.Campo_DNI_paciente.setReadOnly(True)


		if fechaHora != None:
			data = QtCore.QDateTime.fromString(fechaHora, "yyyy-MM-dd h:mm:ss")
			self.campo_hora_fecha.setDateTime(data)

		self.Campo_DNI_Medico.textChanged.connect(self.validar_dni_medico)
		self.campo_hora_fecha.dateTimeChanged.connect(self.validar_fecha)
		self.BotonCancelar.clicked.connect(self.closeEvent)
		self.BotonAceptar.clicked.connect(self.botonAceptar)



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

	def botonAceptar(self):
		if self.validar_dni_medico() and self.validar_fecha():
			#Verifica que el medico ingresado exista
			#resultado = Secretario().existe_medico(self.Campo_DNI_Medico.text())
			if Secretario().existe_medico(self.Campo_DNI_Medico.text()):
				Secretario().editarTurno(self.turno.getMedico(),self.usuario[2],self.turno.getFechayHora(),self.turno.getNro_Turno())
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