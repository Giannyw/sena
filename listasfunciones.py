def ingresar():
    entero=[]

    for x in range(5):
        Numero=int(input("Ingresar el numero"))
        entero.append(Numero)
    imprimir(entero)
    suma (entero)
def imprimir(entero):

    print("Los datos de la lista son")
    for x in entero:
        print(x)

def suma(entero):
    acum=0 
    for x in entero:
        acum = acum+x
    print("la suma de los numero enteros es: ", acum)


ingresar()