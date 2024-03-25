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
    return ( round(areaT, 2) )

def Procentaje(varones, mujeres):
    total = varones+  mujeres

    procV = (varones * 100) / total
    procM = (mujeres * 100) / total

    # proc = [procM, procV]

    return print("El porcentaje de varones es: %" + str(procV) + "\nEl procentaje de mujeres es: %" + str(procM))

def Promedio(c1, ep, c2, ef):
    pf = (c1*20/100) + (ep*25/100) + (c2*20/100) + (ef*35/100)
    return pf 

while True:
    print("*" * 30)
    print("""
        Seleccione la opción:
        1 -> 2a
        2 -> 2b
        3 -> procentaje
        4 -> promedio
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

    elif option == 3:
        varones = int(input("Ingrese la cantidad de varones: "))
        mujeres = int(input("Ingrese la cantidad de mujeres: "))
        Procentaje(varones, mujeres)
        time.sleep(3)
    
    elif option == 4:
        c1 = float(input("Ingrese el consolidado 1: "))
        ep = float(input("Ingrese el parcial: "))
        c2 = float(input("Ingrese el consolidado 2: "))
        ef = float(input("Ingrese el examen final: "))
        print("Su promedio final es: " + str(Promedio(c1, ep, c2, ef)))
        time.sleep(2)

    elif option == 0:
        break
    else:
        print("No es una opción valida")
        print("*" * 20)