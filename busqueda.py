#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

#Esta busca un usuario por codigo
def buscarProp(codProp,diccProptodo): 
        for i in list(diccProptodo.keys()):
            if i==codProp:#Si el propietario ingresado esta en los codigos
                return diccProptodo[codProp]['nombre']

#Esta busca una Playlist por codigo
def buscarPlaylist(codPlaylist,diccPlaylisttodo,diccProptodo): 
    for i in list(diccPlaylisttodo.keys()):
        if i==codPlaylist:#Si la Playlist es en la memoria 
            return diccPlaylisttodo[i]['nombre'], diccProptodo[diccPlaylisttodo[i]['codProp']]['nombre']#Retorna Nombre de playlist y los datos adicionales

#Esta busca una cancion por codigo
def buscarCancion(codCancion,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo): 
    for i in list(diccCancionestodo.keys()):
        if i==codCancion:#Si la Cancion es en la memoria 
            return diccCancionestodo[i]['nombre'], diccArttodo[diccCancionestodo[i]['codArt']]['nombre'],diccAlbumtodo[diccCancionestodo[i]['codAlb']]['nombre'],diccGentodo[diccCancionestodo[i]['codGen']]['nombre'],diccPlaylisttodo[diccCancionestodo[i]['codPlaylist']]['nombre']#Retorna Nombre de cancion y los datos adicionales

def buscarGenero(codGenero,diccGentodo):
    for i in list(diccGentodo.keys()):
        if i==codGenero:
            return diccGentodo[i]['nombre']

def buscarArtista(codArt,diccArttodo,diccGentodo):
    for i in list(diccArttodo.keys()):
        if i==codArt:
            return diccArttodo[i]['nombre'],diccGentodo[diccArttodo[i]['codGen']]['nombre']

def buscarAlbum(codAlb,diccAlbumtodo,diccArttodo):
    for i in list(diccAlbumtodo.keys()):
        if i==codAlb:
            return diccAlbumtodo[i]['nombre'],diccArttodo[diccAlbumtodo[i]['codArt']]['nombre']