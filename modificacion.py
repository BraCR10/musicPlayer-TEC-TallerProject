#Avance final proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from acciones import *

from tkinter import messagebox
def modificarProp(codProp,diccProptodo,nombreModificacionProp,etiquetaConfirmacionModificacionProp):
    if codProp.get()  in list(diccProptodo.keys()) :#Validacion si codigo esta repetido
        mostrarEnPantalla(etiquetaConfirmacionModificacionProp,f"El propietario {diccProptodo[codProp.get()]['nombre']} con el codigo {codProp.get()} se le ha modificado el nombre a {nombreModificacionProp.get()} correctamente!")
        diccProptodo[codProp.get()]['nombre']= nombreModificacionProp.get()#Actualiza en memoria
        limpiar_texto(codProp)
        limpiar_texto(nombreModificacionProp)
    else:
        messagebox.showinfo("Alerta", "El codigo de propietario digitado no existe, digite otro!")
        limpiar_texto(codProp)
    
def modificarPlaylist(codPlaylist,diccPlaylisttodo,nombreModificacionPlaylist,etiquetaConfirmacionModificacionPlaylist):
    if codPlaylist.get()  in list(diccPlaylisttodo.keys()) :#Validacion si codigo esta repetido
        mostrarEnPantalla(etiquetaConfirmacionModificacionPlaylist,f"La playlist {diccPlaylisttodo[codPlaylist.get()]['nombre']} con el codigo {codPlaylist.get()} se le ha modificado el nombre a {nombreModificacionPlaylist.get()} correctamente!")
        diccPlaylisttodo[codPlaylist.get()]['nombre']=nombreModificacionPlaylist.get()
        limpiar_texto(codPlaylist)
        limpiar_texto(nombreModificacionPlaylist)
    else:
        messagebox.showinfo("Alerta", "El codigo de  playlist digitado no existe, digite otro!")
        limpiar_texto(codPlaylist)
    
def modificarGen(codGen,diccGentodo,nombreModificacionGen,etiquetaConfirmacionModificacionGen):
    if codGen.get()  in list(diccGentodo.keys()) :#Validacion si codigo esta repetido
        mostrarEnPantalla(etiquetaConfirmacionModificacionGen,f"El genero {diccGentodo[codGen.get()]['nombre']} con el codigo {codGen.get()} se le ha modificado el nombre a {nombreModificacionGen.get()} correctamente!")
        diccGentodo[codGen.get()]['nombre']=nombreModificacionGen.get()
        limpiar_texto(codGen)
        limpiar_texto(nombreModificacionGen)
    else:
        messagebox.showinfo("Alerta", "El codigo de genero digitado no existe, digite otro!")
        limpiar_texto(codGen)
        
def modificarArt(codArt,diccArttodo,nombreModificacionArt,etiquetaConfirmacionModificacionArt):
    if codArt.get()  in list(diccArttodo.keys()) :#Validacion si codigo esta repetido
        mostrarEnPantalla(etiquetaConfirmacionModificacionArt,f"El artista {diccArttodo[codArt.get()]['nombre']} con el codigo {codArt.get()} se le ha modificado el nombre a {nombreModificacionArt.get()} correctamente!")
        diccArttodo[codArt.get()]['nombre']=nombreModificacionArt.get()
        limpiar_texto(codArt)
        limpiar_texto(nombreModificacionArt)
    else:
        messagebox.showinfo("Alerta", "El codigo de artista digitado no existe, digite otro!")
        limpiar_texto(codArt)
        
def modificarAlbum(codAlb,diccAlbumtodo,nombreModificacionAlb,etiquetaConfirmacionModificacionAlb):
    if codAlb.get()  in list(diccAlbumtodo.keys()) :#Validacion si codigo esta repetido
        mostrarEnPantalla(etiquetaConfirmacionModificacionAlb,f"El album {diccAlbumtodo[codAlb.get()]['nombre']} con el codigo {codAlb.get()} se le ha modificado el nombre a {nombreModificacionAlb.get()} correctamente!")
        diccAlbumtodo[codAlb.get()]['nombre']=nombreModificacionAlb.get()
        limpiar_texto(codAlb)
        limpiar_texto(nombreModificacionAlb)
    else:
        messagebox.showinfo("Alerta", "El codigo de album digitado no existe, digite otro!")
        limpiar_texto(codAlb)
        
def modificarCancion(codCancion,diccCancionestodo):
    nuevo=str(input('\nDigite el nuevo nombre de la cancion: '))
    diccCancionestodo[codCancion]['nombre']=nuevo#Actualiza en memoria

def modificarCancion(codigoModCancion,diccCancionestodo,nombreModCancion,codigoArtModificacionCancion,codigoAlbModificacionCancion,codigoGenModificacionCancion,codigoPlaylistModificacionCancion,etiquetaConfirmacionMoficacionCancion):
    if codigoModCancion.get()  in list(diccCancionestodo.keys()):
        if  diccCancionestodo[codigoModCancion.get()]['codArt']==codigoArtModificacionCancion.get():
            if diccCancionestodo[codigoModCancion.get()]['codAlb']==codigoAlbModificacionCancion.get():
                if diccCancionestodo[codigoModCancion.get()]['codGen']==codigoGenModificacionCancion.get():
                    if diccCancionestodo[codigoModCancion.get()]['codPlaylist']==codigoPlaylistModificacionCancion.get():
                        mostrarEnPantalla(etiquetaConfirmacionMoficacionCancion,f"La cancion {diccCancionestodo[codigoModCancion.get()]['nombre']} con el codigo {codigoModCancion.get()} se le ha modificado el nombre a {nombreModCancion.get()} correctamente!")
                        diccCancionestodo[codigoModCancion.get()]['nombre']=nombreModCancion.get()#Añade  una playlist al dict
                        limpiar_texto(nombreModCancion)
                        limpiar_texto(codigoModCancion)
                        limpiar_texto(codigoArtModificacionCancion)
                        limpiar_texto(codigoGenModificacionCancion)
                        limpiar_texto(codigoAlbModificacionCancion)
                        limpiar_texto(codigoPlaylistModificacionCancion)
                    else:
                        messagebox.showinfo("Alerta", "El codigo digitado de playlist no coincide!")
                        limpiar_texto(codigoPlaylistModificacionCancion)
                else:
                    messagebox.showinfo("Alerta", "El codigo digitado de genero no coincide!")
                    limpiar_texto(codigoGenModificacionCancion)
            else:
                messagebox.showinfo("Alerta", "El codigo digitado de album no coincide!")
                limpiar_texto(codigoAlbModificacionCancion)
        else:
            messagebox.showinfo("Alerta", "El codigo digitado de artista no coincide!")
            limpiar_texto(codigoArtModificacionCancion)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de cancion no existe, digite otro!")
        limpiar_texto(codigoModCancion)

def modificarAdm(codAdm,diccAdmintodo,nombreModificacionAdm,etiquetaConfirmacionModificacionAdm):
    if codAdm.get()  in list(diccAdmintodo.keys()) :#Validacion si codigo esta 
        mostrarEnPantalla(etiquetaConfirmacionModificacionAdm,f"El administrador {diccAdmintodo[codAdm.get()]['nombre']} con el codigo {codAdm.get()} se le ha modificado el nombre a {nombreModificacionAdm.get()} correctamente!",)
        diccAdmintodo[codAdm.get()]['nombre']=nombreModificacionAdm.get()
        limpiar_texto(codAdm)
        limpiar_texto(nombreModificacionAdm)
    else:
        messagebox.showinfo("Alerta", "El codigo de administrador digitado no existe, digite otro!")
        limpiar_texto(codAdm)