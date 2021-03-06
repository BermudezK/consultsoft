import sys
import re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from Model.personal import Personal

class VentanaLogin(QDialog):
  def __init__(self):
    QDialog.__init__(self)
    uic.loadUi("View/ventanaLogin.ui", self)
    
    self.Password.textChanged.connect(self.validar_Password)

    self.botonAcceder.clicked.connect(self.submitAcceder)

  def validar_User(self):
    return len(self.User.text()) == 0
  
  def validar_Password(self):
    return len(self.Password.text()) == 0
    

  def submitAcceder(self):
    message = ''
    if self.validar_Password():
      message += '¡La contraseña es requerida!\n'
    if self.validar_User():
      message += '¡El usuario es requerido!\n'

    if not self.validar_Password() and not self.validar_User():
      self.usuario = Personal.logIn(self.User.text(), self.Password.text())
      if self.usuario:
        self.accept() # si lo descomento no funciona
      else:
        QMessageBox.warning(self, "¡Login incorrecto!", "¡El usuario o contraseña es incorrecto!", QMessageBox.Ok)
        
    else:
      QMessageBox.warning(self, "Error", message, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = VentanaLogin()
    dialogo.show()
    app.exec_()
