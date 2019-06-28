import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from Model.administrador import Administrador

class VentanaMedico(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("./View/ventanaMedico.ui",self)
        #Al hacer focus en el campo ejecuta la funcion
        self.campoNombre.textChanged.connect(self.validar_nombre)
        self.campoApellido.textChanged.connect(self.validar_apellido)
        self.campoDNI.textChanged.connect(self.validar_DNI)
        self.campoTelefono.textChanged.connect(self.validar_telefono)
        self.User.textChanged.connect(self.validar_User)
        self.User.textChanged.connect(self.validar_Password)
        #Al hacer click en el boton ejecuta la funcion
        self.botonAceptar.clicked.connect(self.validar)
        self.botonCancelar.clicked.connect(self.closeEvent)

    #Almacena el campo DNI en la clase persona 
    def validar_DNI(self):
        self.campoDNI.setMaxLength(8)
        dni=self.campoDNI.text()
        validar = re.match("^[0-9]{8,8}$", dni, re.I)
        if dni == "":
            return False
        elif not validar:
            return False
        else:
            return True

    #Almacena el campo Nombre en la clase persona 
    def validar_nombre(self):
        self.campoNombre.setMaxLength(45)
        nombre=self.campoNombre.text()
        validar = re.match("^[A-Z]{1,45}$", nombre, re.I)
        if nombre == "":
            return False
        elif not validar:
            return False
        else:
            return True

    #Almacena el campo Apellido en la clase persona 
    def validar_apellido(self):
        self.campoApellido.setMaxLength(45)
        apellido=self.campoApellido.text()
        validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ]{2,45}$", apellido, re.I)
        if apellido == "":
            return False
        elif not validar:
            return False
        else:
            return True

    #Almacena el campo Telefono en la clase persona 
    def validar_telefono(self):
        self.campoTelefono.setMaxLength(13)
        telefono = self.campoTelefono.text()
        validar = re.match("^[0-9]{10,13}$", telefono, re.I)
        if telefono == "":
            return False
        elif not validar:
            return False
        else:
            return True

    #Almacena el campo Usuario en la clase persona 
    def validar_User(self):
        self.User.setMaxLength(45)
        User = self.User.text()
        validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ\0-9]{6,45}$", User, re.I)
        if User == "":
            return False
        elif not validar:
            return False
        else:
            return True

    def validar_Password(self):
        self.Password.setMaxLength(8)
        Password = self.Password.text()
        validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ\0-9]{4,8}$", Password, re.I)
        if Password == "":
            return False
        elif not validar:
            return False
        else:
            return True

    # Almacena los datos correctos en la Base de Datos
    def validar(self):
        if self.validar_DNI() and self.validar_nombre() and self.validar_apellido() and self.validar_User() and self.validar_Password() and self.validar_telefono():
            #Aca evaluo si el nombre de usuario existe y si el medico a cargar ya existe 
            if Administrador().comprobar_existencia(self.User.text()):
                QMessageBox.warning(self, "Carga Erronea!!","Nombre de Usuario ya existe")
            elif Administrador().comprobar_existencia(self.campoDNI.text()):
                QMessageBox.warning(self, "Carga Erronea!!","El medico ya existe")
            
            else:
                #Aca se carga medico
                # def agregar_medico(self, dni,nombre,apellido,telefono,usuario,password):
                Administrador().agregar_medico(self.campoDNI.text(),self.campoNombre.text(),self.campoApellido.text(),self.campoTelefono.text(),self.User.text(),self.Password.text())
                QMessageBox.information(self,"Carga completada.","Se creo un Doctor correctamente.",QMessageBox.Discard)
                self.campoDNI.setText("")
                self.campoApellido.setText("")
                self.campoNombre.setText("")
                self.campoTelefono.setText("")
                self.User.setText("")
                self.Password.setText("")
                self.campoDNI.setStyleSheet("border: 1px solid black")
                self.campoApellido.setStyleSheet("border: 1px solid black")
                self.campoNombre.setStyleSheet("border: 1px solid black")
                self.campoTelefono.setStyleSheet("border: 1px solid black")
                self.User.setStyleSheet("border: 1px solid black")
                self.Password.setStyleSheet("border: 1px solid black")
        else:
            QMessageBox.warning(self,"Carga Erronea!!","Valor incorrecto o campo vacio.",QMessageBox.Discard)
            if not self.validar_DNI():
                self.campoDNI.setStyleSheet("border: 1px solid red;")
            else: 
                self.campoDNI.setStyleSheet("border: 1px solid green;")
            if not self.validar_nombre():
                self.campoNombre.setStyleSheet("border: 1px solid red;")
            else: 
                self.campoNombre.setStyleSheet("border: 1px solid green;")
            if not self.validar_apellido():
                self.campoApellido.setStyleSheet("border: 1px solid red;")
            else:
                self.campoApellido.setStyleSheet("border: 1px solid green;")
            if not self.validar_telefono():
                self.campoTelefono.setStyleSheet("border: 1px solid red;")
            else:
                self.campoTelefono.setStyleSheet("border: 1px solid green;")
            if not self.validar_User():
                self.User.setStyleSheet("border: 1px solid red;")
            else:
                self.User.setStyleSheet("border: 1px solid green;")
            if not self.validar_Password():
                self.Password.setStyleSheet("border: 1px solid red;")
            else:
                self.Password.setStyleSheet("border: 1px solid green;")

    #Cierra la ventana
    def closeEvent(self,event):
        self.close()

if __name__== '__main__':
    app = QApplication(sys.argv)
    dialogo = VentanaMedico()
    dialogo.show()
    app.exec_()