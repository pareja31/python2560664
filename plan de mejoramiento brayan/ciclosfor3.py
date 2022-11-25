#Imprimir las tablas de multiplicar.
#libro: python paso a paso
for v in range(3,10,2): 
    print("Tabla del "+str(v))
    for n in range(1,10+1):
        print(str(v)+"x"+str(n)+"="+str(v*n))