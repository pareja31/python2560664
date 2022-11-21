import random
vec=[0,1]
tamaño=round((random.random()*25-10)+10)
print("tamamaño",tamaño)
for i in range (2,tamaño):
    vec.append(vec[i-1]+vec[i-2])
print()


def fibonacci (num):
    