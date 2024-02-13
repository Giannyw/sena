Persona = {
    "Nombre":"Leydi Johanna",
    "Apellido":"Cifuentes Martinez",
    "Estatura" : 1.59,
    "Email": "cifuentes@gmail.com",
    "Edad": 50,
    "Ciudad Nacimiento":"Ibague",
    "Genero":["Femenino","Masculino", "Otro"],
}

print(Persona)
#mostrar un elemento
print("El nombre de la persona es: ", {Persona["Nombre"]})

#agregar o eliminar elementos
Persona ["Telefono"]=325558965
print (Persona)

#Modificar elementos
Persona["Telefono"]=26660955
print(Persona)

#Modificar la clave
Persona["Celular"]=Persona.pop("Telefono")
print(Persona)

#interartuar los items de las claves y valores

for clave,valor in Persona.items():
    print (clave, ":" ,valor)