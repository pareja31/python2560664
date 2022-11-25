#crear combinaciones con sin repetirse con una lista
#libro: python paso a paso
combs =[] #lista vacia donde se llenara con los diferentes combos
for x in [1,2,3]:  #datos iniciales
    for y in [3,1,4]:  #datos segundarios
        if x !=y: #codigo para que no se repitan "si x es "diferente" de y entonces agregar ".append" a lista
            combs.append((x,y))

print(combs)