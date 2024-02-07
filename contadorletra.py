frase = input ("Por favor  ingrese una frase")
letra = input ("Por favor ingresar la letra a buscar")

Cletra = 0

for i  in frase:
    if i  == letra:
        Cletra += 1

print("La letra  '%s' aparece %2i en la frase '%s'. " %(letra,Cletra, frase))