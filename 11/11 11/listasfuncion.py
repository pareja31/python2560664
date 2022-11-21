import random
def sumlista(lista):
    sum=0
    for i in lista:
        sum+=i
    return sum
def llenarlista(lista,tam):
    for i in range(tam):
        lista.append(round(random.randrange(100)))
        
lista=[]
tam=round(random.randint(5,15))
list=llenarlista
print(list)
