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
        diccAdmintodo=leerAdmin()
        diccMembresias=leerProp()[1]
        diccGentodo=leerGen()
        diccArttodo=leerArt()
        diccAlbumtodo=leerAlbum()
        diccPlaylisttodo=leerPlaylist()
        diccCancionestodo=leerCanciones()
##########################################################################################################################################################################################
        # Configuración de la ventana login
        ventanaLogin = tk.Tk()
        ventanaLogin.title("Login")
        ventanaLogin.geometry("900x600+170+100")
        ventanaLogin.attributes('-topmost', True)  # Mantiene la ventana en la parte superior
        #Para seleccion
        tipoUsuario= ttk.Combobox(ventanaLogin, values=["Administrador", "Usuario"])
        tipoUsuario.current(1)
        tipoUsuario.pack(pady=30)
        if tipoUsuario=="Administrador":
                bandera=True
        else:
                bandera=False
        #Codigo de usuario
        codigo=tk.Entry(ventanaLogin,font="Arial")
        codigo.pack(pady=10)
        # Botón en la ventana login para ir a menu
        iniciarSesion = tk.Button(ventanaLogin, text="Iniciar sesion", command= lambda:[login(tipoUsuario.get(),codigo.get(),diccProptodo,ventanaRegistro,diccAdmintodo,ventanaLogin,VentanaMenu)])
        iniciarSesion.pack(pady=20)
##########################################################################################################################################################################################
        #Configuracion de ventana de registro
        ventanaRegistro=tk.Toplevel(ventanaLogin)
        ventanaRegistro.title("Registro")
        ventanaRegistro.configure(bg='#E4E4E4')
        ventanaRegistro.withdraw()
        #ventanaRegistro.resizable(0, 0)
        #Grid
        ventanaRegistro.columnconfigure(0, weight=3)
        #Etiqueta de instruccion
        Registarse=tk.Label(ventanaRegistro,text="Registrarse",font=("Arial",25),bg="#C1B2A6")
        Registarse.grid(sticky=tk.N,pady=20)
        #Etiqueta de instruccion
        IngresarCodigo=tk.Label(ventanaRegistro,text="Ingrese su nombre",font=("Arial",16),bg="#C1B2A6")
        IngresarCodigo.grid(sticky=tk.W,padx=35,pady=12)
        #Nombre de usuario
        nombre=tk.Entry(ventanaRegistro,font="Arial")
        nombre.grid(sticky=tk.W,padx=40,pady=56)
        #Etiqueta display
        etiquetaRegistro=tk.Label(ventanaRegistro, text="  ")
        etiquetaRegistro.grid(sticky=tk.W,padx=44,pady=30)
        #Boton de registrar
        
        accionRegistro = tk.Button(ventanaRegistro, text="Registrarse", command=lambda:registar(diccProptodo,diccMembresias,nombre.get(),etiquetaRegistro))
        print(diccMembresias)
        accionRegistro.grid(sticky=tk.W,padx=42,pady=20)
        #Boton de Volver
        botonDeRegistroALogin = tk.Button(ventanaRegistro, text="Volver a menu", command=lambda:navegacionVentanas(ventanaLogin,ventanaRegistro,obtenerDimenciones(ventanaRegistro)))
        botonDeRegistroALogin.grid(sticky=tk.W,padx=46,pady=10)
##########################################################################################################################################################################################       
        # Configuración de la ventana menu
        VentanaMenu = tk.Toplevel(ventanaLogin)
        VentanaMenu.title("Menu")
        VentanaMenu.configure(bg='#E4E4E4')
        VentanaMenu.withdraw()  # Oculta la ventana secundaria inicialmente
        #Creamos menubar
        menubar = tk.Menu(VentanaMenu)
        #Insercion 
        if bandera==True:
                menuinsercion = tk.Menu(menubar,tearoff=0)
                menuinsercion.configure(bg='#C1B2A6')
                menuinsercion.add_command(label="Propietario")
                menuinsercion.add_command(label="Playlist")
                menuinsercion.add_command(label="Genero")
                menuinsercion.add_command(label="Artista")
                menuinsercion.add_command(label="Album")
                menuinsercion.add_command(label="Cancion")
                menubar.add_cascade(label="Insercion", menu=menuinsercion)
        #Buscar
                menubusqueda = tk.Menu(menubar,tearoff=0)
                menubusqueda.configure(bg='#C1B2A6')
                menubusqueda.add_command(label="Propietario")
                menubusqueda.add_command(label="Playlist")
                menubusqueda.add_command(label="Genero")
                menubusqueda.add_command(label="Artista")
                menubusqueda.add_command(label="Album")
                menubusqueda.add_command(label="Cancion")
                menubar.add_cascade(label="Busqueda", menu=menubusqueda)
        else:
                menuinsercion = tk.Menu(menubar,tearoff=0)
                menuinsercion.configure(bg='#C1B2A6')
                menuinsercion.add_command(label="Propietario",background='#A6A6A6')
                menuinsercion.add_command(label="Playlist",background='#A6A6A6')
                menuinsercion.add_command(label="Genero",background='#A6A6A6')
                menuinsercion.add_command(label="Artista",background='#A6A6A6')
                menuinsercion.add_command(label="Album",background='#A6A6A6')
                menuinsercion.add_command(label="Cancion",background='#A6A6A6')
                menubar.add_cascade(label="Insercion", background='#A6A6A6', menu=menuinsercion)

                menubusqueda = tk.Menu(menubar,tearoff=0)
                menubusqueda.configure(bg='#C1B2A6')
                menubusqueda.add_command(label="Propietario")
                menubusqueda.add_command(label="Playlist")
                menubusqueda.add_command(label="Genero")
                menubusqueda.add_command(label="Artista")
                menubusqueda.add_command(label="Album")
                menubusqueda.add_command(label="Cancion")
                menubar.add_cascade(label="Busqueda", menu=menubusqueda)
        VentanaMenu.config(menu=menubar)
        # Botón en la ventana menu para volver a login
        botonCerrarSesion = tk.Button(VentanaMenu, text="Cerrar sesion", command=lambda:navegacionVentanas(ventanaLogin,VentanaMenu,obtenerDimenciones(VentanaMenu)))
        botonCerrarSesion.pack(pady=20)
##########################################################################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaPropietario = tk.Toplevel(ventanaLogin)
        VentanaBusquedaPropietario.title("Busqueda")
        VentanaBusquedaPropietario.configure(bg='#E4E4E4')
        VentanaBusquedaPropietario.withdraw()  # Oculta la ventana secundaria inicialmente
        #Codigo de usuario
        codigoBusqueda=tk.Entry(VentanaBusquedaPropietario,font="Arial")
        codigoBusqueda.pack(pady=10)
        #Etiqueta display
        etiqueta=tk.Label(VentanaBusquedaPropietario, text="")
        etiqueta.pack(pady=20)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaPropietario, text="Buscar", command=lambda:mostrarEnPantalla(etiqueta,buscarProp(codigoBusqueda.get(),diccProptodo)))
        botonDeBusqueda.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaPropietario, text="Volver a menu", command=lambda:navegacionVentanas(VentanaMenu,VentanaBusquedaPropietario,obtenerDimenciones(VentanaMenu)))
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        
        
        


        ventanaLogin.mainloop()

menu()