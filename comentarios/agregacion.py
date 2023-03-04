class Aprendiz:                #crear clase
    def __init__(self,nombre): #contructor para el objeto
        self.__nombre=nombre   #instanciar
        self.__cursos=[]       #curso es una lista
    def agregarCurso(self,nombreCurso):   #metofo para agregar curso
        self.__cursos.append(nombreCurso) #.append se usa para agregar
    def verCursos(self):           #metodo para mostrar el contenido de la clase
        return self.__cursos

class Curso:              #crear clase
    def __init__(self,nombreCurso):   #instanciar la clase
        self.__nombreCurso=nombreCurso

    def getNombreCurso(self):      #metodo para los nombres del curso
        return self.__nombreCurso
    
ob=Aprendiz('Miguel')            #objetos creados partir de las clases
c1=Curso('Python Basico')
c2=Curso('Python Intermedio')
c3=Curso('Java Basico')

ob.agregarCurso(c1)        #se agregan los cursos a la lista de aprendiz
ob.agregarCurso(c2)
ob.agregarCurso(c3)

for curso in ob.verCursos():       #un for para iterar y recorrer la lista
    print(curso.getNombreCurso())  #muestra la lista

del ob         #del para borrar ob "aprendiz"
#print(ob)
print('.....',c1.getNombreCurso()) #se visualizan los cursos ya que son objetos por aparte