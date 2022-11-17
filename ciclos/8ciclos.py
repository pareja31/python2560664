def iguales(a,b,c):   
    a=int(input("ingrese un número: "))
    b=int(input("Ingrese un número: "))
    c=int(input("Ingrese un número: "))
    

    if a==b and a==c and b==c:
        return "todos son iguales"
    elif a==c:
        print("dos son iguales")
    elif a==b:
        print("dos son iguales")
    else:
        print("todos son diferentes")
    
    
print(iguales(1,2,3))
print(iguales(1,1,1))
        
    


   
