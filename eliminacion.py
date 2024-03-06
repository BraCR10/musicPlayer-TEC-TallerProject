from insercion import insertProp
from insercion import insertPlaylist
from insercion import insertAlbum
from insercion import insertGen
from insercion import insertCanciones
from insercion import insertArt
        
def eliminarProp(codProp):
    copiaCod=insertProp()[0]
    copiaTodo=insertProp()[1]
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codProp:
            copiaCod.remove(codProp) 
    for i in copiaTodo:
        if i[0] == codProp:
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo

def eliminarPlaylist(codPlaylist):
    copiaCod=insertPlaylist()[0]
    copiaTodo=insertPlaylist()[1]
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codPlaylist:
            copiaCod.remove(codPlaylist) 
            print(copiaCod)
    for i in copiaTodo:
        if i[0] == codPlaylist:
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo
print(eliminarPlaylist('985'))

def eliminarGenero(codGen):
    copiaCod=insertGen()[0]
    copiaTodo=insertGen()[1]
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codGen:
            copiaCod.remove(codGen) 
    for i in copiaTodo:
        if i[0] == codGen:
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo

def eliminarArtista(codArt):
    copiaCod=insertArt()[0]
    copiaTodo=insertArt()[1]
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codArt:
            copiaCod.remove(codArt) 
    for i in copiaTodo:
        if i[0] == codArt:
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo

def eliminarAlbum(codAlb):
    copiaCod=insertAlbum()[0]
    copiaTodo=insertAlbum()[1]
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codAlb:
            copiaCod.remove(codAlb) 
    for i in copiaTodo:
        if i[0] == codAlb:
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo

def eliminarCanciones(codCancion):
    copiaCod=insertCanciones()[0]
    copiaTodo=insertCanciones()[1]
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codCancion:
            copiaCod.remove(codCancion) 
    for i in copiaTodo:
        if i[0] == codCancion:
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo
