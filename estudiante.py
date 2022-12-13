from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, sueldo, cargo, carrera, nota):
        super().__init__(nombre, edad, sueldo, cargo)
        self.__carrera = carrera
        self.__nota = nota
    
    def __str__(self):
        return super().__str__()+"Carrera: {}\n Nota Final: {}".format(self.__carrera, self.__nota)

    def GetCarrera(self):
        return self.__carrera
    def SetCarrera(self, carrera):
        self.__carrera = carrera
    
    def GetNota(self):
        return self.__nota
    def SetNota(self, nota):
        self.__nota = nota