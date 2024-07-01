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


# Listas globales
nombres = []
tipos = []
generos = []
servicios = []
pasajes = []
totales = []
descuentos = []

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
    try:
        option = int(input("-> "))
        if option == 1:
            # Nombre
            Menu1()
            print("Nombre del cliente")
            nombres.append(input("-> "))
            # tipo
            while True:
                Menu1()
                print("Tipo de cliente (1 o 2)")
                try:
                    usable = int(input("-> "))
                    if usable == 1 or usable == 2:
                        tipos.append(usable)
                        break
                    else:
                        print("*No es una opción válida*")
                        time.sleep(tiempo)
                except:
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
                try:
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
                except:
                    print("Opción no válida")
                    time.sleep(tiempo)
            # Cantidad de pasajes
            while True:
                Menu1()
                print("Cantidad De pasajes")
                try:
                    usable = int(input("-> "))
                    if usable > 0:
                        pasajes.append(usable)
                        subtotal *= usable
                        if usable == 1:
                            descuentos.append(0)
                            totales.append(subtotal)
                        elif usable >=2 and usable <= 5:
                            descuentos.append(10)
                            subtotal = subtotal - (subtotal*0.1)
                            totales.append(subtotal)
                        elif usable >= 6 and usable <= 10:
                            descuentos.append(15)                    
                            subtotal = subtotal - (subtotal*0.15)
                            totales.append(subtotal)
                        else:
                            descuentos.append(25)
                            subtotal = subtotal - (subtotal*0.2)
                            totales.append(subtotal)
                        break
                    else:
                        print("*Opción no valida, solo números mayores a 0*")
                        time.sleep(tiempo)            
                except:
                    print("*No es una opción válida*")
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
                try:
                    selector = int(input("-> "))
                    if selector == 1:
                        cantidad = len(servicios)
                        system("cls")
                        for i in range(cantidad):
                            centrar("Lista de ventas")
                            print(i+1, "°:")
                            print("Nombre: ",nombres[i])
                            print("Tipo de cliente: ", tipos[i])
                            print("Género: ", generos[i])
                            print("Tipo de servicio: ", servicios[i])
                            print("Pasajes comprados: ", pasajes[i])
                            print("Total: S/.", totales[i])
                            print("Descuento: ", descuentos[i])
                            espacio()
                    elif selector == 2:
                        centrar("Por género")
                        print("Masculino: ", generos.count("m"))
                        print("Femenino: ", generos.count("f"))

                        centrar("Por intervalos")

                        # Definir los intervalos
                        intervalos = [
                            (80, 1000),
                            (100, 800)
                        ]
                        # Contar números en cada intervalo
                        conteos = []
                        for intervalo in intervalos:
                            inicio, fin = intervalo
                            conteo = sum(1 for numero in totales if inicio <= numero < fin)
                            conteos.append(conteo)
                        print("80 a 1000: ", conteos[0])
                        print("100 a 800: ", conteos[1])

                        centrar("Por tipo de cliente")
                        print("Tipo 1: ", tipos.count(1))
                        print("Tipo 2: ", tipos.count(2))
                        centrar("Promedio de importes")
                        tipo1 = []
                        tipo2 = []
                        for index, i in enumerate(tipos):
                            if i == 1:
                                tipo1.append(totales[index])
                            else:
                                tipo2.append(totales[index])
                        print("Tipo 1: ", sum(tipo1)/len(tipo1))
                        print("Tipo 2: ", sum(tipo2)/len(tipo2))
                        centrar("Reporte acumulado")
                        print("Cantidad de ventas totales: ", len(totales))
                        print("Sumatoria total: S/.", sum(totales))
                    else:
                        break
                    espacio()
                    usable = input("*Preciona una tecla para continuar*")
                except:
                    print("*No es una opción válida*")
                    time.sleep(tiempo)

        elif option == 3:
            break
        else:
            print("Opción no valida")
    except:
        print("*No es una opción válida*")
        print()
        time.sleep(tiempo)