#Avance final proyecto del reproductor de musica#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from acciones import *
from tkinter import messagebox
def eliminarProp(codigoEliminacionProp,diccProptodo,diccMembresias,diccPlaylisttodo,diccCancionestodo,etiquetaConfirmacionEliminacionProp):
    if codigoEliminacionProp.get()  in list(diccProptodo.keys()):
        mostrarEnPantalla(etiquetaConfirmacionEliminacionProp,f"El propietario {diccProptodo[codigoEliminacionProp.get()]['nombre']} con el codigo {codigoEliminacionProp.get()} se ha eliminado correctamente")
        #Eliminacion de vinculos
        for i in  list(diccPlaylisttodo.keys()):#i itera en una listas con las llaves del dicc playlist
            if diccPlaylisttodo[i]['codProp']==codigoEliminacionProp.get():# Si el prop ligado a esa playlist es el que se elimina
                #Eliminacion de vinculo de playlist
                for codCancion in list(diccCancionestodo.keys()):#codCanciones itera en una lista de llaves de canciones
                    if diccCancionestodo[codCancion]['codPlaylist']==i:#si la playlist ligada a esa cancion se elimina
                        diccCancionestodo.pop(codCancion)#
                diccPlaylisttodo.pop(i)
        #Eliminacion principal
        diccMembresias.pop(codigoEliminacionProp.get())
        diccProptodo.pop(codigoEliminacionProp.get())
        limpiar_texto(codigoEliminacionProp)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de propietario no existe, digite otro existente!")
        limpiar_texto(codigoEliminacionProp)
        
def eliminarPlaylist(codigoEliminacionPlaylist,diccPlaylisttodo,diccCancionestodo,etiquetaConfirmacionEliminacionPlaylist):
    if codigoEliminacionPlaylist.get() in  list(diccPlaylisttodo.keys()):
        mostrarEnPantalla(etiquetaConfirmacionEliminacionPlaylist,f"La playlist {diccPlaylisttodo[codigoEliminacionPlaylist.get()]['nombre']} con el codigo {codigoEliminacionPlaylist.get()} se ha eliminado correctamente")
    #Eliminacion de vinculos
        for i in  list(diccCancionestodo.keys()):#i itera en una listas con las llaves del dicc playlist
            if diccCancionestodo[i]['codPlaylist']==codigoEliminacionPlaylist.get():# Si el prop ligado a esa playlist es el que se elimina
                diccCancionestodo.pop(i)
        #Eliminacion principal
        diccPlaylisttodo.pop(codigoEliminacionPlaylist.get())
        limpiar_texto(codigoEliminacionPlaylist)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de playlist no existe, digite otro existente!")
        limpiar_texto(codigoEliminacionPlaylist)

def eliminarGenero(codigoEliminacionGen,diccGentodo,diccArttodo,diccAlbumtodo,diccCancionestodo,etiquetaConfirmacionEliminacionGen):
    if codigoEliminacionGen.get() in  list(diccGentodo.keys()):
        #Eliminacio de vinculos
        mostrarEnPantalla(etiquetaConfirmacionEliminacionGen,f"El genero {diccGentodo[codigoEliminacionGen.get()]['nombre']} con el codigo {codigoEliminacionGen.get()} se ha eliminado correctamente")
        for i in  list(diccArttodo.keys()):#i itera en una listas con las llaves del dicc playlist
            if diccArttodo[i]['codGen']==codigoEliminacionGen.get():# Si el prop ligado a esa playlist es el que se elimina
                #Eliminacion de vinculo de playlist
                for codAlbum in list(diccAlbumtodo.keys()):#codCanciones itera en una lista de llaves de canciones
                    if diccAlbumtodo[codAlbum]['codArt']==i:#si la playlist ligada a esa cancion se elimina
                        for codCancion in list(diccCancionestodo.keys()):#codCanciones itera en una lista de llaves de canciones
                            if diccCancionestodo[codCancion]['codAlb']==codAlbum or diccCancionestodo[codCancion]['codArt']==i or diccCancionestodo[codCancion]['codGen']==codigoEliminacionGen.get():#si la playlist ligada a esa cancion se elimina
                                diccCancionestodo.pop(codCancion)#
                        diccAlbumtodo.pop(codAlbum)
                diccArttodo.pop(i)
        #Eliminacion principal
        diccGentodo.pop(codigoEliminacionGen.get())
        limpiar_texto(codigoEliminacionGen)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de genero no existe, digite otro existente!")
        limpiar_texto(codigoEliminacionGen)

