from Model.connection import (
    select_turnos,filtrar_por_turno,filtrar_por_paciente,filtrar_por_medico,
    obtenerTurnos,obtener_turno, filtrar_por_fecha,filtrar_para_medico, filtrar_por_fechaHora)


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
        return self._nro_turno
    def getPaciente (self):
        return self._paciente
    def getMedico(self):
        return self._medico
    def getFechayHora(self):
        return self._fechaYhora
    def getEstado(self):
        return self._estado

    nro_turno = property (fget = getNro_Turno , fset = setNro_Turno )
    paciente = property (fget = getPaciente , fset = setPaciente )
    medico = property (fget = getMedico , fset = setMedico )
    fechaYhora = property (fget = getFechayHora , fset = setFechayHora )
    estado = property (fget = getEstado , fset = setEstado )

    def filtrarTurno(self, idTurno):
        #En caso de que el campo este vacio muestra todos los turnos
        if idTurno == "":
            return select_turnos()
        else:
            return filtrar_por_turno(idTurno)

    def filtrarPaciente(self, nombrePaciente):
        return filtrar_por_paciente(nombrePaciente)

    def filtrarMedico(self, nMedico):
        return filtrar_por_medico(nMedico)
        
    def mostrar_turnos(self, desde=None, hasta=None):
        if desde == None and hasta == None:
            return select_turnos()
        else:
            return obtenerTurnos(desde, hasta)


    def filtrarFecha(self, fechabuscada):
        return filtrar_por_fecha(fechabuscada)

    def filtrarFechaHora(self, fechaHora):
            return filtrar_por_fechaHora(fechaHora)

    def mostrar_turnos_medico(self, medico):
            return filtrar_para_medico(medico)

# ----- TRAER UN TURNO DE UNA FILA ----
    
    def traerTurno(self,paciente):
        return obtener_turno(paciente)
