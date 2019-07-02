import sys
from Model.turno_query import cargar_turnos
from PyQt5.QtWidgets import (
 QApplication, QTableWidgetItem,
 QTableWidget, QPushButton, QHBoxLayout, QWidget,
 QDialog, QDesktopWidget
 )
from PyQt5 import uic, QtCore, QtGui
from Model.turno import Turno

class VistaTurnos(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi('./View/vistaTurnos.ui',self)
		#self.center()
		self.cargarTurnosALaTabla(cargar_turnos)
		self.botonNuevoTurno.clicked.connect(self.botonNuevoTurno_on_click)
		self.comboBoxFiltro.currentIndexChanged.connect(self.seleccionarFiltro)
		#self.campoBusqueda.textChanged.connect(self.busqueda)
		

	def cargarTurnosALaTabla(self,consulta):
		turnos = consulta()
		#turnos = cargar_turnos()
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
		filtro = self.comboBoxFiltro.itemText(i)
		if filtro == "Turno":
			pass
			#self.botonBuscar.clicked.connect(self.buscar(busqueda(),Turno().filtrarTurno()))

		elif filtro == "Paciente":
			self.botonBuscar.clicked.connect(self.buscarP())


	def buscarP(self):
		turnosPacientes= Turno().filtrarPaciente(self.campoBusqueda.text())




	def botonNuevoTurno_on_click(self):
		# Cargar un nuevo turno
		# Falta modulo de Pablo
		pass

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

#if __name__ == '__main__':
app = QApplication(sys.argv)
_ventana = VistaTurnos()
_ventana.show()
app.exec_()