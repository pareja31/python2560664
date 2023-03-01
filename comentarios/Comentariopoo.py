

class Persona:                  #se define la clase
    def __init__(self,nombre):  #funcion con parametros incluyendo el contructor
        self.__nombre=nombre    #parametro de la clase persona
        #print('Constructor Activado')        

    def getNombre(self):        #"get" se usa para visualizar el parametro (funcion)
        return self.__nombre    

    def setNombre(self,nombre): #"set" se usa para cambiar el parametro de la clase (funcion)
        self.__nombre=nombre

ob=Persona('anguie')        #se llama a la clase persona y el parametro anguie
print(ob.getNombre())       
ob.setNombre('julian')      #se cambia el parametro con la funcion set
print(ob.getNombre())       #imprime el nuevo valor
#print(type(ob))

class Aprendiz(Persona):    #se crea una subclase llamada aprendiz 
    def __init__(self,nombre,ficha):  #pero ahora se le agrega un nuevo parametro llamada ficha (con sus herencias)
        Persona.__init__(self,nombre)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha

app=Aprendiz('manuel',2560664)  #se le agrega un valor al parametro ficha 
print(app.getFicha())
print(app.getNombre())

class Documento(Persona):    #se crea otra subclase llamada documento
    def __init__(self, nombre,documento): #parametro para numero de documento
        Persona.__init__(self,nombre)
        self.__documento=documento

    def getDocumento(self):
        return self.__documento

    def setDocumento (self,documento):
        self.__documento=documento

asd=Documento("jeorge",103264541)  
print(asd.getDocumento())      
asd.setDocumento("15124456")   
print(asd.getDocumento())


        

