list={}


def cancion(spotify):
    canciones=input("buscar cancion")
    list.update({canciones:{}})
    return spotify

def completar(spotify):
    cancion= input("nombre de la cancion")
    if cancion not in spotify:
         print('La cancion no esta, agreguela primero') 
    artista= input('Ingrese el nombre del artista:') 
    genero=input('Ingrese el genero musical:')
    duracion=input('Ingrese la duracion:')

    if cancion in spotify:
        spotify.update({cancion:{'artista':artista,'genero':genero,'duracion':duracion}})
    return spotify






def bus():
    for i in list:
        a1=input("Busque al artista:")
        if a1 in list[i]:
            print(list[i])
            
    for i in list.values():
        return list

def buscar_artista(spotify):
    bus=input("buscar artista")
    for a in (spotify.values()):
        if bus==a["artista"]:
            print(("el artista esta en la lista: "),bus)
        else:
            print("no esta en la lista")

match list:
    case 1:
        print("ingrese cancion")
        cancion(list)
    case 2:
        print("infromacion completa")
        completar(list)




cancion(list)
completar(list) 
print(list)











