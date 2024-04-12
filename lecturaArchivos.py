#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

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
    texto = open('Genero.txt', 'r',encoding="utf8")
    GenerosOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    Generos=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    for linea in GenerosOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de GeneroOri crea una nueva lista dividiendo cada vez que hay un ';'
        if nuevo[0]=='\n'or len(nuevo)<2 or len(nuevo)>3:#Validacion en caso de lineas con enter o mala sintaxis en el .txt
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
    for i in range(len(Generos)):
        Generos[i]=Generos[i][0],[Generos[i][1]]
    for i in range(len(Generos)):
        Generos+=[Generos[0],Generos[1]]
        Generos=Generos[1:]
    Generos=dict(Generos)  
    return cod,Generos#Lista de codigos y lista de todo    

#Esta funcion lee un fichero llamado Artista.txt y retorna cada linea en una lista dentro de otra lista
def leerArt():
    texto = open('Artista.txt', 'r',encoding="utf8")
    artistasOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    artistas=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos
    codValidos=[]
    for linea in artistasOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de artistasOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0]=='\n'or len(nuevo)<3 or len(nuevo)>4:#Validacion en caso de lineas con enter o mala sintaxis en el .txt
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==3:#Validacion 
                    nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    #Obtiene la lista de codigos registrados
                    if nuevo[2] in leerGen()[0]:#Agrega solo si el genero esta en la lista de codigos que pertenece a insertGen
                        artistas+=[nuevo] 
                        
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==4:#Validacion 
                    if nuevo[2] in leerGen()[0]:#Agrega solo si el genero esta en la lista de codigos que pertenece a insertGen
                        artistas+=[nuevo[:3]]
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    for i in range(len(artistas)):
        artistas[i]=artistas[i][0],[artistas[i][1],artistas[i][2]]
    for i in range(len(artistas)):
        artistas+=[artistas[0],artistas[1]]
        artistas=artistas[1:]
    artistas=dict(artistas)  
    return codValidos,artistas#Lista de codigos y lista de todo

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
    texto = open('Albumes.txt', 'r',encoding="utf8")
    albumOri=texto.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    texto.close()
    albums=[]#Lista para almacenar cambios en los datos del fichero
    cod=[]#Almacena codigos para que no se repitan
    codValidos=[]#Almacena codigos que cumple todas las condiciones
    for linea in albumOri:#Itera en lista sin cambios
        nuevo=linea.split(';')#Por cada elemento de albumOri crea una nueva lista dividiendo cada vez que hay un ';'['1234','Music','620193']
        if nuevo[0]=='\n'or len(nuevo)<2 or len(nuevo)>4:#Validacion en caso de lineas con enter o mala sintaxis en el .txt
            continue
        else:
            if nuevo[0] in cod:#Validacion si codigo esta repetido
                continue
            else:
                cod+=[nuevo[0]]
                if len(nuevo)==3:#Validacion 
                    nuevo[2] = nuevo[2].replace('\n', '') #Elimina cada '\n' en cada elemento [2]
                    if nuevo[2] in leerArt()[0]:#Agrega solo si el artista esta en la lista de codigos que pertenece a insertArt
                        albums+=[nuevo] 
                        codValidos+=[nuevo[0]]
                elif len(nuevo)==4:#Validacion 
                    if nuevo[2] in leerArt()[0]:#Agrega solo si el artista esta en la lista de codigos que pertenece a insertArt
                        albums+=[nuevo[:3]]
                        codValidos+=[nuevo[0]]
                else:#Validacion 
                    continue     
    for i in range(len(albums)):
        albums[i]=albums[i][0],[albums[i][1],albums[i][2]]
    for i in range(len(albums)):
        albums+=[albums[0],albums[1]]
        albums=albums[1:]
    albums=dict(albums)  
    return codValidos,albums#Lista de codigos y lista de todo

def leerCanciones(): 
    archivo=open('Canciones.txt', 'r',encoding="utf8")
    dicc={}
    for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(';')
            if columnas[0] not in list(dicc.keys()) and len(columnas)==6 and columnas[2]==list(leerArt().keys()) and columnas[3]==list(leerAlbum().keys()) and columnas[4]==list(leerGen().keys())and columnas[5]==list(leerPlaylist().keys()):
                cod = columnas[0]
                nombre = columnas[1]
                codArt = columnas[2]
                codAlb = columnas[3]
                codGen= columnas[4]
                codPlaylist= columnas[5]
                dicc[cod]={'nombre':nombre,'codArt':codArt,'codAlb':codAlb,'codGen':codGen,'codPlaylist':codPlaylist }
    return dicc

'''
#Pruebas:
print(insertProp())
print(insertPlaylist())
print(insertGen())
print(insertArt())
print(insertAlbum())
print(insertCanciones())'''

#print(leerPlaylist())
#print(leerCanciones())
#print(leerProp())