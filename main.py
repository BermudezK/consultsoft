import sys, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QDialog
from PyQt5 import uic, QtCore
import platform

from Controller.ventana_secretarios import DSecretario

from Controller.ventana_pacientes import VentanaPacientes
from Controller.ventana_medicos import VentanaMedicos
from Controller.ventana_agenda import VentanaAgenda
from Controller.ventana_login import VentanaLogin
from Controller.ventana_turnos import VentanaTurnos
from Controller.ventana_turnosMedico import VentanaTurnoMedico
# from Controller.ventana_logOut import Ventana_logOut

class MainWindow (QMainWindow):
    def __init__(self, usuario):
        self.usuario = usuario
        
        QMainWindow.__init__(self)
        uic.loadUi('View/home.ui',self)
        self.L_userName.setText(self.usuario[5] + ", " + self.usuario[6])
        if platform.system() == "Linux":
            self.center()
        self.pb_agenda.clicked.connect(self.pb_agenda_on_click)
        self.pb_secretarios.clicked.connect(self.pb_secretarios_on_click)
        self.pb_pacientes.clicked.connect(self.pb_pacientes_on_click)
        self.pb_medicos.clicked.connect(self.pb_medicos_on_click)
        self.pb_turnos.clicked.connect(self.pb_turnos_on_click)
        self.pb_logOut.clicked.connect(self.pb_logOut_on_click)

        if self.usuario[3] == 1: #Administrador
            self.pb_agenda.hide()
            self.pb_pacientes.hide()
            self.pb_secretarios.show()
            self.pb_medicos.show()
            self.pb_turnos.hide()
        elif self.usuario[3] == 2: #Secretario
            self.pb_agenda.show()
            self.pb_pacientes.show()
            self.pb_secretarios.hide()
            self.pb_medicos.show()
            self.pb_turnos.show()
            self.verAgenda()             
        elif self.usuario[3] == 3: #Medico
            self.pb_turnos.show()
            self.pb_turnos.setStyleSheet("""
                #pb_turnos {
                background-color: #00796b;
            }
            """)
            self.pb_agenda.hide()
            self.pb_pacientes.hide()
            self.pb_secretarios.hide()
            self.pb_medicos.hide()
            self.verMisTurnos()

    def verMisTurnos(self):
        dialogo=VentanaTurnoMedico()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
    
    def verAgenda(self):
         # abrir la agenda
        dialogo=VentanaAgenda()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()

    #DEFINIMOS EL METODO PARA VER LOS TURNOS Y FILTRARLOS
    def pb_turnos_on_click (self):
        if self.usuario[3]== 2:
            # si es secretarios mira los turnos para aplicar filtros
            dialogo=VentanaTurnos(self.usuario)
        else:
            # si es medicos mira su turno para dar de baja
            dialogo =VentanaTurnoMedico()
            pass
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
        self.panel.setStyleSheet("""
            #pb_turnos {
                background-color: #00796b;
            }
            #pb_agenda, #pb_medicos,#pb_pacientes, #pb_secretarios{
                background-color: #263238;
            }
            #pb_turnos:hover, #pb_agenda:hover,#pb_medicos:hover,
            #pb_pacientes:hover, #pb_secretarios:hover{
                background-color: #00796b;
            }
        """)

    # DEFINIMOS EL METODO PARA PODER VER EL CALENDARIO
    def pb_agenda_on_click(self):
        dialogo=VentanaAgenda()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
        self.panel.setStyleSheet("""
            #pb_agenda {
                background-color: #00796b;
            }
            #pb_turnos,#pb_medicos,#pb_pacientes, #pb_secretarios{
                background-color: #263238;
            }
            #pb_turnos:hover,#pb_agenda:hover,#pb_medicos:hover,
            #pb_pacientes:hover, #pb_secretarios:hover{
                background-color: #00796b;
            }
        """)
    
    #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON SECRETARIOS
    def pb_secretarios_on_click(self):
        dialogo=VentanaTurno()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
        self.panel.setStyleSheet("""
            #pb_secretarios {
                background-color: #00796b;
            }
            #pb_medicos,#pb_turnos,#pb_pacientes, #pb_agenda{
                background-color: #263238;
            }
            #pb_agenda:hover,#pb_turnos:hover,#pb_medicos:hover,
            #pb_pacientes:hover, #pb_agenda:hover{
                background-color: #00796b;
            }
        """)
    
    #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON PACIENTES
    def pb_pacientes_on_click(self):
        dialogo=VentanaPacientes()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
        self.panel.setStyleSheet("""
            #pb_pacientes {
                background-color: #00796b;
            }
            #pb_medicos,#pb_turnos,#pb_secretarios, #pb_agenda{
                background-color: #263238;
            }
            #pb_agenda:hover,#pb_medicos:hover,#pb_turnos:hover,
            #pb_secretarios:hover, #pb_agenda:hover{
                background-color: #00796b;
            }
        """)
    #DEFINIMOS EL METODO PARA QUE ESCUCHE CUANDO Se HAce CLICK EN EL BOTON MEDICOS
    def pb_medicos_on_click(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo= VentanaMedicos()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()
        self.panel.setStyleSheet("""
            #pb_medicos {
                background-color: #00796b;
            }
            #pb_pacientes,#pb_turnos,#pb_secretarios, #pb_agenda{
                background-color: #263238;
            }
            #pb_agenda:hover,#pb_turnos:hover,#pb_pacientes:hover,
            #pb_secretarios:hover, #pb_agenda:hover{
                background-color: #00796b;
            }
        """) 

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.bottomLeft())
        self.pb_agenda_on_click

    # def pb_logOut_on_click(self):
    #     dialogo = Ventana_logOut()
    #     dialogo.exec_()
    #     return None
    #     self.mdiArea.closeActiveSubWindow()
    #     dialogo = Ventana_logOut()
    #     dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    #     self.mdiArea.addSubWindow(
    #         dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
    #     dialogo.showMaximized()
    #     self.panel.setStyleSheet("""
    #         #pb_medicos {
    #             background-color: #00796b;
    #         }
    #         #pb_pacientes,#pb_secretarios, #pb_agenda{
    #             background-color: #263238;
    #         }
    #         #pb_agenda:hover,#pb_pacientes:hover,
    #         #pb_secretarios:hover, #pb_agenda:hover{
    #             background-color: #00796b;
    #         }
    #     """)

if __name__== '__main__':
    app = QApplication(sys.argv)
    login = VentanaLogin()
    ejec = login.exec_()
    if ejec == QDialog.Accepted:
        print(login.usuario)
        window = MainWindow(login.usuario)
        window.show()
        app.exec_()
