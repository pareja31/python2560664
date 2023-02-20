#ejercicio 8
def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou""áéíóú":
			contador += 1
	return contador

def es_vocal(letra):
    return letra in "aeiou"

      

cad = input("ingrese frase")
cadena_minuscula = cad.lower()
cantidad = contar_vocales(cad)
print(f"En la cadena '{cad}'' hay {cantidad} vocales")
cantidad_consonantes = 0
for letra in cadena_minuscula:
    if letra.isalpha() and not es_vocal(letra):
        cantidad_consonantes += 1
print(f"En la cadena '{cad}' hay {cantidad_consonantes} consonantes")