def eliminarArt(codigoEliminacionArt,diccArttodo,diccAlbumtodo,diccCancionestodo,etiquetaConfirmacionEliminacionArt):
    if codigoEliminacionArt.get() in  list(diccArttodo.keys()):
        mostrarEnPantalla(etiquetaConfirmacionEliminacionArt,f"El artista {diccArttodo[codigoEliminacionArt.get()]['nombre']} con el codigo {codigoEliminacionArt.get()} se ha eliminado correctamente")
        #Eliminacion de vinculos
        for i in  list(diccAlbumtodo.keys()):#i itera en una listas con las llaves del dicc playlist
            if diccAlbumtodo[i]['codArt']==codigoEliminacionArt.get():# Si el prop ligado a esa playlist es el que se elimina
                diccAlbumtodo.pop(i)
        for i in list(diccCancionestodo.keys()):#codCanciones itera en una lista de llaves de canciones
            if diccCancionestodo[i]['codArt']==codigoEliminacionArt.get():#si la playlist ligada a esa cancion se elimina
                diccCancionestodo.pop(i)
        #Eliminacion principal
        diccArttodo.pop(codigoEliminacionArt.get())
        limpiar_texto(codigoEliminacionArt)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de artista no existe, digite otro existente!")
        limpiar_texto(codigoEliminacionArt)
        
def eliminarAlbum(codigoEliminacionAlb,diccAlbumtodo,diccCancionestodo,etiquetaConfirmacionEliminacionAlb):
    if codigoEliminacionAlb.get() in  list(diccAlbumtodo.keys()):
        mostrarEnPantalla(etiquetaConfirmacionEliminacionAlb,f"El album {diccAlbumtodo[codigoEliminacionAlb.get()]['nombre']} con el codigo {codigoEliminacionAlb.get()} se ha eliminado correctamente")
        #Eliminacion de vinculos
        for i in list(diccCancionestodo.keys()):#codCanciones itera en una lista de llaves de canciones
            if diccCancionestodo[i]['codAlb']==codigoEliminacionAlb.get():
                diccCancionestodo.pop(i)
        #Eliminacion principal
        diccAlbumtodo.pop(codigoEliminacionAlb.get())
        limpiar_texto(codigoEliminacionAlb)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de album no existe, digite otro existente!")
        limpiar_texto(codigoEliminacionAlb)

def eliminarCanciones(codigoEliminacionCancion,diccCancionestodo,etiquetaConfirmacionEliminacionCancion):
    print(diccCancionestodo.keys())
    if codigoEliminacionCancion.get() in  list(diccCancionestodo.keys()):
        mostrarEnPantalla(etiquetaConfirmacionEliminacionCancion,f"La cancion {diccCancionestodo[codigoEliminacionCancion.get()]['nombre']} con el codigo {codigoEliminacionCancion.get()} se ha eliminado correctamente")
        #Eliminacion principal
        diccCancionestodo.pop(codigoEliminacionCancion.get())
        limpiar_texto(codigoEliminacionCancion)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de cancion no existe, digite otro existente!")
        limpiar_texto(codigoEliminacionCancion)
    print(diccCancionestodo.keys())
        
def eliminarAdministrador(codigoEliminacionAdm,diccAdmintodo,etiquetaConfirmacionEliminacionAdm):
    if codigoEliminacionAdm.get() in  list(diccAdmintodo.keys()):
        if  (list(diccAdmintodo.keys())[0]=="Codadministrador" and len(diccAdmintodo)>2) or (list(diccAdmintodo.keys())[0]!="Codadministrador" and len(diccAdmintodo)>1):#Validacion de administradores, debe haber por lo menos uno
            mostrarEnPantalla(etiquetaConfirmacionEliminacionAdm,f"El administrador {diccAdmintodo[codigoEliminacionAdm.get()]['nombre']} con el codigo {codigoEliminacionAdm.get()} se ha eliminado correctamente")
            #Eliminacion principal
            diccAdmintodo.pop(codigoEliminacionAdm.get())
            limpiar_texto(codigoEliminacionAdm)
        else:
            messagebox.showinfo("Alerta", "No puedes eliminar este administrador ya debe haber por lo menos uno!")
            limpiar_texto(codigoEliminacionAdm)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de administrador no existe, digite otro existente!")
        limpiar_texto(codigoEliminacionAdm)
        



