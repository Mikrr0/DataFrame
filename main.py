import pandas as pd
import random

from openpyxl import Workbook #pip install openpyxl
from tabulate import tabulate #pip install tabulate

from docente import Docente
from estudiante import Estudiante

obj_docente = Docente
obj_estudiante = Estudiante

def carga_archivo():
    archivo = pd.read_csv("Solemne03.csv", usecols=["Nombres", "Edad", "Sueldo"])  #Abre archivo csv
    archivo = pd.DataFrame(archivo)

    print(archivo)
    filas = len(archivo.index) #Lee filas
    print("Filas:",filas)

def filtros():
    global archivo
    archivo = pd.read_csv("Solemne03.csv", usecols=["Nombres", "Edad", "Sueldo"])  #Abre archivo csv

    archivo = pd.DataFrame(archivo)

    archivo = archivo.dropna() #Elimina archivos NaN

    archivo = archivo.drop(archivo[(archivo["Nombres"] == "TRUE")].index) #Elimina datos TRUE

    archivo = archivo.drop(archivo[(archivo["Nombres"] == "FALSE")].index) #Elimina datos FALSE
 
    archivo = archivo.sort_values("Sueldo") #Ordena datos de menor a mayor de arriba hacia abajo

    archivo = archivo.drop_duplicates("Nombres", keep="last") #Elimina nombres duplicados y extrae el ultimo nombre registrado

    archivo = archivo.drop(archivo[(archivo["Edad"] > 120)].index) #Elimina edad mayor a 120

    archivo = archivo.drop(archivo[(archivo["Edad"] <= 0)].index) #Elimina edad menor e igual a 0

    cargos = ["Docente", "Estudiante"]
    for i in range(len(archivo.index)):
        archivo["Cargo"] = archivo["Nombres"].apply(lambda x: random.choice(cargos))

    print(archivo)
    filas = len(archivo.index) #Lee filas
    print("Filas:",filas)

def docente(archivo):
    global archivo_docente
    grado = ["Magister", "Doctorado", "Licenciado"]
    institucion = ["U Autónoma", "U Católica", "U de Talca", "U de Chile"]
    for i in range(len(archivo.index)):
        archivo["Grado"] = archivo["Nombres"].apply(lambda x: random.choice(grado)) #Elige de forma aleatoria elemento de la lista grado
    for i in range(len(archivo.index)):
        archivo["Institución"] = archivo["Nombres"].apply(lambda x: random.choice(institucion)) #Elige de forma aleatoria elemento de la lista institucion
    archivo = archivo.drop(columns=["Carrera"]) #Borra columna Carrera
    archivo = archivo.drop(columns=["Nota Final"]) #Borra columna Nota Final
    docente = archivo.loc[:,"Cargo"] == "Docente" #Selecciona dato Docente de la columna Cargo
    archivo_docente = archivo.loc[docente]
    print(archivo_docente)

def estudiante(archivo):
    global archivo_estudiante

    carrera = ["Periodismo", "Diseño Gráfico", "Ingeniería informática", "Ingeniería industrial", "Ingeniería en minas", "Arquitectura"]
    for i in range(len(archivo.index)):
        archivo["Carrera"] = archivo["Nombres"].apply(lambda x: random.choice(carrera)) #Elige de forma aleatoria elemento de la lista carrera
    for i in range(len(archivo.index)):
        archivo["Nota Final"]= archivo["Nombres"].apply(lambda x : round(random.uniform(1.0,7.0),2)) #Elige de forma aleatoria numeros entre 1.0 a 7.0 redondeando a 2 decimales
    estudiante = archivo.loc[:,"Cargo"] == "Estudiante" #Selecciona dato Estudiante de la columna Cargo
    archivo_estudiante = archivo.loc[estudiante] 
    print(archivo_estudiante)

def crear_excel(archivo, persona, cont):
    x=0
    while x==0:

        archivo_excel = pd.ExcelWriter(f'{persona}{cont}.xlsx')
        archivo.to_excel(archivo_excel, index = False)
        archivo_excel.save()

        x=1

def ListaToExcel(lista, objeto, persona, cont):
    global nuevo_dataframe
    lista.append(objeto)
    nuevo_dataframe = pd.DataFrame(lista)
    x = 0
    while x==0:

        archivo_excel = pd.ExcelWriter(f'{persona}{cont}.xlsx')
        nuevo_dataframe.to_excel(archivo_excel, index = False)
        archivo_excel.save()

        x=1

def ObjetoEstudiante(archivo):
    global lista_estudiante, obj_estudiante
    lista_estudiante = []
    nombre = archivo["Nombres"]
    edad = archivo["Edad"]
    sueldo = archivo["Sueldo"]
    cargo = archivo["Cargo"]
    carrera = archivo["Carrera"]
    nota = archivo["Nota Final"]
    obj_estudiante = Estudiante(nombre, edad, sueldo, cargo, carrera, nota)

def ObjetoDocente(archivo):
    global lista_docente, obj_docente
    lista_docente = []
    nombre = archivo["Nombres"]
    edad = archivo["Edad"]
    sueldo = archivo["Sueldo"]
    cargo = archivo["Cargo"]
    grado = archivo["Grado"]
    institucion = archivo["Institución"]
    obj_docente = Docente(nombre, edad, sueldo, cargo, grado, institucion)


def main():
    x = 0
    key1 = 0
    key2 = 0
    cont = 0
    acceso = 0
    while x == 0:
        while True:
            try:
                opcion = int(input("[1]Cargar archivo\n[2]Eliminar incoherencias\n[3]Crear lista 'Estudiante'\n[4]Crear lista 'Docente'\n[5]Crear archivo Excel\n[presione cualquier otro número para salir]\n"))
                if opcion == 1:
                    carga_archivo()
                    acceso = 1
                    break
                if opcion == 2 and acceso == 1:
                    filtros()
                    break
                if opcion == 3 and acceso == 1:
                    estudiante(archivo)
                    ObjetoEstudiante(archivo)
                    key1 = 1
                    break
                if opcion == 4 and acceso == 1 and key1 == 1:
                    docente(archivo)
                    ObjetoDocente(archivo)
                    key2 = 1
                    break
                if opcion == 5 and acceso == 1 and key1 == 1 and key2 == 1:
                    cont=cont+1
                    ListaToExcel(lista_docente, obj_docente, "Docente_Objeto", cont)
                    ListaToExcel(lista_estudiante, obj_estudiante, "Estudiante_Objeto", cont)
                    crear_excel(archivo_docente, "Docente", cont)
                    crear_excel(archivo_estudiante, "Estudiante", cont)
                    break
                if opcion >= 6 and acceso == 1:
                    x = 1
                    break
                if opcion >= 6 and acceso == 0:
                    x = 1
                    break
                else:
                    print("[------------------E R R O R------------------]")
                    print("Asegurese de:") 
                    print("Cargar el archivo")
                    print("Tener creada la lista de Estudiante y Docente en respectivo orden")
                    print("[---------------------------------------------]")
            except ValueError:
                print("Ingrese un dígito válido")

main()