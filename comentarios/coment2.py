try:              #prueba de errores
    #print(1/1))   
    raise SyntaxError   #se debe generar manualmente con un raise
except SyntaxError as e: #el "sintaxerror" no se puede manupular com una excepcion ya que el propio lenguaje lo detecta
    print(e)
    print('Cierra el parentesis')
    
try:
    #raise ZeroDivisionError
    print(1/0)                 #ya que no se puede multiplicar por 0 se genera la excepcion "zeroDivisionerror"
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:  #con esta función se puede cambiar el nombre de zeroDivisionerror
    print(zde)
    #print('prueba error')