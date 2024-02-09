año = int(input("Ingrese el año:"))
año_actual = 2024

def abisiesto(año):
    if (año % 4 == 0) and (año % 100 !=0):
        print("El año escrio es bisiesto")
    elif (año % 100 == 0) and (año % 400 == 0):
        print("El año ingresado es bisiesto")
    else:
        print("El año ingresado no es bisiesto")

abisiesto(año)
