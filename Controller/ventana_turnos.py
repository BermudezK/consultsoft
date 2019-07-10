import sys
import time
import datetime
from Model.turno_query import cargar_turnos
from PyQt5.QtWidgets import (
 QApplication, QTableWidgetItem,
 QTableWidget, QPushButton, QHBoxLayout, QWidget,
 QDialog, QDesktopWidget, QMessageBox
 )
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from Model.turno import Turno
from Controller.Ventana_turno import VentanaTurno
from Controller.ventanaEditarTurno import VentanaEditarTurno
from Model.secretario import Secretario


class VentanaTurnos(QDialog):
	def __init__(self, usuario, fechaYHora=None):
		self.usuario = usuario
		QDialog.__init__(self)
		uic.loadUi('./View/vistaTurnos.ui',self)
		# Se carga en una variable para luego mostrarla
		if fechaYHora == None:
			# ojo acá no respeta la Orientacion a objetos
			mostrar_turnos = cargar_turnos()
			self.botonNuevoTurno.show()
		else:
			mostrar_turnos = Turno().filtrarFechaHora(fechaYHora)
			self.botonNuevoTurno.hide()

		for indice, ancho in enumerate((80,150,230,230,50),start=0):
			self.tablaTurnos.setColumnWidth(indice,ancho)
		
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
				self.crearBoton(i)
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
			mostrar_turnos = cargar_turnos()
			self.cargarTurnosALaTabla(mostrar_turnos)
		elif filtro == "Fecha":
			self.campoBusqueda.hide()
			self.dateTimeEdit.show()
			self.botonBuscar.clicked.connect(lambda: self.buscarF())


	def buscarP(self):
		turnosPacientes= Turno().filtrarPaciente(self.campoBusqueda.text())
		self.cargarTurnosALaTabla(turnosPacientes)

	def buscarM(self):
		turnosMedicos = Turno().filtrarMedico(self.campoBusqueda.text())
		self.cargarTurnosALaTabla(turnosMedicos)

	def buscarT(self):
		turnoTurno = Turno().filtrarTurno(self.campoBusqueda.text())
		self.cargarTurnosALaTabla(turnoTurno)

	def buscarF(self):
		fecha_text = self.dateTimeEdit.text()
		fecha = datetime.datetime.strptime(fecha_text, '%Y/%m/%d %H:%M:%S')
		turnoFecha = Turno().filtrarFecha(fecha)
		self.cargarTurnosALaTabla(turnoFecha)




	def botonNuevoTurno_on_click(self, usuario):
		dialogo=VentanaTurno(usuario)
		if dialogo.exec_()==0:
			mostrar_turnos = cargar_turnos()
			self.cargarTurnosALaTabla(mostrar_turnos)
		

	def editar(self, usuario,fila):
		item = self.tablaTurnos.item(fila,0)
		datosTurno = Turno().traerTurno(item.text())
		#Abre la ventana de edicion de turno
		fechaActual = datetime.datetime.today()
		if datosTurno[0][3] < fechaActual:
			 QMessageBox.information(self,"Error","No se puede editar un turno con fecha anterior a la actual",QMessageBox.Ok)
		else:
			dialogo = VentanaEditarTurno(usuario,datosTurno)
			if dialogo.exec_()==0:
				mostrar_turnos = cargar_turnos()
				self.cargarTurnosALaTabla(mostrar_turnos)

	# Crear funcion para borrar un turno
	def borrar(self,fila):
		item = self.tablaTurnos.item(fila,0)
		resultado = QMessageBox.question(self,"Borrar!","Seguro que desea eliminar el turno?",
		QMessageBox.Yes | QMessageBox.No)
		if resultado == QMessageBox.Yes: 
			Secretario().borrarTurno(item.text())
			self.cargarTurnosALaTabla(cargar_turnos())

#Crea los botones de Editar y Eliminar en las columna de Accion.

	def crearBoton(self,posicion):
		# Creo el layout que contendra a los botones
		caja = QHBoxLayout()
		# Creo los botones
		botonEliminar = QPushButton()
		botonEditar = QPushButton()
		# Agrega un icono a los botones
		botonEditar.setIcon(QtGui.QIcon("./icons/edit.svg"))
		botonEliminar.setIcon(QtGui.QIcon("./icons/delete.svg"))
		# Da el tamaño de los botones
		botonEliminar.setMinimumSize(20,20)
		botonEliminar.setMaximumSize(20,20)
		botonEditar.setMinimumSize(20,20)
		botonEditar.setMaximumSize(20,20)
		# Agrego al contenedor los botones creados
		caja.addWidget(botonEliminar)
		caja.addWidget(botonEditar)
		# Creo una elemento del tipo celda
		celda = QWidget()
		# Introduzco el layout con los botones dentro del tipo celda
		celda.setLayout(caja)
		# Creo las acciones
		botonEliminar.clicked.connect(lambda: self.borrar(posicion))
		botonEditar.clicked.connect(lambda: self.editar(self.usuario,posicion))
		# Agrego el elemento celda con los botones dentro de la tabpla en la pocicion (pocicion,4)
		self.tablaTurnos.setCellWidget(posicion,4,celda)

	# Crear funcion para editar un turno



if __name__ == '__main__':
	app = QApplication(sys.argv)
	_ventana = VentanaTurnos()
	_ventana.show()
	app.exec_()