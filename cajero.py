import time
from os import system
def espacio():
    print()
    print("*"*52)

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

# def Animate():
#     x = None
#     while True:
#         system("cls")
#         espacio()
#         centrar("BCP")
#         espacio()
#         x = input("*Precione un tecla para continuar*")
#         if x is None:
#             pass
#         else:
#             break
#         time.sleep(0.2)
#         system("cls")
#         espacio()
#         centrar("_BC")
#         espacio()
#         x = input("*Precione un tecla para continuar*")
#         if x is None:
#             pass
#         else:
#             break
#         time.sleep(0.2)
#         system("cls")
#         espacio()
#         centrar("__B")
#         espacio()
#         x = input("*Precione un tecla para continuar*")
#         if x is None:
#             pass
#         else:
#             break
#         time.sleep(0.2)
#         system("cls")
#         espacio()
#         centrar("___")
#         espacio()
#         x = input("*Precione un tecla para continuar*")
#         if x is None:
#             pass
#         else:
#             break
#         time.sleep(0.2)
#         system("cls")
#         espacio()
#         centrar("P__")
#         espacio()
#         x = input("*Precione un tecla para continuar*")
#         if x is None:
#             pass
#         else:
#             break
#         time.sleep(0.2)
#         system("cls")
#         espacio()
#         centrar("CP_")
#         espacio()
#         x = input("*Precione un tecla para continuar*")
#         if x is None:
#             pass
#         else:
#             break

sueldo = 12000.00
while True:
    espacio()
    centrar("Cajero XD")
    espacio()
    centrar("Elije una opción")
    print('''
1: Depositar
2: Retirar
3: Ver Saldo
4: Salir
    ''')
    option = int(input("-> "))
    match option:
        case 1:
            centrar("Depositar")
            x = float(input("Cantidad: "))
            sueldo += x
            system("cls")
            espacio()
            centrar("Desposito Listo")
            espacio()
            time.sleep(1)
            system("cls")
        case 2:
            centrar("Retirar")
            print("Saldo Actual: S/. ",sueldo)
            espacio()
            x = float(input("Cantidad: "))
            if sueldo >= x:
                sueldo -= x
                system("cls")
                espacio()
                centrar("Retiro efectuado")
                espacio()
                time.sleep(1)
                system("cls")
            else:
                system("cls")
                espacio()
                centrar("ERROR")
                centrar("Saldo insuficiente")
                espacio()
                time.sleep(1.5)
                system("cls")
        case 3:
            system("cls")
            centrar("Saldo Actual")
            print("S/.",sueldo ,"\n")
            z = input("*Preciona cualquier tecla para continuar* \n")
            system("cls")
        case 4:
            system("cls")
            espacio()
            centrar("Hasta la próxima")
            espacio()
            time.sleep(1)
            system("cls")
            break


    

