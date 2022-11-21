spotify={}

def artista(apotify):
    artista=input('esciba el nombre del artista:')
    duracion=input('escriba la duracion de la cancion')
    genero=input('escriba el genero:')
    cancion=input('escriba una cancion del artista:')
    spotify.update({artista:{'Genero': genero,'Cancion':{'Nombre':cancion,'Duracion':duracion}}})
    return spotify

def poner_cancion(spotify):
    artista=input('escriba el nombre del artista:')
    cancion=input('escriba otra cancion del artista:')
    if artista in spotify:
        spotify[artista.append,{cancion[nombre]}]
    return spotify

def buscar_artista(spotify):
    buscar=input('¿Que artista desea buscar?:')
    for i in sorted(spotify.keys()):
        if buscar==i:
            print('el artista', buscar, 'se encunetra en spotify y su genero es:',spotify.get(artista))
        else:
            print('el artista', buscar, '')