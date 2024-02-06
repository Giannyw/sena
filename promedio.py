def calcular_promedio(lista_numeros):
    suma = sum(lista_numeros)
    promedio = suma / len(lista_numeros)
    return promedio

def solicitar_numeros():
    numeros = []
    for i in range(10):
        numero = float(input("Ingresa el número {}: ".format(i+1)))
        numeros.append(numero)
    return numeros


numeros_ingresados = solicitar_numeros()

promedio = calcular_promedio(numeros_ingresados)

print("El promedio de los números ingresados es:", promedio)     
  