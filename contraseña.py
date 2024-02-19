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