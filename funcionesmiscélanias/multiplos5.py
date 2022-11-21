#multiplos de 5
import random
def multiplos5(num):
  for i in range(1, num +1):
    if i % 5 == 0:
        print("es multiplo de 5:",i)
    else:
        print("no es multiplo de 5:",i)
   

lista=[]
for i in range(10):
    lista.append(round(random.random()*100))
    print (lista)
for i in lista:
    print (i)
    multiplos5(i)

    
    
                
    
       
        









    