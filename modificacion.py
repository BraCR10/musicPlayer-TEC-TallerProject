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
    nuevo=str(input('\nDigite el nuevo nombre de la playlist : '))
    diccPlaylisttodo[codPlaylist]['nombre']= nuevo
########################################################################################################
 #Falta   
def modificarGen(codGen,listaTodo,valorACambiar):
    copiaTodo=listaTodo
    ubicacion=0#Ubica el campo que hay que cambiar
    for i in copiaTodo:
        if i[0] == codGen:
                ubicacion=copiaTodo.index(i)#La ubicacion de la lista que hay que cambiar
                copiaTodo[ubicacion].remove(i[1])#Ubicado en la lista donde se encuentra los datos, eliminamos solo el nombre '[1]'
                copiaTodo[ubicacion].insert(1,valorACambiar)#A esa misma lista le insertamos en la posicion de nombres '[1]' el nuevo mobre
                #nombre=i[1] 
    return copiaTodo

#Falta
def modificarArt(codArt,diccArttodo):
    nuevo=str(input('\nDigite el nuevo nombre del artista : '))
    diccArttodo[codArt]['nombre']=nuevo

#Falta
def modificarAlbum(codAlb,listaTodo,valorACambiar):
    copiaTodo=listaTodo
    ubicacion=0#Ubica el campo que hay que cambiar
    for i in copiaTodo:
        if i[0] == codAlb:
                ubicacion=copiaTodo.index(i)#La ubicacion de la lista que hay que cambiar
                copiaTodo[ubicacion].remove(i[1])#Ubicado en la lista donde se encuentra los datos, eliminamos solo el nombre '[1]'
                copiaTodo[ubicacion].insert(1,valorACambiar)#A esa misma lista le insertamos en la posicion de nombres '[1]' el nuevo mobre
                #nombre=i[1] 
    return copiaTodo

