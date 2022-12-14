class Persona():
    def __init__(self, nombre, edad, sueldo, cargo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sueldo = sueldo
        self.__cargo = cargo
    
    def __str__(self):
        return "Nombre: {}\n Edad: {}\n Sueldo: {}\n Cargo: {}\n".format(self.__nombre, self.__edad, self.__sueldo, self.__cargo)

    def GetNombre(self):
        return self.__nombre
    def SetNombre(self, nombre):
        self.__nombre = nombre

    def GetEdad(self):
        return self.__edad
    def SetEdad(self, edad):
        self.__edad = edad

    def GetSueldo(self):
        return self.__sueldo
    def SetSueldo(self, sueldo):
        self.__sueldo = sueldo

    def GetCargo(self):
        return self.__cargo
    def SetCargo(self, cargo):
        self.__cargo = cargo