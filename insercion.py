#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from lecturaArchivos import *
def insertProp(diccTodo):
    cod =str(input('Digite el codigo de propiertario: '))
    nombre= str(input('Digite el nombre de propiertario: '))
    codMem =str(input('Digite el codigo de la membresia: '))
    estado= str(input('Digite 0 para membresia inactiva o 1 para membresia activa : '))
    if estado== '1' or estado== '0':
        if cod  not in list(diccTodo.keys()):#Validacion si codigo esta repetido
            diccTodo[cod]={'nombre':nombre,'codMem':codMem,'estado':estado}#Añade  un propietario al dict
            print('\n---> El nuevo propietario se ha incluido!')
        else:
            print('\n---> El codigo de propietario ya esta en uso') 
    else:
        print('\nEl estado de la membresia debe ser 1 o 0, vuelva a insertar el usuario')
    return diccTodo

def insertPlaylist(listaCod,diccTodo,listaCodProp,diccTodoProp):
    cod =str(input('Digite el codigo de la playlist: '))
    nombre= str(input('Digite el nombre de la playlist: '))
    codProp= str(input('Digite el codigo del propietario al que pertenece: '))
    if cod not in listaCod and codProp in listaCodProp:#Validacion si codigo esta repetido
        if diccTodoProp[codProp][2]=="1":#Busca en el diccionario de Propietarios la key para ver si esta activo
            listaCod+=[cod]
            diccTodo[cod]=[nombre,codProp]
            print('\n---> La nueva playlist se ha incluido!')
        else:
            print('\n---> No se puede insertar la playlist debido a que el propietario no esta activo!')
    else:
        print('\n---> El codigo de playlist ya esta en uso o el codigo de propietario no existe') 
          
    return listaCod,diccTodo
def insertGen(listaCod,diccTodo):
    cod =str(input('Digite el codigo del genero: '))
    nombre= str(input('Digite el nombre del genero: '))
    if cod not in listaCod:#Validacion si codigo esta repetido
        listaCod+=[cod]
        diccTodo[cod]=[nombre]
        print('\n---> El nuevo genero se ha incluido!')
    else:
        print('\n---> El codigo del genero ya esta en uso')  
           
    return listaCod,diccTodo
def insertArt(listaCod,diccTodo,listaCodGen):
    cod =str(input('Digite el codigo del artista: '))
    nombre= str(input('Digite el nombre del artista: '))
    codGen= str(input('Digite el codigo del genero al que pertenece: '))
    if cod not in listaCod and codGen in listaCodGen:#Validacion si codigo esta repetido
        listaCod+=[cod]
        diccTodo[cod]=[nombre,codGen]
        print('\n---> El nuevo artista  se ha incluido!')
    else:
        print('\n---> El codigo del artista ya esta en uso o el codigo de genero no existe')
           
    return listaCod,diccTodo
def insertAlbum(listaCod,diccTodo,listaCodArt):
    cod =str(input('Digite el codigo del album: '))
    nombre= str(input('Digite el nombre del album: '))
    codArt= str(input('Digite el codigo del artista al que pertenece: '))
    if cod not in listaCod and codArt in listaCodArt:#Validacion si codigo esta repetido
        listaCod+=[cod]
        diccTodo[cod]=[nombre,codArt]
        print('\n---> El nuevo album  se ha incluido!')
    else:
        print('\n---> El codigo del album ya esta en uso o el codigo de artista no existe') 
           
    return listaCod,diccTodo
def insertCanciones(listaCod,diccTodo,listaCodArt,listaCodAlbum,listaCodGen,listaCodPlaylist):
    cod =str(input('Digite el codigo de la cancion: '))
    nombre= str(input('Digite el nombre de la cancion: '))
    codArt= str(input('Digite el codigo del artista al que pertenece: '))
    codAlb= str(input('Digite el codigo del album al que pertenece: '))
    codGen= str(input('Digite el codigo del genero al que pertenece: '))
    codPlaylist= str(input('Digite el codigo de la playlist al que pertenece: '))
    if cod not in listaCod and codArt in listaCodArt and codAlb in listaCodAlbum and codGen in listaCodGen and codPlaylist in listaCodPlaylist:#Validacion si codigo esta repetido
        listaCod+=[cod]
        diccTodo[cod]=[nombre,codArt,codAlb,codGen,codPlaylist]
        print('\n---> La nueva cancion  se ha incluido!')
    else:
        print('\n---> El codigo de la cancion ya esta en uso o digito algun codigo no existente') 
           
    return listaCod,diccTodo
