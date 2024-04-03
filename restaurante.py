platos = [
    {
        "id" : 1,
        "name": "Seco de pollo",
        "price": 13
    },
    {
        "id": 2,
        "name": "Aji de gallina",
        "price": 14
    },
    {
        "id": 3,
        "name" : "Seco de res",
        "price": 12
    }
]
entradas = [
    {
        "id": 1,
        "name": "Aguadito",
        "price": 5
    },
    {
        "id": 2,
        "name": "Sopa a la minuta",
        "price": 4
    }
]

contador = 0
usable1 = []
usable2 = []
total = 0

def espacio():
    print()
    print("*"*52)

def centrar(message):
    tamaño = len(message)
    a = round((50 - tamaño) / 2)
    print("*"*a, message, "*"*a)

def Derecha(message1, message2):
    tamaño = len(message1) + len(message2)
    a = round(50 - tamaño)
    print(message1, "."*a, message2)

def subTotal(option):
    plato1 = entradas[option[0]-1]
    plato2 = platos[option[1]-1]
    total = plato1['price'] + plato2['price']
    return total

def listar(data, message):
    centrar(message)
    for i in data:
        name = i['name']
        price = "S/. " + str(i['price'])
        Derecha(name, price)

while True:
    print("Bienvenido al restaurante ejemplo")
    espacio()
    centrar("Menu")

    print("Entradas")
    for i in entradas:
        print(str(i['id']) + ":  " + i['name'] +" S/." + str(i['price']))
    print("Platos")
    for i in platos:
        print(str(i['id']) + ":  " + i['name'] + " S/." + str(i['price']))
    option = []
    option.append(int(input("Elija el número de sopa de desea: ")))
    option.append(int(input("Elija el número de plato de desea: ")))


    usable1.append(entradas[option[0]-1])
    usable2.append(platos[option[1]-1])

    total += subTotal(option)

    espacio()
    print("Subtotal: ",subTotal(option))
    print("""
        1:  Tomar otra orden
        2:  Terminar""")
    selector = int(input(": "))
    if selector == 2:
        espacio()
        centrar("Boleta")

        listar(usable1, "Entradas")
        listar(usable2, "Platos Principales")
        totalm = "S/. " + str(total)
        Derecha("TOTAL", totalm)
        break
    option = []
    
