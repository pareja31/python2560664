import random
def primos(num):
    for i in range(2,num):
        if num%i==0:
            return "Es primo"

lista=[]
for i in range(10):
    lista.append(round(random.randrange(100)))
print(lista)

print(primos)
print(i)

def amigos(x,y):
    sumx=sumaDivisores(x)
    sumy=sumaDivisiores(y)
    if sumx==y and sumy==x:
        return "Son amigos"
    else:
        return"No son amigos"
print(220,284)