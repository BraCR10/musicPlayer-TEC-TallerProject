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
def eliminadorDeVinculados(dato,listacod,listaTodo):#La usamos para eliminar cosas que se ven afectadas por la eliminacion de otras
    cont=0#Almacena la cantidad de codigos ligados que hay que eliminar
    i=0
    while i<len(listaTodo):#Obtiene la cantidad de codigos que hay que eliminar en la lista de Todo
        if listaTodo[i][2]==dato:
            cont+=1
        i+=1
    while cont>0:#Elimina codigo por codigo 
        if listaTodo[0][2] == dato:
            listacod,listaTodo,decartar=eliminarPlaylist(listaTodo[0][0],listacod,listaTodo)
        i+=1
        cont-=1
    return listacod,listaTodo        
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
                    cont=0#Almacena la cantidad de codigos ligados que hay que eliminar
                    i=0
                    listaPropcod,listaProptodo,nombre=eliminarProp(dato,listaPropcod,listaProptodo)#Actualiza la lista si el codigo no existe, la deja igual
                    listaPlaylistcod,listaPlaylisttodo=eliminadorDeVinculados(dato,listaPlaylistcod,listaPlaylisttodo)
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
                    for i in listaPlaylisttodo:#Pasa playlist por playlist verificando los codigos de prop registrados
                        if i[2]==codprop:
                            check=1
                            break
                    if check==1:#Si hay codigos
                        listaPlaylistcod,listaPlaylisttodo,nombre=eliminarPlaylist(codplaylist,listaPlaylistcod,listaPlaylisttodo)#Actualiza la lista si el codigo no existe, la deja igual
                        print(f'\nLa playlist  "{nombre}" ha sido eliminada correctamente')
                        if volver():
                            continue
                        else:
                            break
                    else:
                        print('\n El codigo de propietario no tiene relacion con la playlist')
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
            elif opcion==3:
                dato=str(input('\nDigite el codigo de propietario a eliminar: '))
                if dato in listaGencod:
                    listaGencod,listaGentodo,nombre=eliminarGenero(dato,listaGencod,listaGentodo)#Actualiza la lista si el codigo no existe, la deja igual
                    print(f'\nEl genero "{nombre}" ha sido eliminado correctamente')
                    if volver():
                        continue
                    else:
                        break
                else:
                    print('\n--->El genero no exite')
                    if volver():
                        continue
                    else:
                        break
            elif opcion==4:
                dato=str(input('\nDigite el codigo de artista a eliminar: '))
                if dato in listaArtcod:
                    listaArtcod,listaArttodo,nombre=eliminarArt(dato,listaArtcod,listaArttodo)#Actualiza la lista si el codigo no existe, la deja igual
                    print(f'\nEl artista "{nombre}" ha sido eliminado correctamente')
                    if volver():
                        continue
                    else:
                        break
                else:
                    print('\n--->El artista no exite')
                    if volver():
                        continue
                    else:
                        break
            elif opcion==5:
                dato=str(input('\nDigite el codigo de album a eliminar: '))
                if dato in listaAlbumcod:
                    listaAlbumcod,listaAlbumtodo,nombre=eliminarAlbum(dato,listaAlbumcod,listaAlbumtodo)#Actualiza la lista si el codigo no existe, la deja igual
                    print(f'\nEl album "{nombre}" ha sido eliminado correctamente')
                    if volver():
                        continue
                    else:
                        break
                else:
                    print('\n--->El album no exite')
                    if volver():
                        continue
                    else:
                        break
            elif opcion==6:
                dato=str(input('\nDigite el codigo de la cancion a eliminar: '))
                if dato in listaCancionescod:
                    listaCancionescod,listaCancionestodo,nombre=eliminarCanciones(dato,listaCancionescod,listaCancionestodo)#Actualiza la lista si el codigo no existe, la deja igual
                    print(f'\nLa cancion "{nombre}" ha sido eliminado correctamente')
                    if volver():
                        continue
                    else:
                        break
                else:
                    print('\n--->La cancion no exite')
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
            print('\nLista de opciones:\n')
            print('1- Ver Propietario') 
            print('2- Ver Playlist') 
            print('3- Ver Genero') 
            print('4- Ver Artista') 
            print('5- Ver Album') 
            print('6- Ver Cancion') 
            opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
            if opcion==1:
                print('\nLos propietarios registrados: \n')
                i=0
                print('Codigo - Nombre ')
                while i < len(listaProptodo):
                    print('-----------------------------------------')
                    print(f'{listaProptodo[i][0]} - {listaProptodo[i][1]}')
                    i+=1
            elif opcion==2:
                print('\nLas playlists registradas: ')
                i=0
                print('Codigo - Nombre - Codigo del Propietario \n')
                while i < len(listaPlaylisttodo):
                    print('-----------------------------------------')
                    print(f'{listaPlaylisttodo[i][0]} - {listaPlaylisttodo[i][1]} - {listaPlaylisttodo[i][2]}')
                    i+=1
            elif opcion==3:
                print('\nLos generos registrados: \n')
                i=0
                print('Codigo - Nombre ')
                while i < len(listaGentodo):
                    print('-----------------------------------------')
                    print(f'{listaGentodo[i][0]} - {listaGentodo[i][1]}')
                    i+=1
            elif opcion==4:
                print('\nLos artista registrados: \n')
                i=0
                print('Codigo - Nombre - Codigo del Genero ')
                while i < len(listaArttodo):
                    print('-----------------------------------------')
                    print(f'{listaArttodo[i][0]} - {listaArttodo[i][1]} - {listaArttodo[i][2]}')
                    i+=1
            elif opcion==5:
                print('\nLos albumes registrados: \n')
                i=0
                print('Codigo - Nombre - Codigo del Artista ')
                while i < len(listaAlbumtodo):
                    print('-----------------------------------------')
                    print(f'{listaAlbumtodo[i][0]} - {listaAlbumtodo[i][1]} - {listaAlbumtodo[i][2]}')
                    i+=1
            elif opcion==6:
                print('\nLas canciones registrados: \n')
                i=0
                print('Codigo - Nombre - Codigo del Artista - Codigo del Album - Codigo de Genero - Codigo de Playlist ')
                while i < len(listaCancionestodo):
                    print('-----------------------------------------')
                    print(f'{listaCancionestodo[i][0]} - {listaCancionestodo[i][1]} - {listaCancionestodo[i][2]} - {listaCancionestodo[i][3]} - {listaCancionestodo[i][4]} - {listaCancionestodo[i][5]}')
                    i+=1
            if volver():
                continue
            else:
                break
        elif opcion==5:
            break
        else:
            if opcionNoExiste():
                continue
            else:
                break
menu()