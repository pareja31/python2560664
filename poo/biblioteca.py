class lector:
    def __init__(self,nombre,direccion,telefono):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
    def getnombre(self):
        return self.__nombre
    def gettelefono(self):
        return self.__telefono
    



class estudiante (lector):
    def __init__(self,codigoestudiante):
        self.__codigoestudiante=codigoestudiante
    def getcodigoestudiante(self):
        return self.__codigoestudiante



class docente (lector):
    def __init__(self,codigodocente):
        self.codigodocente=codigodocente


class pedido:
    
    def __init__(self,titulomaterial,codigomaterial):
        self.__titulomaterial=titulomaterial
        self.__codigomaterial=codigomaterial
    def gettitulomaterial (self):
        return self.__titulomaterial
    def getcodigomaterial(self):
        return self.__codigomaterial
    
    
    

class bibliotecario(pedido):
    def __init__(self,idpersonal):
        self__idpersonal=idpersonal

class material():
    def __init__ (self, recervado,disponible, libros):
        self.recervado=recervado
        self.disponibles=disponible
        self.libros=libros
        biblioteca=[]
        
    
        
    def getrecervado(self):
        return self.recervado
    

p1=lector("docente","manuel","cra 2c #26-30", 3203664241)
print(p1.getnombre())
print(p1.gettelefono())
        

        
    




        

