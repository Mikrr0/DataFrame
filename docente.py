from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, edad, sueldo, cargo, grado, institucion):
        super().__init__(nombre, edad, cargo, sueldo)
        self.__grado = grado
        self.__institucion = institucion

    def __str__(self):
        return super().__str__()+"Grado: {}\n Institución Asociada: {}".format(self.__grado, self.__institucion)

    def GetGrado(self):
        return self.__grado
    def SetGrado(self, grado):
        self.__grado = grado

    def GetInstitucion(self):
        return self.__institucion
    def SetInstitucion(self, institucion):
        self.__institucion = institucion

