#Esta funcion lee un fichero llamado propietario.txt y retorna cada linea en una lista dentro de otra lista
def insertProp(): 
    texto = open('propietario.txt', 'r')
    propietariosOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    propietarios=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in propietariosOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de propietariosOri crea una nueva lista dividiendo cada vez que hay un ';'['1234', 'Juan Perez']
        if nuevo[0] in cod:#Validacion si codigo esta repetido
            continue
        else:
            cod+=[nuevo[0]]
            if len(nuevo)==2:#Validacion 
                nuevo[1] = nuevo[1].replace('\n', '') #Elimina cada '\n' en cada elemento [1]
                propietarios+=[nuevo]
            elif len(nuevo)==3:#Validacion 
                album+=[nuevo[:2]]
            else:#Validacion 
                continue          
    return cod
#Esta funcion lee un fichero llamado Artista.txt y retorna cada linea en una lista dentro de otra lista
def insertArt():
    texto = open('Artistas.txt', 'r')
    artistasOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    artista=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in artistasOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de artistasOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0] in cod:#Validacion si codigo esta repetido
            continue
        else:
            cod+=[nuevo[0]]
            if len(nuevo)==3:#Validacion 
                nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                codgen=insertGen()#Obtiene la lista de codigos registrados
                if nuevo[2] in codgen:#Agrega solo si el genero esta
                    artista+=[nuevo] 
            elif len(nuevo)==4:#Validacion 
                codgen=insertGen()
                if nuevo[2] in codgen:#Agrega solo si el genero esta
                    artista+=[nuevo[:3]]
            else:#Validacion 
                continue     
    return cod
#Esta funcion lee un fichero llamado Genero.txt y retorna cada linea en una lista dentro de otra lista
def insertGen():
    texto = open('genero.txt', 'r')
    GenerosOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    Generos=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in GenerosOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de propietariosOri crea una nueva lista dividiendo cada vez que hay un ';'['1234', 'Juan Perez']
        if nuevo[0] in cod:#Validacion si codigo esta repetido
            continue
        else:
            cod+=[nuevo[0]]
            if len(nuevo)==2:#Validacion 
                nuevo[1] = nuevo[1].replace('\n', '') #Elimina cada '\n' en cada elemento [1]
                Generos+=[nuevo]
            else:#Validacion 
                continue          
    return cod
#Esta funcion lee un fichero llamado Playlist.txt y retorna cada linea en una lista dentro de otra lista
def insertPlaylist():
    texto = open('Playlist.txt', 'r')
    playlistOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    playlist=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in playlistOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de artistasOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0] in cod:#Validacion si codigo esta repetido
            continue
        else:
            cod+=[nuevo[0]]
            if len(nuevo)==3:#Validacion 
                nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                codprop=insertProp()#Obtiene la lista de codigos registrados
                if nuevo[2] in codprop:#Agrega solo si el propietario esta
                    playlist+=[nuevo] 
            elif len(nuevo)==4:#Validacion 
                codprop=insertProp()
                if nuevo[2] in codprop:#Agrega solo si el genero esta
                    playlist+=[nuevo[:3]]
            else:#Validacion 
                continue     
    return cod
#Esta funcion lee un fichero llamado Album.txt y retorna cada linea en una lista dentro de otra lista
def insertAlbum(): 
    texto = open('Album.txt', 'r')
    albumOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    album=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in albumOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de albumOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0] in cod:#Validacion si codigo esta repetido
            continue
        else:
            cod+=[nuevo[0]]
            if len(nuevo)==3:#Validacion 
                nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                codprop=insertProp()#Obtiene la lista de codigos registrados
                if nuevo[2] in codprop:#Agrega solo si el propietario esta
                    album+=[nuevo] 
            elif len(nuevo)==4:#Validacion 
                codprop=insertProp()
                if nuevo[2] in codprop:#Agrega solo si el propietario esta
                    album+=[nuevo[:3]]
            else:#Validacion 
                continue     
    return cod

#Esta funcion lee un fichero llamado Canciones.txt y retorna cada linea en una lista dentro de otra lista
def insertCanciones(): 
    texto = open('Canciones.txt', 'r')
    cancionesOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    canciones=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in cancionesOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de cancionesOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0] in cod:#Validacion si codigo esta repetido
            continue
        else:
            cod+=[nuevo[0]]
            if len(nuevo)==6:#Validacion 
                nuevo[5] = nuevo[5].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                codArt=insertArt()#Obtiene la lista de codigos registrados
                codPlaylist=insertPlaylist()
                codGen=insertGen()
                codAlbum=insertAlbum()
                if (nuevo[2] in codArt) and (nuevo[3] in codAlbum) and (nuevo[4] in codGen) and (nuevo[5] in codPlaylist) :#Agrega solo si los otros estan
                    canciones+=[nuevo] 
            elif len(nuevo)==7:#Validacion 
                codArt=insertArt()#Obtiene la lista de codigos registrados
                codPlaylist=insertPlaylist()
                codGen=insertGen()
                codAlbum=insertAlbum()
                if (nuevo[2] in codArt) and (nuevo[3] in codAlbum) and (nuevo[4] in codGen) and (nuevo[5] in codPlaylist) :#Agrega solo si los otros estan
                    canciones+=[nuevo[:6]] 
            else:#Validacion 
                continue     
    return cod


