import sys
import time
import datetime
from PyQt5.QtWidgets import (
 QApplication, QTableWidgetItem,
 QTableWidget, QPushButton, QHBoxLayout, QWidget,
 QDialog, QDesktopWidget,
 )
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from Model.turno import Turno
from Controller.Ventana_turno import VentanaTurno


class VentanaTurnos(QDialog):
	def __init__(self, usuario, fechaYHora=None):
		self.usuario = usuario
		QDialog.__init__(self)
		uic.loadUi('./View/vistaTurnos.ui',self)
		# Se carga en una variable para luego mostrarla
		if fechaYHora == None:
			# ojo acá no respeta la Orientacion a objetos
			mostrar_turnos = Turno().mostrar_turnos()
			self.botonNuevoTurno.show()
		else:
			mostrar_turnos = Turno().filtrarFechaHora(fechaYHora)
			self.botonNuevoTurno.hide()
		
		self.cargarTurnosALaTabla(mostrar_turnos)
		self.botonNuevoTurno.clicked.connect(lambda: self.botonNuevoTurno_on_click(self.usuario))
		self.comboBoxFiltro.currentIndexChanged.connect(self.seleccionarFiltro)
		self.dateTimeEdit.hide()
		

	def cargarTurnosALaTabla(self,consulta):
		turnos = consulta
		self.tablaTurnos.setRowCount(len(turnos))
		self.tablaTurnos.setEditTriggers(QTableWidget.NoEditTriggers)

		# Recorre la lista, para agregarlo en la tabla
		for i in range(len(turnos)):
			# Agarra la primera fila
			turno = turnos[i]
			columna = 0
			for x in turno:
				# Agrega el valor de la posicion(x) de la fila
				item = QTableWidgetItem(str(x))
				item.setTextAlignment(QtCore.Qt.AlignCenter)
				self.tablaTurnos.setItem(i,columna,item)
				#Crea el boton en la fila i
				#self.crearBoton(i)
				columna = columna + 1

	def seleccionarFiltro(self,i):
		# Segun el filtro que eligas traera algunos valores
		filtro = self.comboBoxFiltro.itemText(i)
		if filtro == "Turnos":
			self.campoBusqueda.show()
			self.dateTimeEdit.hide()
			self.botonBuscar.clicked.connect(lambda: self.buscarT())
		elif filtro == "Paciente":
			self.campoBusqueda.show()
			self.dateTimeEdit.hide()
			# Al cliquear en el buscador, busca los nombre o apellidos que se paresca a lo escrito.
			self.botonBuscar.clicked.connect(lambda: self.buscarP())
		elif filtro == "Medico":
			self.campoBusqueda.show()
			self.dateTimeEdit.hide()
			self.botonBuscar.clicked.connect(lambda: self.buscarM())
		elif filtro == "-------":
			self.campoBusqueda.show()
			self.dateTimeEdit.hide()
			mostrar_turnos = Turno().mostrar_turnos()
			self.cargarTurnosALaTabla(mostrar_turnos)
		elif filtro == "Fecha":
			self.campoBusqueda.hide()
			self.dateTimeEdit.show()
			self.botonBuscar.clicked.connect(lambda: self.buscarF())


	def buscarP(self):
		turnosPacientes= Turno().filtrarPaciente(self.campoBusqueda.text())
		if turnosPacientes:
			self.cargarTurnosALaTabla(turnosPacientes)

	def buscarM(self):
		turnosMedicos = Turno().filtrarMedico(self.campoBusqueda.text())
		if turnosMedicos:
			self.cargarTurnosALaTabla(turnosMedicos)

	def buscarT(self):
		turnoTurno = Turno().filtrarTurno(self.campoBusqueda.text())
		if turnoTurno:
			self.cargarTurnosALaTabla(turnoTurno)

	def buscarF(self):
		fecha_text = self.dateTimeEdit.text()
		fecha = datetime.datetime.strptime(fecha_text, '%Y/%m/%d %H:%M:%S')
		turnoFecha = Turno().filtrarFecha(fecha)
		if turnoFecha:
			self.cargarTurnosALaTabla(turnoFecha)

	def botonNuevoTurno_on_click(self, usuario):
		dialogo=VentanaTurno(usuario)
		if dialogo.exec_()==0:
			mostrar_turnos = cargar_turnos()
			self.cargarTurnosALaTabla(mostrar_turnos)
		

# Crea los botones de Editar y Eliminar en las columna de Accion.
"""
	def crearBoton(self,posicion):
		# Creo el layout que contendra a los botones
		caja = QHBoxLayout()
		# Creo los botones
		botonEliminar = QPushButton()
		botonEditar = QPushButton()
		# Agrega un icono a los botones
		botonEditar.setIcon(QtGui.QIcon("../icons/edit.svg"))
		botonEliminar.setIcon(QtGui.QIcon("../icons/delete.svg"))
		# Da el tamaño de los botones
		botonEliminar.setMinimumSize(20,20)
		botonEliminar.setMaximumSize(20,20)
		botonEditar.setMinimumSize(20,20)
		botonEditar.setMaximumSize(20,20)
		# Creo las acciones
		botonEliminar.clicked.connect(self.borrar)
		botonEditar.clicked.connect(self.editar)
		# Agrego al contenedor los botones creados
		caja.addWidget(botonEliminar)
		caja.addWidget(botonEditar)
		# Creo una elemento del tipo celda
		celda = QWidget()
		# Introduzco el layout con los botones dentro del tipo celda
		celda.setLayout(caja)
		# Agrego el elemento celda con los botones dentro de la tabpla en la pocicion (pocicion,4)
		self.tablaTurnos.setCellWidget(posicion,4,celda)

	# Crear funcion para editar un turno
	def editar(self):
		print("Editar")

	# Crear funcion para borrar un turno
	def borrar(self):
		print("Borrar")

"""

if __name__ == '__main__':
	app = QApplication(sys.argv)
	_ventana = VentanaTurnos()
	_ventana.show()
	app.exec_()