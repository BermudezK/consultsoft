import sys, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5 import uic, QtCore
from Controller.ventana_secretarios import DSecretario
from Controller.ventana_pacientes import VentanaPacientes
from Controller.ventana_medicos import VentanaMedicos

class MainWindow (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('View/home.ui',self)
        self.center()
        self.pb_secretarios.clicked.connect(self.pb_secretarios_on_click)
        self.pb_pacientes.clicked.connect(self.pb_pacientes_on_click)
        self.pb_medicos.clicked.connect(self.pb_medicos_on_click)
    
    #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON SECRETARIOS
    def pb_secretarios_on_click(self):
        dialogo=DSecretario()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
        dialogo.exec_()
    
    #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON PACIENTES
    def pb_pacientes_on_click(self):
        dialogo=VentanaPacientes()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
        dialogo.exec_()
    
    #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON MEDICOS
    def pb_medicos_on_click(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo= VentanaMedicos()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
        dialogo.exec_()
    
    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.bottomLeft())

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()