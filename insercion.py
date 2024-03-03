#Esta funcion lee un fichero llamado propietario.txt y retorna cada linea en una lista dentro de otra lista
def insertProp(): 
    texto = open('propietario.txt', 'r')
    propietariosOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    propietarios=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in propietariosOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de propietariosOri crea una nueva lista dividiendo cada vez que hay un ';'['1234', 'Juan Perez']
        if nuevo[0]=='\n':#Validacion
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==2:#Validacion 
                    nuevo[1] = nuevo[1].replace('\n', '') #Elimina cada '\n' en cada elemento [1]
                    propietarios+=[nuevo]
                elif len(nuevo)==3:#Validacion 
                    propietarios+=[nuevo[:2]]
                else:#Validacion 
                    continue          
    return cod,propietarios

#Esta funcion lee un fichero llamado Genero.txt y retorna cada linea en una lista dentro de otra lista
def insertGen():
    texto = open('genero.txt', 'r')
    GenerosOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    Generos=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in GenerosOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de propietariosOri crea una nueva lista dividiendo cada vez que hay un ';'['1234', 'Juan Perez']
        if nuevo[0]=='\n':#Validacion
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==2:#Validacion 
                    nuevo[1] = nuevo[1].replace('\n', '') #Elimina cada '\n' en cada elemento [1]
                    Generos+=[nuevo]
                elif len(nuevo)==3:#Validacion 
                    Generos+=[nuevo[:2]]
                else:#Validacion 
                    continue          
    return cod,Generos

#Esta funcion lee un fichero llamado Artista.txt y retorna cada linea en una lista dentro de otra lista
def insertArt():
    texto = open('Artista.txt', 'r')
    artistasOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    artistas=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    codValidos=[]
    for linea in artistasOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de artistasOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0]=='\n':
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==3:#Validacion 
                    nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    #Obtiene la lista de codigos registrados
                    id,todo=insertGen()
                    if nuevo[2] in id:#Agrega solo si el genero esta
                        artistas+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==4:#Validacion 
                    id,todo=insertGen()
                    if nuevo[2] in id:#Agrega solo si el genero esta
                        artistas+=[nuevo[:3]]
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    return codValidos,artistas

#Esta funcion lee un fichero llamado Playlist.txt y retorna cada linea en una lista dentro de otra lista
def insertPlaylist():
    texto = open('Playlist.txt', 'r')
    playlistOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    playlists=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    codValidos=[]
    for linea in playlistOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de artistasOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0]=='\n':#Validacion
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==3:#Validacion 
                    nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    codprop,todo=insertProp()#Obtiene la lista de codigos registrados
                    if nuevo[2] in codprop:#Agrega solo si el propietario esta
                        playlists+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==4:#Validacion 
                    codprop,todo=insertProp()#Obtiene la lista de codigos registrados
                    if nuevo[2] in codprop:#Agrega solo si el genero esta
                        playlists+=[nuevo[:3]]
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    return codValidos,playlists

#Esta funcion lee un fichero llamado Album.txt y retorna cada linea en una lista dentro de otra lista
def insertAlbum(): 
    texto = open('Album.txt', 'r')
    albumOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    albums=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos para que no se repitan
    codValidos=[]#Almacena codigos que cumple todas las condiciones
    for linea in albumOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de albumOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0]=='\n':#Validacion
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==3:#Validacion 
                    nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    codart,todo=insertArt()#Obtiene la lista de codigos registrados
                    if nuevo[2] in codart:#Agrega solo si el propietario esta
                        albums+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==4:#Validacion 
                    codart,todo=insertArt()#Obtiene la lista de codigos registrados
                    if nuevo[2] in codart:#Agrega solo si el propietario esta
                        albums+=[nuevo[:3]]
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    return codValidos,albums

#Esta funcion lee un fichero llamado Canciones.txt y retorna cada linea en una lista dentro de otra lista
def insertCanciones(): 
    texto = open('Canciones.txt', 'r')
    cancionesOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    canciones=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    codValidos=[]
    for linea in cancionesOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de cancionesOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0]=='\n':#Validacion
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==6:#Validacion 
                    nuevo[5] = nuevo[5].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    codArt,todo=insertArt()#Obtiene la lista de codigos registrados
                    codPlaylist,todo=insertPlaylist()
                    codGen,todo=insertGen()
                    codAlbum,todo=insertAlbum()
                    if nuevo[2] in codArt and nuevo[3] in codAlbum and nuevo[4] in codGen and nuevo[5] in codPlaylist :#Agrega solo si los otros estan
                        canciones+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==7:#Validacion 
                    codArt,todo=insertArt()#Obtiene la lista de codigos registrados
                    codPlaylist,todo=insertPlaylist()
                    codGen,todo=insertGen()
                    codAlbum,todo=insertAlbum()
                    if (nuevo[2] in codArt) and (nuevo[3] in codAlbum) and (nuevo[4] in codGen) and (nuevo[5] in codPlaylist) :#Agrega solo si los otros estan
                        canciones+=[nuevo[:6]] 
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    return codValidos,canciones

