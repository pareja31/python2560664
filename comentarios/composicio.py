class Curso:            #crear clase
    def __init__(self,titulo):  #contructor
        self.__titulo=titulo   #instanciar objeto

    def getTitulo(self):     #titulo del curso
        return self.__titulo  #renorna el titulo

class Aprendiz:               #crear clase aprendiz
    def __init__(self,nombre):  #contructor de la clase
        self.__nombre=nombre #instanciar objeto
        self.__cursos=[]  #se guarda en una lista

    def agregarCurso(self,nombreCursito):  # metodo para agregar el curso
        cursito=Curso(nombreCursito)   #se intancia titulo que seria "nombrecursito"
        self.__cursos.append(cursito)  #linea en la que se agrefa cursito a la lista de curso

    def getCursos(self):      #objeter el contenido del curso
        return self.__cursos
    
ap=Aprendiz('Sofia')          #se llenan los datos de los parametros
ap.agregarCurso('Python Basico')
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():    #el for recorre ap "los nombres del curso"
    print(c.getTitulo())

del ap   #se borra el nombre del aprendiz