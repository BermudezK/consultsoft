from Model.persona import Persona

class Paciente (Persona):
    def __init__(self, dni=None,nombre=None,apellido=None,telefono=None,id_usuario=None,usuario=None,password=None):
        super(Paciente,self).__init__(dni,nombre,apellido,telefono)