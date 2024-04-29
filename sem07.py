from os import system
import time

def espacio():
    print()
    print("*"*50)

def centrar(message):
    tamaño = len(message)
    a = round((50 - tamaño) / 2)
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
categorias = ["A", "B", "C", "D", "E"]
penalidad = [3, 5, 7, 9, 12]
decibeles = ["50 o menos", "51-70", "71-90", "91-110", "Más de 110"]
acumulado = 0
valor = None
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
                x = 0
                while x != 1:
                    CalcMenu()
                    print("*Escriba la Categoria*")
                    category = input("->")
                    for i in categorias:
                        if i == category.upper():
                            # LLamar al valor
                            x = 1
                            break
                        else:
                            centrar("ERROR")
                            centrar("Opción no válida")
                            espacio()
                            time.sleep(2)
                        
            case 2:
                system("cls")
                print("Reporte")
                time.sleep(2)
            case 3:
                break

