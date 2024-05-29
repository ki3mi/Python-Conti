import time
from os import system


def espacio():
    print()
    print("*"*52)
def centrar(message):
    tamaño = len(message)
    a = round((50 - tamaño) / 2)
    print("*"*a, message, "*"*a)

def estats_batalla():
    print(f'Vida del {enemigo.nombre}: {enemigo.vida}')
    print(f'Vida de {personaje.nombre}: {personaje.vida}')
def menu_batalla():
    print('''
1 -> Atacar
otro -> Retirada
''')

class Guerrero():
    def __init__(self, nombre, fuerza, inteligencia, vida, nivel, oro):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.nivel = nivel
        self.oro = oro

    def atacar(self):
        ataque = self.fuerza
        return ataque
    
    def perder_vida(self, ataque):
        if self.vida > 0:
            self.vida -= ataque
        else:
            return {"res" : "Está muerto"}

    def ganar_vida(self, puntos):
        total = self.vida + puntos
        if self.vida == self.vida_max:
            return {"res" : "Vida completa"}
        else:            
            if total >= self.vida_max:
                total -= self.vida_max
                self.vida = self.vida_max
            else:
                self.vida += puntos
            return {"res": f"+{total} puntos"}
    
    
class Mago(Guerrero):
    def atacar(self):
        ataque = self.fuerza * self.inteligencia
        return ataque
    


def pelear():
    continuar = 1
    while enemigo.vida > 0 and personaje.vida > 0 and continuar == 1:
        espacio()
        estats_batalla()
        menu_batalla()
        continuar = int(input())
        if personaje.vida > 0 and enemigo.vida > 0 and continuar == 1:
            centrar(f'Ataca {personaje.nombre}')
            enemigo.perder_vida(personaje.atacar())
            print(f'Daño: {personaje.fuerza}')
            centrar(f'Ataca {enemigo.nombre}')
            personaje.perder_vida(enemigo.atacar())
            print(f'Daño: {enemigo.fuerza * enemigo.inteligencia}')
            time.sleep(1)
        system('cls')


    if enemigo.vida > 0 or continuar != 1:
        print('Ganador: ',enemigo.nombre)
        print('Vida restante: ',enemigo.vida)
    else:
        print('Ganador: ',personaje.nombre)
        print('Vida restante: ',personaje.vida)



personaje = Guerrero('Miguel', 2, 2, 10, 2, 100)
enemigo = Mago('Mago', 1, 1, 10, 1, 20)
pelear()

enemigo = Mago('Demonio', 3,1,10,1,20)
pelear()
