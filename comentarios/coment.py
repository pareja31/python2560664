def divisores(num): #funcion con parametro num
    try:                        #se prueba por si ocurre un error
        for i in range(1,num+1): #el for recorre, el +1 es para que muestre todos los valores
            if num%i==0:       #si num mod i es igual a 0 entoces imprimira i como divisor del num   
                print(i,' es divisor')
    except ZeroDivisionError:  #una excepcion si el divisor es 0 
        print('indeterminacion')
    except TypeError:   #si se excribe un tipo de valor indivisible como letras o simbolos
        print(type(num),'Tipo de dato no soportado')

var=int(input('ingrese numero')) #se especifica que sea un numero entero
divisores(var) #se llama la funcion
print('El programa continua en esta linea')