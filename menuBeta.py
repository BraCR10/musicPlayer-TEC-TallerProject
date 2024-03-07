from insercion import insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp
from busqueda import buscarAlbum,buscarArtista,buscarCancion,buscarGenero,buscarPlaylist,buscarProp
from eliminacion import eliminarProp,eliminarCanciones,eliminarPlaylist

def menu():
    listaPropcod,listaProptodo=insertProp()
    listaGencod,listaGentodo=insertGen()
    listaArtcod,listaArttodo=insertArt()
    listaAlbumcod,listaAlbumtodo=insertAlbum()
    listaPlaylistcod,listaPlaylisttodo=insertPlaylist()
    listaCancionescod,listaCancionestodo=insertCanciones()
    while True:
        print('\nBienvenidos a el reproductor\n')
        print('Escoja una opcion:\n')
        print('1- Buscar')   
        print('2- Eliminar')  
        print('3- Listas dipnibles')
        print('4- Salir') 
        opcion=int(input('\nDigite un numero: '))
        if opcion==1:#Busquedas
            print('\nEscoja una opcion:\n')
            print('1- Buscar Propietario') 
            opcion=int(input('\nDigite un numero: '))
            if opcion==1:
                dato=str(input('\nDigite el codigo: '))
                print('\n El propietario es: ',buscarProp(dato))
                opcion=str(input('Volver? Y/N: '))
                if opcion == 'Y' or opcion == 'y':
                    continue
                else:
                    break
        elif opcion==2:#Eliminaciones
            print('\nEscoja una opcion:\n')
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
        elif opcion==3:#Consultas
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