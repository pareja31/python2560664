#python 3 "pagina 112"
#pedir numeros hasta que se introduzca un 0 para realizar la suma

i=1
suma=0
print("Introduce uns serie de números.Si es 0 entendemos que es para terminar.")
print("Número",i,":",end="")
número=eval(input())
suma=suma+número
while número!=0:
    i=i+1
    print("Número",i,":",end="")
    número=eval(input())
    suma=suma+número
print("La suma de todos los números es",suma)