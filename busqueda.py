from insercion import insertProp
from insercion import insertPlaylist

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



