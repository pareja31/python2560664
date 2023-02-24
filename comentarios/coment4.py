def edad(): #funcion
    try:  #buscar errores
        tuedad=int(input("introduce tu edad")) #ingresar edad
        print(f'tu edad es  {tuedad}') #f para imprimir texto {} para imprir variable
        #print('Tu edad es ',tuedad) #otra forma de imprimir
    except ValueError as e:  #se renombra valueerror a e   
        print(e) #se debe imprimir cuando se renombra
        print("La edad debe ser un valor numerico...") #si se escribe un valor que no es, vuelve a preguntar la edad hasta que se intrduzca un numero
        edad() #para que sea infinito 
    
    
edad() #se llama la funcion