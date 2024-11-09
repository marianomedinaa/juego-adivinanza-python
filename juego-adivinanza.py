

import random


numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_max_intentos = 5
intentos_faltantes = 4
adivinado = False

print("bienvenido al juego de adivinar el número secreto, ma men!")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("introduce un número del 1 al 99: ") # TODO: convertir a número
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicitaciones, has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("el número es mayor al incresado")
    else:
        print("el número es menor al ingresado")

    cant_intentos += 1

    if not intentos_faltantes == 1:
        print("te quedan ", intentos_faltantes," intentos")
        intentos_faltantes -= 1
    else:
        print("te queda ", intentos_faltantes," intento")


if not cant_intentos < cant_max_intentos:
    print("GAME OVER, no has podido adivinar dentro de los 5 intentos")  