#libro: python para todos "pagina 40"
#uncion para agregar elementos a una lista

def f(x, y):  #funcion
    x = x + 3 #como no tiene ".append" se agrega fuera de la lista
    y.append(40) #se puede colocar cualquier valor
    print (x, y)

x = 22
y = [22]
f(x, y) #se llama a la funcion
print (x, y)