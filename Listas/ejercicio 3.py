#este ejercicio es mio

import random 

total_pares=0
total_impares=0
promedio_impares=0
cont=0
vector=[]
rango=random.randint(10,25)
for i in range(rango):
    vector.append(round(random.random()*100))

for i in range (rango):
    if vector[i]%2==0:
        total_pares+=vector[i]
    else:
        total_impares+=vector[i]
        cont+=1
        promedio_impares=total_impares//cont

print("La longitud de la lista es:",rango,"y los valores son:",vector)
print("la suma de los pares fue:",total_pares)
print("El promedio de los impares es:", total_impares)
            
