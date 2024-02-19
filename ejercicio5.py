# Función para calcular la nota media de un alumno
def calcular_media(notas):
    return sum(notas) / len(notas)

# Crear un diccionario para almacenar los nombres y notas de los alumnos
alumnos = {}

# Pedir el número de alumnos
num_alumnos = int(input("Introduce el número de alumnos: "))

# Pedir el nombre y las notas de cada alumno
for _ in range(num_alumnos):
    nombre = input("Introduce el nombre del alumno: ")
    if nombre in alumnos:
        print("Error: el alumno ya existe.")
        continue
    notas = []
    nota = float(input("Introduce la nota del alumno (introduce un número negativo para terminar): "))
    while nota >= 0:
        notas.append(nota)
        nota = float(input("Introduce otra nota (introduce un número negativo para terminar): "))
    alumnos[nombre] = notas

# Mostrar la lista de alumnos y la nota media de cada uno
print("\nLista de alumnos y nota media:")
for nombre, notas in alumnos.items():
    media = calcular_media(notas)
    print(f"{nombre}: {notas} - Media: {media:.2f}")