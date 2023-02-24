values = (1, 3)  #una tupla con dos valores
#x,y=10,12     (se pueden agregar a dos variables un valor por separado con comas)
#print(divmod(10,3))  (el divimod sirve para dividir los valores en tuplas mostrando el cosiente y el residuo)
try:
    q, r = divmod(*values) #con el signo * en values asigna los valores a "q" y "r" para dividirlos con la funcion "divimod"
    #print('valor de q=',q)
    print(f'q={q}') #la f sirve para imprimir un valor con un texto y los {} para agregrar el valor o la variable
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e: #se agregra una excepcion por si se agrega un 0 a la divicion y se remplaza el nombre con el "as" a e
    print(type(e), e)