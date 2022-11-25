#Números primos hasta n:
n=int(input("Introduce un número: ")) #se pide un numero
for i in range(2,n+1): #se inicia en 2 hasta el numero introducido
    cont=0 #un contador que va sumando de acuerdo a los numeros requeridos
    for j in range(1,n+1):  
        if i%j==0: #condicion para sacar los numeros primos
            cont+=1 #el resultado se agrega a "contador"
    if cont==2: #si es igual a 2 se inicia a imprimir i
        print(i)