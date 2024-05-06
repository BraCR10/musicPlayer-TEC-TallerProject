#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from lecturaArchivos import *
from acciones import *
from tkinter import messagebox
def insertProp(diccTodo,diccMembresias,cod,nombre,codMem,estado,etiquetaConfirmacionInsercionProp):
    
    if estado.get()== '1' or estado.get()== '0' :
        if cod.get()  not in list(diccTodo.keys()) :#Validacion si codigo esta repetido
            if codMem.get() not in list(diccMembresias.values()):
                diccTodo[cod.get()]={'nombre':nombre.get(),'codMem':codMem.get(),'estado':estado.get()}#Añade  un propietario al dict
                diccMembresias[cod.get()]=codMem.get()
                mostrarEnPantalla(etiquetaConfirmacionInsercionProp,"El propietario se ha insertado correctamente",)
                limpiar_texto(nombre)
                limpiar_texto(cod)
                limpiar_texto(estado)
                limpiar_texto(codMem)
            else:
                messagebox.showinfo("Alerta", "El codigo digitado de membresia ya existe, digite otro!")
                limpiar_texto(codMem)
        else:
            messagebox.showinfo("Alerta", "El codigo de propietario digitado ya existe, digite otro!")
            limpiar_texto(cod)

    else:
        messagebox.showinfo("Alerta", "El estado de la membresia debe ser 1 o 0")
        limpiar_texto(estado)
    return diccTodo,diccMembresias

def insertPlaylist(diccTodo,diccTodoProp,cod,nombre,codProp,etiquetaConfirmacionInsercionPlaylist):
    if cod.get() not in list(diccTodo.keys()) :#Validacion si codigo esta repetido
        if codProp.get() in list(diccTodoProp.keys()):
            diccTodo[cod.get()]={'nombre':nombre.get(),'codProp':codProp.get()}#Añade  una playlist al dict
            mostrarEnPantalla(etiquetaConfirmacionInsercionPlaylist,"La playlist se ha insertado correctamente",)
            limpiar_texto(nombre)
            limpiar_texto(cod)
            limpiar_texto(codProp)
        else:
            messagebox.showinfo("Alerta", "El codigo digitado de propietario no existe, digite otro existente!")
            limpiar_texto(codProp)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de playlist ya existe, digite otro!")
        limpiar_texto(cod)  
    return diccTodo

def insertGen(diccTodo,cod,nombre,etiquetaConfirmacionInsercionGen):
    if cod.get() not in  list(diccTodo.keys()):#Validacion si codigo esta repetido
        diccTodo[cod.get()]={'nombre':nombre.get()}#Añade  un genero al dict
        mostrarEnPantalla(etiquetaConfirmacionInsercionGen,"El genero se ha insertado correctamente",)
        limpiar_texto(nombre)
        limpiar_texto(cod)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de genero  ya existe, digite otro!")
        limpiar_texto(cod)      
    return diccTodo

def insertArt(diccTodo,diccTodoGen,cod,nombre,codGen,etiquetaConfirmacionInsercionArt):
    if cod.get() not in list(diccTodo.keys()):
        if codGen.get() in list(diccTodoGen.keys()):#Validacion si codigo esta repetido
            diccTodo[cod.get()]={'nombre':nombre.get(),'codGen':codGen.get()}#Añade  una playlist al dict
            mostrarEnPantalla(etiquetaConfirmacionInsercionArt,"El artista se ha insertado correctamente",)
            limpiar_texto(nombre)
            limpiar_texto(cod)
            limpiar_texto(codGen)
        else:
            messagebox.showinfo("Alerta", "El codigo digitado de genero no existe, digite otro existente!")
            limpiar_texto(codGen)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de artista ya existe, digite otro!")
        limpiar_texto(cod)     
    return diccTodo

def insertAlbum(diccTodo,diccTodoArt,cod,nombre,codArt,etiquetaConfirmacionInsercionAlb):
    if cod.get() not in list(diccTodo.keys()) :
        if codArt.get() in list(diccTodoArt.keys()):#Validacion si codigo esta repetido
            diccTodo[cod.get()]={'nombre':nombre.get(),'codArt':codArt.get()}#Añade  una playlist al dict
            mostrarEnPantalla(etiquetaConfirmacionInsercionAlb,"El album se ha insertado correctamente",)
            limpiar_texto(nombre)
            limpiar_texto(cod)
            limpiar_texto(codArt)
        else:
            messagebox.showinfo("Alerta", "El codigo digitado de artista no existe, digite otro existente!")
            limpiar_texto(codArt)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de album ya existe, digite otro!")
        limpiar_texto(cod)     
    return diccTodo

def insertCanciones(diccTodo,diccTodoArt,diccTodoAlbum,diccTodoGen,diccTodoPlaylist,cod,nombre,codArt,codAlb,codGen,codPlaylist,etiquetaConfirmacionInsercionCancion):
    if cod.get() not in list(diccTodo.keys()):
        if codArt.get() in list(diccTodoArt.keys()):
            if codAlb.get() in list(diccTodoAlbum.keys()) :
                if codGen.get() in list(diccTodoGen.keys()) :
                    if codPlaylist.get() in list(diccTodoPlaylist.keys()):#Validacion si codigo esta repetido
                        diccTodo[cod.get()]={'nombre':nombre.get(),'codArt':codArt.get(),'codAlb':codAlb.get(),'codGen':codGen.get(),'codPlaylist':codPlaylist.get()}#Añade  una playlist al dict
                        mostrarEnPantalla(etiquetaConfirmacionInsercionCancion,"La cancion se ha insertado correctamente",)
                        limpiar_texto(nombre)
                        limpiar_texto(cod)
                        limpiar_texto(codArt)
                        limpiar_texto(codGen)
                        limpiar_texto(codAlb)
                        limpiar_texto(codPlaylist)
                    else:
                        messagebox.showinfo("Alerta", "El codigo digitado de playlist no existe, digite otro existente!")
                        limpiar_texto(codPlaylist)
                else:
                    messagebox.showinfo("Alerta", "El codigo digitado de genero no existe, digite otro existente!")
                    limpiar_texto(codGen)
            else:
                messagebox.showinfo("Alerta", "El codigo digitado de album no existe, digite otro existente!")
                limpiar_texto(codAlb)
        else:
            messagebox.showinfo("Alerta", "El codigo digitado de artista no existe, digite otro existente!")
            limpiar_texto(codArt)
    else:
        messagebox.showinfo("Alerta", "El codigo digitado de cancion ya existe, digite otro!")
        limpiar_texto(cod)
    return diccTodo