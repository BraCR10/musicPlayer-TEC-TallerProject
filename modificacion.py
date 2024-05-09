#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from acciones import *

from tkinter import messagebox
def modificarProp(codProp,diccProptodo,nombreModificacionProp,etiquetaConfirmacionModificacionProp):
    if codProp.get()  in list(diccProptodo.keys()) :#Validacion si codigo esta repetido
        diccProptodo[codProp.get()]['nombre']= nombreModificacionProp.get()#Actualiza en memoria
        mostrarEnPantalla(etiquetaConfirmacionModificacionProp,f"El propietario con el codigo {codProp.get()} se le ha modificado el nombre correctamente!",)
        limpiar_texto(codProp)
        limpiar_texto(nombreModificacionProp)
    else:
        messagebox.showinfo("Alerta", "El codigo de propietario digitado no existe, digite otro!")
        limpiar_texto(codProp)
    
def modificarPlaylist(codPlaylist,diccPlaylisttodo,nombreModificacionPlaylist,etiquetaConfirmacionModificacionPlaylist):
    if codPlaylist.get()  in list(diccPlaylisttodo.keys()) :#Validacion si codigo esta repetido
        diccPlaylisttodo[codPlaylist.get()]['nombre']=nombreModificacionPlaylist.get()
        mostrarEnPantalla(etiquetaConfirmacionModificacionPlaylist,f"La playlist con el codigo {codPlaylist.get()} se le ha modificado el nombre correctamente!",)
        limpiar_texto(codPlaylist)
        limpiar_texto(nombreModificacionPlaylist)
    else:
        messagebox.showinfo("Alerta", "El codigo de  playlist digitado no existe, digite otro!")
        limpiar_texto(codPlaylist)
    
def modificarGen(codGen,diccGentodo,nombreModificacionGen,etiquetaConfirmacionModificacionGen):
    if codGen.get()  in list(diccGentodo.keys()) :#Validacion si codigo esta repetido
        diccGentodo[codGen.get()]['nombre']=nombreModificacionGen.get()
        mostrarEnPantalla(etiquetaConfirmacionModificacionGen,f"El genero con el codigo {codGen.get()} se le ha modificado el nombre correctamente!",)
        limpiar_texto(codGen)
        limpiar_texto(nombreModificacionGen)
    else:
        messagebox.showinfo("Alerta", "El codigo de genero digitado no existe, digite otro!")
        limpiar_texto(codGen)
        
def modificarArt(codArt,diccArttodo,nombreModificacionArt,etiquetaConfirmacionModificacionArt):
    if codArt.get()  in list(diccArttodo.keys()) :#Validacion si codigo esta repetido
        diccArttodo[codArt.get()]['nombre']=nombreModificacionArt.get()
        mostrarEnPantalla(etiquetaConfirmacionModificacionArt,f"El artista con el codigo {codArt.get()} se le ha modificado el nombre correctamente!",)
        limpiar_texto(codArt)
        limpiar_texto(nombreModificacionArt)
    else:
        messagebox.showinfo("Alerta", "El codigo de artista digitado no existe, digite otro!")
        limpiar_texto(codArt)
        
def modificarAlbum(codAlb,diccAlbumtodo,nombreModificacionAlb,etiquetaConfirmacionModificacionAlb):
    if codAlb.get()  in list(diccAlbumtodo.keys()) :#Validacion si codigo esta repetido
        diccAlbumtodo[codAlb.get()]['nombre']=nombreModificacionAlb.get()
        mostrarEnPantalla(etiquetaConfirmacionModificacionAlb,f"El album con el codigo {codAlb.get()} se le ha modificado el nombre correctamente!",)
        limpiar_texto(codAlb)
        limpiar_texto(nombreModificacionAlb)
    else:
        messagebox.showinfo("Alerta", "El codigo de album digitado no existe, digite otro!")
        limpiar_texto(codAlb)
        
def modificarCancion(codCancion,diccCancionestodo):
    nuevo=str(input('\nDigite el nuevo nombre de la cancion: '))
    diccCancionestodo[codCancion]['nombre']=nuevo#Actualiza en memoria

def modificarCancion(codigoModCancion,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo,nombreModCancion,codigoArtModificacionCancion,codigoAlbModificacionCancion,codigoGenModificacionCancion,codigoPlaylistModificacionCancion,etiquetaConfirmacionMoficacionCancion):
    if codigoModCancion.get()  in list(diccCancionestodo.keys()):
        if  diccCancionestodo[codigoModCancion.get()]['codArt']==codigoArtModificacionCancion.get():
            if diccCancionestodo[codigoModCancion.get()]['codAlb']==codigoAlbModificacionCancion.get():
                if diccCancionestodo[codigoModCancion.get()]['codGen']==codigoGenModificacionCancion.get():
                    if diccCancionestodo[codigoModCancion.get()]['codPlaylist']==codigoPlaylistModificacionCancion.get():
                        diccCancionestodo[codigoModCancion.get()]['nombre']=nombreModCancion.get()#Añade  una playlist al dict
                        mostrarEnPantalla(etiquetaConfirmacionMoficacionCancion,"La cancion se ha insertado correctamente",)
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
    if codAdm.get()  in list(diccAdmintodo.keys()) :#Validacion si codigo esta repetido
        diccAdmintodo[codAdm.get()]['nombre']=nombreModificacionAdm.get()
        mostrarEnPantalla(etiquetaConfirmacionModificacionAdm,f"El administrador con el codigo {codAdm.get()} se le ha modificado el nombre correctamente!",)
        limpiar_texto(codAdm)
        limpiar_texto(nombreModificacionAdm)
    else:
        messagebox.showinfo("Alerta", "El codigo de administrador digitado no existe, digite otro!")
        limpiar_texto(codAdm)