precios_frutas = {
    "manzana": 2500,
    "pera": 3000,
    "platano": 1800,
    "naranja": 2000
}

def calcular_precio_final(fruta, cantidad):
    if fruta.lower() in precios_frutas:
        precio_unitario = precios_frutas[fruta.lower()]
        precio_final = precio_unitario * cantidad
        return precio_final
    else:
        return "Error: la fruta no existe en el diccionario de precios."

while True:
    fruta = input("Introduce el nombre de la fruta (o 'salir' para terminar): ")
    if fruta.lower() == "salir":
        break
    cantidad = int(input("Introduce la cantidad de {} vendida: ".format(fruta)))
    precio_final = calcular_precio_final(fruta, cantidad)
    print("El precio final de {} es: {}".format(fruta, precio_final))
    continuar = input("¿Quieres hacer otra consulta? (s/n): ")
    if continuar.lower() != "s":
        break

print("Vuelve pronto <3")