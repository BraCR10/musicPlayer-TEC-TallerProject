#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
#Commit
from lecturaArchivos import *#leerAlbum,leerArt,leerCanciones,leerGen,leerPlaylist,leerProp
from insercion import *#insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp

#Funciones auxiliares
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
#Menu principal
def menu():
    try :
        #Listas principales, se original de leer
        listaPropcod,diccProptodo=leerProp()
        listaGencod,diccGentodo=leerGen()
        listaArtcod,diccArttodo=leerArt()
        listaAlbumcod,diccAlbumtodo=leerAlbum()
        listaPlaylistcod,diccPlaylisttodo=leerPlaylist()
        listaCancionescod,diccCancionestodo=leerCanciones()
        while True:
            #Opciones de menu
            print('\n--- BIENVENIDOS A EL REPRODUCTOR ---\n')
            print('Lista de opciones:\n')
            print('1- Insertar')
            print('2- Ver datos cargados')
            print('3- Salir')
            #print('789- Datos diponibles') 
            opcion=int(input('\nEscoja un numero: '))
            if opcion==1:#Insercion
                print('\n------------------------------------------------------------------')
                print('\nLista de opciones:\n')
                print('1- Insertar Propietario') 
                print('2- Insertar Playlist') 
                print('3- Insertar Genero') 
                print('4- Insertar Artista') 
                print('5- Insertar Album') 
                print('6- Insertar Cancion') 
                print('7- Volver') 
                opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                if opcion==1:
                    listaPropcod,diccProptodo=insertProp(listaPropcod,diccProptodo)
                    if volver()==1:
                        continue
                    else:
                        break
                elif opcion==2:
                    listaPlaylistcod,diccPlaylisttodo=insertPlaylist(listaPlaylistcod,diccPlaylisttodo,listaPropcod,diccProptodo)
                    if volver()==1:
                        continue
                    else:
                        break
                elif opcion==3:
                    listaGencod,diccGentodo=insertGen(listaGencod,diccGentodo)
                    if volver()==1:
                        continue
                    else:
                        break
                elif opcion==4:
                    listaArtcod,diccArttodo=insertArt(listaArtcod,diccArttodo,listaGencod)
                    if volver()==1:
                        continue
                    else:
                        break
                elif opcion==5:
                    listaAlbumcod,diccAlbumtodo=insertAlbum(listaAlbumcod,diccAlbumtodo,listaArtcod)
                    if volver()==1:
                        continue
                    else:
                        break
                elif opcion==6:
                    listaCancionescod,diccCancionestodo=insertCanciones(listaCancionescod,diccCancionestodo,listaArtcod,listaAlbumcod,listaGencod,listaPlaylistcod)
                    if volver()==1:
                        continue
                    else:
                        break
                elif opcion==7:
                    continue
                else:
                    if opcionNoExiste():
                        continue
                    else:
                        break
           
            elif opcion==2:#Consultas
                print('\nLista de opciones:\n')
                print('1- Ver Propietario') 
                print('2- Ver Playlist') 
                print('3- Ver Genero') 
                print('4- Ver Artista') 
                print('5- Ver Album') 
                print('6- Ver Cancion') 
                print('7- Volver') 
                opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                if opcion==1:
                    print('\nLos propietarios registrados: \n')
                    i=0
                    print('Codigo - Nombre - Mebresia - Estado ')
                    claves = list(diccProptodo.keys())
                    while i < len(diccProptodo):
                        print('-----------------------------------------')
                        print(f'{claves[i]} - {diccProptodo[claves[i]][0]} - {diccProptodo[claves[i]][1]} - {diccProptodo[claves[i]][2]}')
                        i+=1
                elif opcion==2:
                    print('\nLas playlists registradas: ')
                    i=0
                    print('Codigo - Nombre - Codigo del Propietario \n')
                    claves = list(diccPlaylisttodo.keys())
                    while i < len(diccPlaylisttodo):
                        print('-----------------------------------------')
                        print(f'{claves[i]} - {diccPlaylisttodo[claves[i]][0]}- {diccPlaylisttodo[claves[i]][1]}')
                        i+=1
                elif opcion==3:
                    print('\nLos generos registrados: \n')
                    i=0
                    print('Codigo - Nombre ')
                    claves = list(diccGentodo.keys())
                    while i < len(diccGentodo):
                        print('-----------------------------------------')
                        print(f'{claves[i]} - {diccGentodo[claves[i]][0]}')
                        i+=1
                elif opcion==4:
                    print('\nLos artista registrados: \n')
                    i=0
                    claves = list(diccArttodo.keys())
                    print('Codigo - Nombre - Codigo del Genero ')
                    while i < len(diccArttodo):
                        print('-----------------------------------------')
                        print(f'{claves[i]} - {diccArttodo[claves[i]][0]} - {diccArttodo[claves[i]][1]}')
                        i+=1
                elif opcion==5:
                    print('\nLos albumes registrados: \n')
                    i=0
                    claves = list(diccAlbumtodo.keys())
                    print('Codigo - Nombre - Codigo del Artista ')
                    while i < len(diccAlbumtodo):
                        print('-----------------------------------------')
                        print(f'{claves[i]} - {diccAlbumtodo[claves[i]][0]} - {diccAlbumtodo[claves[i]][1]}')
                        i+=1
                elif opcion==6:
                    print('\nLas canciones registrados: \n')
                    i=0
                    claves = list(diccCancionestodo.keys())
                    print('Codigo - Nombre - Codigo del Artista - Codigo del Album - Codigo de Genero - Codigo de Playlist ')
                    while i < len(diccCancionestodo):
                        print('----------------------------------------------------------------------------------------------------')
                        print(f'{claves[i]} - {diccCancionestodo[claves[i]][0]} - {diccCancionestodo[claves[i]][1]} - {diccCancionestodo[claves[i]][2]} - {diccCancionestodo[claves[i]][3]} - {diccCancionestodo[claves[i]][4]}  ')
                       
                        i+=1
                if volver():
                    continue
                else:
                    break
            elif opcion==3:#Salir
                break
            else:#No existe
                if opcionNoExiste():
                    continue
                else:
                    break
    except ValueError:
        print( "\n---> Debes digitar un numero entero para escojer una opcion\n")       
    except NameError:
        print( "\n---> El programa ha tenido incovenientes\n")
        
    except TypeError:
        print( "\n---> El programa ha tenido incovenientes\n")
    except IndexError:
        print( "\n---> El programa ha tenido incovenientes\n")
    except KeyboardInterrupt:
        print( "\n---> El programa ha tenido incovenientes\n")
    finally:
        print( "\n---> Vuelva a cargar el programa\n")             
menu()