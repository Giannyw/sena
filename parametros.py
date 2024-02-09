texto="Buenos dias definiendo un parametro en una funcion"

#funcion sin parametros
def mensaje():
    N1= int (input("ingresar el primer numero"))
    N2= int(input("ingresar el segundo numero"))
    calcularmayor(N1,N2)
    positivo(N1,N2)

#funcion con parametros
def calcularmayor(num1,num2): 
    if num1>num2:
        print("El primero numero es el mayor")
    elif num1==num2:
        print("Son numeros iguales")
    else:
        print("El segundo numero es el mayor")
    
def positivo (p1,p2):
    if p1>0 and p2>0:
        print("Son numeros positivo")
    else:
        print("Al menos uno de los numero no es positivo")

mensaje ()
    