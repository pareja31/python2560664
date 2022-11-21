supermerc = {}

while True:
    name = input("Ingresa el nombre del producto: ")
    if name == '':
        break
    
    score = int(input("ingrese precio: "))
    
    if name in supermerc:
        supermerc[name] += (score,)
    else:
        supermerc[name] = (score,)
        
for name in sorted(supermerc.keys()):
    adicionar = 0
    counter = 0
    for score in supermerc[name]:
        adicionar += score
        counter += 1
    adicionar+=score
        
        
    print(name, ":", adicionar / counter)
    print("total a pagar",adicionar)





   


    