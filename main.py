
import random

numero_secreto = random.randint(1, 20)
intentos = 0
max_intentos = 5
adivinado = False

print("Estoy pensando en un número entre 1 y 20.")
while intentos < max_intentos and not adivinado:
    intento = int(input("Intenta adivinar el número: "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intentos.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número es mayor que", intento)
    else:
        print("El número es menor que", intento)

if not adivinado:
    print("Lo siento, no adivinaste el número en el número máximo de intentos.")
    print("El número secreto era", numero_secreto)