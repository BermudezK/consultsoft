import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QMessageBox, QTableWidget, QTableWidgetItem, QCompleter, QComboBox
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from Model.administrador import Administrador
from Controller.ventana_paciente import VentanaPaciente

#from PyQt5.QtCore import Qt, QSortFilterProxyModel
#from PyQt5.QtCore import QStringListModel
#aca agregar el rol de medico 


#este es el filtro
"""
class ExtendedComboBox(QComboBox):
    def _init_(self, parent=None):
        super(ExtendedComboBox, self)._init_(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # agregar un modelo de filtro para filtrar elementos iguales
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # agregue un  completer, que utiliza el filtro
        self.completer = QCompleter(self.pFilterModel, self)
        # mostrar todos los resultados (filtrados) 
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # conectar con el filtro
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)


    # al seleccionar un elemento del completer, selecciona el elemento que corresponde al combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))


    # cambio de modelo, actualiza los modelos del filtro y el completer
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    #en el cambio de la columna del modelo, actualiza la columna del modelo del filtro y el completer
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)    
"""
def crearBoton(self,posicion):
    		# Creo el layout que contendra a los botones
		caja = QHBoxLayout()
		# Creo los botones
		botonCancelar = QPushButton()
		botonaceptar = QPushButton()
		# Agrega un icono a los botones
		botonaceptar.setIcon(QtGui.QIcon("../icons/edit.svg"))
		botonCancelar.setIcon(QtGui.QIcon("../icons/delete.svg"))
		# Da el tamaño de los botones
		botonCancelar.setMinimumSize(20,20)
		botonCancelar.setMaximumSize(20,20)
		botonaceptar.setMinimumSize(20,20)
		botonaceptar.setMaximumSize(20,20)
		# Creo las acciones
		botonCancelar.clicked.connect(self.cancelar)
		botonaceptar.clicked.connect(self.aceptar)
		# Agrego al contenedor los botones creados
		caja.addWidget(botonCancelar)
		caja.addWidget(botonaceptar)
		# Creo una elemento del tipo celda
		celda = QWidget()
		# Introduzco el layout con los botones dentro del tipo celda
		celda.setLayout(caja)
		# Agrego el elemento celda con los botones dentro de la tabpla en la pocicion (pocicion,4)
		self.tablaTurnos.setCellWidget(posicion,4,celda)

	# Crear funcion para aceptar un turno
def aceptar(self):
            print("Aceptar")

	# Crear funcion para cancelar un turno
def cancelar(self):
	      print("cancelar")

class Displayappointment(QDialog):
      def __init__(self):
            QDialog.__init__(self)
            uic.loadUi('./View/displyappointment.ui', self)
            self.cargarPacientesALaTabla()
            #self.pb_cargarPaciente.clicked.connect(self.pb_agregarPaciente_on_click)
      
      def cargarPacientesALaTabla(self):
            pacientes = Administrador().obtener_pacientes()
            self.tablePaciente.setRowCount(len(pacientes))
            self.tablePaciente.setEditTriggers(QTableWidget.NoEditTriggers)
           
            for i in range(len(pacientes)):
                paciente = pacientes[i]
                columna = 0
                for x in paciente:
                    item = QTableWidgetItem(str(x))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tablePaciente.setItem(i,columna, item)
                    self.crearBoton(i)#aca va el boton de aceptar o cancelar turno
                    columna = columna + 1
    


                    
if __name__== '__main__':
    app = QApplication(sys.argv)
    dialogo = Displayappointment()
    dialogo.show()
    app.exec_()
