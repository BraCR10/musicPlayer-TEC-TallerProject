from busqueda import *
def reportesProp(diccProptodo,cont):
    reporte = open(f"reportePropietario{cont}.txt", "a")#Crea un nuevo archivo .txt
    reporte.write('\nLos propietarios registrados son: \n')#Agerga datos al archivo
    i=0
    reporte.write('\nCodigo - Nombre - Codigo de membresia - Estado')#Agerga datos al archivo
    for i in list(diccProptodo.keys()):
        reporte.write('\n-----------------------------------------')#Agerga datos al archivo
        reporte.write(f"\n {i} -{diccProptodo[i]['nombre']} - {diccProptodo[i]['codMem']} - {diccProptodo[i]['estado']}")#Agerga datos al archivo
    reporte.close()#Cierra archivo
    
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
