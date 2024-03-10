#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

from insercion import *#insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp
from busqueda import * #buscarAlbum,buscarArtista,buscarCancion,buscarGenero,buscarPlaylist,buscarProp
from eliminacion import *#eliminarProp,eliminarCanciones,eliminarPlaylist
from modificacion import *
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
        print('4- Modificar')
        print('5- Datos diponibles')
        print('6- Salir') 
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
                    print('\n ---> El nombre del propietario es: ',buscarProp(dato,listaProptodo))
                if volver()==1:
                    continue
                else:
                    break
            elif opcion==2:
                dato=str(input('\nDigite el codigo de playlist: '))
                if buscarPlaylist(dato,listaPlaylisttodo,listaProptodo)==None:
                    print('\n ---> La playlist no existe')
                else:
                    print('\n ---> El nombre de la playlist es: ',buscarPlaylist(dato,listaPlaylisttodo,listaProptodo)[0], 'y el nombre del propietario es:', buscarPlaylist(dato,listaPlaylisttodo,listaProptodo)[1])
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
                    print('\n ---> El artista es: ',buscarArtista(dato,listaArttodo,listaGentodo)[0],' y el genero es: ',buscarArtista(dato,listaArttodo,listaGentodo)[1])
                if volver()==1:
                    continue
                else:
                    break
            elif opcion==5:
                dato=str(input('\nDigite el codigo de album: '))
                if buscarAlbum(dato,listaAlbumtodo,listaArttodo,listaGentodo)==None:
                    print('\n ---> El album no existe')
                else:
                    print(f'\n ---> El album es: {buscarAlbum(dato,listaAlbumtodo,listaArttodo,listaGentodo)[0]}, el artista es: {buscarAlbum(dato,listaAlbumtodo,listaArttodo,listaGentodo)[1]} y  el genero es: {buscarAlbum(dato,listaAlbumtodo,listaArttodo,listaGentodo)[2]}')
                if volver()==1:
                    continue
                else:
                    break
            elif opcion==6:
                dato=str(input('\nDigite el codigo de cancion: '))
                if buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)==None:
                    print('\n ---> La cancion no existe')
                else:
                    print(f'\n ---> La cancion es: {buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[0]}, el artista: {buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[1]}, el album es: {buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[2]}, el genero es: {buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[3]} y la playlist es: {buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[4]} ' )
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
                dato=str(input('\nDigite el codigo de propietario a eliminar: ')) #Recibe un codigo de propietario
                if dato in listaPropcod: #Si el codigo esta en la lista de codigos de propietraios, entra.
                    # Eliminacion principal
                    listaPropcod,listaProptodo,nombre=eliminarProp(dato,listaPropcod,listaProptodo) #Elimina el propietario
                    # Eliminacion de playlists y canciones vinculadas
                    codigosPlaylistEliminados=[] #Crea nueva lista para los codigos de los propietarios eliminados
                    i=0 
                    t=0
                    while i < len(listaPlaylisttodo): #Mientras que i sea menor que el largo de la lista de playlist, entra.
                        if listaPlaylisttodo[i][2]==dato: #Si el codigo esta asociado a una playlist, sigue.
                            codigosPlaylistEliminados.append(listaPlaylisttodo[i][0]) #Agrega el codigo que esta vinculado a la playlist a la lista con los codigos eliminados
                            listaCancionestodo=[cancion for cancion in listaCancionestodo if cancion[5]!=listaPlaylisttodo[i][0]] #Hace que la lista de cancionestodo sea igual a que si hay una cancion dentro de la lista de canciones todo que contenga el codigo de la playlist eliminada en la posicion 5, elimine esa cancion de la lista y guarde la lista sin esa cancion.
                            listaPlaylisttodo.pop(i) #Corta la lista para volver a entrar al ciclo
                        else: 
                            i+=1 #Aumenta el i 
                    # Eliminacion de propietario
                    print(f'\nEl propietario "{nombre}" ha sido eliminado correctamente') #Imprime este mensaje si fue eliminado
                else:
                    print(f'\nEl propietario con el código "{dato}" no existe en la lista de propietarios.') #Imprime esto si no fue eliminado
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
                    if check==1:#Si el prop si esta vinculado a la playlist
                        #Eliminacion principal
                        listaPlaylistcod,listaPlaylisttodo,nombre=eliminarPlaylist(codplaylist,listaPlaylistcod,listaPlaylisttodo)#Actualiza la lista si el codigo no existe, la deja igual
                        #Eliminacion de vinculos
                        #Eliminacion de canciones
                        cont=0#Contador de veces que esta presente el codigo eliminado 
                        i=0
                        while i<len(listaCancionestodo):#Obtiene las veces que va a tener que operar el siguiente while, cont hace referecia a la cantidad de elementos que hay que eliminar en la lista vinculada
                            if listaCancionestodo[i][5]==codplaylist:#codplaylist es el codigo eliminado originalmente
                                cont+=1
                            i+=1
                        i=0
                        check=0#Verifica si se elimino un dato de la lista vinculada 
                        while cont>0:
                            if listaCancionestodo[i][5] == codplaylist:#2 son codprop
                                listaCancionescod,listaCancionestodo,decartar=eliminarCanciones(listaCancionestodo[i][0],listaCancionescod,listaCancionestodo)#Se almacena la nueva lista proporcionada por la funcion de eliminar se almacena y la misma lista, descartar es un dato adicional que aqui no se usa
                                check=1#Ya se elimino un elemento 
                                cont-=1
                            if check==1:
                                i=0#i debe volver a 0 ya que el elmento 0 es otro, el pasado ya se elimino 
                                check=0
                            else:
                                i+=1# i incrementa, la unica forma de que esto pase, es que aun falte un elemento por eliminar, por lo tanto se debe recorrer la lista 
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
                dato=str(input('\nDigite el codigo del genero a eliminar: '))
                if dato in listaGencod:
                    #Eliminacion principal
                    listaGencod,listaGentodo,nombre=eliminarGenero(dato,listaGencod,listaGentodo)#Actualiza la lista si el codigo no existe, la deja igual
                    #Eliminacion de viculos
                    #Eliminar Artistas
                    cont=0#Contador de veces que esta presente el codigo eliminado 
                    i=0
                    while i<len(listaArttodo):#Obtiene las veces que va a tener que operar el siguiente while, cont hace referecia a la cantidad de elementos que hay que eliminar en la lista vinculada
                        if listaArttodo[i][2]==dato:#Dato es el codigo eliminado originalmente
                            cont+=1
                        i+=1
                    i=0
                    check=0#Verifica si se elimino un dato de la lista vinculada 
                    codigosArtistaEliminados=[]
                    while cont>0:
                        if listaArttodo[i][2] == dato:#Dato es el codigo eliminado originalmente
                            codigosArtistaEliminados+=[listaArttodo[i][0]]#Almacena los codigos eliminados para usarlos depsues en canciones
                            listaArtcod,listaArttodo,decartar=eliminarArt(listaArttodo[i][0],listaArtcod,listaArttodo)#Se almacena la nueva lista proporcionada por la funcion de eliminar se almacena y la misma lista, descartar es un dato adicional que aqui no se usa
                            check=1#Ya se elimino un elemento 
                            cont-=1
                        if check==1:
                            i=0#i debe volver a 0 ya que el elmento 0 es otro, el pasado ya se elimino 
                            check=0
                        else:
                            i+=1# i incrementa, la unica forma de que esto pase, es que aun falte un elemento por eliminar, por lo tanto se debe recorrer la lista 
                    #Elimina Canciones
                    cont=0#Contador de veces que esta presente el codigo eliminado 
                    i=0
                    while i<len(listaCancionestodo):#Obtiene las veces que va a tener que operar el siguiente while, cont hace referecia a la cantidad de elementos que hay que eliminar en la lista vinculada
                        if listaCancionestodo[i][4]==dato:#Dato es el codigo eliminado originalmente
                            cont+=1
                        i+=1
                    i=0
                    check=0#Verifica si se elimino un dato de la lista vinculada 
                    while cont>0:
                        if listaCancionestodo[i][4] == dato:#Dato es el codigo eliminado originalmente
                            listaCancionescod,listaCancionestodo,descartar=eliminarCanciones(listaCancionestodo[i][0],listaCancionescod,listaCancionestodo)
                            check=1#Ya se elimino un elemento 
                            cont-=1
                        if check==1:
                            i=0#i debe volver a 0 ya que el elmento 0 es otro, el pasado ya se elimino 
                            check=0
                        else:
                            i+=1# i incrementa, la unica forma de que esto pase, es que aun falte un elemento por eliminar, por lo tanto se debe recorrer la lista 
                    #Eliminacion de albumes, viculada con artistas
                    i=len(listaAlbumtodo)-1
                    temp=0#Cuenta las veces que se cmpara los artistas con los albums
                    constante=len(listaAlbumtodo)#El tamano de la lista de albums
                    while codigosArtistaEliminados!=[]:
                        if codigosArtistaEliminados[0] == listaAlbumtodo[i][2]:
                            listaAlbumcod,listaAlbumtodo,descartar=eliminarAlbum(listaAlbumtodo[i][0],listaAlbumcod,listaAlbumtodo)#Almacena la nueva listas
                            i=len(listaAlbumtodo)
                        i-=1
                        temp+=1
                        if temp==constante:
                            temp=0
                            i=len(listaAlbumtodo)-1#Permite buscar de nuevo y revisar dato por dato
                            if len(codigosArtistaEliminados)>1:
                                codigosArtistaEliminados=codigosArtistaEliminados[1:]#Elimina el dato ya verificado 100%
                                i=0
                            else:
                                codigosArtistaEliminados.pop(0)#Elimina el dato ya verificado 100%
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
                    #Eliminacion principal
                    listaArtcod,listaArttodo,nombre=eliminarArt(dato,listaArtcod,listaArttodo)#Actualiza la lista si el codigo no existe, la deja igual
                    #Elimina vinculos
                    #Elimina Canciones
                    cont=0#Contador de veces que esta presente el codigo eliminado 
                    i=0
                    while i<len(listaCancionestodo):#Obtiene las veces que va a tener que operar el siguiente while, cont hace referecia a la cantidad de elementos que hay que eliminar en la lista vinculada
                        if listaCancionestodo[i][2]==dato:#Dato es el codigo eliminado originalmente
                            cont+=1
                        i+=1
                    i=0
                    check=0#Verifica si se elimino un dato de la lista vinculada 
                    while cont>0:
                        if listaCancionestodo[i][2] == dato:#Dato es el codigo eliminado originalmente
                            listaCancionescod,listaCancionestodo,decartar=eliminarCanciones(listaCancionestodo[i][0],listaCancionescod,listaCancionestodo)
                            check=1#Ya se elimino un elemento 
                            cont-=1
                        if check==1:
                            i=0#i debe volver a 0 ya que el elmento 0 es otro, el pasado ya se elimino 
                            check=0
                        else:
                            i+=1# i incrementa, la unica forma de que esto pase, es que aun falte un elemento por eliminar, por lo tanto se debe recorrer la lista 
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
                    #Eliminacion principal
                    listaAlbumcod,listaAlbumtodo,nombre=eliminarAlbum(dato,listaAlbumcod,listaAlbumtodo)#Actualiza la lista si el codigo no existe, la deja igual
                    #Elimina vinculos
                    #Elimina Canciones
                    cont=0#Contador de veces que esta presente el codigo eliminado 
                    i=0
                    while i<len(listaCancionestodo):#Obtiene las veces que va a tener que operar el siguiente while, cont hace referecia a la cantidad de elementos que hay que eliminar en la lista vinculada
                        if listaCancionestodo[i][3]==dato:#Dato es el codigo eliminado originalmente
                            cont+=1
                        i+=1
                    i=0
                    check=0#Verifica si se elimino un dato de la lista vinculada 
                    while cont>0:
                        if listaCancionestodo[i][3] == dato:#Dato es el codigo eliminado originalmente
                            listaCancionescod,listaCancionestodo,decartar=eliminarCanciones(listaCancionestodo[i][0],listaCancionescod,listaCancionestodo)
                            check=1#Ya se elimino un elemento 
                            cont-=1
                        if check==1:
                            i=0#i debe volver a 0 ya que el elmento 0 es otro, el pasado ya se elimino 
                            check=0
                        else:
                            i+=1# i incrementa, la unica forma de que esto pase, es que aun falte un elemento por eliminar, por lo tanto se debe recorrer la lista 
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
                    #Elimicacion principal
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
        elif opcion==4:#Modificar
            print('\nLista de opciones:\n')
            print('1- Modificar Propietario') 
            print('2- Modificar Playlist') 
            print('3- Modificar Genero') 
            print('4- Modificar Artista') 
            print('5- Modificar Album') 
            print('6- Modificar Cancion') 
            opcion=int(input('\nEscoja un numero segun la accion que desea realizar: '))
            if opcion==1:
                dato=str(input('\nDigite el codigo de propietario a modificar: '))
                if dato in listaPropcod:
                    print(f'\n--->El propietario es: {buscarProp(dato,listaProptodo)}')
                    nuevo=str(input('\nDigite el nuevo nombre de propietario: '))
                    listaProptodo=modificarProp(dato,listaProptodo,nuevo)
                    print('\n--->El nombre de propietario modifico con exito!')
                    if volver():
                        continue
                    else:
                        break
            if opcion==6:
                dato=str(input('\nDigite el codigo de cancion a modificar: '))
                codArt=str(input('\nDigite el codigo del artista ligado a la cancion a modificar: '))
                codAlb=str(input('\nDigite el codigo de album ligado a la cancion a modificar: '))
                codGen=str(input('\nDigite el codigo del genero ligado a la cancion a modificar: '))
                codPlaylist=str(input('\nDigite el codigo de la playlist ligada a la cancion a modificar: '))
                if dato in listaCancionescod and buscarArtista(codArt,listaArttodo,listaGentodo)[0] == buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[1] and buscarAlbum(codAlb,listaAlbumtodo,listaArttodo,listaGentodo)[0] == buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[2] and buscarGenero(codGen,listaGentodo) == buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[3] and buscarPlaylist(codPlaylist,listaPlaylisttodo,listaProptodo)[0] == buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[4]:
                    print(f'\n--->La cancion es: {buscarCancion(dato,listaCancionestodo,listaArttodo,listaAlbumtodo,listaGentodo,listaPlaylisttodo)[0]}')
                    nuevo=str(input('\nDigite el nuevo nombre de la cancion: '))
                    listaCancionestodo=modificarcancion(dato,listaCancionestodo,nuevo)
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
            else:
                if opcionNoExiste():
                    continue
                else:
                    break
        elif opcion==5:#Consultas
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
                    print('----------------------------------------------------------------------------------------------------')
                    print(f'{listaCancionestodo[i][0]} - {listaCancionestodo[i][1]} - {listaCancionestodo[i][2]} - {listaCancionestodo[i][3]} - {listaCancionestodo[i][4]} - {listaCancionestodo[i][5]}')
                    i+=1
            if volver():
                continue
            else:
                break
        elif opcion==6:
            break
        else:
            if opcionNoExiste():
                continue
            else:
                break
menu()