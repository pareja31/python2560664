import random
vector=0
rango=random.randint(10,25)
for n in range(rango):
    vector.append(round(random.random()*100))
print(vector)
for n in vector:
    i=1
    cont=0
    while(n>=1):
        if n%i==0:
            cont+=1
    i+=1
if not cont>2 or n<=1:
    print("numero primo",n)
        