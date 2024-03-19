#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

#Esta busca un usuario por codigo
def buscarProp(codProp,listaProp): 
        nombre=[]
        for i in listaProp:
            if i[0]==codProp:#Si el propietario ingresado esta en los codigos
                nombre=i[1]      
        if nombre!=[]:
            return nombre
#print(insertProp()[1])

#Esta busca una Playlist por codigo
def buscarPlaylist(codPlaylist,listaPlaylist,listaProp): 
    nombrePlaylist=[]
    codProp=[]
    for i in listaPlaylist:
        if i[0]==codPlaylist:#Si la Playlist es en la memoria 
            nombrePlaylist=i[1] #Almacena nombre de la playlist
            codProp=i[2]#Almacena el codigo de la persona
    for i in listaProp:
        if i[0]==codProp:#Verifica el codigo de la persona
            nombreProp=i[1] #Obtiene el nombre de la persona
    if nombrePlaylist!=[] and codProp!=[]:
        return nombrePlaylist,nombreProp#Retorna Nombre de playlist y Nombre de persona al que pertenece

#Esta busca una cancion por codigo
def buscarCancion(codCancion,listaCancion,listaArt,listaAlbum,listaGen,listaPlaylist): 
    nombreCancion=[]
    codArt=[]
    codAlbum=[]
    codGenero=[]
    codPlaylist=[]
    for i in listaCancion:
        if i[0]==codCancion:#Si la Cancion es en la memoria 
            nombreCancion=i[1] #Almacena nombre de la Cancion
            codArt=i[2]#Almacena el codigo del Artista
            codAlbum=i[3]
            codGenero=i[4]
            codPlaylist=i[5]
            nombreArt=0
            nombreAlbum=0
            nombreGenero=0
            nombrePlaylist=0
    for i in listaArt:
        if i[0]==codArt:#Verifica el codigo del genero
            nombreArt=i[1] #Obtiene el nombre del Genero
    for i in listaAlbum:
        if i[0]==codAlbum:#Verifica el codigo del album
            nombreAlbum=i[1] #Obtiene el nombre del album
    for i in listaGen:
        if i[0]==codGenero:#Verifica el codigo del artista
            nombreGenero=i[1] #Obtiene el nombre del artista
    for i in listaPlaylist:
        if i[0]==codPlaylist:#Verifica el codigo de la playlist
            nombrePlaylist=i[1] #Obtiene el nombre de la playlist
    if nombreCancion!=[] and nombreArt!=0 and nombreAlbum!=0 and nombreGenero!=0 and nombrePlaylist!=0: 
        return nombreCancion,nombreArt,nombreAlbum,nombreGenero,nombrePlaylist#Retorna Nombre de cancion y los datos adicionales


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

#Pruebas
'''print(buscarProp('1234'))
print(buscarGenero('109'))
print(buscarPlaylist('3920'))
print(buscarArtista('11534'))'''
#print(buscarAlbum('34561',insertAlbum()[1],insertArt()[1],insertGen()[1]))
#print(buscarCancion('124'))