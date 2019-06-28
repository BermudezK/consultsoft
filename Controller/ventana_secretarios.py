import sys, re
from Model.administrador import Administrador
from Controller.ventana_secretario import VentanaSecretario
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem,QPushButton,QHBoxLayout
from PyQt5 import uic, QtCore

class DSecretario (QDialog):
    def __init__(self):
        QDialog.__init__(self)

        #CARGO EL FORMULARIO
        uic.loadUi('View/ventanaSecretarios.ui',self)
        self.cargarSecretariosALaTabla()
        self.pb_cargarSecretario.clicked.connect(self.pb_agregarSecretario_on_click)

    def cargarSecretariosALaTabla(self):
        # como el fin principal de este formulario es el de ver los secretarios del sistema 
        # debemos pedirle (como controlador) al modelo que nos dé los secretarios existentes
        secretarios = Administrador().obtener_secretarios()
        # #una vez obtenidos todos los secretarios cargados en el sistema debemos
        # # agregarlos a nuestra vista
        # # calculamos el total de filas que tendra nuestra tabla deacuerdo a la cantidad de secretarios
        self.tableWidget.setRowCount(len(secretarios))

        for i in range(len(secretarios)):
                secretario = secretarios[i]
                columna = 0
                for x in secretario:
                    item = QTableWidgetItem(str(x))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i,columna, item)
                    columna = columna + 1
    def pb_agregarSecretario_on_click(self):
        dialog = VentanaSecretario()
        if dialog.exec_() == 0:
            self.cargarSecretariosALaTabla()


if __name__== '__main__':
    app = QApplication(sys.argv)
    dialogo=DSecretario()
    dialogo.show()
    app.exec_()
