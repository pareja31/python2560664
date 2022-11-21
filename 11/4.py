import random
lista=[]
a=int(0)
na=random.randint(10,25)
for i in range (na):
    lista.append(round(random.random()*100))
print("desorden",lista)
print("cantidad de lista",lista._len_())

b=False
a=False
while b==False:
    b=True
    for i in range (len(lista)-1):
        if lista[i]>lista[i+1]:
            h=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=h
            b=False
print("ordenado de menor a mayor",lista)

while a==false:
    a=True
    for a in range(len(lista)-1):
        if lista[k]<lista[k+1]
        u=lista[k]
        lista[k]=lista[k+1]
        lista[k+1]=u
        a=False
print("mayor a menor", lista)
