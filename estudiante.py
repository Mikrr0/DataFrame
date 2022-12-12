from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, cargo, sueldo, carrera):
        super().__init__(nombre, edad, cargo, sueldo)
        self.__carrera = carrera
    
    def __str__(self):
        return super().__str__()+"Carrera: {}\n".format(self.__carrera)

    def GetCarrera(self):
        return self.__carrera
    def SetCarrera(self, carrera):
        self.__carrera = carrera