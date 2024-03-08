#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

from insercion import *#insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp
from busqueda import * #buscarAlbum,buscarArtista,buscarCancion,buscarGenero,buscarPlaylist,buscarProp
from eliminacion import *#eliminarProp,eliminarCanciones,eliminarPlaylist

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
            opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
            if opcion==1:
                dato=str(input('\nDigite el codigo de propietario: '))
                if buscarProp(dato,listaProptodo)==None:
                    print('\n ---> El propietario no existe')
                else:
                    print('\n ---> El propietario es: ',buscarProp(dato,listaProptodo))
                print('\nVolver al menu principal o salir?:')
                print('\n1- Volver al menu principal')   
                print('2- Salir de reproductor')  
                opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                if opcion==1:
                    continue
                else:
                    break
            else:
                print('\n ---> Esta opcion no exite')
                print('\nVolver al menu principal o salir?:')
                print('\n1- Volver al menu principal')   
                print('2- Salir de reproductor')  
                opcion=int(input('\nEscoja un numero segun la accion que desea realizar:  '))
                if opcion == 1:
                    continue
                else:
                    break
        elif opcion==2:
            print('En proceso')
        elif opcion==3:#Eliminaciones
            print('\nLista de opciones:\n')
            print('1- Eliminar Propietario') 
            print('6- Eliminar Cancion') 
            opcion=int(input('\nDigite un numero: '))
            if opcion==1:
                dato=str(input('Digite el codigo a eliminar: '))
                listaPropcod,listaProptodo=eliminarProp(dato)
                for i in listaPlaylisttodo:
                    if i[2]==dato:
                        listaPlaylistcod,listaPlaylisttodo=eliminarPlaylist(i[0])
            
                print('\n Ha sido eliminado correctamente')
            if opcion==6:
                dato=str(input('Digite el codigo a eliminar: '))
                listaPropcod,listaProptodo=eliminarProp(dato)
                print('\n Ha sido eliminado correctamente')
            opcion=str(input('Volver? Y/N: '))
            if opcion == 'Y' or opcion == 'y':
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
            break
menu()