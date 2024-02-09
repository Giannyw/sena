def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def contar_bisiestos(desde, hasta):
    return sum(1 for año in range(desde, hasta + 1) if es_bisiesto(año))

# Solicitar al usuario el rango de años
año_inicial = int(input("Ingrese el año inicial: "))
año_final = int(input("Ingrese el año final: "))

bisiestos_pasados = contar_bisiestos(año_inicial, año_final)
print(f"En el período de {año_inicial} a {año_final}, han pasado {bisiestos_pasados} años bisiestos.")