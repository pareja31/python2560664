#Libro: python fácil Página 71  
#Un programa que imprima una lista infinita
#con los múltiplos de un número ingresado.

Lista=[] #lista vacia
i=1 #se inicia
Num=int(input("Ingrese un número: ")) #se solicita un numero (entero)
while Num>0: #mientras el numero sea mayor que 0 se ejecutara
    Lista.append(Num*i) #la funcion ".append" es para agregar elementos a la lista
    print(Lista) 
    i=i+1 #que se agregue 1 elemento mas el anterior
else:
    print("no se pueden encontrar los multiplos de este numero")