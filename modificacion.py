#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
def modificarProp(codProp,diccProptodo):
    nuevo=str(input('\nDigite el nuevo nombre de propietario: '))
    diccProptodo[codProp]['nombre']= nuevo#Actualiza en memoria
def modificarCancion(codCancion,diccCancionestodo):
    nuevo=str(input('\nDigite el nuevo nombre de la cancion: '))
    diccCancionestodo[codCancion]['nombre']=nuevo#Actualiza en memoria
def modificarPlaylist(codPlaylist,diccPlaylisttodo):
    nuevo=str(input('\nDigite el nuevo nombre de la playlist: '))
    diccPlaylisttodo[codPlaylist]['nombre']= nuevo 
def modificarGen(codGen,diccGentodo):
    nuevo=str(input('\nDigite el nuevo nombre del genero: '))
    diccGentodo[codGen]['nombre']=nuevo
def modificarArt(codArt,diccArttodo):
    nuevo=str(input('\nDigite el nuevo nombre del artista: '))
    diccArttodo[codArt]['nombre']=nuevo
def modificarAlbum(codAlb,diccAlbumtodo):
    nuevo=str(input('\nDigite el nuevo nombre del album: '))
    diccAlbumtodo[codAlb]['nombre']=nuevo

