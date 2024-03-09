#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

def eliminarProp(codProp,listaCod,listaTodo):
    copiaCod=listaCod
    copiaTodo=listaTodo
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codProp:
            copiaCod.remove(codProp) 
    for i in copiaTodo:
        if i[0] == codProp:
                nombre=i[1]
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo,nombre

def eliminarPlaylist(codPlaylist,listaCod,listaTodo):
    copiaCod=listaCod
    copiaTodo=listaTodo
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codPlaylist:
            copiaCod.remove(codPlaylist) 
    for i in copiaTodo:
        if i[0] == codPlaylist:
                nombre=i[1]
                copiaTodo.remove(i) 
     
    #print(copiaTodo)
    return copiaCod,copiaTodo,nombre
#print(eliminarPlaylist('123',['123','127'],[['12','lll'],['123','127']]))  
#print(eliminarPlaylist('98',[],[['98', 'Musicaaaaaaaaaaaaaaal1', '123'], ['8844', 'pppppppppppp', '123'], ['77777777777777777', 'fffffffffffffffffffff', '123'], ['1745', 'Merengues unicos', '45780'], ['985', 'Viajando por la musica', '231'], ['3920', 'Volver al pasado', '50129']]))
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

def eliminarCanciones(codCancion,listaCod,listaTodo):
    copiaCod=listaCod
    copiaTodo=listaTodo
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codCancion:
            copiaCod.remove(codCancion) 
    for i in copiaTodo:
        if i[0] == codCancion:
                nombre=i[1]
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo,nombre



'''
#Pruebas
print(eliminarProp(''))
print(eliminarProp('1234'))
print('\n',eliminarGenero(''))
print(eliminarGenero('109'))
print('\n',eliminarPlaylist(''))
print(eliminarPlaylist('3920'))
print('\n',eliminarArt(''))
print(eliminarArt('11534'))
print('\n',eliminarAlbum(''))
print(eliminarAlbum('34561'))
print('\n',eliminarCanciones(''))
print(eliminarCanciones('124'))'''