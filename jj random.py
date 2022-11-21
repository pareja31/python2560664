import random

cont = 0
suma = 0
suma2=0
moda = 0
promedio = 0
mediana = 0


vector = []
vector2 = [] 

rango = random.randint(10,25)

for i in range(rango):
    vector.append(round(random.random()*100))
    vector2 = vector
    cont += 1
    suma += vector[i]
    promedio  = suma / cont




print(vector)
print ("rango de los numeros",rango)
print('La suma de los números generados es',suma)
print('El promedio de los números generados es',promedio)