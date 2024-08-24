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