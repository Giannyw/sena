def mostrar_menu():
    print("1-Añadir número a la lista")
    print("2-Añadir número de la lista en una posición")
    print("3-Longitud de la lista")
    print("4-Eliminar el último número")
    print("5-Eliminar un número")
    print("6-Contar números")
    print("7-Posiciones de un número")
    print("8-Mostrar números")
    print("9-Salir")
    opcion = int(input("Elige una opción: "))
    return opcion

def añadir_numero(lista):
    numero = int(input("Introduce el número a añadir: "))
    lista.append(numero)
    print("Número añadido correctamente.")

def añadir_numero_posicion(lista):
    numero = int(input("Introduce el número a añadir: "))
    posicion = int(input("Introduce la posición en la que añadir el número: ")) - 1
    if 0 <= posicion < len(lista):
        lista.insert(posicion, numero)
        print("Número añadido correctamente.")
    else:
        print("La posición no es válida.")

def longitud_lista(lista):
    print(f"La longitud de la lista es: {len(lista)}")

def eliminar_ultimo_numero(lista):
    if lista:
        ultimo_numero = lista.pop()
        print(f"Se ha eliminado el número {ultimo_numero} correctamente.")
    else:
        print("La lista está vacía.")

def eliminar_numero(lista):
    posicion = int(input("Introduce la posición del número a eliminar: ")) - 1
    if 0 <= posicion < len(lista):
        numero_eliminado = lista.pop(posicion)
        print(f"Se ha eliminado el número {numero_eliminado} correctamente.")
    else:
        print("La posición no es válida.")

def contar_numeros(lista):
    numero = int(input("Introduce el número a contar: "))
    apariciones = lista.count(numero)
    print(f"El número {numero} aparece {apariciones} veces en la lista.")

def posiciones_numero(lista):
    numero = int(input("Introduce el número del que quieres saber las posiciones: "))
    posiciones = [i+1 for i, x in enumerate(lista) if x == numero]
    if posiciones:
        print(f"El número {numero} está en las posiciones: {', '.join(map(str, posiciones))}")
    else:
        print(f"El número {numero} no está en la lista.")

def mostrar_numeros(lista):
    print("Los números en la lista son:", lista)

# inicio
lista = []
opcion = 0
while opcion != 9:
    opcion = mostrar_menu()
    if opcion == 1:
        añadir_numero(lista)
    elif opcion == 2:
        añadir_numero_posicion(lista)
    elif opcion == 3:
        longitud_lista(lista)
    elif opcion == 4:
        eliminar_ultimo_numero(lista)
    elif opcion == 5:
        eliminar_numero(lista)
    elif opcion == 6:
        contar_numeros(lista)
    elif opcion == 7:
        posiciones_numero(lista)
    elif opcion == 8:
        mostrar_numeros(lista)
    elif opcion == 9:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Inténtalo de nuevo.")