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

def insertPlaylist(diccTodo,diccTodoProp):
    cod =str(input('Digite el codigo de la playlist: '))
    nombre= str(input('Digite el nombre de la playlist: '))
    codProp= str(input('Digite el codigo del propietario al que pertenece: '))
    if cod not in list(diccTodo.keys()) and codProp in list(diccTodoProp.keys()):#Validacion si codigo esta repetido
        if diccTodoProp[codProp]['estado']=="1":#Busca en el diccionario de Propietarios la key para ver si esta activo
            diccTodo[cod]={'nombre':nombre,'codProp':codProp}#Añade  una playlist al dict
            print('\n---> La nueva playlist se ha incluido!')
        else:
            print('\n---> No se puede insertar la playlist debido a que el propietario no esta activo!')
    else:
        print('\n---> El codigo de playlist ya esta en uso o el codigo de propietario no existe')    
    return diccTodo

def insertGen(diccTodo):
    cod =str(input('Digite el codigo del genero: '))
    nombre= str(input('Digite el nombre del genero: '))
    if cod not in  list(diccTodo.keys()):#Validacion si codigo esta repetido
        diccTodo[cod]={'nombre':nombre}#Añade  un genero al dict
        print('\n---> El nuevo genero se ha incluido!')
    else:
        print('\n---> El codigo del genero ya esta en uso')       
    return diccTodo
#insertGen(leerGen) PEDIENTE DE REVISAR

def insertArt(diccTodo,diccTodoGen):
    cod =str(input('Digite el codigo del artista: '))
    nombre= str(input('Digite el nombre del artista: '))
    codGen= str(input('Digite el codigo del genero al que pertenece: '))
    if cod not in list(diccTodo.keys()) and codGen in list(diccTodoGen.keys()):#Validacion si codigo esta repetido
        diccTodo[cod]={'nombre':nombre,'codGen':codGen}#Añade  una playlist al dict
        print('\n---> El nuevo artista se ha incluido!')
    else:
        print('\n---> El codigo de artista ya esta en uso o el codigo de genero no existe')    
    return diccTodo

def insertAlbum(diccTodo,diccTodoArt):
    cod =str(input('Digite el codigo del album: '))
    nombre= str(input('Digite el nombre del album: '))
    codArt= str(input('Digite el codigo del artista al que pertenece: '))
    if cod not in list(diccTodo.keys()) and codArt in list(diccTodoArt.keys()):#Validacion si codigo esta repetido
        diccTodo[cod]={'nombre':nombre,'codArt':codArt}#Añade  una playlist al dict
        print('\n---> El nuevo album se ha incluido!')
    else:
        print('\n---> El codigo de album ya esta en uso o el codigo de artista no existe')    
    return diccTodo

def insertCanciones(diccTodo,diccTodoArt,diccTodoAlbum,diccTodoGen,diccTodoPlaylist):
    cod =str(input('Digite el codigo de la cancion: '))
    nombre= str(input('Digite el nombre de la cancion: '))
    codArt= str(input('Digite el codigo del artista al que pertenece: '))
    codAlb= str(input('Digite el codigo del album al que pertenece: '))
    codGen= str(input('Digite el codigo del genero al que pertenece: '))
    codPlaylist= str(input('Digite el codigo de la playlist al que pertenece: '))
    if cod not in list(diccTodo.keys()) and codArt in list(diccTodoArt.keys()) and codAlb in list(diccTodoAlbum.keys()) and codGen in list(diccTodoGen.keys()) and codPlaylist in list(diccTodoPlaylist.keys()):#Validacion si codigo esta repetido
        diccTodo[cod]={'nombre':nombre,'codArt':codArt,'codAlb':codAlb,'codGen':codGen,'codPlaylist':codPlaylist}#Añade  una playlist al dict
        print('\n---> La nueva cancion se ha incluido!')
    else:
        print('\n---> El codigo de cancion ya esta en uso o alguno de los codigos de los requerimientos asociados no existe')    
    return diccTodo