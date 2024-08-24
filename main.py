def saludar(nombre):
    """
    Función que saluda a una persona.

    Args:
        nombre: El nombre de la persona a la que se saluda.

    Returns:
        Un mensaje de saludo.
    """
    return f"¡Hola, {nombre}!"

def despedirse(nombre):
    """
    Función que se despide de una persona.

    Args:
        nombre: El nombre de la persona a la que se despide.

    Returns:
        Un mensaje de despedida.
    """
    return f"¡Adiós, {nombre}!"

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    saludo = saludar(nombre)
    print(saludo)
    despedida = despedirse(nombre)
    print(despedida)



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