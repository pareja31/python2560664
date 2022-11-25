#libro: libro para principiantes desarolladores


num=int(input("ingresar un numero "))
cont=0
for i in range (1, num+1):
    if num%i==0:
        cont=cont+1
if cont>2:
    print("no es un numero primo")
else:(print(num,"es un numero primo"))