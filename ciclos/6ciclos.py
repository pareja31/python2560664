cont = 0
max = 0
n = int(input('Ingrese numeros')) 
for n in range(5):
    while n >= 0:
        n = int(input('Ingrese numeros')) 
        if n > max:
            max = n
    
print('El mayor numero es',max)
