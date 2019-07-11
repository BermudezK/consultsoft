import sys
import datetime
import calendar
from PyQt5.QtWidgets import (
  QApplication, QTableWidgetItem,
  QTableWidget, QPushButton,
  QHBoxLayout, QWidget,
  QDialog, QDesktopWidget, QMessageBox
)
from PyQt5 import uic, QtCore
from Model.turno import Turno

from Controller.ventana_turnos import VentanaTurnos
from Controller.Ventana_turno import VentanaTurno

class VentanaAgenda(QDialog):
	def __init__(self, usuario):
		self.usuario=usuario
		QDialog.__init__(self)
		uic.loadUi('./View/ventanaAgenda.ui',self)
		hoy = datetime.date.today()
		self.obtenerSemana(hoy)
		self.cargarHeader(self._semana)
		self.l_month.setText(hoy.strftime('%B')+'/'+ hoy.strftime('%Y'))
		self._retaso=0
		self.cambiarSemana(0)
		self.agenda.cellClicked.connect(lambda: self.agregarTurno(self._rango))
		self.pb_right.clicked.connect(lambda: self.cambiarSemana(1))
		self.pb_left.clicked.connect(lambda: self.cambiarSemana(-1))

	
	# Con este metodo abriremos la ventana para agregar 
	# turnos y le pasaremos el dia 
	# en el cuel queremos almacenarlo
	def agregarTurno(self, fecha):
		columna=self.agenda.currentColumn()
		hora =self.agenda.currentRow() + 6
		fechaHora= str(fecha[columna]) + ' '+str(hora)+':00:00'
		if datetime.date.today() <= fecha[columna]:
			dialogo = VentanaTurno(self.usuario,fechaHora)
			dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
			if dialogo.exec_()==0:
				self.cambiarSemana(0)
		else:
			QMessageBox.information(self, "Error", "No es permite agregar un turno una fecha anterior a la actual" , QMessageBox.Discard)
			
	# esta funcion carga los datos en la tabla
	def cargarCitas(self):
		self.agenda.clearContents()
		desde =self._rango[0]
		hasta = self._rango[-1]
		turnos = Turno().mostrar_turnos(desde,hasta)
		# por cada uno de los turnos que traemos de la base de datos
		for turno in turnos:
			# obtenemos la columna correspondiente al día del self._rango especifico
			columna=self._rango.index(turno[0])
			# obtenemos la fila que se corresponde con un self._rango de hora en particular
			fila = turno[1] - 6
			# acá creo el layout (es un contenedor) que va a contener a los botones de manera horizaontal
			caja = QHBoxLayout()
			# acá creo los botones (se pueden costumizar para que tengan un icon hay que investigar nomas)
			boton1 = QPushButton(str(turno[2]))
			#
			# acá agrego al contenedor los botones creados
			caja.addWidget(boton1)
			# acá creo un elemento del tipo celda 
			celda = QWidget()
			# aca introduzco el layout con los botones dentro del elemento del tipo celda
			celda.setLayout(caja)
			# acá agrego el elemento celda con los botones ya cargados dentro 
			# de la tabla en la posicion (0,0)
			self.agenda.setCellWidget(fila,columna,celda)
			# acá le agrego la funcion que se ejecuta cada vez que el boton escucha el evento de clicked
			boton1.clicked.connect(lambda *args,hora=turno[1], fecha=turno[0]: self.goToFilter(fecha,hora))
			self.agenda.resizeRowsToContents()

	
	# con esto iremos a los filtros y 
	# traremos los turnos en el self._rango de fecha 
	# que se han solicitado en desde y hasta
	def goToFilter(self, fecha, hora):
		dia = str(fecha) +' '+ str(hora) +':00:00'
		dialogo = VentanaTurnos(self.usuario, dia)
		dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		dialogo.show()
		

	# este metodo me permitirá obtener una lista de tuplas que contendrá los dias de la
	# semana actual con su fecha, si el dia es domingo me traerá la semana próxima
	def obtenerSemana(self, dia):
		self._semana = []
		self._rango = []
		for i in range(0 - dia.weekday(), 7 - dia.weekday()):
			fecha = dia + datetime.timedelta(days=i)
			self._rango.append(fecha)
			self._semana.append( fecha.strftime('%A') + ' \n ' + fecha.strftime('%d') )

	# Esta funcion carga las cabeceras del tableWidget con la info del dia y 
	# numero de la semana
	def cargarHeader(self, semana):        
		self.agenda.setHorizontalHeaderLabels(semana)

	
	# este metodo cambia los valores del calendario n semanas 
	# antes/despues de la semana actual mostrada en el calendario
	def cambiarSemana(self, cuanto):
		self._retaso = self._retaso + cuanto
		dias = datetime.timedelta(7 * self._retaso)
		hoy = datetime.date.today() - dias
		self.obtenerSemana(hoy)
		self.l_month.setText(hoy.strftime('%B') +'/'+ hoy.strftime('%Y') )
		self.cargarHeader(self._semana)
		self.cargarCitas()

if __name__=='__main__':
	app = QApplication(sys.argv)
	_ventana = VentanaAgenda()
	_ventana.show()
	app.exec_()