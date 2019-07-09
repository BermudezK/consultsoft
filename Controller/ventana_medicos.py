import sys
from PyQt5.QtWidgets import (
  QApplication,
  QTableWidgetItem,
  QTableWidget,
  QPushButton,
  QHBoxLayout,
  QWidget,
  QDialog,
  QDesktopWidget,
)
from PyQt5 import uic, QtCore, QtGui
from Model.secretario import Secretario
from Model.medico import Medico
from Controller.ventana_medico import VentanaMedico
from Controller.ventana_agenda import VentanaAgenda


class VentanaMedicos(QDialog):
  def __init__(self):
    QDialog.__init__(self)
    uic.loadUi('./View/ventanaMedicos.ui', self)
    self.center()
    self.cargarMedicosALaTabla()
    self.pb_cargarMedico.clicked.connect(self.pb_agregarMedico_on_click)
    
  def cargarMedicosALaTabla(self):
    medicos = Secretario.obtener_medicos()
    self.tableMedicos.setRowCount(len(medicos))
    self.tableMedicos.setEditTriggers(QTableWidget.NoEditTriggers)
    
    for i in range(len(medicos)):
      medico = medicos[i]
      columna = 0
      for x in medico:
        item = QTableWidgetItem(str(x))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableMedicos.setItem(i, columna, item)
        columna = columna + 1
      self.crearBotones(self.tableMedicos, i, columna, medico)

  def crearBotones(self, tabla, fila, columna, medico):
    # Creo el layout que contendra a los botones
    caja = QHBoxLayout()
    # Creo los botones
    # botonEliminar = QPushButton()
    botonEditar = QPushButton()
    # Agrega un icono a los botones
    
    estiloBasicoBoton = """
      .QPushButton{
        border:none;
        background-color: transparent;}
    """
    botonEditar.setStyleSheet(estiloBasicoBoton)
    # botonEliminar.setStyleSheet(estiloBasicoBoton)
    
    botonEditar.setIcon(QtGui.QIcon("./icons/edit.svg"))
    # botonEliminar.setIcon(QtGui.QIcon("./icons/delete.svg"))
    
    # Da el tamaño de los botones
    # botonEliminar.setMinimumSize(20,20)
    # botonEliminar.setMaximumSize(20,20)
    botonEditar.setMinimumSize(20,20)
    botonEditar.setMaximumSize(20,20)

    # Creo las acciones
    # botonEliminar.clicked.connect(self.eliminarMedico)
    botonEditar.clicked.connect(self.editarMedico(medico))
    
    # Agrego al contenedor los botones creados
    # caja.addWidget(botonEliminar)
    caja.addWidget(botonEditar)
    # Creo una elemento del tipo celda
    celda = QWidget()
    # Introduzco el layout con los botones dentro del tipo celda
    celda.setLayout(caja)
    # Agrego el elemento celda con los botones dentro de la tabpla en la pocicion (pocicion,4)
    tabla.setCellWidget(fila, columna, celda)
    
  #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON agregar pacientes
  def pb_agregarMedico_on_click(self):
    dialogo=VentanaMedico()
    if dialogo.exec_()==0:
      self.cargarMedicosALaTabla()
        
  # def eliminarMedico(self):
  #   print('Eliminar medico')

  def editarMedico(self, medico):
    def callback():      
      medicoFound = Secretario.obtener_medico(medico[0])
      
      med = Medico(medicoFound[0],medicoFound[1],medicoFound[2],medicoFound[3],None,medicoFound[4],medicoFound[5])
      dialogo = VentanaMedico(med)
      if dialogo.exec_() == 0:
        self.cargarMedicosALaTabla()
    return callback

  def center(self):
    # geometry of the main window
    qr = self.frameGeometry()

    # center point of screen
    cp = QDesktopWidget().availableGeometry().center()

    # move rectangle's center point to screen's center point
    qr.moveCenter(cp)

    # top left of rectangle becomes top left of window centering it
    self.move(qr.topLeft())
if __name__== '__main__':
  app = QApplication(sys.argv)
  _ventana = VentanaMedicos()
  _ventana.showMaximized()
  app.exec_()
