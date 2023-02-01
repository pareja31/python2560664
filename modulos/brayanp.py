
def multiplos(lista):
    Lista=[] 
    i=1 
    Num=int(input("Ingrese un número: ")) 
    while Num>0: 
        Lista.append(Num*i) 
        print(Lista) 
        i=i+1 
    else:
        print("no se pueden encontrar los multiplos de este numero")




def num_mayor (a,b,c):
    a=int(input("introduce un numero"))
    b=int(input("introduce un numero"))
    c=int(input("introduce un numero"))
    print(a,b,c)

    if a>b and a>c:
        print (a, "es el numero mayor")
    elif b>a and b>c:
        print (b, "es elnumero mayor")
    else:
        print (c, "es el numero mayor")



def tablas (n):
    n=int(input("ingrese un numero"))
    for v in range(3,n,2): 
        print("Tabla del "+str(v))
        for n in range(1,10+1):
            print(str(v)+"x"+str(n)+"="+str(v*n))
        



def max (n):
    c=0
    max=0
    n=int(input('ingrese numero negativo para parar'))
    while n>=0:
        n=int(input('ingrese numero negativo para parar'))
        if n>=max:
            max= n
    print("El número mayor es:",max)












