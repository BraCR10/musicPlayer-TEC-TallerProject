from busqueda import *
from statistics import mode





























































































































































def reportesProp(diccProptodo,cont):
    reporte = open(f"reportePropietario{cont}.txt", "a")#Crea un nuevo archivo .txt
    reporte.write('\nLos propietarios registrados son: \n')#Agerga datos al archivo
    i=0
    reporte.write('\nCodigo - Nombre - Codigo de membresia - Estado')#Agerga datos al archivo
    for i in list(diccProptodo.keys()):
        reporte.write('\n-----------------------------------------')#Agerga datos al archivo
        reporte.write(f"\n {i} -{diccProptodo[i]['nombre']} - {diccProptodo[i]['codMem']} - {diccProptodo[i]['estado']}")#Agerga datos al archivo
    reporte.close()#Cierra archivo
    print('\n ---> El reporte de propietarios se ha creado correctamente')
    
def reportesPlaylist(diccPlaylisttodo,diccProptodo,cont):
    codProp=str(input('\nDigite el codigo de propietario para mostrar las playlist vinculadas: '))
    if codProp in list(diccProptodo.keys()):
        print(f'\n ---> El reporte de playlist del propietario {buscarProp(codProp,diccProptodo)} se ha creado correctamente')
        reporte = open(f"reportePlaylist{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Las playlist del propietario {buscarProp(codProp,diccProptodo)} son: \n')#Agerga datos al archivo
        reporte.write('\nCodigo - Nombre - Codigo del Propietario ')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------')#Agerga datos al archivo
        for i in list(diccPlaylisttodo.keys()):
            if diccPlaylisttodo[i]['codProp']==codProp:
                reporte.write(f"\n{i} - {diccPlaylisttodo[i]['nombre']} - {diccPlaylisttodo[i]['codProp']}")#Agerga datos al archivo
        reporte.close()#Cierra archivo
    else:
        print(f'\n -->El propietario con el codigo {codProp} no existe\n')

def reporteGeneros(diccGentodo,cont):
    reporte = open(f"reporteGeneros{cont}.txt", "a")#Crea un nuevo archivo .txt
    reporte.write('\nLos generos registrados son: \n')#Agerga datos al archivo
    i=0
    reporte.write('\nCodigo - Nombre')#Agerga datos al archivo
    for i in list(diccGentodo.keys()):
        reporte.write('\n-----------------------------------------')#Agerga datos al archivo
        reporte.write(f"\n {i} -{diccGentodo[i]['nombre']}")#Agerga datos al archivo
    reporte.close()#Cierra archivo
    print('\n ---> El reporte de generos se ha creado correctamente')

def reporteArt(diccArttodo,diccGentodo,cont):
    codGen=str(input('\nDigite el codigo de genero para mostrar los artistas vinculados: '))
    if codGen in list(diccGentodo.keys()):
        reporte = open(f"reporteArtistas{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Los artistas del genero {buscarGenero(codGen,diccGentodo)} son: \n')#Agerga datos al archivo
        reporte.write('\nCodigo - Nombre - Codigo del Genero ')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------')#Agerga datos al archivo
        for i in list(diccArttodo.keys()):
            if diccArttodo[i]['codGen']==codGen:
                reporte.write(f"\n{i} - {diccArttodo[i]['nombre']} - {diccArttodo[i]['codGen']}")#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte de artistas del genero {buscarGenero(codGen,diccGentodo)} se ha creado correctamente')
    else:
        print(f'\n -->El genero con el codigo {codGen} no existe\n')

def resporteAlbumes(diccAlbumtodo,diccArttodo,cont):
    codArt=str(input('\nDigite el codigo de artista para mostrar los albumes vinculados: '))
    if codArt in list(diccArttodo.keys()):
        reporte = open(f"reporteAlbumes{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Los albumes del artista {buscarArtista(codArt,diccArttodo)} son: \n')#Agerga datos al archivo
        reporte.write('\nCodigo - Nombre - Codigo del Artista ')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------')#Agerga datos al archivo
        for i in list(diccAlbumtodo.keys()):
            if diccAlbumtodo[i]['codArt']==codArt:
                reporte.write(f"\n{i} - {diccAlbumtodo[i]['nombre']} - {diccAlbumtodo[i]['codArt']}")#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte de albumes del artista {buscarArtista(codArt,diccArttodo)} se ha creado correctamente')
    else:
        print(f'\n -->El genero con el codigo {codArt} no existe\n')

def reporteCancion(diccCancionestodo,diccArttodo,cont):
    codArt=str(input('\nDigite el codigo de artista para mostrar las canciones vinculados: '))
    if codArt in list(diccArttodo.keys()):
        reporte = open(f"reporteCanciones{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> Las canciones del artista {buscarArtista(codArt,diccArttodo)} son: \n')#Agerga datos al archivo
        reporte.write('\nCodigo - Nombre - Codigo del Artista ')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------')#Agerga datos al archivo
        for i in list(diccCancionestodo.keys()):
            if diccCancionestodo[i]['codArt']==codArt:
                reporte.write(f"\n{i} - {diccCancionestodo[i]['nombre']} - {diccCancionestodo[i]['codArt']}")#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte de canciones del artista {buscarArtista(codArt,diccArttodo)} se ha creado correctamente')
    else:
        print(f'\n -->El genero con el codigo {codArt} no existe\n')

def reportemodacanciones(diccCancionestodo,lista,cont):
    if lista==[]:
        print('\n --->El reporte no se puede crear ya que no hay suficientes datos\n')
    else:
        cancionmasreproducida=mode(lista)
        reporte=open(f"reporteCancionMasReproducida{cont}.txt", "a")#Crea un nuevo archivo .txt
        reporte.write(f'\n ---> La cancion mas reproducida es: \n')#Agerga datos al archivo
        reporte.write('\n-----------------------------------------\n')
        reporte.write(f'\n {diccCancionestodo[cancionmasreproducida]['nombre']}')#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte de la cancion mas reproducida se ha creado correctamente')

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
        reporte.write(f'\n {diccGentodo[generomassolicitado]['nombre']}')#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte del genero mas solicitado se ha creado correctamente')

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
        reporte.write(f'\n {diccAlbumtodo[albummassolicitado]['nombre']}')#Agerga datos al archivo
        reporte.close()#Cierra archivo
        print(f'\n ---> El reporte del genero mas solicitado se ha creado correctamente')