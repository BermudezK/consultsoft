import sys, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QDialog
from PyQt5 import uic, QtCore
import platform
from Model.administrador import Administrador
from Model.secretario import Secretario
from Model.medico import Medico

from Controller.ventana_secretarios import VentanaSecretarios
from Controller.ventana_pacientes import VentanaPacientes
from Controller.ventana_medicos import VentanaMedicos
from Controller.ventana_agenda import VentanaAgenda
from Controller.ventana_login import VentanaLogin
from Controller.ventana_turnos import VentanaTurnos
from Controller.ventana_turnosMedico import VentanaTurnoMedico
from Controller.ventana_logOut import Ventana_logOut


class MainWindow (QMainWindow):
    def __init__(self, usuario):        
        QMainWindow.__init__(self)
        uic.loadUi('View/home.ui',self)

        if usuario[7] == 1: #Administrador
            # (dni,nombre,apellido,telefono,id_usuario,usuario,password)
            self.usuario = Administrador(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6])     
            self.pb_agenda.hide()
            self.pb_pacientes.hide()
            self.pb_secretarios.show()
            self.pb_medicos.show()
            self.pb_turnos.hide()
            self.verLosMedicos()

        elif usuario[7] == 2: #Secretario
            self.usuario = Secretario(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6])
            self.pb_agenda.show()
            self.pb_pacientes.show()
            self.pb_secretarios.hide()
            self.pb_medicos.show()
            self.pb_turnos.show()
            self.verAgenda()             
        elif usuario[7] == 3: #Medico
            self.usuario = Medico(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6])
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
        
        self.L_userName.setText(self.usuario.nombre + ", " + self.usuario.apellido)
        self.pb_agenda.clicked.connect(self.pb_agenda_on_click)
        self.pb_secretarios.clicked.connect(self.pb_secretarios_on_click)
        self.pb_pacientes.clicked.connect(self.pb_pacientes_on_click)
        self.pb_medicos.clicked.connect(self.pb_medicos_on_click)
        self.pb_turnos.clicked.connect(self.pb_turnos_on_click)
        self.pd_logOut.clicked.connect(self.pb_logOut_on_click)

    def verMedicos(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo=VentanaMedicos()
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()

    def verMisTurnos(self):
        self.mdiArea.closeActiveSubWindow()
        dialogo=VentanaTurnoMedico(self.usuario)
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()

    def verLosMedicos(self):
            self.mdiArea.closeActiveSubWindow()
            dialogo=VentanaMedicos(self.usuario)
            dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
            dialogo.showMaximized()

    def verAgenda(self):
         # abrir la agenda
        self.mdiArea.closeActiveSubWindow()
        dialogo=VentanaAgenda(self.usuario)
        dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        dialogo.showMaximized()

    #DEFINIMOS EL METODO PARA VER LOS TURNOS Y FILTRARLOS
    def pb_turnos_on_click (self):
        self.mdiArea.closeActiveSubWindow()
        if isinstance(self.usuario, Secretario):
            # si es secretarios mira los turnos para aplicar filtros
            dialogo=VentanaTurnos(self.usuario)
            dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.mdiArea.addSubWindow(dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
            dialogo.showMaximized()
        else:
            # si es medicos mira su turno para dar de baja
            self.verMisTurnos()
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
        self.mdiArea.closeActiveSubWindow()
        dialogo=VentanaAgenda(self.usuario)
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
        self.mdiArea.closeActiveSubWindow()
        dialogo=VentanaSecretarios(self.usuario)
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
        self.mdiArea.closeActiveSubWindow()
        dialogo=VentanaPacientes(self.usuario)
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
        dialogo= VentanaMedicos(self.usuario)
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

    def pb_logOut_on_click(self):
        dialogo = Ventana_logOut()
        ejecLogout = dialogo.exec_()

        if ejecLogout == QDialog.Accepted:
            self.mdiArea.close()
            self.close()
            # login = VentanaLogin()
            # ejecLogin = login.exec_()
            
        
        # self.mdiArea.closeActiveSubWindow()
        # dialogo = Ventana_logOut()
        # dialogo.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # self.mdiArea.addSubWindow(
        #     dialogo, QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        # dialogo.showMaximized()
        # self.panel.setStyleSheet("""
        #     #pb_medicos {
        #         background-color: #00796b;
        #     }
        #     #pb_pacientes,#pb_secretarios, #pb_agenda{
        #         background-color: #263238;
        #     }
        #     #pb_agenda:hover,#pb_pacientes:hover,
        #     #pb_secretarios:hover, #pb_agenda:hover{
        #         background-color: #00796b;
        #     }
        # """)

if __name__== '__main__':
    app = QApplication(sys.argv)
    ejecLogin = True

    while ejecLogin:
        login = VentanaLogin()
        ejecLogin = login.exec_()

        if ejecLogin == QDialog.Accepted:
            window = MainWindow(login.usuario)
            window.show()
            app.exec_()
            window.close()
