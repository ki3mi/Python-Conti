def validar():
    letra  = input("Letra: ")
    estados = {
        "M":0,
        "m":0,
        "F":1,
        "f":1,
        "finish":0,
    }
    for i in estados:
        if letra == i:
            return(True)
        if i == "finish":
            return(False)
