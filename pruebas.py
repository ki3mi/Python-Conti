def ejercicio1():
    sueldo = float(input("ingrese el sueldo base: "))

    ventas = float(input("Ingrese el monto de las ventas: "))

    sueldoF = sueldo + ventas*0.8

    print(sueldoF)

def centrar(message):
    tamaño = len(message)
    a = round((50 - tamaño) / 2)
    print("*"*a, message, "*"*a)


def Derecha(message1, message2):
    tamaño = len(message1) + len(message2)
    a = round(50 - tamaño)
    print(message1, "."*a, message2)

Derecha("Frugos", "S/. 15")
Derecha("Oreo", "S/. 5")

# Estoy en git
