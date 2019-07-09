import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QMessageBox, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget  
from PyQt5 import uic, QtCore, QtGui
from Model.secretario import Secretario
from Controller.ventana_paciente import VentanaPaciente
class VentanaPacientes(QDialog):
      def __init__(self):
            QDialog.__init__(self)
            uic.loadUi('./View/ventanaPacientes.ui', self)
            self.cargarPacientesALaTabla()
            self.pb_cargarPaciente.clicked.connect(self.pb_agregarPaciente_on_click)
      
      def cargarPacientesALaTabla(self):
            pacientes = Secretario().obtener_pacientes()
            self.tablePaciente.setRowCount(len(pacientes))
            self.tablePaciente.setEditTriggers(QTableWidget.NoEditTriggers)
           
            for i in range(len(pacientes)):
                  paciente = pacientes[i]
                  columna = 0
                  for x in paciente:
                        item = QTableWidgetItem(str(x))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tablePaciente.setItem(i,columna, item)
                        columna = columna + 1
                  self.crearBotones(self.tablePaciente,i,columna,paciente)
                  
     
      #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON agregar pacientes
      def pb_agregarPaciente_on_click(self):
            dialogo=VentanaPaciente()
            if dialogo.exec_() == 0:
                  self.cargarPacientesALaTabla()
      
      def crearBotones(self, tabla, fila, columna, paciente):
            # Creo el layout que contendra a los botones
            caja = QHBoxLayout()
            # Creo los botones
            botonEliminar = QPushButton()
            botonEditar = QPushButton()
            # Agrega un icono a los botones
            
            estiloBasicoBoton = """
                  background-color: transparent;
            """
            botonEditar.setStyleSheet(estiloBasicoBoton)
            botonEliminar.setStyleSheet(estiloBasicoBoton)
            
            botonEditar.setIcon(QtGui.QIcon("./icons/edit.svg"))
            botonEliminar.setIcon(QtGui.QIcon("./icons/delete.svg"))
            
            # Da el tamaño de los botones
            botonEliminar.setMinimumSize(20,20)
            botonEliminar.setMaximumSize(20,20)
            botonEditar.setMinimumSize(20,20)
            botonEditar.setMaximumSize(20,20)

            # Creo las acciones
            #botonEliminar.clicked.connect(self.eliminarMedico)
            botonEditar.clicked.connect(self.editarPaciente(paciente))
            
            # Agrego al contenedor los botones creados
            caja.addWidget(botonEliminar)
            caja.addWidget(botonEditar)
            # Creo una elemento del tipo celda
            celda = QWidget()
            # Introduzco el layout con los botones dentro del tipo celda
            celda.setLayout(caja)
            # Agrego el elemento celda con los botones dentro de la tabpla en la pocicion (pocicion,4)
            tabla.setCellWidget(fila, columna, celda)
      
      def editarPaciente(self, paciente):
            def callback():
                  dni, nombre, apellido, telefono = paciente

                  pacienteFound = Secretario.obtener_paciente(dni)

                  dialogo = VentanaPaciente(pacienteFound)
                  if dialogo.exec_() == 0:
                        self.cargarPacientesALaTabla()
            return callback
      

        
if __name__== '__main__':
      app = QApplication(sys.argv)
      dialogo = VentanaPacientes()
      dialogo.show()
      app.exec_()