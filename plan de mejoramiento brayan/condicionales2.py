#libro: python paso a paso

suma=0
print("El programa irá pidiendo números y los irá sumando hasta que la suma supere el valor de 100")
while True:
    numero=eval(input("Ingrese un número: "))
    suma=suma+numero
    if suma>=100:
        break
print("La suma ha sido de:",suma)