import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from Model.administrador import Administrador
from Model.medico import Medico

class VentanaMedico(QDialog):
    def __init__(self,usuario,medico=None):
        self.usuario = usuario
        QDialog.__init__(self)
        uic.loadUi("View/ventanaMedico.ui", self)
        self.medico = medico

        if isinstance(self.medico,Medico):
            self.campoDNI.setDisabled(True)
            self.labelFormMedico.setText('Editar medico')
            self.campoDNI.setText(str(self.medico.dni))
            self.campoNombre.setText(str(self.medico.nombre))
            self.campoApellido.setText(str(self.medico.apellido))
            self.campoTelefono.setText(str(self.medico.telefono))
            self.User.setText(str(self.medico.usuario))
            self.Password.setText(str(self.medico.password))
            self.Password2.setText(str(self.medico.password))

            
        #Al hacer focus en el campo ejecuta la funcion
        self.campoNombre.textChanged.connect(self.validar_nombre)
        self.campoApellido.textChanged.connect(self.validar_apellido)
        self.campoDNI.textChanged.connect(self.validar_DNI)
        self.campoTelefono.textChanged.connect(self.validar_telefono)
        self.User.textChanged.connect(self.validar_User)
        self.User.textChanged.connect(self.validar_Password)
        #self.User.textChanged.connect(self.validar_Password2)
        #Al hacer click en el boton ejecuta la funcion
        self.botonAceptar.clicked.connect(self.validar)
        self.botonCancelar.clicked.connect(self.closeEvent)

    #Almacena el campo DNI en la clase persona
    def validar_DNI(self):
        self.campoDNI.setMaxLength(8)
        dni = self.campoDNI.text()
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
        nombre = self.campoNombre.text()
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
        apellido = self.campoApellido.text()
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
        validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ\0-9]{2,45}$", User, re.I)
        if User == "":
            return False
        elif not validar:
            return False
        else:
            return True

    def validar_Password(self):
        self.Password.setMaxLength(8)
        self.Password2.setMaxLength(8)
        Password = self.Password.text()
        Password2 = self.Password2.text()
        validar = re.match("^[A-Z\sáéíóúàèìùäëïöüñ\0-9]{2,8}$", Password, re.I)
        validar = re.match(
            "^[A-Z\sáéíóúàèìùäëïöüñ\0-9]{2,8}$", Password2, re.I)
        if Password == "":
            return False
        elif Password != Password2:
            return False
        elif not validar:
            return False
        else:
            return True

    # Almacena los datos correctos en la Base de Datos

    def validar(self):

        if self.validar_DNI() and self.validar_nombre() and self.validar_apellido() and self.validar_User() and self.validar_Password() and self.validar_telefono():
            #Aca evaluo si el nombre de usuario existe y si el medico a cargar ya existe
            if isinstance(self.medico, Medico):
                if (self.medico.usuario != self.User.text() and self.usuario.existe_usuario(self.User.text())>0):
                    QMessageBox.warning(self, "Carga Erronea!!", "Nombre de Usuario ya existe")
                else:
                    nuevosDatos = {
                        'dni': self.campoDNI.text(),
                        'nombre': self.campoNombre.text(),
                        'apellido': self.campoApellido.text(),
                        'telefono': self.campoTelefono.text(),
                        'password': self.Password.text(),
                        'username': self.User.text(),
                    }
                    Administrador().modificar_medico(self.medico.dni, self.medico.usuario, nuevosDatos)
                    QMessageBox.information(self, "Carga completada.", "Se actualizo un Doctor correctamente.", QMessageBox.Discard)
                    self.close()
            else:
                if self.usuario.existe_usuario(self.User.text())>0:
                    QMessageBox.warning(self, "Carga Erronea!!", "Nombre de Usuario ya existe")
                elif (not isinstance(self.medico,Medico)) and  self.usuario.existe_personal(self.campoDNI.text(),3):
                    QMessageBox.warning(self, "Carga Erronea!!", "El medico ya existe") 
                else:
                    #Aca se carga medico
                    # def agregar_medico(self, dni,nombre,apellido,telefono,usuario,password):
                    self.usuario.agregar_medico(self.campoDNI.text(), self.campoNombre.text(),
                                                self.campoApellido.text(), self.campoTelefono.text(), self.User.text(), self.Password.text())
                    QMessageBox.information(
                        self, "Carga completada.", "Se creo un Doctor correctamente.", QMessageBox.Discard)
                    self.campoDNI.setText("")
                    self.campoApellido.setText("")
                    self.campoNombre.setText("")
                    self.campoTelefono.setText("")
                    self.User.setText("")
                    self.Password.setText("")
                    self.Password2.setText("")
                    self.campoDNI.setStyleSheet("border: 1px solid black")
                    self.campoApellido.setStyleSheet("border: 1px solid black")
                    self.campoNombre.setStyleSheet("border: 1px solid black")
                    self.campoTelefono.setStyleSheet("border: 1px solid black")
                    self.User.setStyleSheet("border: 1px solid black")
                    self.Password.setStyleSheet("border: 1px solid black")
                    self.Password2.setStyleSheet("border: 1px solid black")
        else:
            QMessageBox.warning(
                self, "Carga Erronea!!", "Valor incorrecto o campo vacio.", QMessageBox.Discard)
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
            if not self.validar_Password():
                self.Password2.setStyleSheet("border: 1px solid red;")
            else:
                self.Password2.setStyleSheet("border: 1px solid green;")
    #Cierra la ventana
    def closeEvent(self, event):
        self.close()

if __name__== '__main__':
    app = QApplication(sys.argv)
    dialogo = VentanaMedico()
    dialogo.show()
    app.exec_()
