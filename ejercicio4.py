# Crear un diccionario para almacenar la cesta de la compra
cesta_compra = {}

# Función para calcular el coste total de la cesta de la compra
def calcular_coste_total(cesta):
    total = sum(cesta.values())
    return total

# Ciclo para añadir artículos a la cesta de la compra
while True:
    articulo = input("Introduce el nombre del artículo (o 'terminar' para finalizar): ")
    if articulo.lower() == "terminar":
        break
    precio = float(input("Introduce el precio del artículo: "))
    cesta_compra[articulo] = precio

# Mostrar la lista de la compra y el coste total
print("\nLista de la compra:")
for articulo, precio in cesta_compra.items():
    print(f"{articulo}: ${precio:.2f}")
print(f"\nCoste total: ${calcular_coste_total(cesta_compra):.2f}")