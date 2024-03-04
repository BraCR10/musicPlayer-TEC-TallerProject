from insercion import insertProp
from insercion import insertPlaylist
from insercion import insertAlbum
from insercion import insertGen
from insercion import insertCanciones
from insercion import insertArt
#Esta busca un usuario por codigo
def buscarProp(codProp): 
    for i in insertProp()[1]:
          if i[0]==codProp:#Si el propietario ingresado esta en los codigos
              nombre=i[1]      
    return nombre

#Esta busca una Playlist por codigo
def buscarPlaylist(codPlaylist): 
    for i in insertPlaylist()[1]:
          if i[0]==codPlaylist:#Si la Playlist es en la memoria 
              nombrePlaylist=i[1] #Almacena nombre de la playlist
              codProp=i[2]#Almacena el codigo de la persona
    for i in insertProp()[1]:
        if i[0]==codProp:#Verifica el codigo de la persona
            nombreProp=i[1] #Obtiene el nombre de la persona

    return nombrePlaylist,nombreProp#Retorna Nombre de playlist y Nombre de persona al que pertenece

#Esta busca una cancion por codigo
def buscarCancion(codCancion): 
    for i in insertCanciones()[1]:
          if i[0]==codCancion:#Si la Cancion es en la memoria 
              nombreCacion=i[1] #Almacena nombre de la Cancion
              codArt=i[2]#Almacena el codigo del Artista
              codAlbum=i[3]
              codGenero=i[4]
              codPlaylist=i[5]
    for i in insertGen()[1]:
        if i[0]==codGenero:#Verifica el codigo del genero
            nombreGenero=i[1] #Obtiene el nombre del Genero
    for i in insertAlbum()[1]:
        if i[0]==codAlbum:#Verifica el codigo del album
            nombreAlbum=i[1] #Obtiene el nombre del album
    for i in insertArt()[1]:
        if i[0]==codArt:#Verifica el codigo del artista
            nombreArtista=i[1] #Obtiene el nombre del artista
    for i in insertPlaylist()[1]:
        if i[0]==codPlaylist:#Verifica el codigo de la playlist
            nombrePlaylist=i[1] #Obtiene el nombre de la playlist

    return nombreCacion,nombreArtista,nombreAlbum,nombreGenero,nombrePlaylist#Retorna Nombre de cancion y los datos adicionales
