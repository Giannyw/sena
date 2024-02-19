def precio_entrada():
    """Calcula el precio de entrada según la edad del cliente."""
    edad = int(input("Ingresa tu edad: "))

    if edad < 4:
        print("Entrada gratuita.")
    elif 4 <= edad <= 18:
        print("El precio de la entrada es 30000.")
    else:
        print("El precio de la entrada es 50000.")