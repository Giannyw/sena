tupla = (2,4,6)
fecha = (9, "febrero",2024)

print(tupla)
print(fecha)

palabras = int (input("Cuantas palabras desea agregar"))

if palabras <1:
    print ("No es valido")
else:
    lista = []
    for i in range(palabras):
        palabras = input(f" Escriba la palabra {i+1}: ")
        lista += [palabras]
    print(f"la lista creada es: {lista}")
