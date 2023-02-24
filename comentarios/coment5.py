def try_syntax(numerator, denominator): #funcion con dos parametros
    try: #buscar errores (inicio de excepcion)
        print(f'In the try block: {numerator}/{denominator}') #se dice que "{}/{}"" que el numerador y el denominador se dividiran
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator #se establece la division
    except ZeroDivisionError as zde: #se renombra la excepcion "zeroDivicionerror"
        print(zde)  #se debe imprimir despues de renombrar
    else:           #un else por si no hay ningun error
        print('The result is:', result) #se imprimira el resultado
        return result
    finally:
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 12)) #se llama la funcion con los valores