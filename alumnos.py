def grupo_alumnos():
    """Determina el grupo al que pertenece un alumno según su nombre y sexo."""
    nombre = input("Ingresa tu nombre: ")
    sexo = input("Ingresa tu sexo (H para hombre, M para mujer): ")

    if (sexo.upper() == 'M' and nombre.upper() < 'M') or (sexo.upper() == 'H' and nombre.upper() > 'N'):
        print(f"{nombre} pertenece al Grupo A.")
    else:
        print(f"{nombre} pertenece al Grupo B.")
