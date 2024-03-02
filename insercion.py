#Esta funcion lee un fichero llamado propietario.txt y reorna cada linea en una lista dentro de otra lista
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
            if nuevo==['\n'] or len(nuevo)!=2:#Validacion si hay un enter o un elemento diferente
                nuevo=[]
            else:#Validacion
                nuevo[1] = nuevo[1].replace('\n', '') #Elimina cada '\n' en cada elemento [1]
                propietarios+=[nuevo]          
    return propietarios
