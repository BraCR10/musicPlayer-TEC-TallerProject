#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 

def insertProp(listaCod,listaTodo):
    cod =str(input('Digite el codigo de propiertario: '))
    nombre= str(input('Digite el nombre de propiertario: '))
    if cod not in listaCod:#Validacion si codigo esta repetido
        listaCod+=[cod]
        listaTodo+=[[cod,nombre]]  
        print('\n---> El nuevo propietario se ha incluido!')
    else:
        print('\n---> El codigo de propietario ya esta en uso')    
    return listaCod,listaTodo
def insertPlaylist(listaCod,listaTodo,listaCodProp):
    cod =str(input('Digite el codigo de la playlist: '))
    nombre= str(input('Digite el nombre de la playlist: '))
    codProp= str(input('Digite el codigo del propietario al que pertenece: '))
    if cod not in listaCod and codProp in listaCodProp:#Validacion si codigo esta repetido
        listaCod+=[cod]
        listaTodo+=[[cod,nombre,codProp]]  
        print('\n---> La nueva playlist se ha incluido!')
    else:
        print('\n---> El codigo de playlist ya esta en uso o el codigo de propietario no existe')    
    return listaCod,listaTodo
def insertGen(listaCod,listaTodo):
    cod =str(input('Digite el codigo del genero: '))
    nombre= str(input('Digite el nombre del genero: '))
    if cod not in listaCod:#Validacion si codigo esta repetido
        listaCod+=[cod]
        listaTodo+=[[cod,nombre]]  
        print('\n---> El nuevo genero se ha incluido!')
    else:
        print('\n---> El codigo del genero ya esta en uso')    
    return listaCod,listaTodo
def insertArt(listaCod,listaTodo,listaCodGen):
    cod =str(input('Digite el codigo del artista: '))
    nombre= str(input('Digite el nombre del artista: '))
    codGen= str(input('Digite el codigo del genero al que pertenece: '))
    if cod not in listaCod and codGen in listaCodGen:#Validacion si codigo esta repetido
        listaCod+=[cod]
        listaTodo+=[[cod,nombre,codGen]]  
        print('\n---> El nuevo artista  se ha incluido!')
    else:
        print('\n---> El codigo del artista ya esta en uso o el codigo de genero no existe')    
    return listaCod,listaTodo
def insertAlbum(listaCod,listaTodo,listaCodArt):
    cod =str(input('Digite el codigo del album: '))
    nombre= str(input('Digite el nombre del album: '))
    codArt= str(input('Digite el codigo del artista al que pertenece: '))
    if cod not in listaCod and codArt in listaCodArt:#Validacion si codigo esta repetido
        listaCod+=[cod]
        listaTodo+=[[cod,nombre,codArt]]  
        print('\n---> El nuevo album  se ha incluido!')
    else:
        print('\n---> El codigo del album ya esta en uso o el codigo de artista no existe')    
    return listaCod,listaTodo
def insertCanciones(listaCod,listaTodo,listaCodArt,listaCodAlbum,listaCodGen,listaCodPlaylist):
    cod =str(input('Digite el codigo de la cancion: '))
    nombre= str(input('Digite el nombre de la cancion: '))
    codArt= str(input('Digite el codigo del artista al que pertenece: '))
    codAlb= str(input('Digite el codigo del album al que pertenece: '))
    codGen= str(input('Digite el codigo del genero al que pertenece: '))
    codPlaylist= str(input('Digite el codigo de la playlist al que pertenece: '))
    if cod not in listaCod and codArt in listaCodArt and codAlb in listaCodAlbum and codGen in listaCodGen and codPlaylist in listaCodPlaylist:#Validacion si codigo esta repetido
        listaCod+=[cod]
        listaTodo+=[[cod,nombre,codArt,codAlb,codGen,codPlaylist]]  
        print('\n---> La nueva cancion  se ha incluido!')
    else:
        print('\n---> El codigo de la cancion ya esta en uso o digito algun codigo no existente')    
    return listaCod,listaTodo