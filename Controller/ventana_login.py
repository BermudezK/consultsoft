import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from Model.administrador import Administrador
from Model.personal_query import logIn

class VentanaLogin(QDialog):
  def __init__(self):
    QDialog.__init__(self)
    uic.loadUi("View/ventanaLogin.ui", self)

    self.User.textChanged.connect(self.validar_User)
    self.Password.textChanged.connect(self.validar_Password)

    self.botonAcceder.clicked.connect(self.submitAcceder)

  def validar_User(self):
    self.User.setMaxLength(45)
    User = self.User.text()
    validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ\0-9]{2,45}$", User, re.I)
    if User == "":
      return False
    elif not validar:
      return False
    else:
      return True

  def validar_Password(self):
    self.Password.setMaxLength(8)
    Password = self.Password.text()
    validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ\0-9]{2,8}$", Password, re.I)
    
    if Password == "":
      return False
    elif not validar:
      return False
    else:
      return True

  def submitAcceder(self):
    if self.validar_Password() and self.validar_User():
      print('Ok')

    else:
      print('Mal')

    styleValid = "border: 1px solid green; background-color: transparent;"
    styleInvalid = "border: 1px solid red; background-color: transparent;"

    if self.validar_Password():
      self.Password.setStyleSheet(styleValid)
    else: 
      self.Password.setStyleSheet(styleInvalid)

    if self.validar_User():
      self.User.setStyleSheet(styleValid)
    else:
      self.User.setStyleSheet(styleInvalid)

    # SI YA TIENEN LA INFORMACION DE LOS USUARIOS PORQUE NO MANEJARLOS COMO UN OBJETO DE LA 
    # CLASE USUARIO??????????
    self.usuario = logIn(userName=self.User.text(), password=self.Password.text())    
    if self.usuario:
      # usuario_id, username, personal_dni, rol_id, nombre_rol, nombre, apellido = self.usuario
      # print(usuario_id, username, personal_dni, rol_id, nombre_rol, nombre, apellido)
      # # QMessageBox.information(self, f"Bienvenido {apellido}, {nombre}. Rol {nombre_rol}", QMessageBox.Discard)
      
      # SI ES CORRECTO LA VENTANA QUEDARÁ EN ACEPTADO, porfa no tocar esta linea
      self.accept()
    else:
      QMessageBox.warning(self,"Ingreso", "¡Disfrute de nuestro sistema nae!!")

if __name__== '__main__':
    app = QApplication(sys.argv)
    dialogo = VentanaLogin()
    dialogo.show()
    app.exec_()
