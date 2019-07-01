import sys
import datetime
import calendar
from PyQt5.QtWidgets import (
  QApplication, QTableWidgetItem,
  QTableWidget, QPushButton,
  QHBoxLayout, QWidget,
  QDialog, QDesktopWidget
)
from PyQt5 import uic, QtCore

class VentanaAgenda(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('./View/ventanaAgenda.ui',self)
        self._retaso=0

        self.pb_right.clicked.connect(lambda: self.cambiarSemana(1))
        self.pb_left.clicked.connect(lambda: self.cambiarSemana(-1))

        hoy = datetime.date.today()
        semana, rango= self.obtenerSemana(hoy)
        print(rango)
        self.cargarHeader(semana)
        self.l_month.setText(hoy.strftime('%B')+'/'+ hoy.strftime('%Y'))
        self.cargarCitas()
    
    # esta funcion carga los datos en la tabla
    def cargarCitas(self):
        self.agenda.setRowCount(4)

        for i in range(4):
            # acá creo el layout (es un contenedor) que va a contener a los botones de manera horizaontal
            caja = QHBoxLayout()
            # acá creo los botones (se pueden costumizar para que tengan un icon hay que investigar nomas)
            boton1 = QPushButton('cita1')
            boton2 = QPushButton('cita2')
            # acá le agrego la funcion que se ejecuta cada vez que el boton escucha el evento de clicked
            # boton1.clicked.connect(self.hola1)
            # boton2.clicked.connect(self.hola2)
            #
            # acá agrego al contenedor los botones creados
            caja.addWidget(boton1)
            caja.addWidget(boton2)
            # acá creo un elemento del tipo celda 
            celda = QWidget()
            # aca introduzco el layout con los botones dentro del elemento del tipo celda
            celda.setLayout(caja)
            # acá agrego el elemento celda con los botones ya cargados dentro 
            # de la tabla en la posicion (0,0)
            self.agenda.setCellWidget(0,0,celda)

    # este metodo me permitirá obtener una lista de tuplas que contendrá los dias de la
    # semana actual con su fecha, si el dia es domingo me traerá la semana próxima
    def obtenerSemana(self, dia):
        semana = []
        rango = []
        for i in range(0 - dia.weekday(), 7 - dia.weekday()):
            fecha = dia + datetime.timedelta(days=i)
            rango.append(fecha)
            semana.append( fecha.strftime('%A') + ' \n ' + fecha.strftime('%d') )
        return semana, rango
    
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
        semana,rango = self.obtenerSemana(hoy)
        self.l_month.setText(hoy.strftime('%B') +'/'+ hoy.strftime('%Y') )
        self.cargarHeader(semana)

# if __name__=='__main__':
app = QApplication(sys.argv)
_ventana = VentanaAgenda()
_ventana.show()
app.exec_()