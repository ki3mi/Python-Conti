import time
from os import system

def espacio():
    print()
    print("*"*50)

def centrar(message):
    tamaño = len(message)
    a = round((48 - tamaño) / 2)
    print("*"*a, message, "*"*a)

def Menu1():
    system("cls")
    espacio
    centrar("Datos del cliente")
    espacio

def validar(letra):
    estados = {
        "M":0,
        "m":0,
        "F":1,
        "f":1,
        "finish":0,
    }
    for i in estados:
        if letra == i:
            return(False)
        if i == "finish":
            print("*Opción no válida solo M o F*")
            time.sleep(0.2)
            return(True)


# Variables globales
nombres = []
tipos = []
generos = []
pasajes = []
servicios = []
totales = []
subtotal = None
tiempo = 0.8

while True:
    system("cls")
    espacio()
    centrar("Menu")
    espacio()
    print('''
1:  Registrar venta
2:  Reportar venta
3:  Salir
''')
    espacio
    # Opcion del menu
    print("*Seleccione una Opción*")
    option = int(input("-> "))

    # Opción
    if option == 1:
        # Nombre
        Menu1()
        print("Nombre del cliente")
        nombres.append(input("-> "))
        # tipo
        while True:
            Menu1()
            print("Tipo de cliente (1 o 2)")
            usable = int(input("-> "))
            if usable == 1 or usable == 2:
                tipos.append(usable)
                break
            else:
                print("*No es una opción válida*")
                time.sleep(tiempo)
        # genero
        Menu1()
        print("Genero del cliente (M o F)")
        validado = True
        while validado:
            usable = input("-> ")
            validado = validar(usable)
        generos.append(usable)
        # Servicio
        while True:
            Menu1()
            print('''
Tipo de servicio
1:  Imperial
2:  Vip
3:  Gold''')
            usable = int(input("-> "))
            if usable == 1 or usable == 2 or usable == 3:
                servicios.append(usable)
                if usable == 1:
                    subtotal = 50
                elif usable == 2:
                    subtotal = 60
                elif usable == 3:
                    subtotal = 70
                break
            else:
                print("No es una opción válida")
                time.sleep(tiempo)
        # Cantidad de pasajes
        while True:
            Menu1()
            print("Cantidad De pasajes")
            usable = int(input("-> "))
            if usable > 0:
                pasajes.append(usable)
                break
            else:
                print("*Opción no valida, solo números mayores a 0*")
                time.sleep(tiempo)
        
    elif option == 2:
        while True:
            system("cls")
            espacio()
            centrar("Reporte de ventas")
            espacio()

            print('''
1:  Mostrar todas las ventas
2:  Mostrar reporte acumulado
3:  Salir
''')
            print("*Seleccione un opción*")
            selector = int(input("-> "))
            if selector == 1:
                cantidad = len(servicios)
                for i in range(cantidad):
                    system("cls")
                    centrar("Lista de ventas")

            elif selector == 2:
                pass
            else:
                break
            time.sleep(5)

    elif option == 3:
        break
    else:
        print("Opción no valida")



