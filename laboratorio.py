#diseño de menu para juegos
# 1 salir
# 2 juego de dados
# 3 grupo de estudiantes
# 4 cobro de entradas
# 5 contraseña
# 6 calculo de la factura

import random

def tirar_dado():
    """Simula tirar un dado de 6 caras."""
    return random.randint(1, 6)

def juego_de_dados():
    """Simula un juego de dados entre Álvaro y Bárbara."""
    alvaro = tirar_dado()
    barbara = tirar_dado()

    print(f'Álvaro tiró un {alvaro}')
    print(f'Bárbara tiró un {barbara}')

    if alvaro > barbara:
        print('Álvaro gana!')
    elif alvaro < barbara:
        print('Bárbara gana!')
    else:
        print('¡Empate!')

def grupo_alumnos():
    """Determina el grupo al que pertenece un alumno según su nombre y sexo."""
    nombre = input("Ingresa tu nombre: ")
    sexo = input("Ingresa tu sexo (H para hombre, M para mujer): ")

    if (sexo.upper() == 'M' and nombre.upper() < 'M') or (sexo.upper() == 'H' and nombre.upper() > 'N'):
        print(f"{nombre} pertenece al Grupo A.")
    else:
        print(f"{nombre} pertenece al Grupo B.")

def precio_entrada():
    """Calcula el precio de entrada según la edad del cliente."""
    edad = int(input("Ingresa tu edad: "))

    if edad < 4:
        print("Entrada gratuita.")
    elif 4 <= edad <= 18:
        print("El precio de la entrada es 30000.")
    else:
        print("El precio de la entrada es 50000.")

def verificar_contrasena():
    """Verifica la contraseña ingresada por el usuario con un máximo de 3 intentos."""
    contrasena_correcta = "mi_contrasena"
    intentos = 0

    while intentos < 3:
        contrasena_ingresada = input("Ingresa la contraseña: ")
        if contrasena_ingresada == contrasena_correcta:
            print("Contraseña correcta. Acceso permitido.")
            break
        else:
            intentos += 1
            print(f"Contraseña incorrecta. Intento {intentos}/3. Inténtalo nuevamente.")

    if intentos == 3:
        print("Número máximo de intentos alcanzado. Acceso denegado.")

def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    """Calcula el total de una factura después de aplicarle el IVA."""
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total_con_iva = cantidad_sin_iva + iva
    return total_con_iva

def menu_principal():
    """Muestra el menú principal y ejecuta la opción seleccionada por el usuario."""
    while True:
        print("\nMenú Principal:")
        print("1. Salir")
        print("2. Juego de dados")
        print("3. Grupo de alumnos")
        print("4. Precio de entrada")
        print("5. Verificar contraseña (3 intentos)")
        print("6. Calcular total factura con IVA")

        opcion = input("Ingresa el número de la opción deseada: ")

        if opcion == '1':
            print("¡Hasta luego!")
            break
        elif opcion == '2':
            juego_de_dados()
        elif opcion == '3':
            grupo_alumnos()
        elif opcion == '4':
            precio_entrada()
        elif opcion == '5':
            verificar_contrasena()
        elif opcion == '6':
            cantidad_sin_iva = float(input("Ingresa la cantidad sin IVA: "))
            porcentaje_iva = float(input("Ingresa el porcentaje de IVA (opcional, presiona Enter para usar el 21% por defecto): ") or 21)
            total_factura = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)
            print(f"El total de la factura con IVA es: {total_factura}")
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")

if __name__ == "__main__":
    menu_principal()