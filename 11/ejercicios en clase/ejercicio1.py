import random
lista=[round(random.random()*100) for i in range(20)]
print("lista",lista)

impar=[x for x in lista if x%2!=0]
print(impar)
par=[x for x in lista if x%2==0]
print(par)

parimpar=[0 if x%2==0 else x for x in lista]
print(parimpar)

