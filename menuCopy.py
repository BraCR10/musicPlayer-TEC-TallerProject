#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from lecturaArchivos import *#leerAlbum,leerArt,leerCanciones,leerGen,leerPlaylist,leerProp
from insercion import *#insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp
from busqueda import * #buscarAlbum,buscarArtista,buscarCancion,buscarGenero,buscarPlaylist,buscarProp
from eliminacion import *#eliminarProp,eliminarCanciones,eliminarPlaylist,eliminarAlbum,eliminarGenero,eliminarArtistas
from modificacion import *#ModificarPlaylist,modificarArt,modificarCancion,modificarGen,modificarProp
from login import *#registar,pagar,exportarTXT,factura
from playsound import *
from reportes import *
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
    #try:
        #Listas principales, se original de leer
        diccProptodo=leerProp()[0]#Devuelve una lista con membresias
        diccMembresias=leerProp()[1]
        diccGentodo=leerGen()
        diccArttodo=leerArt()
        diccAlbumtodo=leerAlbum()
        diccPlaylisttodo=leerPlaylist()
        diccCancionestodo=leerCanciones()
        ColaDeReproduccion=[]
        #Verificador de login
        bandera=0
        #Contador de facturas al mismo usuario
        contFacturas=1
        #Contadores para crear los reportes 
        cont=''
        #Listas para crear reportes
        temp=[]
        #Listas para nunca buscados
        albumNuncaBuscado=[]
        artistaNuncaBuscado=[]
        modaMusica=[]
        while True:
            if bandera==0:
                print('\n--- BIENVENIDOS A EL REPRODUCTOR ---\n')
                codigo=str(input('Digite su codigo de propietario: '))#Para saber quien 
            if codigo not in list(diccProptodo.keys()) and bandera==0:#Si el usuario no existe
                print('\n ---> El  propietario no esta registrado! ')
                print('\nLista de opciones:\n')
                print('1- Registrarse') 
                print('2- Atras') 
                print('3- Salir') 
                opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                if opcion==1:#Buscar Propietario
                    registar(diccProptodo,diccMembresias)#Registro
                    if volver()==1:
                        continue
                    else:
                        break
                elif opcion==2:
                    continue
                elif opcion==3:
                    break
                else: 
                    if opcionNoExiste():
                        continue
                    else:
                        break   
            elif codigo in list(diccProptodo.keys()) and diccProptodo[codigo]['estado']=='0' and bandera==0:
                print('\n ---> El  propietario no esta activo! ')
                print('\nLista de opciones:\n')
                print('1- Activar') 
                print('2- Salir') 
                opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                if opcion==1:
                    factura(diccProptodo,codigo)
                    print('\nLista de opciones:\n')
                    print('1- Exportar a .txt') 
                    print('2- Pagar') 
                    print('3- Salir') 
                    opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                    if opcion==1:
                        exportarTXT(diccProptodo,codigo,contFacturas)
                        contFacturas+=1
                        print('\nLista de opciones:\n')
                        print('1- Pagar') 
                        print('2- Salir')
                        opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                        if opcion==1:
                            pagar(diccProptodo,diccMembresias,codigo)
                    elif opcion==2:
                        pagar(diccProptodo,diccMembresias,codigo)
                    else:
                        continue
                    if volver()==1:
                        continue
                    else:
                        break
                elif opcion==2:
                    continue
                else: 
                    if opcionNoExiste():
                        continue
                    else:
                        break 
            elif codigo in list(diccProptodo.keys()) and diccProptodo[codigo]['estado']=='1' or bandera ==1:
                bandera=1
                #Opciones de menu
                print('Lista de opciones:\n')
                print('1- Buscar')
                print('2- Insertar ')
                print('3- Reproducir')   
                print('4- Eliminar')  
                print('5- Modificar')
                print('6- Reportes')
                print('7- Consultar factura')
                print('8- Salir')
                #print('789- Datos diponibles') 
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
                    print('7- Volver') 
                    opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                    if opcion==1:#Buscar Propietario
                        dato=str(input('\nDigite el codigo de propietario: '))
                        if buscarProp(dato,diccProptodo)==None:#Validacion
                            print('\n ---> El propietario no existe')
                        else:#Validacion
                            print('\n ---> El nombre del propietario es: ',buscarProp(dato,diccProptodo))
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==2:#Buscar Playlist
                        dato=str(input('\nDigite el codigo de playlist: '))
                        if buscarPlaylist(dato,diccPlaylisttodo,diccProptodo)==None:#Validacion
                            print('\n ---> La playlist no existe')
                        else:#Validacion
                            print('\n ---> El nombre de la playlist es: ',buscarPlaylist(dato,diccPlaylisttodo,diccProptodo)[0], 'y el nombre del propietario es:', buscarPlaylist(dato,diccPlaylisttodo,diccProptodo)[1])
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==3:#Buscar Genero
                        dato=str(input('\nDigite el codigo de genero: '))
                        if buscarGenero(dato,diccGentodo)==None:#Validacion
                            print('\n ---> El genero no existe')
                        else:#Validacion
                            print('\n ---> El genero es: ',buscarGenero(dato,diccGentodo))
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==4:#Buscar Artistas
                        dato=str(input('\nDigite el codigo de artista: '))
                        if buscarArtista(dato,diccArttodo,diccGentodo)==None:#Validacion
                            print('\n ---> El artista no existe')
                        else:#Validacion
                            artistaNuncaBuscado+=[dato]
                            print('\n ---> El artista es: ',buscarArtista(dato,diccArttodo,diccGentodo)[0],' y el genero es: ',buscarArtista(dato,diccArttodo,diccGentodo)[1])
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==5:#Buscar Album
                        dato=str(input('\nDigite el codigo de album: '))
                        if buscarAlbum(dato,diccAlbumtodo,diccArttodo)==None:#Validacion
                            print('\n ---> El album no existe')
                        else:#Validacion
                            albumNuncaBuscado+=[dato]
                            print(f'\n ---> El album es: {buscarAlbum(dato,diccAlbumtodo,diccArttodo)[0]}, el artista es: {buscarAlbum(dato,diccAlbumtodo,diccArttodo)[1]}')
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==6:#Buscar cancion
                        dato=str(input('\nDigite el codigo de cancion: '))
                        if buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)==None:#Validacion
                            print('\n ---> La cancion no existe')
                        else:#Validacion
                            print(f'\n ---> La cancion es: {buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}, el artista: {buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[1]}, el album es: {buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[2]}, el genero es: {buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[3]} y la playlist es: {buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[4]} ' )
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==7:#Salir
                        continue
                    else:#No existe
                        if opcionNoExiste():
                            continue
                        else:
                            break
                elif opcion==2:#Insercion
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
                    if opcion==1:#Insertar Propietario
                        diccProptodo,diccMembresias=insertProp(diccProptodo,diccMembresias)
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==2:#Insertar Playlist
                        diccPlaylisttodo=insertPlaylist(diccPlaylisttodo,diccProptodo)
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==3:#Insertar Genero
                        diccGentodo=insertGen(diccGentodo)
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==4:#Insertar Artista
                        diccArttodo=insertArt(diccArttodo,diccGentodo)
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==5:#Insertar Album
                        diccAlbumtodo=insertAlbum(diccAlbumtodo,diccArttodo)
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==6:#Insertar canciones
                        diccCancionestodo=insertCanciones(diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==7:#Salir
                        continue
                    else:#INo existe
                        if opcionNoExiste():
                            continue
                        else:
                            break
                elif opcion==3:#Reproducir
                    print('\nLista de opciones:\n')
                    print('1- Añadir una cancion a la cola de reproduccion') 
                    print('2- Ver la cola de reproduccion') 
                    print('3- Reproducir cola de reproduccion')
                    print('4- Volver')
                    opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                    if opcion==1:#Agregar cancion
                        if len(ColaDeReproduccion)>=5:#Validacion
                            print('\n ---> La cola de reproduccion ya esta en su limite, no se puede agregar mas canciones')
                        else:#Validacion
                            dato=str(input('\nDigite el codigo de la cancion que desea añadir a la cola de reproduccion: ')) #Recibe un codigo de cancion
                            codArt= str(input('Digite el codigo del artista al que pertenece: '))
                            codAlb= str(input('Digite el codigo del album al que pertenece: '))
                            codGen= str(input('Digite el codigo del genero al que pertenece: '))
                            codPlaylist= str(input('Digite el codigo de la playlist al que pertenece: '))
                            codprop=str(input('Digite el codigo de propietario: '))
                            if dato in list(diccCancionestodo.keys()) and diccCancionestodo[dato]['codArt']==codArt and diccCancionestodo[dato]['codAlb']==codAlb and diccCancionestodo[dato]['codGen']==codGen and diccCancionestodo[dato]['codPlaylist']==codPlaylist and codprop in list(diccProptodo.keys()) and diccProptodo[codprop]['estado']=='1':
                                ColaDeReproduccion+=[dato]
                                print ('\n --->Se ha agregado la cancion: ',buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0], ' con el codigo:', dato, "a la cola de reproduccion!\n")
                            else:
                                print("\n --->Cancion inexsistente o los datos relacionados son incorrectos\n")
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==2:
                        print('\nLa cola de reproduccion es: ')
                        i=0
                        print('\nCodigo   -   Cancion   -   Artista ')
                        while i < len(ColaDeReproduccion):
                            print('----------------------------------------------')
                            if buscarCancion(ColaDeReproduccion[i],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)==None:
                                print('************** Eliminado **************')
                                ColaDeReproduccion.pop(i)#Elimina de cola de reproduccion lo que ya no existe por haberse eliminado
                            else:
                                print(f'{ColaDeReproduccion[i]}  -  {buscarCancion(ColaDeReproduccion[i],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}  -  {buscarCancion(ColaDeReproduccion[i],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[1]}')
                                i+=1
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==3:
                        i=0
                        for i in ColaDeReproduccion:
                            print('\n---> Si desea dejar de reproducir la cancion ejecute la tecla Ctrl + C, sin embargo, tenga en cuenta que esta accion detendra todo el programa y tendra que volver a inicializar el programa en caso de quiera seguir haciendo uso del mismo')
                            CodCancion=ColaDeReproduccion[0]
                            ruta=f'Canciones Wav\{CodCancion}.wav'
                            playsound(ruta)
                            modaMusica+=[CodCancion]
                            ColaDeReproduccion=ColaDeReproduccion[1:]
                        print('\n---> La cola de reproduccion ha quedado vacia')
                        if volver()==1:
                            continue
                        else:
                            break
                    elif opcion==4:
                        continue
                    else:
                        if opcionNoExiste():
                            continue
                        else:
                            break
                elif opcion==4:#Eliminacion
                    print('\nLista de opciones:\n')
                    print('1- Eliminar Propietario') 
                    print('2- Eliminar Playlist') 
                    print('3- Eliminar Genero') 
                    print('4- Eliminar Artista') 
                    print('5- Eliminar Album') 
                    print('6- Eliminar Cancion') 
                    print('7- Volver') 
                    opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                    if opcion==1: #Eliminar Propietario
                        dato=str(input('\nDigite el codigo de propietario a eliminar: ')) #Recibe un codigo de propietario
                        if dato in  list(diccProptodo.keys()): #Si el codigo esta en la lista de codigos de propietraios, entra.
                            print(f'\nEl propietario "{buscarProp(dato,diccProptodo)}" ha sido eliminado correctamente') #Imprime este mensaje si fue eliminado
                            #El mensaje se imprime debido a que busca dentro de la mima lista, si se  imprime despues dice 'None'
                            eliminarProp(dato,diccProptodo,diccMembresias,diccPlaylisttodo,diccCancionestodo)  
                        else:
                            print(f'\nEl propietario con el código "{dato}" no existe en la lista de propietarios.') #Imprime esto si no fue eliminado
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==2:#Eliminar playlist
                        dato=str(input('\nDigite el codigo de playlist a eliminar: ')) #Recibe un codigo de playlist
                        if dato in list(diccPlaylisttodo.keys()):
                            print(f'\nLa playlist "{buscarPlaylist(dato,diccPlaylisttodo,diccProptodo)[0]}" ha sido eliminado correctamente') #Imprime este mensaje si fue eliminado
                            #El mensaje se imprime debido a que busca dentro de la misma lista, si se  imprime despues dice 'None'
                            eliminarPlaylist(dato,diccPlaylisttodo,diccCancionestodo)  
                        else:
                            print(f'\nLa playlist  con el código "{dato}" no existe en la lista de playlists.') #Imprime esto si no fue eliminado
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==3:
                        dato=str(input('\nDigite el codigo de genero a eliminar: ')) #Recibe un codigo de genero
                        if dato in diccGentodo: #Si el codigo esta en la lista de codigos de propietraios, entra. 
                            print(f'\nEl genero "{buscarGenero(dato,diccGentodo)}" ha sido eliminado correctamente') #Imprime este mensaje si fue eliminado
                            eliminarGenero(dato,diccGentodo,diccArttodo,diccAlbumtodo,diccCancionestodo)
                        else:
                            print(f'\nEl Genero con el codigo "{dato}" no existe en la lista de generos')
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==4:
                        dato=str(input('\nDigite el codigo de artista a eliminar: '))
                        if dato in diccArttodo:
                            print(f'\nEl artista "{buscarArtista(dato,diccArttodo,diccGentodo)[0]}" ha sido eliminado correctamente')
                            eliminarArt(dato,diccArttodo,diccAlbumtodo,diccCancionestodo)
                        else:
                            print(f'\nEl artista con el codigo "{dato}" no existe en la lista de artistas')
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==5:
                        dato=str(input('\nDigite el codigo de album a eliminar: '))
                        if dato in diccAlbumtodo:
                            print(f'\nEl album "{buscarAlbum(dato,diccAlbumtodo,diccArttodo)[0]}" ha sido eliminado correctamente')
                            eliminarAlbum(dato,diccAlbumtodo,diccCancionestodo)
                        else:
                            print(f'\nEl album con el codigo "{dato}" no exite en la lista de albumes')
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==6:#Eliminar Cancion
                        dato=str(input('\nDigite el codigo de la cancion a eliminar: '))
                        if dato in list(diccCancionestodo.keys()):
                            print(f'\nLa cancion "{buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}" ha sido eliminado correctamente') #Imprime este mensaje si fue eliminado
                            #El mensaje se imprime debido a que busca dentro de la misma lista, si se  imprime despues dice 'None'
                            eliminarCanciones(dato,diccCancionestodo)  
                        else:
                            print(f'\nLa cancion  con el código "{dato}" no existe en la lista de canciones.') #Imprime esto si no fue eliminado
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==7:#Salir
                        continue
                    else:#No existe
                        if opcionNoExiste():
                            continue
                        else:
                            break     
                elif opcion==5:#Modificacion
                    print('\nLista de opciones:\n')
                    print('1- Modificar Propietario') 
                    print('2- Modificar Playlist') 
                    print('3- Modificar Genero') 
                    print('4- Modificar Artista') 
                    print('5- Modificar Album') 
                    print('6- Modificar Cancion') 
                    print('7- Volver') 
                    opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                    if opcion==1:#Modifica propietario
                        dato=str(input('\nDigite el codigo de propietario a modificar: '))
                        if dato in list(diccProptodo.keys()):#Revisa una lista de llaves
                            print(f'\n--->El propietario es: {buscarProp(dato,diccProptodo)}')
                            modificarProp(dato,diccProptodo)
                            print('\n--->El nombre de propietario se modifico con exito!')
                        else:
                            print('\n--->El propietario no existe') 
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==2:#Modifica playlist
                        dato=str(input('\nDigite el codigo de playlist a modificar: '))
                        if dato in list(diccPlaylisttodo.keys()):#Revisa una lista de llaves
                            print(f'\n--->La playlist es: {buscarPlaylist(dato,diccPlaylisttodo,diccProptodo)[0]}')
                            modificarPlaylist(dato,diccPlaylisttodo)
                            print('\n--->El nombre de la playlist se modifico con exito!')
                        else:
                            print('\n--->La playlist no existe')
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==3:#Modifica genero
                        dato=str(input('\nDigite el codigo de genero a modificar: '))
                        if dato in list(diccGentodo.keys()):
                            print(f'\n--->El genero es: {buscarGenero(dato,diccGentodo)[0]}')
                            modificarGen(dato,diccGentodo)
                            print('\n--->El nombre del genero se modifico con exito!')
                        else:
                            print('\n--->El genero no existe')
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==4:#Modifica Artistas
                        dato=str(input('\nDigite el codigo del artista a modificar: '))
                        if dato in list(diccArttodo.keys()):
                            print(f'\n--->El artista es: {buscarArtista(dato,diccArttodo,diccGentodo)[0]}')
                            modificarArt(dato,diccArttodo)
                            print('\n--->El nombre del artista se modifico con exito!')
                        else:
                            print('\n--->El artista no existe ')
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==5:#Modifica Albumes
                        dato=str(input('\nDigite el codigo del album a modificar: '))
                        if dato in list(diccAlbumtodo.keys()):
                            print(f'\n--->El Album es: {buscarAlbum(dato,diccAlbumtodo,diccArttodo)[0]}')
                            modificarAlbum(dato,diccAlbumtodo)
                            print('\n--->El nombre del album se modifico con exito!')
                        else:
                            print('\n--->El album no existe') 
                        if volver():
                            continue
                        else:
                            break
                    elif opcion==6:#Modifica Cancion
                        dato=str(input('\nDigite el codigo de cancion a modificar: '))
                        codArt=str(input('\nDigite el codigo del artista ligado a la cancion a modificar: '))
                        codAlb=str(input('\nDigite el codigo de album ligado a la cancion a modificar: '))
                        codGen=str(input('\nDigite el codigo del genero ligado a la cancion a modificar: '))
                        codPlaylist=str(input('\nDigite el codigo de la playlist ligada a la cancion a modificar: '))
                        if dato in list(diccCancionestodo.keys()) and diccCancionestodo[dato]['codArt']==codArt and diccCancionestodo[dato]['codAlb']==codAlb and diccCancionestodo[dato]['codGen']==codGen and diccCancionestodo[dato]['codPlaylist']==codPlaylist:  ##Revisa una lista de llaves de canciones y ademas valida que los demas datos existan
                            print(f'\n--->La cancion es: {buscarCancion(dato,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
                            modificarCancion(dato,diccCancionestodo)
                            print('\n--->El nombre la cancion se modifico con exito!')
                            if volver():
                                continue
                            else:
                                break
                        else:
                            print('\n--->La cancion no exite o los datos no coinciden')
                            if volver():
                                continue
                            else:
                                break
                    elif opcion==7:#Salir
                        continue
                    else:#No existe
                        if opcionNoExiste():
                            continue
                        else:
                            break
                elif opcion==6:#Reportes

                    from statistics import mode
                    print('\nLista de opciones:\n')
                    print('1- Reporte de Propietario')
                    print('2- Reporte de Playlist') 
                    print('3- Reporte de Genero') 
                    print('4- Reporte de Artista') 
                    print('5- Reporte de Album') 
                    print('6- Reporte de Cancion')
                    print('7- Reporte de Canción más reproducida')
                    print('8- Reporte de Artista con más canciones')
                    print('9- Reporte de Álbum con más canciones')
                    print('10- Reporte de Genero más solicitado')
                    print('11- Reporte de Propietario con más playlist')
                    print('12- Reporte de Álbum más solicitado')
                    print('13- Playlist con más canciones')
                    print('14- Genero con más artistas')
                    print('15- Genero con más álbumes')
                    print('16- Artista con más álbumes')
                    print('17- Canción que mas se repite en una playlist')
                    print('18- Album nunca buscado')
                    print('19- Artista nunca buscado')
                    print('20- Propietario sin playlist')
                    print('21- Canción nunca reproducida')
                    print('22- Volver')
                    opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                    if opcion==1:#Reporte propietarios
                        reportesProp(diccProptodo,cont)
                        cont=cont+'.'
                    elif opcion==2:#Reporte playlist
                        reportesPlaylist(diccPlaylisttodo,diccProptodo,cont)
                        cont=cont+'.'
                    elif opcion==3:#Reporte Genero
                        reporteGeneros(diccGentodo,cont)
                        cont=cont+'.'
                    elif opcion==4:#Reporte Artistas
                        reporteArt(diccArttodo,diccGentodo,cont)
                        cont=cont+'.'
                    elif opcion==5:#Reporte Album
                        resporteAlbumes(diccAlbumtodo,diccArttodo,cont)
                        cont=cont+'.'
                    elif opcion==6:#Reporte Cancion
                        reporteCancion(diccCancionestodo,diccArttodo,cont)
                        cont=cont+'.'
                    elif opcion==7:#Reporte Cancion mas reproducida
                        reportemodacanciones(diccCancionestodo,modaMusica,cont)
                        cont=cont+'.'
                    elif opcion==8:#Reporte de Artista con más canciones
                        artistaConMasCanciones(diccCancionestodo,temp,cont,diccArttodo,diccGentodo)
                        cont=cont+'.'
                    elif opcion==9:#Reporte de Álbum con más canciones
                        albumConMasCanciones(diccCancionestodo,temp,cont,diccAlbumtodo,diccArttodo)
                        cont=cont+'.'
                    elif opcion==10:#Reporte de Genero más solicitado
                        reportemodagenero(diccCancionestodo,diccGentodo,modaMusica,cont)
                        cont=cont+'.'
                    elif opcion==11:# Reporte de Propietario con más playlist
                        propietarioConMasPlaylist(diccProptodo,temp,cont,diccPlaylisttodo)
                        cont=cont+'.'
                    elif opcion==12:# Reporte de Álbum más solicitad
                        reportemodaalbum(diccCancionestodo,diccAlbumtodo,modaMusica,cont)
                        cont=cont+'.'
                    elif opcion==13:# Playlist con más canciones
                        playlistConMasCanciones(diccCancionestodo,temp,cont,diccPlaylisttodo,diccProptodo)
                        cont=cont+'.'
                    elif opcion==14:# Genero con más artistas
                        generoConMasArtistas(diccGentodo,temp,cont,diccArttodo)
                        cont=cont+'.'
                    elif opcion==15:# Genero con más álbumes
                        generoConMasAlbumes(diccGentodo,temp,cont,diccArttodo,diccAlbumtodo)
                        cont=cont+'.'
                    elif opcion==16:# Artista con más álbumes
                        artistaConMasAlbumes(temp,cont,diccArttodo,diccAlbumtodo,diccGentodo)
                        cont=cont+'.'
                    elif opcion==17:# Canción que mas se repite en una playlist
                        print('En proceso')
                    elif opcion==18:# Album nunca buscado
                        albumNuncaBuscadoFun(albumNuncaBuscado,diccAlbumtodo,temp,cont,diccArttodo)
                        cont=cont+'.'
                    elif opcion==19:# Artista nunca buscado
                        print('En proceso')
                    elif opcion==20:#  Propietario sin playlist
                        print('En proceso')
                    elif opcion==21:# Canción nunca reproducida
                        print('En proceso')
                    elif opcion==22:# Salir
                        continue
                    else:#No existe
                        if opcionNoExiste():
                            continue
                        else:
                            break 
                elif opcion==789:#Consultas
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
                            temp=list(diccProptodo[claves[i]].keys())#Almacena todas las llaves que pertenecena el diccionario con la llave
                            print('-----------------------------------------')
                            print(f'{claves[i]} - {diccProptodo[claves[i]][temp[0]]} - {diccProptodo[claves[i]][temp[1]]} - {diccProptodo[claves[i]][temp[2]]}')
                            i+=1
                    elif opcion==2:
                        print('\nLas playlists registradas: ')
                        i=0
                        print('Codigo - Nombre - Codigo del Propietario \n')
                        claves = list(diccPlaylisttodo.keys())
                        while i < len(diccPlaylisttodo):
                            temp=list(diccPlaylisttodo[claves[i]].keys())#Almacena todas las llaves que pertenecena el diccionario con la llave
                            print('-----------------------------------------')
                            print(f'{claves[i]} - {diccPlaylisttodo[claves[i]][temp[0]]} - {diccPlaylisttodo[claves[i]][temp[1]]} ')
                            i+=1
                    elif opcion==3:
                        print('\nLos generos registrados: \n')
                        i=0
                        print('Codigo - Nombre ')
                        claves = list(diccGentodo.keys())
                        while i < len(diccGentodo):
                            temp=list(diccGentodo[claves[i]].keys())#Almacena todas las llaves que pertenecena el diccionario con la llave
                            print('-----------------------------------------')
                            print(f'{claves[i]} - {diccGentodo[claves[i]][temp[0]]} ')
                            i+=1
                    elif opcion==4:
                        print('\nLos artista registrados: \n')
                        i=0
                        claves = list(diccArttodo.keys())
                        print('Codigo - Nombre - Codigo del Genero ')
                        while i < len(diccArttodo):
                            temp=list(diccArttodo[claves[i]].keys())#Almacena todas las llaves que pertenecena el diccionario con la llave
                            print('-----------------------------------------')
                            print(f'{claves[i]} - {diccArttodo[claves[i]][temp[0]]} - {diccArttodo[claves[i]][temp[1]]} ')
                            i+=1
                    elif opcion==5:
                        print('\nLos albumes registrados: \n')
                        i=0
                        claves = list(diccAlbumtodo.keys())
                        print('Codigo - Nombre - Codigo del Artista ')
                        while i < len(diccAlbumtodo):
                            temp=list(diccAlbumtodo[claves[i]].keys())#Almacena todas las llaves que pertenecena el diccionario con la llave
                            print('-----------------------------------------')
                            print(f'{claves[i]} - {diccAlbumtodo[claves[i]][temp[0]]} - {diccAlbumtodo[claves[i]][temp[1]]} ')
                            i+=1
                    elif opcion==6:
                        print('\nLas canciones registrados: \n')
                        i=0
                        claves = list(diccCancionestodo.keys())
                        print('Codigo - Nombre - Codigo del Artista - Codigo del Album - Codigo de Genero - Codigo de Playlist ')
                        while i < len(diccCancionestodo):
                            temp=list(diccCancionestodo[claves[i]].keys())#Almacena todas las llaves que pertenecena el diccionario con la llave
                            print('----------------------------------------------------------------------------------------------------')
                            print(f'{claves[i]} - {diccCancionestodo[claves[i]][temp[0]]} - {diccCancionestodo[claves[i]][temp[1]]} - {diccCancionestodo[claves[i]][temp[2]]} - {diccCancionestodo[claves[i]][temp[3]]} - {diccCancionestodo[claves[i]][temp[4]]}')
                            
                            i+=1
                    if volver():
                        continue
                    else:
                        break
                elif opcion==7:#Factura
                    factura(diccProptodo,codigo)
                    print('\nLista de opciones:\n')
                    print('1- Exportar factura a .txt') 
                    print('2- Salir')  
                    opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
                    if opcion==1:
                        exportarTXT(diccProptodo,codigo,contFacturas)
                        contFacturas+=1
                    elif opcion==2:
                        continue
                    else:
                        if opcionNoExiste():
                            continue
                        else:
                            break
                    if volver():
                        continue
                    else:
                        break
                elif opcion==8:#Salir
                    bandera=0
                    continue
                else:#No existe
                    if opcionNoExiste():
                        continue
                    else:
                        break
    #except ValueError:
    #    print( "\n---> Debes digitar un numero entero para escojer una opcion\n")       
    #except NameError:
    #    print( "\n---> El programa ha tenido incovenientes\n")
        
    #except TypeError:
    #    print( "\n---> El programa ha tenido incovenientes\n")
    #except IndexError:
    #    print( "\n---> El programa ha tenido incovenientes\n")
    #except KeyboardInterrupt:
    #    print( "\n---> El programa ha tenido incovenientes\n")
    #finally:
    #    print( "\n---> Vuelva a cargar el programa\n")  
        
menu()
