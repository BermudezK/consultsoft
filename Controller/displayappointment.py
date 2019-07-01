import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic, QtCore
from Model.secretario import Secretario
from Controller.ventana_paciente import VentanaPaciente

class Displayappointment(QDialog):
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
     
      #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON agregar pacientes
      #def pb_agregarPaciente_on_click(self):
       #     dialogo=VentanaPaciente()
        #    if dialogo.exec_() == 0:
         #         self.cargarPacientesALaTabla()

        
if __name__== '__main__':
      app = QApplication(sys.argv)
      dialogo = VentanaPacientes()
      dialogo.show()
      app.exec_()