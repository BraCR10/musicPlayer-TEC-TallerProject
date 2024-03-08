#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

from insercion import *#insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp
from busqueda import * #buscarAlbum,buscarArtista,buscarCancion,buscarGenero,buscarPlaylist,buscarProp
from eliminacion import *#eliminarProp,eliminarCanciones,eliminarPlaylist
def opcionNoExiste():
    print('\n ---> Esta opcion no exite')
    print('\nVolver al menu principal o salir?:')
    print('\n1- Volver al menu principal')   
    print('2- Salir de reproductor')  
    opcion=int(input('\nEscoja un numero segun la accion que desea realizar:  '))
    if opcion == 1:
        return True
def volver():
    print('\nVolver al menu principal o salir?:')
    print('\n1- Volver al menu principal')   
    print('2- Salir de reproductor')  
    opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
    if opcion==1:
        return True
def menu():
    listaPropcod,listaProptodo=insertProp()
    listaGencod,listaGentodo=insertGen()
    listaArtcod,listaArttodo=insertArt()
    listaAlbumcod,listaAlbumtodo=insertAlbum()
    listaPlaylistcod,listaPlaylisttodo=insertPlaylist()
    listaCancionescod,listaCancionestodo=insertCanciones()
    while True:
        print('\n--- BIENVENIDOS A EL REPRODUCTOR ---\n')
        print('Lista de opciones:\n')
        print('1- Buscar')#Agregar a cola
        print('2- Reproducir')   
        print('3- Eliminar')  
        print('4- Datos diponibles')
        print('5- Salir') 
        opcion=int(input('\nEscoja un numero: '))
        if opcion==1:#Busquedas
            print('\n------------------------------------------------------------------')
            print('\nLista de opciones:\n')
            print('1- Buscar Propietario') 
            print('2- Buscar Playlist') 
            print('3- Buscar Genero') 
            print('4- Buscar Artista') 
            print('5- Buscar Album') 
            print('6- Buscar Cancion') 
            opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
            if opcion==1:
                dato=str(input('\nDigite el codigo de propietario: '))
                if buscarProp(dato,listaProptodo)==None:
                    print('\n ---> El propietario no existe')
                else:
                    print('\n ---> El propietario es: ',buscarProp(dato,listaProptodo))
                if volver()==1:
                    continue
                else:
                    break
            elif opcion==2:
                dato=str(input('\nDigite el codigo de playlist: '))
                if buscarPlaylist(dato,listaPlaylisttodo,listaProptodo)==None:
                    print('\n ---> La playlist no existe')
                else:
                    print('\n ---> La playlist es: ',buscarPlaylist(dato,listaPlaylisttodo,listaProptodo))
                if volver()==1:
                    continue
                else:
                    break
            elif opcion==3:
                dato=str(input('\nDigite el codigo de genero: '))
                if buscarGenero(dato,listaGentodo)==None:
                    print('\n ---> El genero no existe')
                else:
                    print('\n ---> El genero es: ',buscarGenero(dato,listaGentodo))
                if volver()==1:
                    continue
                else:
                    break
            elif opcion==4:
                dato=str(input('\nDigite el codigo de artista: '))
                if buscarArtista(dato,listaArttodo,listaGentodo)==None:
                    print('\n ---> El artista no existe')
                else:
                    print('\n ---> La playlist es: ',buscarArtista(dato,listaArttodo,listaGentodo))
                if volver()==1:
                    continue
                else:
                    break
            elif opcion==5:
                dato=str(input('\nDigite el codigo de album: '))
                if buscarAlbum(dato,listaAlbumtodo,listaArttodo,listaGentodo)==None:
                    print('\n ---> El album no existe')
                else:
                    print('\n ---> el album es: ',buscarAlbum(dato,listaAlbumtodo,listaArttodo,listaGentodo))
                if volver()==1:
                    continue
                else:
                    break
            elif opcion==6:
                dato=str(input('\nDigite el codigo de cancion: '))
                if buscarCancion(dato,listaCancionestodo,listaAlbumtodo,listaArttodo,listaGentodo)==None:
                    print('\n ---> La cancion no existe')
                else:
                    print('\n ---> La cancion es: ',buscarCancion(dato,listaCancionestodo,listaAlbumtodo,listaArttodo,listaGentodo))
                if volver()==1:
                    continue
                else:
                    break
            else:
                if opcionNoExiste():
                    continue
                else:
                    break
        elif opcion==2:
            print('En proceso')
        elif opcion==3:#Eliminaciones
            print('\nLista de opciones:\n')
            print('1- Eliminar Propietario') 
            print('2- Eliminar Playlist') 
            print('3- Eliminar Genero') 
            print('4- Eliminar Artista') 
            print('5- Eliminar Album') 
            print('6- Eliminar Cancion') 
            opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
            if opcion==1:
                dato=str(input('\nDigite el codigo de propietario a eliminar: '))
                if dato in listaPropcod:
                    listaPropcod,listaProptodo,nombre=eliminarProp(dato)#Actualiza la lista si el codigo no existe, la deja igual
                    for i in listaPlaylisttodo:
                        if i[2]==dato:#Los elemento [2] de todo lista contienen codProp
                            listaPlaylistcod,listaPlaylisttodo=eliminarPlaylist(i[0])#Actualiza la lista si el codigo no existe, la deja igual
                    print(f'\nEl propietario "{nombre}" ha sido eliminado correctamente')
                    if volver():
                        continue
                    else:
                        break
                else:
                    print('\n--->El propietario no exite')
                    if volver():
                        continue
                    else:
                        break
            elif opcion==2:
                codplaylist=str(input('\nDigite el codigo de playlist a eliminar: '))
                codprop=str(input('\nDigite el codigo de propietario al que pertenece la playlist: '))
                if codplaylist in listaPlaylistcod and codprop in listaPropcod :
                    check=0#Para verificar si el prop tiene vinculada la playlist
                    for i in listaPlaylisttodo:
                        if i[2]==codprop:
                            check=1
                            break
                    if check==1:
                        listaPlaylistcod,listaPlaylisttodo,nombre=eliminarPlaylist(codplaylist)#Actualiza la lista si el codigo no existe, la deja igual
                        for i in listaCancionestodo:
                            if i[5]==codplaylist:#Los elemento [5] de todo lista contienen codPlaylist
                                listaCancionescod,listaCancionestodo=eliminarCanciones(i[0])#Actualiza la lista si el codigo no existe, la deja igual
                        print(f'\nEl propietario "{nombre}" ha sido eliminado correctamente')
                        if volver():
                            continue
                        else:
                            break
                else:
                    print('\n--->La playlist no existe o los datos no conciden')
                    if volver():
                        continue
                    else:
                        break
            else:
                if opcionNoExiste():
                    continue
                else:
                    break 
           
        elif opcion==4:#Consultas
            print('Escoja una opcion:\n')
            print('1- Ver Propietarios')
            print('2- Ver Playlist')
            opcion=int(input('Digite un numero: '))
            if opcion==1:
                print(listaProptodo)
            if opcion==2:
                print(listaPlaylisttodo)
            opcion=str(input('Volver? Y/N: '))
            if opcion == 'Y' or opcion == 'y':
                continue
            else:
                break
        else:
            if opcionNoExiste():
                continue
            else:
                break
menu()