#este programa llama todos los valores del diccionario
def funcion (dictionary):
    for a in dictionary.values():
        print(a)
    
d={"iphone":"ios",
   "samsung":"android",
   "elgi":"android"
}
j = input("que informacion quieres ? ")

try:
    print(f"el valor de su solicitud es  {d[j]}")
except KeyError:
    print(f"no hay ningun parametro {j}")

else:
    print("los valores almacenados que puedes escoger son ")  




funcion(d)