from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, edad, cargo, sueldo, grado):
        super().__init__(nombre, edad, cargo, sueldo)
        self.__grado = grado

    def __str__(self):
        return super().__str__()+"Grado: {}\n".format(self.__grado)

    def GetGrado(self):
        return self.__grado
    def SetGrado(self, grado):
        self.__grado = grado
