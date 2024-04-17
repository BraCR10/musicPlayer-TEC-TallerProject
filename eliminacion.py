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
#############################################################################################################################
#Falta
def eliminarGenero(codGen,listaCod,listaTodo):
    copiaCod=listaCod
    copiaTodo=listaTodo
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codGen:
            copiaCod.remove(codGen) 
    for i in copiaTodo:
        if i[0] == codGen:
                nombre=i[1]
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo,nombre
#Falta
def eliminarArt(codArt,listaCod,listaTodo):
    copiaCod=listaCod
    copiaTodo=listaTodo
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codArt:
            copiaCod.remove(codArt) 
    for i in copiaTodo:
        if i[0] == codArt:
                nombre=i[1]
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo,nombre
#Falta
def eliminarAlbum(codAlb,listaCod,listaTodo):
    copiaCod=listaCod
    copiaTodo=listaTodo
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codAlb:
            copiaCod.remove(codAlb) 
    for i in copiaTodo:
        if i[0] == codAlb:
                nombre=i[1]
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo,nombre





