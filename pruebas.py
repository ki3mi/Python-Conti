import time
import os

# Funciones auxiliares
def espacio():
    print()
    print("*" * 50)

def centrar(message):
    tamaño = len(message)
    a = round((48 - tamaño) / 2)
    print("*" * a, message, "*" * a)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu_principal():
    limpiar_pantalla()
    espacio()
    centrar("Sistema de Gestión de Ventas")
    espacio()
    print('''
1:  Ingresar nueva venta
2:  Ver reporte de ventas
3:  Salir
''')
    espacio()

def validar_genero(letra):
    estados = {
        "M": 0,
        "m": 0,
        "F": 1,
        "f": 1
    }
    if letra in estados:
        return False
    else:
        print("*Entrada inválida, use solo M o F*")
        time.sleep(0.2)
        return True

def obtener_tipo_cliente():
    while True:
        limpiar_pantalla()
        espacio()
        centrar("Tipo de cliente")
        espacio()
        print("Seleccione tipo de cliente (1 o 2)")
        try:
            usable = int(input("-> "))
            if usable == 1 or usable == 2:
                return usable
            else:
                print("*Opción no válida*")
                time.sleep(0.8)
        except ValueError:
            print("*Opción no válida*")
            time.sleep(0.8)

def obtener_tipo_servicio():
    while True:
        limpiar_pantalla()
        espacio()
        centrar("Tipo de servicio")
        espacio()
        print('''
    Tipos de servicio disponibles:
    1:  Imperial
    2:  Vip
    3:  Gold''')
        try:
            usable = int(input("-> "))
            if usable in [1, 2, 3]:
                return usable
            else:
                print("*Opción no válida*")
                time.sleep(0.8)
        except ValueError:
            print("*Entrada no válida*")
            time.sleep(0.8)

def obtener_cantidad_pasajes():
    while True:
        limpiar_pantalla()
        espacio()
        centrar("Cantidad de pasajes")
        espacio()
        print("Ingrese la cantidad de pasajes")
        try:
            usable = int(input("-> "))
            if usable > 0:
                return usable
            else:
                print("*Número inválido, debe ser mayor a 0*")
                time.sleep(0.8)
        except ValueError:
            print("*Entrada no válida*")
            time.sleep(0.8)

def mostrar_ventas(nombres, tipos, generos, servicios, pasajes, totales, descuentos):
    cantidad = len(servicios)
    limpiar_pantalla()
    espacio()
    centrar("Lista de Ventas Registradas")
    espacio()
    for i in range(cantidad):
        print(i + 1, "° Venta:")
        print("Cliente: ", nombres[i])
        print("Tipo de cliente: ", tipos[i])
        print("Género: ", generos[i])
        print("Tipo de servicio: ", servicios[i])
        print("Pasajes adquiridos: ", pasajes[i])
        print("Total: S/.", totales[i])
        print("Descuento: ", descuentos[i])
        espacio()
    input("*Presione cualquier tecla para continuar*")

def reporte_acumulado(tipos, generos, totales):
    limpiar_pantalla()
    espacio()
    centrar("Reporte Acumulado de Ventas")
    espacio()
    print("Cantidad total de ventas: ", len(totales))
    print("Suma total: S/.", sum(totales))
    espacio()

    centrar("Ventas por Género")
    print("Clientes Masculinos: ", generos.count("M"))
    print("Clientes Femeninos: ", generos.count("F"))

    centrar("Ventas por Tipo de Cliente")
    print("Tipo 1: ", tipos.count(1))
    print("Tipo 2: ", tipos.count(2))

    centrar("Promedio de Importes")
    tipo1 = [total for i, total in enumerate(totales) if tipos[i] == 1]
    tipo2 = [total for i, total in enumerate(totales) if tipos[i] == 2]
    promedio_tipo1 = sum(tipo1) / len(tipo1) if tipo1 else 0
    promedio_tipo2 = sum(tipo2) / len(tipo2) if tipo2 else 0
    print("Promedio Tipo 1: ", promedio_tipo1)
    print("Promedio Tipo 2: ", promedio_tipo2)

    centrar("Ventas por Intervalos")
    intervalos = [
        (80, 1000),
        (100, 800)
    ]
    for inicio, fin in intervalos:
        conteo = sum(1 for total in totales if inicio <= total < fin)
        print(f"Ventas entre {inicio} y {fin}: {conteo}")

    espacio()
    input("*Presione cualquier tecla para continuar*")

# Listas globales
nombres = []
tipos = []
generos = []
servicios = []
pasajes = []
totales = []
descuentos = []

tiempo = 0.8

while True:
    mostrar_menu_principal()
    print("*Seleccione una opción*")
    try:
        option = int(input("-> "))
        if option == 1:
            # Ingresar nueva venta
            limpiar_pantalla()
            espacio()
            centrar("Registrar Nueva Venta")
            espacio()

            # Nombre del cliente
            print("Ingrese nombre del cliente")
            nombres.append(input("-> "))

            # Tipo de cliente
            tipos.append(obtener_tipo_cliente())

            # Género del cliente
            limpiar_pantalla()
            espacio()
            centrar("Género del Cliente")
            espacio()
            print("Ingrese género del cliente (M o F)")
            validado = True
            while validado:
                usable = input("-> ")
                validado = validar_genero(usable)
            generos.append(usable)

            # Tipo de servicio
            servicios.append(obtener_tipo_servicio())
            
            # Cantidad de pasajes
            pasajes.append(obtener_cantidad_pasajes())

            # Calcular total y descuento
            subtotal = servicios[-1] * pasajes[-1]
            if pasajes[-1] == 1:
                descuentos.append(0)
            elif 2 <= pasajes[-1] <= 5:
                descuentos.append(10)
                subtotal *= 0.9
            elif 6 <= pasajes[-1] <= 10:
                descuentos.append(15)
                subtotal *= 0.85
            else:
                descuentos.append(25)
                subtotal *= 0.8
            totales.append(subtotal)

            limpiar_pantalla()
            espacio()
            centrar("Venta registrada exitosamente")
            espacio()
            input("*Presione cualquier tecla para continuar*")

        elif option == 2:
            # Ver reporte de ventas
            while True:
                limpiar_pantalla()
                espacio()
                centrar("Reporte de Ventas")
                espacio()
                print('''
1:  Mostrar todas las ventas
2:  Mostrar reporte acumulado
3:  Salir
''')
                print("*Seleccione una opción*")
                try:
                    selector = int(input("-> "))
                    if selector == 1:
                        mostrar_ventas(nombres, tipos, generos, servicios, pasajes, totales, descuentos)
                    elif selector == 2:
                        reporte_acumulado(tipos, generos, totales)
                    elif selector == 3:
                        break
                    else:
                        print("*Opción no válida*")
                        time.sleep(tiempo)
                except ValueError:
                    print("*Entrada no válida*")
                    time.sleep(tiempo)

        elif option == 3:
            # Salir del programa
            break

        else:
            print("Opción no válida")

    except ValueError:
        print("*Entrada no válida*")
        time.sleep(tiempo)
