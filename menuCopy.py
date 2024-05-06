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
        ventanaLogin.geometry("600x600+170+100")
        ventanaLogin.columnconfigure(0,weight=3)
        ventanaLogin.configure(bg='#D5CEC1')
        ventanaLogin.attributes('-topmost', True)  # Mantiene la ventana en la parte superior
        #Para seleccion
        InicioDeSesion=tk.Label(ventanaLogin,text="Inicio de sesión", font=("Sitka Text Semibold",25),bg="#28342C", foreground='#E4E4E4')
        InicioDeSesion.grid(pady=30,sticky=tk.N)
        SeleccioneOpcion=tk.Label(ventanaLogin,text="Seleccione una de las dos opciones:",font=("Sitka Text Semibold",15),bg="#28342C", foreground='#E4E4E4')
        SeleccioneOpcion.grid(sticky=tk.N, pady=50)
        tipoUsuario= ttk.Combobox(ventanaLogin,values=["Administrador", "Usuario"],font=("Times New Roman",15))
        tipoUsuario.current(0)
        tipoUsuario.grid(pady=0,sticky=tk.N)
        #Codigo de usuario
        codigolabel=tk.Label(ventanaLogin,text="Digite su código:",font=("Sitka Text Semibold",15),bg="#28342C", foreground='#E4E4E4')
        codigolabel.grid(pady=50,sticky=tk.N)
        codigo=tk.Entry(ventanaLogin,font=("Times New Roman",15),background='#E4E4E4')
        codigo.grid(pady=0,sticky=tk.N)
        # Botón en la ventana login para ir a menu
        iniciarSesion = tk.Button(ventanaLogin, text="Iniciar sesion", command= lambda:[login(tipoUsuario.get(),codigo.get(),diccProptodo,ventanaPago,ventanaRegistro,diccAdmintodo,ventanaLogin,VentanaMenu)], font=("Times New Roman",15),bg='#102512',fg='#E4E4E4')
        iniciarSesion.grid(pady=20,sticky=tk.N)
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
        accionRegistro = tk.Button(ventanaRegistro, text="Registrarse", command=lambda:[registar(diccProptodo,diccMembresias,nombre.get(),etiquetaRegistro),limpiar_texto(nombre)])
        accionRegistro.grid(sticky=tk.W,padx=42,pady=20)
        #Boton de Volver
        botonDeRegistroALogin = tk.Button(ventanaRegistro, text="Volver a menu", command=lambda:navegacionVentanas(ventanaLogin,ventanaRegistro,obtenerDimenciones(ventanaRegistro)))
        botonDeRegistroALogin.grid(sticky=tk.W,padx=46,pady=10)
