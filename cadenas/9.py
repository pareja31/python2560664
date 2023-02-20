#ejercicio 9



cad =(input("ingrese cadena"))

for i in range(2, len(cad) + 1):
    subcadena = cad[:i]
    print(subcadena)