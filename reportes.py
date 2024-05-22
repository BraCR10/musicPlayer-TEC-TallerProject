#Avance final proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from busqueda import *
from statistics import mode
from tkinter import messagebox

cont=0
def reportesProp(diccProptodo):
    global cont
    reporte = open(f"reportePropietario{cont}.txt", "a")#Crea un nuevo archivo .txt
    reporte.write('\nLos propietarios registrados son: \n')#Agerga datos al archivo
    i=0
    reporte.write('\nCodigo - Nombre - Codigo de membresia - Estado\n')#Agerga datos al archivo
    for i in list(diccProptodo.keys()):
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f"\n {i} -{diccProptodo[i]['nombre']} - {diccProptodo[i]['codMem']} - {diccProptodo[i]['estado']}\n")#Agerga datos al archivo
    reporte.close()#Cierra archivo
    cont+=1

def reportesPlaylist(diccPlaylisttodo,diccProptodo,codProp):
    global cont
    temp=[]
    for i in list(diccPlaylisttodo.keys()):
            if diccPlaylisttodo[i]['codProp']==codProp:
                temp+=[i]
            else:
                continue
    if temp!=[]:
        if codProp in list(diccProptodo.keys()):
            reporte = open(f"reportePlaylist{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> Las playlist del propietario {buscarProp(codProp,diccProptodo)} son: \n')#Agerga datos al archivo
            reporte.write('\nCodigo - Nombre - Codigo del Propietario \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
            for i in list(diccPlaylisttodo.keys()):
                if diccPlaylisttodo[i]['codProp']==codProp:
                    reporte.write(f"\n{i} - {diccPlaylisttodo[i]['nombre']} - {diccPlaylisttodo[i]['codProp']}\n")#Agerga datos al archivo
            reporte.close()#Cierra archivo
            messagebox.showinfo("Alerta", "El reporte se ha creado correctamente!")
        else:
            messagebox.showinfo("Alerta", "El codigo digitado de propietario no tiene playlist asociadas, digite otro.")
    else:
        messagebox.showinfo("Alerta",'El reporte no se puede crear ya que no hay suficientes datos')
    cont+=1

def reporteGeneros(diccGentodo):
    global cont
    reporte = open(f"reporteGeneros{cont}.txt", "a")#Crea un nuevo archivo .txt
    reporte.write('\nLos generos registrados son: \n')#Agerga datos al archivo
    i=0
    reporte.write('\nCodigo - Nombre\n')#Agerga datos al archivo
    for i in list(diccGentodo.keys()):
        reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
        reporte.write(f"\n {i} -{diccGentodo[i]['nombre']}\n")#Agerga datos al archivo
    reporte.close()#Cierra archivo
    cont+=1

def reporteArt(diccArttodo,diccGentodo,codGen):
    global cont
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
            messagebox.showinfo("Alerta","El reporte de artistas del genero se ha creado correctamente!")
        else:
            messagebox.showinfo("Aletra","El genero con el codigo dado no existe")
    else:
        messagebox.showinfo("Alerta",'El reporte no se puede crear ya que no hay suficientes datos')
    cont+=1

def reporteAlbumes(diccAlbumtodo,diccArttodo,diccGentodo,codArt):
    global cont
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
            messagebox.showinfo("Alerta",'El reporte de albumes del artista dado se ha creado correctamente')
        else:
            messagebox.showinfo("Alerta",'El artista con el codigo dado no existe')
    else:
        messagebox.showinfo("Alerta",'El reporte no se puede crear ya que no hay suficientes datos')
    cont+=1

def reporteCancion(diccCancionestodo,diccArttodo,diccGentodo,codArt):
    global cont
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
            messagebox.showinfo("Alerta",'El reporte de canciones del artista dado se ha creado correctamente')
        else:
            messagebox.showinfo("Alerta",'El artista con el codigo dado no existe')
    else:
        messagebox.showinfo("Alerta",'El reporte no se puede crear ya que no hay suficientes datos')
    cont+=1
        
def artistaConMasCanciones(diccCancionestodo,diccArttodo,diccGentodo):
    global cont
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
    cont+=1

def reportemodacanciones(diccCancionestodo,lista):
    global cont
    if lista==[]:
        reporte=open(f"reporteCancionMasReproducida{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
        reporte.close()#Cierra archivo
    else:
        modacanciones=[]
        for i in lista:
            if i in list(diccCancionestodo.keys()):
                modacanciones+=i
        print(modacanciones)
        if modacanciones!=[]:
            cancionmasreproducida=mode(modacanciones)
            reporte=open(f"reporteCancionMasReproducida{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> La cancion mas reproducida es: \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')
            reporte.write(f'\n >>> {diccCancionestodo[cancionmasreproducida]["nombre"]}\n')#Agerga datos al archivo
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte de la cancion mas reproducida se ha creado correctamente\n')
        else:
            reporte=open(f"reporteCancionMasReproducida{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> La cancion mas reproducida ha sido eliminada \n')#Agerga datos al archivo
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte de la cancion mas reproducida se ha creado correctamente\n')
    cont+=1

def reportemodagenero(diccCancionestodo,diccGentodo,lista):
    global cont
    if lista==[]:
        reporte=open(f"reporteGeneroMasSolicitado{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
        reporte.close()#Cierra archivo
    else:
        modageneros=[]
        for i in lista:
            if i in list(diccCancionestodo.keys()):
                modageneros+=[diccCancionestodo[i]['codGen']]
        if modageneros!=[]:
            generomassolicitado=mode(modageneros)
            reporte=open(f"reporteGeneroMasSolicitado{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> El genero mas solicitado es: \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')
            reporte.write(f'\n >>> {diccGentodo[generomassolicitado]["nombre"]}\n')#Agerga datos al archivo
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte del genero mas solicitado se ha creado correctamente\n')
        else:
            reporte=open(f"reporteGeneroMasSolicitado{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> El genero mas solicitado ha sido eliminado \n')#Agerga datos al archivo
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte del genero mas solicitado se ha creado correctamente\n')
    cont+=1
        
def albumConMasCanciones(diccCancionestodo,diccAlbumtodo,diccArttodo):
    global cont
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
    cont+=1

def propietarioConMasPlaylist(diccProptodo,diccPlaylisttodo):
    global cont
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
    cont+=1

def reportemodaalbum(diccCancionestodo,diccAlbumtodo,lista):
    global cont
    if lista==[]:
        reporte=open(f"reporteAlbumMasSolicitado{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
        reporte.close()#Cierra archivo
    else:
        modaalbumes=[]
        for i in lista:
            if i in list(diccCancionestodo.keys()):
                 modaalbumes+=[diccCancionestodo[i]['codAlb']]
        if modaalbumes!=[]:
            albummassolicitado=mode(modaalbumes)
            reporte=open(f"reporteAlbumMasSolicitado{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> El Album mas solicitado es: \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')
            reporte.write(f'\n >>> {diccAlbumtodo[albummassolicitado]["nombre"]}\n')#Agerga datos al archivo
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte del genero mas solicitado se ha creado correctamente\n')
        else:
            reporte=open(f"reporteAlbumMasSolicitado{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> El Album mas solicitado ha sido eliminado \n')#Agerga datos al archivo
    
            reporte.close()#Cierra archivo
            print(f'\n ---> El reporte del genero mas solicitado se ha creado correctamente\n')
    cont+=1

def playlistConMasCanciones(diccCancionestodo,diccPlaylisttodo,diccProptodo):
    global cont
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
    cont+=1

def generoConMasArtistas(diccGentodo,diccArttodo):
    global cont
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
    cont+=1

def generoConMasAlbumes(diccGentodo,diccArttodo,diccAlbumtodo):
    global cont
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
    cont+=1

def artistaConMasAlbumes(diccArttodo,diccAlbumtodo,diccGentodo):
    global cont
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
    cont+=1

def albumNuncaBuscadoFun(albumNuncaBuscado,diccAlbumtodo,diccArttodo):
    global cont
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
    cont+=1

def cancionNuncaReproducidaFun(diccCancionestodo,modaMusica,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo):
    global cont
    temp=[]
    for i in list(diccCancionestodo.keys()):
        if i not in modaMusica :
            temp+=[i]
    if temp!=[]:
        for i in temp:
            reporte = open(f"Reporte_Cancion_Nunca_Reproducida{cont}.txt", "a")#Crea un nuevo archivo .txt
            reporte.write(f'\n ---> Reporte de las canciones nunca reproducidas : \n')#Agerga datos al archivo
            reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
            for i in temp:
                reporte.write(f'\n >>> {buscarCancion(i,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]} \n')#Agerga datos al archivo
                reporte.write('\n-----------------------------------------\n')#Agerga datos al archivo
            reporte.close()#Cierra el archivo
            print('\n ---> El reporte de las canciones nunca reproducidas se ha creado correctamente\n')#Mensaje
    else:
        reporte = open(f"Reporte_Cancion_Nunca_Reproducida{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write('\n --->El reporte no se puede crear pues todos las canciones han sido  reproducidas o no hay\n')
        reporte.close()#Cierra el archivo
    cont+=1

def artistaNuncaBuscadoFun(artistaNuncaBuscado,diccGentodo,diccArttodo):
    global cont
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
    cont+=1

def propietarioSinPlayList(diccProptodo,diccPlaylisttodo):
    global cont
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
    cont+=1