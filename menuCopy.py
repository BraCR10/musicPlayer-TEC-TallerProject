#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from lecturaArchivos import *#leerAlbum,leerArt,leerCanciones,leerGen,leerPlaylist,leerProp
from insercion import *#insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp
from busqueda import * #buscarAlbum,buscarArtista,buscarCancion,buscarGenero,buscarPlaylist,buscarProp
from login import *#registar,pagar,exportarTXT,factura
import tkinter as tk
from tkinter import ttk
from acciones import * 
def menu():
        diccProptodo=leerProp()[0]#Devuelve una lista con membresias
        diccMembresias=leerProp()[1]
        diccGentodo=leerGen()
        diccArttodo=leerArt()
        diccAlbumtodo=leerAlbum()
        diccPlaylisttodo=leerPlaylist()
        diccCancionestodo=leerCanciones()
        # Configuración de la ventana login
        ventanaLogin = tk.Tk()
        ventanaLogin.title("Login")
        ventanaLogin.geometry("700x200+500+100")
        ventanaLogin.attributes('-topmost', True)  # Mantiene la ventana en la parte superior
        #Para seleccion
        tipoUsuario= ttk.Combobox(ventanaLogin, values=["Administrador", "Usuario"])
        tipoUsuario.current(1)
        tipoUsuario.pack(pady=30)
        #Codigo de usuario
        codigo=tk.Entry(ventanaLogin,font="Arial")
        codigo.pack(pady=10)
        # Botón en la ventana login para ir a menu
        iniciarSesion = tk.Button(ventanaLogin, text="Iniciar sesion", command= lambda:login(tipoUsuario,codigo.get(),diccProptodo,ventanaLogin,VentanaMenu))
        iniciarSesion.pack(pady=20)
        
        
        

        # Configuración de la ventana menu
        VentanaMenu = tk.Toplevel(ventanaLogin)
        VentanaMenu.title("Menu")
        VentanaMenu.withdraw()  # Oculta la ventana secundaria inicialmente
        # Botón en la ventana menu para volver a login
        botonVolverMenuPrincipal = tk.Button(VentanaMenu, text="Volver a login", command=lambda:volverVentana(ventanaLogin,VentanaMenu,obtenerDimenciones(VentanaMenu)))
        botonVolverMenuPrincipal.pack(pady=20)

        ventanaLogin.mainloop()
    
menu()