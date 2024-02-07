n = int(input("Ingrese el numero de empleados"))    

cont = 0
cont1 = 0
Gasto = 0

for ini in range (n):
    Sueldo = float(input("El valor del sueldo de los empleado"))
    Gasto = Gasto+Sueldo
    if Sueldo >= 1300000 and Sueldo <=3000000:
        cont +=1
    elif Sueldo > 3000000:
        cont1 +=1


print("Los gastos de la empresa total: ", Gasto)
print("Empleados que ganan entre 1300000 y 3000000 son: ",cont)
print("Empleados que ganan mas de 3000000 son: ",cont1)
