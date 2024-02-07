alturas = input("Ingrese un conjunto de números de alturas de personas, separados por espacios: ")

# Convertir la entrada del usuario en una lista de números enteros
alturas_list = [int(altura) for altura in alturas.split()]

# Calcular la altura promedio de las personas
altura_promedio = sum(alturas_list) / len(alturas_list)

# Mostrar la altura promedio de las personas
print("La altura promedio de las personas es:", altura_promedio)