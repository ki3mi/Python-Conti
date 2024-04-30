from os import system
import time

def espacio():
    print()
    print("*"*50)

def centrar(message):
    tamaño = len(message)
    a = round((48 - tamaño) / 2)
    print("*"*a, message, "*"*a)

def Extremos(message1, message2):
    tamaño = len(message1) + len(message2)
    a = round(50 - tamaño)
    print(message1, "."*a, message2)
def Derecha(message):
    tamaño = len(message)
    tamaño = round(50 - tamaño)
    print("*"*tamaño, message)

def Izquierda(message):
    tamaño = len(message)
    tamaño = round(50 - tamaño)
    print(message, "*"*tamaño)

def CalcMenu():
    system("cls")
    espacio()
    centrar("Calcular")
    espacio()
    
categorias = ["A", "B", "C", "D", "E","F"]
penalidad = {"A":3, "B":5, "C":7, "D":9, "E":12}
decibeles = {"A":"50 o menos", "B":"51-70", "C":"71-90", "D":"91-110", "E":"Más de 110"}
acumulado = 0
valor = None
usable = None

# Almacen
reportCat = []
reportMon = []
reportPen = []

# Programa
while True:
    system("cls")
    espacio()
    centrar("Menú principal")
    espacio()
    print('''
1.  Calcular
2.  Reporte
3.  Salir

''')
    print("*Elija una opción*")
    option = int(input("-> "))
    if option > 3 or option < 1:
        print("Opción no valida")
        time.sleep(1)
    else:
        match option:
            case 1:
                CalcMenu()
                print("Ingrese el monto base")
                montoB = float(input("-> "))
                system("cls")
                CalcMenu()
                print("Ingrese el tipo de cambio actual")
                cambio = float(input("-> "))
                x = 0
                while x != 1:
                    CalcMenu()
                    print("*Escriba la Categoria*")
                    print(categorias)
                    category = input("-> ")
                    for i in categorias:
                        if i == category.upper():
                            # LLamar al valor
                            montoB *= cambio
                            acumulado = montoB * (penalidad[i]/100)
                            reportPen.append(montoB * (penalidad[i]/100))
                            reportCat.append(i)
                            reportMon.append(montoB)
                            usable = i
                            x = 1
                            break
                        elif i == "F":
                            system("cls")
                            centrar("ERROR")
                            centrar("Opción no válida")
                            espacio()
                            time.sleep(2)
            case 2:
                system("cls")
                espacio()
                centrar("Reporte")
                espacio()
                print
                print("Reporte Acumulado: S/.", acumulado)
                print('*Escriba "S" si quiere ver el Historial*')
                print("*Escriba cualquier otra tecla para salir*")
                option3 = input("-> ")
                if option3.upper() == "S":
                    system("cls")
                    centrar("Historial de Reportes")
                    for i in range(len(reportCat)):
                        print("-> ",i+1,":")
                        print("Monto Base: S/.",reportMon[i])
                        print("Monto Base: S/.",reportPen[i])
                        print("Categoria: ",reportCat[i])
                        print("Ruido en Decibeles: ",decibeles[reportCat[i]])
                    espacio()
                    z = input("*Preciona cualquier tecla para continuar* \n")
                else:
                    pass
            case 3:
                system("cls")
                espacio()
                centrar("Adios")
                centrar("Estudiante")
                centrar("Ccente Mejia Jose Carlos")
                espacio()
                time.sleep(2)
                system("cls")
                break

