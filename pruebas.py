# def ejercicio1():
#     sueldo = float(input("ingrese el sueldo base: "))

#     ventas = float(input("Ingrese el monto de las ventas: "))

#     sueldoF = sueldo + ventas*0.8

#     print(sueldoF)

# def centrar(message):
#     tamaño = len(message)
#     a = round((50 - tamaño) / 2)
#     print("*"*a, message, "*"*a)


# def Derecha(message1, message2):
#     tamaño = len(message1) + len(message2)
#     a = round(50 - tamaño)
#     print(message1, "."*a, message2)
# # cambio de saloess a solares
    
# def SolaDolar(soles):
#     total = soles*3.8
#     return total 

# # print("Ingrese el monto a cambiar")
# # soles = float(input(":> "))
# # print("El dolares es: ", SolaDolar(soles))

# def Sueldo(horas, monto):
#     bruto = horas * monto
#     afp = bruto*0.11
#     salud = bruto*0.05
#     neto = bruto - afp - salud

#     return(bruto, neto, afp, salud)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# # name = input("Nombre del trbajador: ")


# # print("Ingrese el sueldo de ", name)
# # horas = float(input(":> "))
# # print("Ingrese el monto por hora de ", name)
# # monto = float(input(":> "))

# # sueldos = Sueldo(horas, monto)
# # print("El suelo bruto es: ", sueldos[0])
# # print("El sueldo neto es: ", sueldos[1])
# # print("Descuentos")
# # print("AFP 11%: ",sueldos[2])
# # print("EsSalud 5%: ",sueldos[3])


def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = func(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
