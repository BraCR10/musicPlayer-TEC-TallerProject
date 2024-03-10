def modificarProp(codProp,listaTodo,valorACambiar):
    copiaTodo=listaTodo
    ubicacion=0#Ubica el campo que hay que cambiar
    for i in copiaTodo:
        if i[0] == codProp:
                ubicacion=copiaTodo.index(i)#La ubicacion de la lista que hay que cambiar
                print(i[1])
                copiaTodo[ubicacion].remove(i[1])#Ubicado en la lista donde se encuentra los datos, eliminamos solo el nombre '[1]'
                copiaTodo[ubicacion].insert(1,valorACambiar)#A esa misma lista le insertamos en la posicion de nombres '[1]' el nuevo mobre
                #nombre=i[1] 
    return copiaTodo
def modificarGen(codGen,listaTodo,valorACambiar):
    copiaTodo=listaTodo
    ubicacion=0#Ubica el campo que hay que cambiar
    for i in copiaTodo:
        if i[0] == codGen:
                ubicacion=copiaTodo.index(i)#La ubicacion de la lista que hay que cambiar
                print(i[1])
                copiaTodo[ubicacion].remove(i[1])#Ubicado en la lista donde se encuentra los datos, eliminamos solo el nombre '[1]'
                copiaTodo[ubicacion].insert(1,valorACambiar)#A esa misma lista le insertamos en la posicion de nombres '[1]' el nuevo mobre
                #nombre=i[1] 
    return copiaTodo
def modificarPlaylist(codPlaylist,listaTodo,valorACambiar):
    copiaTodo=listaTodo
    ubicacion=0#Ubica el campo que hay que cambiar
    for i in copiaTodo:
        if i[0] == codPlaylist:
                ubicacion=copiaTodo.index(i)#La ubicacion de la lista que hay que cambiar
                print(i[1])
                copiaTodo[ubicacion].remove(i[1])#Ubicado en la lista donde se encuentra los datos, eliminamos solo el nombre '[1]'
                copiaTodo[ubicacion].insert(1,valorACambiar)#A esa misma lista le insertamos en la posicion de nombres '[1]' el nuevo mobre
                #nombre=i[1] 
    return copiaTodo
def modificarArt(codArt,listaTodo,valorACambiar):
    copiaTodo=listaTodo
    ubicacion=0#Ubica el campo que hay que cambiar
    for i in copiaTodo:
        if i[0] == codArt:
                ubicacion=copiaTodo.index(i)#La ubicacion de la lista que hay que cambiar
                print(i[1])
                copiaTodo[ubicacion].remove(i[1])#Ubicado en la lista donde se encuentra los datos, eliminamos solo el nombre '[1]'
                copiaTodo[ubicacion].insert(1,valorACambiar)#A esa misma lista le insertamos en la posicion de nombres '[1]' el nuevo mobre
                #nombre=i[1] 
    return copiaTodo
def modificarcancion(codCancion,listaTodo,valorACambiar):
    copiaTodo=listaTodo
    ubicacion=0#Ubica el campo que hay que cambiar
    for i in copiaTodo:
        if i[0] == codCancion:
                ubicacion=copiaTodo.index(i)#La ubicacion de la lista que hay que cambiar
                print(i[1])
                copiaTodo[ubicacion].remove(i[1])#Ubicado en la lista donde se encuentra los datos, eliminamos solo el nombre '[1]'
                copiaTodo[ubicacion].insert(1,valorACambiar)#A esa misma lista le insertamos en la posicion de nombres '[1]' el nuevo mobre
                #nombre=i[1] 
    return copiaTodo


