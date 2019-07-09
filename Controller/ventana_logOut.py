import sys
import re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, qApp
from PyQt5 import uic
from Controller.ventana_login import VentanaLogin
#from main import MainWindow

class Ventana_logOut(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("View/logOut.ui", self)
        
        #Al hacer click en el boton ejecuta la funcion
        self.botonAceptar.clicked.connect(qApp.quit)
        self.botonCancelar.clicked.connect(self.closeEvent)

    def closeEvent(self, event):
         self.close()
