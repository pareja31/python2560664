#libro: libro fuera de biblioteca "todo lo que debes saber de python"
#solo pueden entrar quienes temnga la edad requerida
#hombres mayores de 21 y mujeres mayores de 18

hombres_edad = 21
mujeres_edad =18
carlos_edad= 23
juan_edad=18
marta_edad=29

if carlos_edad > hombres_edad and juan_edad > hombres_edad and marta_edad > mujeres_edad:
    print ("puede pasar los 3 porque cumplen con la edad minima")
if carlos_edad < hombres_edad or juan_edad< hombres_edad or marta_edad<mujeres_edad:
    print("algunos no cumplen la condicion de edad, no pueden entrar juntos")
if carlos_edad> hombres_edad:
    print ("carlos puede pasar")
else:
    print("carlos no puede pasar")

if juan_edad >hombres_edad:
    print ("juan puede pasar")
else:
    print("juan no puede pasar")

if marta_edad>mujeres_edad:
    print("marta puede pasar")
else:
    ("marta no puede pasar")