#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

def eliminarProp(codProp,diccProptodo,diccMembresias,diccPlaylisttodo,diccCancionestodo):
    #Eliminacion de vinculos
    for i in  list(diccPlaylisttodo.keys()):#i itera en una listas con las llaves del dicc playlist
        if diccPlaylisttodo[i]['codProp']==codProp:# Si el prop ligado a esa playlist es el que se elimina
            #Eliminacion de vinculo de playlist
            for codCancion in list(diccCancionestodo.keys()):#codCanciones itera en una lista de llaves de canciones
                if diccCancionestodo[codCancion]['codPlaylist']==i:#si la playlist ligada a esa cancion se elimina
                    diccCancionestodo.pop(codCancion)#
            diccPlaylisttodo.pop(i)
    #Eliminacion principal
    diccMembresias.pop(codProp)
    diccProptodo.pop(codProp)
        
def eliminarPlaylist(codPlaylist,diccPlaylisttodo,diccCancionestodo):
    #Eliminacion de vinculos
    for i in  list(diccCancionestodo.keys()):#i itera en una listas con las llaves del dicc playlist
        if diccCancionestodo[i]['codPlaylist']==codPlaylist:# Si el prop ligado a esa playlist es el que se elimina
            diccCancionestodo.pop(i)
    #Eliminacion principal
    diccPlaylisttodo.pop(codPlaylist)

def eliminarCanciones(dato,diccCancionestodo):
    #Eliminacion principal
    diccCancionestodo.pop(dato)

def eliminarGenero(codGen,diccGentodo,diccArttodo,diccAlbumtodo,diccCancionestodo):
    #Eliminacio de vinculos
    for i in  list(diccArttodo.keys()):#i itera en una listas con las llaves del dicc playlist
        if diccArttodo[i]['codGen']==codGen:# Si el prop ligado a esa playlist es el que se elimina
            #Eliminacion de vinculo de playlist
            for codAlbum in list(diccAlbumtodo.keys()):#codCanciones itera en una lista de llaves de canciones
                if diccAlbumtodo[codAlbum]['codArt']==i:#si la playlist ligada a esa cancion se elimina
                    for codCancion in list(diccCancionestodo.keys()):#codCanciones itera en una lista de llaves de canciones
                        if diccCancionestodo[codCancion]['codAlb']==i:#si la playlist ligada a esa cancion se elimina
                            diccCancionestodo.pop(codCancion)#
                    diccAlbumtodo.pop(codAlbum)#
            diccArttodo.pop(i)
    #Eliminacion principal
    diccGentodo.pop(codGen)

def eliminarArt(codArt,diccArttodo,diccAlbumtodo,diccCancionestodo):
    #Eliminacion de vinculos
    for i in  list(diccAlbumtodo.keys()):#i itera en una listas con las llaves del dicc playlist
        if diccAlbumtodo[i]['codArt']==codArt:# Si el prop ligado a esa playlist es el que se elimina
            diccAlbumtodo.pop(i)
    for i in list(diccCancionestodo.keys()):#codCanciones itera en una lista de llaves de canciones
        if diccCancionestodo[i]['codArt']==codArt:#si la playlist ligada a esa cancion se elimina
            diccCancionestodo.pop(i)
    #Eliminacion principal
    diccArttodo.pop(codArt)
#Falta
def eliminarAlbum(codAlb,diccAlbumtodo,diccCancionestodo):
    #Eliminacion de vinculos
    for i in list(diccCancionestodo.keys()):#codCanciones itera en una lista de llaves de canciones
        if diccCancionestodo[i]['codAlb']==codAlb:
            diccCancionestodo.pop(i)
    #Eliminacion principal
    diccAlbumtodo.pop(codAlb)





