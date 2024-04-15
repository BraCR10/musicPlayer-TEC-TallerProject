#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
#Esta funcion lee un fichero llamado Propietarios.txt y retorna cada linea en una lista dentro de otra lista
def leerProp(): 
    archivo=open('Propietario.txt', 'r',encoding="utf8")
    dicc={}
    for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(';')
            if columnas[0] not in list(dicc.keys()) and len(columnas)==4 and (columnas[3]=='1'or columnas[3]=='0') :
                cod = columnas[0]
                nombre = columnas[1]
                codMem = columnas[2]
                estado = columnas[3]
                dicc[cod]={'nombre':nombre,'codMem':codMem,'estado':estado}
    return dicc
#Esta funcion lee un fichero llamado Genero.txt y retorna cada linea en una lista dentro de otra lista
def leerGen(): 
    archivo=open('Genero.txt', 'r',encoding="utf8")
    dicc={}
    for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(';')
            if columnas[0] not in list(dicc.keys()) and len(columnas)==2:
                cod = columnas[0]
                nombre = columnas[1]
                dicc[cod]={'nombre':nombre}
    return dicc  
#Esta funcion lee un fichero llamado Artista.txt y retorna cada linea en una lista dentro de otra lista
def leerArt(): 
    archivo=open('Artista.txt', 'r',encoding="utf8")
    dicc={}
    for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(';')
            if columnas[0] not in list(dicc.keys()) and len(columnas)==3 and columnas[2] in list(leerGen().keys()):#Agrega solo si esta el usuario activo 
                cod = columnas[0]
                nombre = columnas[1]
                codGen = columnas[2]
                dicc[cod]={'nombre':nombre,'codGen':codGen}
    return dicc
#Esta funcion lee un fichero llamado Playlist.txt y retorna cada linea en una lista dentro de otra lista
def leerPlaylist(): 
    archivo=open('Playlist.txt', 'r',encoding="utf8")
    dicc={}
    for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(';')
            if columnas[0] not in list(dicc.keys()) and len(columnas)==3 and columnas[2] in list(leerProp().keys()) and leerProp()[columnas[2]]['estado']=='1':#Agrega solo si esta el usuario activo 
                cod = columnas[0]
                nombre = columnas[1]
                codProp = columnas[2]
                dicc[cod]={'nombre':nombre,'codProp':codProp}
    return dicc
#Esta funcion lee un fichero llamado Album.txt y retorna cada linea en una lista dentro de otra lista
def leerAlbum(): 
    archivo=open('Albumes.txt', 'r',encoding="utf8")
    dicc={}
    for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(';')
            if columnas[0] not in list(dicc.keys()) and len(columnas)==3 and columnas[2] in list(leerArt().keys()):#Agrega solo si existe el artista.
                cod = columnas[0]
                nombre = columnas[1]
                codArt = columnas[2]
                dicc[cod]={'nombre':nombre,'codArt':codArt}
    return dicc
#Esta funcion lee un fichero llamado Canciones.txt y retorna cada linea en una lista dentro de otra lista
def leerCanciones(): 
    archivo=open('Canciones.txt', 'r',encoding="utf8")
    dicc={}
    for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(';')
            if columnas[0] not in list(dicc.keys()) and len(columnas)==6 and columnas[2] in list(leerArt().keys()) and columnas[3] in list(leerAlbum().keys()) and columnas[4] in list(leerGen().keys())and columnas[5] in list(leerPlaylist().keys()):
                cod = columnas[0]
                nombre = columnas[1]
                codArt = columnas[2]
                codAlb = columnas[3]
                codGen= columnas[4]
                codPlaylist= columnas[5]
                dicc[cod]={'nombre':nombre,'codArt':codArt,'codAlb':codAlb,'codGen':codGen,'codPlaylist':codPlaylist }
    return dicc
