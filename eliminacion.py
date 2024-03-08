#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

from insercion import *

        
def eliminarProp(codProp):
    copiaCod=insertProp()[0]
    copiaTodo=insertProp()[1]
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codProp:
            copiaCod.remove(codProp) 
    for i in copiaTodo:
        if i[0] == codProp:
                nombre=i[1]
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo,nombre

def eliminarPlaylist(codPlaylist):
    copiaCod=insertPlaylist()[0]
    copiaTodo=insertPlaylist()[1]
    for i in copiaCod:#i obtiene el valor de cada argumento
        if i == codPlaylist:
            copiaCod.remove(codPlaylist) 
    for i in copiaTodo:
        if i[0] == codPlaylist:
                nombre=i[1]
                copiaTodo.remove(i) 
    return copiaCod,copiaTodo,nombre

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

def eliminarArt(codArt):
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