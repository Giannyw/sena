#Modificar elementos
Persona["Telefono"]=26660955
print(Persona)

#Modificar la clave
Persona["Celular"]=Persona.pop("Telefono")
print(Persona)

#interartuar los items de las claves y valores

for clave,valor in Persona.items():
    print (clave, ":" ,valor)