##########################################################################################################################################################################################
        #Configuracion de ventana de pago
        ventanaPago=tk.Toplevel(ventanaLogin)
        ventanaPago.title("Pago")
        ventanaPago.configure(bg='#E4E4E4')
        ventanaPago.withdraw()
        #ventanaRegistro.resizable(0, 0)
        #Grid
        ventanaPago.columnconfigure(0, weight=3)
        #Etiqueta de instruccion
        pago=tk.Label(ventanaPago,text="Pago",font=("Arial",25),bg="#C1B2A6")
        pago.grid(sticky=tk.N,pady=20)
        #Etiqueta de instruccion
        #IngresarCodigo=tk.Label(ventanaPago,text="Ingrese su nombre",font=("Arial",16),bg="#C1B2A6")
        #IngresarCodigo.grid(sticky=tk.W,padx=35,pady=12)
        #Nombre de usuario
        numTarjeta=tk.Entry(ventanaPago,font="Arial")
        numTarjeta.grid(sticky=tk.W,padx=40,pady=56)
        fecha=tk.Entry(ventanaPago,font="Arial")
        fecha.grid(sticky=tk.W,padx=40,pady=56)
        codigoSeguridad=tk.Entry(ventanaPago,font="Arial")
        codigoSeguridad.grid(sticky=tk.W,padx=40,pady=56)
        #Etiqueta display
        etiquetaPago=tk.Label(ventanaPago, text="  ")
        etiquetaPago.grid(sticky=tk.W,padx=44,pady=30)
        #Boton de pagar
        accionPagar = tk.Button(ventanaPago, text="Pagar", command=lambda:[pagar(diccProptodo,diccMembresias,codigo.get(),etiquetaPago),limpiar_texto(numTarjeta),limpiar_texto(fecha),limpiar_texto(codigoSeguridad)])
        accionPagar.grid(sticky=tk.W,padx=42,pady=20)
        #Boton de Volver
        botonDeRegistroALogin = tk.Button(ventanaPago, text="Volver a menu", command=lambda:navegacionVentanas(ventanaLogin,ventanaPago,obtenerDimenciones(ventanaRegistro)))
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
        if tipoUsuario.get()=="Administrador":
                bandera=True
        else:
                bandera=False

        if bandera==True:
                menuinsercion = tk.Menu(menubar,tearoff=0)
                menuinsercion.configure(bg='#C1B2A6')
                menuinsercion.add_command(label="Propietario",command=lambda:navegacionVentanas(VentanaInsercionProp,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menuinsercion.add_command(label="Playlist")
                menuinsercion.add_command(label="Genero")
                menuinsercion.add_command(label="Artista")
                menuinsercion.add_command(label="Album")
                menuinsercion.add_command(label="Cancion")
                menubar.add_cascade(label="Insercion", menu=menuinsercion)
                #Buscar
                menubusqueda = tk.Menu(menubar,tearoff=0)
                menubusqueda.configure(bg='#C1B2A6')
                menubusqueda.add_command(label="Propietario",command=lambda:navegacionVentanas(VentanaBusquedaPropietario,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menubusqueda.add_command(label="Playlist",command=lambda:navegacionVentanas(VentanaBusquedaPlaylist,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menubusqueda.add_command(label="Genero",command=lambda:navegacionVentanas(VentanaBusquedaGenero,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menubusqueda.add_command(label="Artista",command=lambda:navegacionVentanas(VentanaBusquedaArtista,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menubusqueda.add_command(label="Album",command=lambda:navegacionVentanas(VentanaBusquedaAlbum,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menubusqueda.add_command(label="Cancion",command=lambda:navegacionVentanas(VentanaBusquedaCancion,VentanaMenu,obtenerDimenciones(VentanaMenu)))
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
        codigoBusquedaProp=tk.Entry(VentanaBusquedaPropietario,font="Arial")
        codigoBusquedaProp.pack(pady=10)
        #Etiqueta display
        etiquetaProp=tk.Label(VentanaBusquedaPropietario, text="")
        etiquetaProp.pack(pady=20)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaPropietario, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaProp,buscarProp(codigoBusquedaProp.get(),diccProptodo)))
        botonDeBusqueda.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaPropietario, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaPropietario,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaProp),mostrarEnPantalla(etiquetaProp,"")])
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaPlaylist= tk.Toplevel(ventanaLogin)
        VentanaBusquedaPlaylist.title("Busqueda")
        VentanaBusquedaPlaylist.configure(bg='#E4E4E4')
        VentanaBusquedaPlaylist.withdraw()  # Oculta la ventana secundaria inicialmente
        #Codigo de usuario
        codigoBusquedaPlaylist=tk.Entry(VentanaBusquedaPlaylist,font="Arial")
        codigoBusquedaPlaylist.pack(pady=10)
        #Etiqueta display
        etiquetaPlaylist=tk.Label(VentanaBusquedaPlaylist, text="")
        etiquetaPlaylist.pack(pady=20)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaPlaylist, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaPlaylist, buscarPlaylist(codigoBusquedaPlaylist.get(),diccPlaylisttodo,diccProptodo)))
        botonDeBusqueda.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaPlaylist, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaPlaylist,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaPlaylist),mostrarEnPantalla(etiquetaPlaylist,"")])
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaGenero= tk.Toplevel(ventanaLogin)
        VentanaBusquedaGenero.title("Busqueda")
        VentanaBusquedaGenero.configure(bg='#E4E4E4')
        VentanaBusquedaGenero.withdraw()  # Oculta la ventana secundaria inicialmente
        #Codigo de usuario
        codigoBusquedaGenero=tk.Entry(VentanaBusquedaGenero,font="Arial")
        codigoBusquedaGenero.pack(pady=10)
        #Etiqueta display
        etiquetaGenero=tk.Label(VentanaBusquedaGenero, text="")
        etiquetaGenero.pack(pady=20)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaGenero, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaGenero, buscarGenero(codigoBusquedaGenero.get(),diccGentodo)))
        botonDeBusqueda.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaGenero, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaGenero,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaGenero),mostrarEnPantalla(etiquetaGenero,"")])
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaArtista= tk.Toplevel(ventanaLogin)
        VentanaBusquedaArtista.title("Busqueda")
        VentanaBusquedaArtista.configure(bg='#E4E4E4')
        VentanaBusquedaArtista.withdraw()  # Oculta la ventana secundaria inicialmente
        #Codigo de usuario
        codigoBusquedaArtista=tk.Entry(VentanaBusquedaArtista,font="Arial")
        codigoBusquedaArtista.pack(pady=10)
        #Etiqueta display
        etiquetaArtista=tk.Label(VentanaBusquedaArtista, text="")
        etiquetaArtista.pack(pady=20)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaArtista, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaArtista, buscarArtista(codigoBusquedaArtista.get(),diccArttodo,diccGentodo)))
        botonDeBusqueda.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaArtista, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaArtista,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaArtista),mostrarEnPantalla(etiquetaArtista,"")])
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaAlbum= tk.Toplevel(ventanaLogin)
        VentanaBusquedaAlbum.title("Busqueda")
        VentanaBusquedaAlbum.configure(bg='#E4E4E4')
        VentanaBusquedaAlbum.withdraw()  # Oculta la ventana secundaria inicialmente
        #Codigo de usuario
        codigoBusquedaAlbum=tk.Entry(VentanaBusquedaAlbum,font="Arial")
        codigoBusquedaAlbum.pack(pady=10)
        #Etiqueta display
        etiquetaAlbum=tk.Label(VentanaBusquedaAlbum, text="")
        etiquetaAlbum.pack(pady=20)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaAlbum, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaAlbum, buscarAlbum(codigoBusquedaAlbum.get(),diccAlbumtodo,diccArttodo)))
        botonDeBusqueda.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaAlbum, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaAlbum,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaAlbum),mostrarEnPantalla(etiquetaAlbum,"")])
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaCancion= tk.Toplevel(ventanaLogin)
        VentanaBusquedaCancion.title("Busqueda")
        VentanaBusquedaCancion.configure(bg='#E4E4E4')
        VentanaBusquedaCancion.withdraw()  # Oculta la ventana secundaria inicialmente
        #Codigo de usuario
        codigoBusquedaCancion=tk.Entry(VentanaBusquedaCancion,font="Arial")
        codigoBusquedaCancion.pack(pady=10)
        #Etiqueta display
        etiquetaCancion=tk.Label(VentanaBusquedaCancion, text="")
        etiquetaCancion.pack(pady=20)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaCancion, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaCancion, buscarCancion(codigoBusquedaCancion.get(),diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)))
        botonDeBusqueda.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaCancion, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaCancion,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaCancion),mostrarEnPantalla(etiquetaCancion,"")])
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaInsercionProp= tk.Toplevel(ventanaLogin)
        VentanaInsercionProp.title("Busqueda")
        VentanaInsercionProp.configure(bg='#E4E4E4')
        VentanaInsercionProp.withdraw()  # Oculta la ventana secundaria inicialmente
        #Codigo de Propietario
        codigoInsericionProp=tk.Entry(VentanaInsercionProp,font="Arial")
        codigoInsericionProp.pack(pady=10)
        #nombre de Prop
        nombreInsercionProp=tk.Entry(VentanaInsercionProp,font="Arial")
        nombreInsercionProp.pack(pady=10)
        #Codigo de membresia
        codigoInsercionMem=tk.Entry(VentanaInsercionProp,font="Arial")
        codigoInsercionMem.pack(pady=10)
        #estado
        estadoInsercionMem=tk.Entry(VentanaInsercionProp,font="Arial")
        estadoInsercionMem.pack(pady=10)
        #Etiqueta display
        etiquetaConfirmacionInsercionProp=tk.Label(VentanaInsercionProp, text="")
        etiquetaConfirmacionInsercionProp.pack(pady=20)
        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionProp, text="Buscar", command=lambda:insertProp(diccProptodo,diccMembresias,codigoInsericionProp,nombreInsercionProp,codigoInsercionMem,estadoInsercionMem,etiquetaConfirmacionInsercionProp))
        botonDeinsercion.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionProp, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionProp,obtenerDimenciones(VentanaMenu)),limpiar_texto(nombreInsercionProp),limpiar_texto(codigoInsercionMem),limpiar_texto(estadoInsercionMem),limpiar_texto(codigoInsericionProp),mostrarEnPantalla(etiquetaConfirmacionInsercionProp,"")])
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaInsercionPlaylist= tk.Toplevel(ventanaLogin)
        VentanaInsercionPlaylist.title("Busqueda")
        VentanaInsercionPlaylist.configure(bg='#E4E4E4')
        VentanaInsercionPlaylist.withdraw()  # Oculta la ventana secundaria inicialmente
        #Codigo de Playlist
        codigoInsericionPlaylist=tk.Entry(VentanaInsercionPlaylist,font="Arial")
        codigoInsericionPlaylist.pack(pady=10)
        #Nombre de Playlist
        nombreInsercionPlaylist=tk.Entry(VentanaInsercionPlaylist,font="Arial")
        nombreInsercionPlaylist.pack(pady=10)
        #Codigo Prop
        codigoPropInsercionPlaylist=tk.Entry(VentanaInsercionPlaylist,font="Arial")
        codigoPropInsercionPlaylist.pack(pady=10)
        #Etiqueta display
        etiquetaConfirmacionInsercionPlaylist=tk.Label(VentanaInsercionPlaylist, text="")
        etiquetaConfirmacionInsercionPlaylist.pack(pady=20)
        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionPlaylist, text="Buscar", command=lambda:insertPlaylist(diccPlaylisttodo,diccProptodo,codigoInsericionPlaylist,nombreInsercionPlaylist,codigoPropInsercionPlaylist))
        botonDeinsercion.pack(pady=20)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionPlaylist, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionPlaylist,obtenerDimenciones(VentanaMenu)),limpiar_texto(nombreInsercionPlaylist),limpiar_texto(codigoInsericionPlaylist),limpiar_texto(codigoPropInsercionPlaylist),mostrarEnPantalla(etiquetaConfirmacionInsercionPlaylist,"")])
        botonDeBusquedaAMenu.pack(pady=20)
##############################################################################################################################################
        
        
        


        ventanaLogin.mainloop()

menu()