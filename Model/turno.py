from Model.turno_query import obtenerTurnos

class Turno():
    def __init__(self, nro_turno=None, paciente=None, medico=None, fechaYhora=None, estado=None):
        self.setNro_Turno(nro_turno)
        self.setPaciente(paciente)
        self.setMedico(medico)
        self.setFechayHora(fechaYhora)
        self.setEstado(estado)
    
    def setNro_Turno (self, nro_turno):
        self._nro_turno = nro_turno
    def setPaciente (self,paciente):
        self._paciente = paciente
    def setMedico(self,medico):
        self._medico = medico
    def setFechayHora(self,fechaYhora):
        self._fechaYhora = fechaYhora
    def setEstado(self,estado):
        self._estado = estado

    def getNro_Turno (self):
        return _nro_turno
    def getPaciente (self):
        return _paciente
    def getMedico(self):
        return _medico
    def getFechayHora(self):
        return _fechaYhora
    def getEstado(self):
        return _estado

    nro_turno = property (fget = getNro_Turno , fset = setNro_Turno )
    paciente = property (fget = getPaciente , fset = setPaciente )
    medico = property (fget = getMedico , fset = setMedico )
    fechaYhora = property (fget = getFechayHora , fset = setFechayHora )
    estado = property (fget = getEstado , fset = setEstado )

    def mostrar_turnos(self, desde, hasta):
        return obtenerTurnos(desde, hasta)
