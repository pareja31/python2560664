#ejercicio 5
s=input("Ingrese una frase")
def suma(sum):
    total=0
    for i in sum:
        total+=ord(i)
    return total

print("El total es:", suma(s))