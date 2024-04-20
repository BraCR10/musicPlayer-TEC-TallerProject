from busqueda import *
from statistics import mode

def reportesProp(diccProptodo,cont):
    reporte = open(f"reportePropietario{cont}.txt", "a")#Crea un nuevo archivo .txt
    reporte.write('\nLos propietarios registrados son: \n')#Agerga datos al archivo
    i=0
    reporte.write('\nCodigo - Nombre - Codigo de membresia - Estado\n')#Agerga datos al archivo
    for i in list(diccProptodo.keys()):
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f"\n {i} -{diccProptodo[i]['nombre']} - {diccProptodo[i]['codMem']} - {diccProptodo[i]['estado']}\n")#Agerga datos al archivo
    reporte.close()#Cierra archivo
    print('\n ---> El reporte de propietarios se ha creado correctamente\n')
    
def reportesPlaylist(diccPlaylisttodo,diccProptodo,cont):
    codProp=str(input('\nDigite el codigo de propietario para mostrar las playlist vinculadas: '))
    temp=[]
    for i in list(diccPlaylisttodo.keys()):
            if diccPlaylisttodo[i]['codProp']==codProp:
                temp+=[i]
            else:
                continue
    if temp!=[]:
        if codProp in list(diccProptodo.keys()):
            print(f'\n ---> El reporte de playlist del propietario {buscarProp(codProp,diccProptodo)} se ha creado correctamente\n')
            reporte = open(f"reportePlaylist{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> Las playlist del propietario {buscarProp(codProp,diccProptodo)} son: \n')#Agerga datos al archivo
            reporte.write('\nCodigo - Nombre - Codigo del Propietario \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
            for i in list(diccPlaylisttodo.keys()):
                if diccPlaylisttodo[i]['codProp']==codProp:
                    reporte.write(f"\n{i} - {diccPlaylisttodo[i]['nombre']} - {diccPlaylisttodo[i]['codProp']}\n")#Agerga datos al archivo
            reporte.close()#Cierra archivo
        else:
            print(f'\n -->El propietario con el codigo {codProp} no existe\n')
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')

def reporteGeneros(diccGentodo,cont):
    reporte = open(f"reporteGeneros{cont}.txt", "a")#Crea un nuevo archivo .txt
    reporte.write('\nLos generos registrados son: \n')#Agerga datos al archivo
    i=0
    reporte.write('\nCodigo - Nombre\n')#Agerga datos al archivo
    for i in list(diccGentodo.keys()):
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f"\n {i} -{diccGentodo[i]['nombre']}\n")#Agerga datos al archivo
    reporte.close()#Cierra archivo
    print('\n ---> El reporte de generos se ha creado correctamente\n')

def reporteArt(diccArttodo,diccGentodo,cont):
    codGen=str(input('\nDigite el codigo de genero para mostrar los artistas vinculados: '))
    temp=[]
    for i in list(diccArttodo.keys()):
            if diccArttodo[i]['codGen']==codGen:
                temp+=[i]
            else:
                continue
    if temp!=[]:
        if codGen in list(diccGentodo.keys()):
            reporte = open(f"reporteArtistas{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> Los artistas del genero {buscarGenero(codGen,diccGentodo)} son: \n')#Agerga datos al archivo
            reporte.write('\nCodigo - Nombre - Codigo del Genero \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
            for i in list(diccArttodo.keys()):
                if diccArttodo[i]['codGen']==codGen:
                    reporte.write(f"\n{i} - {diccArttodo[i]['nombre']} - {diccArttodo[i]['codGen']}\n")#Agerga datos al archivo
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte de artistas del genero {buscarGenero(codGen,diccGentodo)} se ha creado correctamente\n')
        else:
            print(f'\n -->El genero con el codigo {codGen} no existe\n')
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')

def reporteAlbumes(diccAlbumtodo,diccArttodo,diccGentodo,cont):
    codArt=str(input('\nDigite el codigo de artista para mostrar los albumes vinculados: '))
    temp=[]
    for i in list(diccAlbumtodo.keys()):
            if diccAlbumtodo[i]['codArt']==codArt:
                temp+=[i]
            else:
                continue
    if temp!=[]:
        if codArt in list(diccArttodo.keys()):
            reporte = open(f"reporteAlbumes{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> Los albumes del artista {buscarArtista(codArt,diccArttodo,diccGentodo)[0]} son: \n')#Agerga datos al archivo
            reporte.write('\nCodigo - Nombre - Codigo del Artista \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
            for i in list(diccAlbumtodo.keys()):
                if diccAlbumtodo[i]['codArt']==codArt:
                    reporte.write(f"\n{i} - {diccAlbumtodo[i]['nombre']} - {diccAlbumtodo[i]['codArt']}\n")#Agerga datos al archivo
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte de albumes del artista {buscarArtista(codArt,diccArttodo,diccGentodo)[0]} se ha creado correctamente\n')
        else:
            print(f'\n -->El genero con el codigo {codArt} no existe\n')
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')

def reporteCancion(diccCancionestodo,diccArttodo,diccGentodo,cont):
    codArt=str(input('\nDigite el codigo de artista para mostrar las canciones vinculados: '))
    temp=[]
    for i in list(diccCancionestodo.keys()):
            if diccCancionestodo[i]['codArt']==codArt:
                temp+=[i]
            else:
                continue
    if temp!=[]:
        if codArt in list(diccArttodo.keys()):
            reporte = open(f"reporteCanciones{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> Las canciones del artista {buscarArtista(codArt,diccArttodo,diccGentodo)[0]} son: \n')#Agerga datos al archivo
            reporte.write('\nCodigo - Nombre - Codigo del Artista \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
            for i in list(diccCancionestodo.keys()):
                if diccCancionestodo[i]['codArt']==codArt:
                    reporte.write(f"\n{i} - {diccCancionestodo[i]['nombre']} - {diccCancionestodo[i]['codArt']}\n")#Agerga datos al archivo
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte de canciones del artista {buscarArtista(codArt,diccArttodo,diccGentodo)[0]} se ha creado correctamente\n')
        else:
            print(f'\n -->El genero con el codigo {codArt} no existe\n')
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
        
def artistaConMasCanciones(diccCancionestodo,temp,cont,diccArttodo,diccGentodo):
    temp=[]
    for i in list(diccCancionestodo.keys()):
        temp+=[diccCancionestodo[i]['codArt']]
    if temp!=[]:
        var=mode(temp)#Almacena el codigo de playlist con mas tendencia
        reporte = open(f"Reporte_Artistas_Con_Mas_Canciones{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de la  artistas con mas canciones: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f'\n >>> El artista con mas canciones es : {buscarArtista(var,diccArttodo,diccGentodo)[0]} con {temp.count(var)} cancion(es) relacionadas\n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte del artista con mas canciones se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
        
def reportemodacanciones(diccCancionestodo,lista,cont):
    if lista==[]:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
    else:
        cancionmasreproducida=mode(lista)
        reporte=open(f"reporteCancionMasReproducida{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> La cancion mas reproducida es: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')
        reporte.write(f'\n >>> {diccCancionestodo[cancionmasreproducida]["nombre"]}\n')#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte de la cancion mas reproducida se ha creado correctamente\n')

def reportemodagenero(diccCancionestodo,diccGentodo,lista,cont):
    if lista==[]:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
    else:
        modageneros=[]
        for i in lista:
            modageneros+=[diccCancionestodo[i]['codGen']]
        generomassolicitado=mode(modageneros)
        reporte=open(f"reporteGeneroMasSolicitado{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> El genero mas solicitado es: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')
        reporte.write(f'\n >>> {diccGentodo[generomassolicitado]["nombre"]}\n')#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte del genero mas solicitado se ha creado correctamente\n')
        
def albumConMasCanciones(diccCancionestodo,temp,cont,diccAlbumtodo,diccArttodo):
    temp=[]
    for i in list(diccCancionestodo.keys()):
        temp+=[diccCancionestodo[i]['codAlb']]
    if temp!=[]:
        var=mode(temp)#Almacena el codigo de playlist con mas tendencia
        reporte = open(f"Reporte_Albumes_Con_Mas_Canciones{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de album con mas canciones: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f'\n >>> El album con mas canciones es : {buscarAlbum(var,diccAlbumtodo,diccArttodo)[0]} con {temp.count(var)} cancion(es) relacionadas\n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte del album con mas canciones se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')

def propietarioConMasPlaylist(diccProptodo,temp,cont,diccPlaylisttodo):
    temp=[]
    for i in list(diccPlaylisttodo.keys()):
        temp+=[diccPlaylisttodo[i]['codProp']]
    if temp!=[]:
        var=mode(temp)#Almacena el codigo de playlist con mas tendencia
        reporte = open(f"Reporte_Propietario_Con_Mas_Playlist{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de propietario con mas playlist: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f'\n >>> El propietario con mas playlist es : {buscarProp(var,diccProptodo)} con {temp.count(var)} playlist(s) relacionadas\n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte de propietario con mas playlist se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')

def reportemodaalbum(diccCancionestodo,diccAlbumtodo,lista,cont):
    if lista==[]:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
    else:
        modaalbumes=[]
        for i in lista:
            modaalbumes+=[diccCancionestodo[i]['codAlb']]
        albummassolicitado=mode(modaalbumes)
        reporte=open(f"reporteAlbumMasSolicitado{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> El Album mas solicitado es: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')
        reporte.write(f'\n >>> {diccAlbumtodo[albummassolicitado]["nombre"]}\n')#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte del genero mas solicitado se ha creado correctamente\n')

def playlistConMasCanciones(diccCancionestodo,temp,cont,diccPlaylisttodo,diccProptodo):
    temp=[]
    for i in list(diccCancionestodo.keys()):
        temp+=[diccCancionestodo[i]['codPlaylist']]
    if temp!=[]:
        var=mode(temp)#Almacena el codigo de playlist con mas tendencia
        reporte = open(f"Reporte_Playlist_Con_Mas_Canciones{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de la  playlist con mas canciones: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f'\n >>> La playlist con mas canciones es : {buscarPlaylist(var,diccPlaylisttodo,diccProptodo)[0]} con {temp.count(var)} cancion(es) relacionadas\n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte de la playlist con mas canciones se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
   
def generoConMasArtistas(diccGentodo,temp,cont,diccArttodo):
    temp=[]
    for i in list(diccArttodo.keys()):
        temp+=[diccArttodo[i]['codGen']]
    if temp!=[]:
        var=mode(temp)#Almacena el codigo de playlist con mas tendencia
        reporte = open(f"Reporte_Genero_Con_Mas_Artistas{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de del genero con mas artistas: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f'\n >>> El genero con mas artistas es :  {buscarGenero(var,diccGentodo)} con {temp.count(var)} artista(s) relacionados \n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte del genero con mas artistas se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')

def generoConMasAlbumes(diccGentodo,temp,cont,diccArttodo,diccAlbumtodo):
    temp=[]
    for i in list(diccAlbumtodo.keys()):
        temp+=[diccArttodo[diccAlbumtodo[i]['codArt']]['codGen']]#Almacena todos los codigos de genero de todos los artistas vinculados a un album
    if temp!=[]:
        var=mode(temp)#Almacena el codigo de playlist con mas tendencia
        reporte = open(f"Reporte_Genero_Con_Mas_Albumes{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de del genero con mas albumes : \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f'\n >>> El genero con mas albumes es :  {buscarGenero(var,diccGentodo)} con {temp.count(var)} album(es) relacionados \n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte del genero con mas albumes se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
    
def artistaConMasAlbumes(temp,cont,diccArttodo,diccAlbumtodo,diccGentodo):
    temp=[]
    for i in list(diccAlbumtodo.keys()):
        temp+=[diccAlbumtodo[i]['codArt']]
    if temp!=[]:
        var=mode(temp)#Almacena el codigo de playlist con mas tendencia
        reporte = open(f"Reporte_Artista_Con_Mas_Albumes{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de el artista con mas albumes : \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f'\n >>> El artista con mas albumes es :  {buscarArtista(var,diccArttodo,diccGentodo)[0]} con {temp.count(var)} album(es) relacionados \n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte el artista con mas albumes se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
        
def albumNuncaBuscadoFun(albumNuncaBuscado,diccAlbumtodo,temp,cont,diccArttodo):
    temp=[]
    for i in list(diccAlbumtodo.keys()):
        if i not in albumNuncaBuscado:
            temp+=[i]
    if temp!=[]:
        reporte = open(f"Reporte_Album_Nunca_Buscado{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de los albumes nunca buscados : \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        for i in temp:
            reporte.write(f'\n >>>  {buscarAlbum(i,diccAlbumtodo,diccArttodo)[0]} \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte de los albumes nunca buscados se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear pues todos los albumes han sido  buscados\n')
        
def cancionNuncaReproducidaFun(diccCancionestodo,modaMusica,temp,cont,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo):
    temp=[]
    for i in list(diccCancionestodo.keys()):
        if i not in modaMusica:
            temp+=[i]
    if temp!=[]:
        reporte = open(f"Reporte_Cancion_Nunca_Reproducida{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de las canciones nunca reproducidas : \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        for i in temp:
            reporte.write(f'\n >>> {buscarCancion(i,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]} \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte de las canciones nunca reproducidas se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear pues todos las canciones han sido  reproducidas o no hay\n')

def artistaNuncaBuscadoFun(artistaNuncaBuscado,diccGentodo,temp,cont,diccArttodo):
    temp=[]
    for i in list(diccArttodo.keys()):
        if i not in artistaNuncaBuscado:
            temp+=[i]
    if temp!=[]:
        reporte = open(f"Reporte_Artista_Nunca_Buscado{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de los artistas nunca buscados : \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        for i in temp:
            reporte.write(f'\n >>>  { buscarArtista(i,diccArttodo,diccGentodo)[0]} \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte de los artistas nunca buscados se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear pues todos los artistas han sido  buscados\n')
        
def propietarioSinPlayList(diccProptodo,diccPlaylisttodo,temp,cont):
    temp=[]
    for i in list(diccPlaylisttodo.keys()):
        temp+=[i]
    if temp!=[]:
        reporte = open(f"Reporte_Propietarios_Sin_Playlist{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Reporte de los propietarios sin playlist : \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        for i in list(diccProptodo.keys()):
            if i not in temp:
                reporte.write(f'\n >>>  { buscarProp(i,diccProptodo)} \n')#Agerga datos al archivo
                reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.close()#Cierra el archivo
        print('\n ---> El reporte de los propietarios sin playlist se ha creado correctamente\n')#Mensaje
    else:
        print('\n --->El reporte no se puede crear pues todos los artistas han sido  buscados\n')
    