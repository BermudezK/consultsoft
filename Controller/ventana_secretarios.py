import sys, re
from Model.administrador import Administrador
from Model.secretario import Secretario

from Controller.ventana_secretario import VentanaSecretario
from Controller.ventana_Editar_Secretario import VentanaEditarsecretario
from PyQt5.QtWidgets import   QApplication,QTableWidgetItem,QTableWidget,QPushButton,QHBoxLayout,QWidget,QDialog,QDesktopWidget
from PyQt5 import uic, QtCore, QtGui

class VentanaSecretarios (QDialog):
    def __init__(self,usuario):
        self.usuario=usuario
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
                    self.crearBotones(i)

    def crearBotones(self, fila):
        # Creo el layout que contendra a los botones
        caja = QHBoxLayout()
        # Creo los botones
        botonEditar = QPushButton()
        # Agrega un icono a los botones
        
        estiloBasicoBoton = """
        .QPushButton{
            border:none;
            background-color: transparent;}
        """
        botonEditar.setStyleSheet(estiloBasicoBoton)
  
        
        botonEditar.setIcon(QtGui.QIcon("./icons/edit.svg"))
     
        
        # Da el tamaño de los botones
        botonEditar.setMinimumSize(20,20)
        botonEditar.setMaximumSize(20,20)

        # Creo las acciones
  
        botonEditar.clicked.connect(lambda:self.editar(fila))
        
        # Agrego al contenedor los botones creados

        caja.addWidget(botonEditar)
        # Creo una elemento del tipo celda
        celda = QWidget()
        # Introduzco el layout con los botones dentro del tipo celda
        celda.setLayout(caja)
        # Agrego el elemento celda con los botones dentro de la tabpla en la pocicion (pocicion,4)
        self.tableWidget.setCellWidget(fila, 4, celda)


    def pb_agregarSecretario_on_click(self):
        dialog = VentanaSecretario()
        if dialog.exec_() == 0:
            self.cargarSecretariosALaTabla()


    def editar(self, fila):
        item = self.tableWidget.item(fila,0)
        datos = Administrador().traer_secretario(item.text())
        #Abre la ventana de edicion de turno
        # dni,nombre,apellido,telefono,id_usuario,usuario,password
        # P.personal_DNI, P.nombre,P.apellido, P.telefono, U.userName, U.password 
        secretario = Secretario(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6])
        dialogo = VentanaEditarsecretario(self.usuario,secretario)
        if dialogo.exec_()==0:
            self.cargarSecretariosALaTabla()




if __name__== '__main__':
    app = QApplication(sys.argv)
    dialogo=DSecretario()
    dialogo.show()
    app.exec_()
