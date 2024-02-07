def obtener_promedio_edades(edades):
    total_edades = sum(edades)
    return total_edades / len(edades)


edades_manana = []
print("Ingresar las edades de los estudiantes del turno mañana:")
for i in range(6):
    edad = int(input(f"Ingrese la edad del estudiante {i + 1}: "))
    edades_manana.append(edad)


edades_tarde = []
print("\nIngresar las edades de los estudiantes del turno tarde:")
for i in range(7):
    edad = int(input(f"Ingrese la edad del estudiante {i + 1}: "))
    edades_tarde.append(edad)


edades_noche = []
print("\nIngresar las edades de los estudiantes del turno noche:")
for i in range(12):
    edad = int(input(f"Ingrese la edad del estudiante {i + 1}: "))
    edades_noche.append(edad)

promedio_manana = obtener_promedio_edades(edades_manana)
promedio_tarde = obtener_promedio_edades(edades_tarde)
promedio_noche = obtener_promedio_edades(edades_noche)


print(f"\nPromedio de edades del turno mañana: {promedio_manana}")
print(f"Promedio de edades del turno tarde: {promedio_tarde}")
print(f"Promedio de edades del turno noche: {promedio_noche}")

 
if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print("\nEl turno mañana tiene el promedio de edades mayor.")
elif promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
    print("\nEl turno tarde tiene el promedio de edades mayor.")
else:
    print("\nEl turno noche tiene el promedio de edades mayor.")