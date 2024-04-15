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
    

#Faltan###########################################################################################################
def buscarGenero(codGenero,listaGen):
    nombreGenero=[]
    for i in listaGen:
        if i[0]==codGenero:#Si el genero esta en la memoria
            nombreGenero=i[1] #Almacena nombre del genero
    if nombreGenero!=[]:
        return nombreGenero #Retorna el nombre del genero

def buscarArtista(codArtista,listaArt,listaGen):
    nombreArtista=[]
    codGenero=[]
    nombreGenero=0
    for i in listaArt:
        if i[0]==codArtista:
            nombreArtista=i[1]
            codGenero=i[2]
    for i in listaGen:
        if i[0]==codGenero:
            nombreGenero=i[1]
    if nombreArtista!=[] and nombreGenero!=0:
        return nombreArtista,nombreGenero

def buscarAlbum(codAlbum,listaAlbum,listaArt,listaGen):
    nombreAlbum=[]
    codArtista=[]
    codGenero=[]
    nombreArtista=0 
    nombreGenero=0
    for i in listaAlbum:
        if i[0]==codAlbum:
            nombreAlbum=i[1]
            codArtista=i[2]
    for i in listaArt:
        if i[0]==codArtista:
            nombreArtista=i[1]
            codGenero=i[2]
    for i in listaGen:
        if i[0]==codGenero:
            nombreGenero=i[1]
    if nombreAlbum!=[] and nombreArtista!=0 and nombreGenero!=0:
        return nombreAlbum,nombreArtista,nombreGenero

