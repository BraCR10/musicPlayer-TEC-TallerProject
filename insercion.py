#Esta funcion lee un fichero llamado propietario.txt y retorna cada linea en una lista dentro de otra lista
def insertProp(): 
    texto = open('propietario.txt', 'r')
    propietariosOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    propietarios=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in propietariosOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de propietariosOri crea una nueva lista dividiendo cada vez que hay un ';'['1234', 'Juan Perez']
        if nuevo[0]=='\n':#Validacion en caso de lineas con enter
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
    return cod,propietarios#Lista de codigos y lista de todo

#Esta funcion lee un fichero llamado Genero.txt y retorna cada linea en una lista dentro de otra lista
def insertGen():
    texto = open('genero.txt', 'r')
    GenerosOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    Generos=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in GenerosOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de GeneroOri crea una nueva lista dividiendo cada vez que hay un ';'
        if nuevo[0]=='\n':#Validacion en caso de lineas con enter
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
    return cod,Generos#Lista de codigos y lista de todo

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
        if nuevo[0]=='\n':#Validacion en caso de lineas con enter
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==3:#Validacion 
                    nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    #Obtiene la lista de codigos registrados
                    if nuevo[2] in insertGen()[0]:#Agrega solo si el genero esta en la lista de codigos que pertenece a insertGen
                        artistas+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==4:#Validacion 
                    if nuevo[2] in insertGen()[0]:#Agrega solo si el genero esta en la lista de codigos que pertenece a insertGen
                        artistas+=[nuevo[:3]]
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    return codValidos,artistas#Lista de codigos y lista de todo

#Esta funcion lee un fichero llamado Playlist.txt y retorna cada linea en una lista dentro de otra lista
def insertPlaylist():
    texto = open('playlist.txt', 'r')
    playlistOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    playlists=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    codValidos=[]
    for linea in playlistOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de PlaylistOri crea una nueva lista dividiendo cada vez que hay un ';'
        if nuevo[0]=='\n':##Validacion en caso de lineas con enter
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==3:#Validacion 
                    nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    if nuevo[2] in insertProp()[0]:#Agrega solo si el propietario esta en la lista de codigos que pertenece a insertProp
                        playlists+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==4:#Validacion 
                    if nuevo[2] in insertProp()[0]:#Agrega solo si el propietario esta en la lista de codigos que pertenece a insertProp
                        playlists+=[nuevo[:3]]
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    return codValidos,playlists#Lista de codigos y lista de todo

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
        if nuevo[0]=='\n':##Validacion en caso de lineas con enter
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==3:#Validacion 
                    nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    if nuevo[2] in insertArt()[0]:#Agrega solo si el artista esta en la lista de codigos que pertenece a insertArt
                        albums+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==4:#Validacion 
                    if nuevo[2] in insertArt()[0]:#Agrega solo si el artista esta en la lista de codigos que pertenece a insertArt
                        albums+=[nuevo[:3]]
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    return codValidos,albums#Lista de codigos y lista de todo

#Esta funcion lee un fichero llamado Canciones.txt y retorna cada linea en una lista dentro de otra lista
def insertCanciones(): 
    texto = open('Canciones.txt', 'r')
    cancionesOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    canciones=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    codValidos=[]
    for linea in cancionesOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de cancionesOri crea una nueva lista dividiendo cada vez que hay un ';'
        if nuevo[0]=='\n':##Validacion en caso de lineas con enter
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==6:#Validacion 
                    nuevo[5] = nuevo[5].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    if nuevo[2] in insertArt()[0] and nuevo[3] in insertAlbum()[0] and nuevo[4] in insertGen()[0] and nuevo[5] in insertPlaylist()[0] :#Revisa la lista de codigos de cada funcion, si cumple todo entonces almacena la cancion
                        canciones+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==7:#Validacion 
                    if nuevo[2] in insertArt()[0] and nuevo[3] in insertAlbum()[0] and nuevo[4] in insertGen()[0] and nuevo[5] in insertPlaylist()[0] :#Revisa la lista de codigos de cada funcion, si cumple todo entonces almacena la cancion
                        canciones+=[nuevo[:6]] 
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    return codValidos,canciones
print(insertCanciones())
