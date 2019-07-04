import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QMessageBox, 
							QTableWidget, QTableWidgetItem, QPushButton,QWidget,
							QCompleter, QComboBox, QHBoxLayout,QPushButton)
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from Controller.ventana_medico import VentanaMedico
from Controller.ventana_paciente import VentanaPaciente
from Model.administrador import Administrador


class VentanaTurnoMedico(QDialog):
	def __init__(self,medico):
		QDialog.__init__(self)
		uic.loadUi('./View/displyappointment.ui', self)
		self.cargarPacientesALaTabla()
		#self.pb_cargarPaciente.clicked.connect(self.pb_agregarPaciente_on_click)
	
	def cargarPacientesALaTabla(self):
		pacientes = Administrador().obtener_pacientes()
		self.tablaTurnos.setRowCount(len(pacientes))
		self.tablaTurnos.setEditTriggers(QTableWidget.NoEditTriggers)
		
		for i in range(len(pacientes)):
			paciente = pacientes[i]
			columna = 0
			for x in paciente:
				item = QTableWidgetItem(str(x))
				item.setTextAlignment(QtCore.Qt.AlignCenter)
				self.tablaTurnos.setItem(i,columna, item)
				# self.crearBoton(i)#aca va el boton de aceptar o cancelar turno
				columna = columna + 1
	
	# def crearBoton(self,posicion):
	# 	# Creo el layout que contendra a los botones
	# 	caja = QHBoxLayout()
	# 	# Creo los botones
	# 	botonCancelar = QPushButton()
	# 	botonaceptar = QPushButton()
	# 	# Agrega un icono a los botones
	# 	botonaceptar.setIcon(QtGui.QIcon("../icons/edit.svg"))
	# 	botonCancelar.setIcon(QtGui.QIcon("../icons/delete.svg"))
	# 	# Da el tamaño de los botones
	# 	botonCancelar.setMinimumSize(20,20)
	# 	botonCancelar.setMaximumSize(20,20)
	# 	botonaceptar.setMinimumSize(20,20)
	# 	botonaceptar.setMaximumSize(20,20)
	# 	# Creo las acciones
	# 	botonCancelar.clicked.connect(self.cancelar)
	# 	botonaceptar.clicked.connect(self.aceptar)
	# 	# Agrego al contenedor los botones creados
	# 	caja.addWidget(botonCancelar)
	# 	caja.addWidget(botonaceptar)
	# 	# Creo una elemento del tipo celda
	# 	celda = QWidget()
	# 	# Introduzco el layout con los botones dentro del tipo celda
	# 	celda.setLayout(caja)
	# 	# Agrego el elemento celda con los botones dentro de la tabpla en la pocicion (pocicion,4)
	# 	self.tablaTurnos.setCellWidget(posicion,4,celda)

	# 		# Crear funcion para aceptar un turno
	# def aceptar(self):
	# 	print("Aceptar")

	# 	# Crear funcion para cancelar un turno
	# def cancelar(self):
	# 	print("cancelar")

					
if __name__== '__main__':
	app = QApplication(sys.argv)
	dialogo = VentanaTurnoMedico()
	dialogo.show()
	app.exec_()
