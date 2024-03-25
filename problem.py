import math
import time

def Area(a, b):
    cuadrado = b*b
    triangulo = (a-b)*b/2
    area = cuadrado + triangulo
    return (area)

def Area2():
    lado = float(input("Ingreseel valor del lado: "))
    radio = lado/2
    areaT = math.pi * (radio ** 2)
    return ( areaT )

while True:
    print("*" * 30)
    print("""
        Seleccione la opción:
        1 -> 2a
        2 -> 2b
        0 -> salir del programa
""")
    option = int(input("-> "))

    if option == 1:
        b = float(input("Ingrese la base: "))
        a = float(input("Ingrese la altura: "))
        print("El área es: " + str(Area(a,b)))
        time.sleep(2)
    elif option == 2:
        print("El área es: " + str(Area2()))
        time.sleep(2)
    elif option == 0:
        break
    else:
        print("No es una opción valida")
        print("*" * 20)