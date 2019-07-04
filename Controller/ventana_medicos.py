import sys
from PyQt5.QtWidgets import (
  QApplication, QTableWidgetItem,
  QTableWidget, QPushButton,
  QHBoxLayout, QWidget,
  QDialog, QDesktopWidget
)
from PyQt5 import uic, QtCore
from Model.secretario import Secretario
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
        self.tableMedicos.setItem(i,columna, item)
        columna = columna + 1

  #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON agregar pacientes
  def pb_agregarMedico_on_click(self):
        dialogo=VentanaMedico()
        if dialogo.exec_()==0:
          self.cargarMedicosALaTabla()
        
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
