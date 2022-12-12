import pandas as pd
from openpyxl import Workbook
from docente import Docente
import random

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
    for i in range(len(archivo.index)):
        archivo["Grado"] = archivo["Nombres"].apply(lambda x: random.choice(grado))
    archivo = archivo.drop(columns=["Carrera"])
    docente = archivo.loc[:,"Cargo"] == "Docente"
    archivo_docente = archivo.loc[docente]
    print(archivo_docente)

def estudiante(archivo):
    global archivo_estudiante

    carrera = ["Periodismo", "Diseño Gráfico", "Ingeniería informática", "Ingeniería industrial", "Ingeniería en minas", "Arquitectura"]
    for i in range(len(archivo.index)):
        archivo["Carrera"] = archivo["Nombres"].apply(lambda x: random.choice(carrera))
        estudiante = archivo.loc[:,"Cargo"] == "Estudiante"
        archivo_estudiante = archivo.loc[estudiante]
        print(archivo_estudiante)


def crear_excel(archivo, persona, cont):
    x=0
    while x==0:

        archivo_excel = pd.ExcelWriter(f'{persona}{cont}.xlsx')
        archivo.to_excel(archivo_excel, index = False)
        archivo_excel.save()

        x=1

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
                    key1 = 1
                    break
                if opcion == 4 and acceso == 1 and key1 == 1:
                    docente(archivo)
                    key2 = 1
                    break
                if opcion == 5 and acceso == 1 and key1 == 1 and key2 == 1:
                    cont=cont+1
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