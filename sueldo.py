
sueldos = input("Ingrese los sueldos de los empleados, separados por espacios: ")


sueldos_list = [int(sueldo) for sueldo in sueldos.split()]


empleados_entre_10_y_300 = sum(1 for sueldo in sueldos_list if 10000000 <= sueldo <= 30000000)


empleados_mas_de_3000 = sum(1 for sueldo in sueldos_list if sueldo > 30000000)


importe_sueldos = sum(sueldos_list)

print("Cantidad de empleados que cobran entre $10.000.000 y $300.000:", empleados_entre_10_y_300)
print("Cantidad de empleados que cobran más de $3.000.000:", empleados_mas_de_3000)
print("Importe que gasta la empresa en sueldos al personal:", importe_sueldos)