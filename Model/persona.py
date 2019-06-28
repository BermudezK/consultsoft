class Persona:
    def __init__(self, dni=None, nombre=None, apellido=None, telefono=None):
        self.setDNI(dni)
        self.setNombre(nombre)
        self.setApellido(apellido)
        self.setTelefono(telefono)

    def setDNI(self,dni):
        self._dni= dni
    def setNombre(self,nombre):
        self._nombre=nombre
    def setApellido(self,apellido):
        self._apellido=apellido
    def setTelefono(self,telefono):
        self._telefono=telefono
    
    def getDNI(self):
        return self._dni
    def getNombre(self):
        return self._nombre
    def getApellido(self):
        return self._apellido
    def getTelefono(self)    :
        return self._telefono
    
    dni = property(fget=getDNI, fset=setDNI)
    nombre = property(fget=getNombre, fset=setNombre)
    apellido = property(fget=getApellido, fset=setApellido)
    telefono = property(fget=getTelefono, fset=setTelefono)
