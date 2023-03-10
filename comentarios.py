from aprendiz import * #se importan las clases previamente realizadas
from curso import *



with open('herencia/aprendices.txt','r') as flujo:    #aqui lo que se hace es poner la ruta de un archivo "txt"
    datos=flujo.read()                                #la "r" es para que lea el archivo    y el ".read" es para que lo devuelva como una cadena de texto 
    print(datos)                                      #imprime lo que haya en datos
    #flujo.write('2560664,maria,123')
aprendices=[]                                         #una lista vacia local
with open('herencia/aprendices.txt','r') as flujo:    #aqui nuevamete se llama el archivo para leerlo
    for linea in flujo:                               #se crea un print para que recorra flujo (que es el archivo)
        #print(linea)
        aprendices.append(linea.rsplit())             #para almacenarlo en la lista aprendices  

datosxlinea=[]                                        #se crea otra lista vacia
for aprendiz in aprendices:                           #se realiza un for para que se recorra la lista dentro de la lista aprendices              
    datosxlinea.append(aprendiz[0].split(','))        #con el metodo ".split" se parte la cadena de texto por cada "," que haya en la lista 
                                                      #ya que los datos que muestra en la lista es uno solo
#print(ob.getNombre())

print(datosxlinea)

listaDeObjetos=[]
for apr in datosxlinea:
     f=apr[0]
     n=apr[1]
     d=apr[2]
     ob=Aprendiz(f,n,d)
     print(ob)
     listaDeObjetos.append(ob)

for xx in listaDeObjetos:
    print(xx.getNombre())
    print(xx.getDocumento())
    print(xx.getFicha())