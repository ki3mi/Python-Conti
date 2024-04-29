while True:
    letra  = input("Letra: ")
    estados = {
        "B":0,
        "b":0,
        "F":1,
        "f":1,
        "C":2,
        "c":2,
        "finish":0
    }
    res = ["buque", "fragata", "crucero"]
    for i in estados:
        if letra == i:
            print(res[estados[i]])
        if i == "finish":
            print("Letra no válida")