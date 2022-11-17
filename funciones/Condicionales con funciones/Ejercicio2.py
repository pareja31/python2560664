#Ingresar 3 números y definir cuántos números hay iguales.
def iguales(a,b,c):
    a=int(input("Ingrese un número: "))
    b=int(input("Ingrese el segundo número: "))
    c=int(input("Ingrese el tercer número: "))
    if a==b and a==c and b==c:
        print("Los tres números son iguales")
    elif a==b or a==c or b==c:
        print("Hay dos números iguales")
    else:
        print("Todos los números son distintos")
        
print(iguales(30,20,30)) 