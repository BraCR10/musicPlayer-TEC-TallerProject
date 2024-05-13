#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from lecturaArchivos import *#leerAlbum,leerArt,leerCanciones,leerGen,leerPlaylist,leerProp
from insercion import *#insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp
from busqueda import * #buscarAlbum,buscarArtista,buscarCancion,buscarGenero,buscarPlaylist,buscarProp
import tkinter as tk
from tkinter import ttk
from acciones import * 
from modificacion import *#ModificarPlaylist,modificarArt,modificarCancion,modificarGen,modificarProp
from eliminacion import *#eliminarProp,eliminarCanciones,eliminarPlaylist,eliminarAlbum,eliminarGenero,eliminarArtistas
from reproducir import *
diccProptodo=leerProp()[0]#Devuelve una lista con membresias
diccAdmintodo=leerAdmin()
diccMembresias=leerProp()[1]
diccGentodo=leerGen()
diccArttodo=leerArt()
diccAlbumtodo=leerAlbum()
diccPlaylisttodo=leerPlaylist()
diccCancionestodo=leerCanciones()
ColasDeReproduccion={}#Cada propietarion tiene su propia cola
######################################################################################################################################
ventanaLogin = tk.Tk()
VentanaMenu = tk.Toplevel(ventanaLogin)
VentanaMenu.withdraw()  # Oculta la ventana secundaria inicialmente
verificadorElementosMenu=False
GenerosBoton=tk.Button()
ArtistasBoton=tk.Button()
#######################################################################################################################################################################################
def login(tipoUsuario,codigo,diccProptodo,ventanaPago,ventanaRegistro,diccAdminTodo,ventanaLogin,VentanaMenu):
    if  tipoUsuario=='Usuario' and codigo not in list(diccProptodo.keys()) :
        return navegacionVentanas(ventanaRegistro,ventanaLogin,obtenerDimenciones(ventanaLogin))
    elif  tipoUsuario=='Usuario' and codigo in list(diccProptodo.keys()) and diccProptodo[codigo]['estado'][0]=='0':
        return navegacionVentanas(ventanaPago,ventanaLogin,obtenerDimenciones(ventanaLogin))
    elif  tipoUsuario=='Usuario'and codigo in list(diccProptodo.keys()) and diccProptodo[codigo]['estado'][0]=='1':
        menu(tipoUsuario,codigo)
        return navegacionVentanas(VentanaMenu,ventanaLogin,obtenerDimenciones(ventanaLogin))
    elif  tipoUsuario=='Administrador' and codigo in list(diccAdminTodo.keys()):
        menu(tipoUsuario,codigo)
        return navegacionVentanas(VentanaMenu,ventanaLogin,obtenerDimenciones(ventanaLogin))
    elif tipoUsuario=='Administrador' and codigo not in list(diccAdminTodo.keys()):
        messagebox.showinfo("Alerta", "El codigo no pertenece a ningun administrador")
    
#######################################################################################################################################################################################
def loginVentana():
        ##########################################################################################################################################################################################
        # Configuración de la ventana login
        ventanaLogin.title("Login")
        ventanaLogin.geometry(f"{ventanaLogin.winfo_screenwidth()}x{ventanaLogin.winfo_screenheight()}")
        ventanaLogin.columnconfigure(0,weight=3)
        ventanaLogin.configure(bg='#D5CEC1')
        ventanaLogin.attributes('-topmost', True)  # Mantiene la ventana en la parte superior
        #Para seleccion
        InicioDeSesion=tk.Label(ventanaLogin,text="Inicio de sesión", font=("Sitka Text Semibold",25),bg="#28342C", foreground='#E4E4E4')
        InicioDeSesion.grid(pady=30,sticky=tk.N)
        SeleccioneOpcion=tk.Label(ventanaLogin,text="Seleccione una de las dos opciones:",font=("Sitka Text Semibold",15),bg="#28342C", foreground='#E4E4E4')
        SeleccioneOpcion.grid(sticky=tk.N, pady=50)
        tipoUsuario= ttk.Combobox(ventanaLogin,values=["Administrador", "Usuario"],font=("Times New Roman",15))
        tipoUsuario.current(1)
        tipoUsuario.grid(pady=0,sticky=tk.N)
        #Codigo de usuario
        codigolabel=tk.Label(ventanaLogin,text="Digite su código de propietario o administrador:",font=("Sitka Text Semibold",15),bg="#28342C", foreground='#E4E4E4')
        codigolabel.grid(pady=50,sticky=tk.N)
        codigo=tk.Entry(ventanaLogin,font=("Times New Roman",15),background='#E4E4E4')
        codigo.grid(pady=0,sticky=tk.N)
        # Botón en la ventana login para ir a menu
        iniciarSesion = tk.Button(ventanaLogin, text="Iniciar sesion", command= lambda:[login(tipoUsuario.get(),codigo.get(),diccProptodo,ventanaPago,ventanaRegistro,diccAdmintodo,ventanaLogin,VentanaMenu)], font=("Times New Roman",15),bg='#102512',fg='#E4E4E4')
        iniciarSesion.grid(pady=20,sticky=tk.N)
        confg=tk.Label(ventanaLogin,text="Digite su código:",bg="#D5CEC1", foreground='#D5CEC1')
        confg.grid(pady=60,sticky=tk.N)
        ##########################################################################################################################################################################################
        #Configuracion de ventana de registro
        ventanaRegistro=tk.Toplevel(ventanaLogin)
        ventanaRegistro.title("Registro")
        ventanaRegistro.configure(bg='#28342C')
        ventanaRegistro.withdraw()
        #ventanaRegistro.resizable(0, 0)
        #Grid
        ventanaRegistro.columnconfigure(0, weight=3)
        #Etiqueta de instruccion
        Registarse=tk.Label(ventanaRegistro,text="Registrarse",font=("Sitka Text Semibold",25),bg="#E4E4E4",foreground='#28342C')
        Registarse.grid(sticky=tk.N,pady=30)
        #Etiqueta de instruccion
        IngresarCodigo=tk.Label(ventanaRegistro,text="Ingrese su nombre:",font=("Sitka Text Semibold",15),bg="#E4E4E4",foreground='#28342C')
        IngresarCodigo.grid(sticky=tk.N,pady=35)
        #Nombre de usuario
        nombre=tk.Entry(ventanaRegistro,font=("Times New Roman",15),background='#E4E4E4')
        nombre.grid(sticky=tk.N,pady=0)
        #Etiqueta display
        etiquetaRegistro=tk.Label(ventanaRegistro, text="  ",font=("Times New Roman",15),background='#28342C',fg="#E4E4E4")
        etiquetaRegistro.grid(sticky=tk.N,pady=25)
        #Boton de registrar
        accionRegistro = tk.Button(ventanaRegistro, text="Registrarse", command=lambda:[registar(diccProptodo,diccMembresias,nombre.get(),etiquetaRegistro),limpiar_texto(nombre)],font=("Times New Roman",15),background='#C1B2A6',fg="#102512")
        accionRegistro.grid(sticky=tk.N,pady=10)
        #Boton de Volver
        botonDeRegistroALogin = tk.Button(ventanaRegistro, text="Volver a menu", command=lambda:[navegacionVentanas(ventanaLogin,ventanaRegistro,obtenerDimenciones(ventanaRegistro)),mostrarEnPantalla(etiquetaRegistro,"")],font=("Times New Roman",15),background='#C1B2A6',fg="#102512")
        botonDeRegistroALogin.grid(sticky=tk.N,pady=30)
        ##########################################################################################################################################################################################
        #Configuracion de ventana de pago
        ventanaPago=tk.Toplevel(ventanaLogin)
        ventanaPago.title("Pago")
        ventanaPago.configure(bg='#D5CEC1')
        ventanaPago.withdraw()
        #ventanaRegistro.resizable(0, 0)
        #Grid
        ventanaPago.columnconfigure(0, weight=3)
        #Etiqueta de instruccion
        pago=tk.Label(ventanaPago,text="Pago",font=("Sitka Text Semibold",25),bg="#28342C",fg="#E4E4E4")
        pago.grid(sticky=tk.N,pady=20)
        #Nombre de usuario
        NumTrabLabel1=tk.Label(ventanaPago,text="Digite su numero de tarjeta:",font=("Sitka Text Semibold",15),bg="#28342C",fg="#E4E4E4")
        NumTrabLabel1.grid(sticky=tk.N,pady=15)
        numTarjeta=tk.Entry(ventanaPago,font=("Times New Roman",15),background='#E4E4E4')
        numTarjeta.grid(sticky=tk.N,pady=0)
        NumTrabLabel2=tk.Label(ventanaPago,text="Digite la fecha de expiración:",font=("Sitka Text Semibold",15),bg="#28342C",fg="#E4E4E4")
        NumTrabLabel2.grid(sticky=tk.N,pady=15)
        fecha=tk.Entry(ventanaPago,font=("Times New Roman",15),background='#E4E4E4')
        fecha.grid(sticky=tk.N,pady=0)
        NumTrabLabel3=tk.Label(ventanaPago,text="Digite su pin:",font=("Sitka Text Semibold",15),bg="#28342C",fg="#E4E4E4")
        NumTrabLabel3.grid(sticky=tk.N,pady=15)
        codigoSeguridad=tk.Entry(ventanaPago,font=("Times New Roman",15),background='#E4E4E4')
        codigoSeguridad.grid(sticky=tk.N,pady=0)
        #Etiqueta display
        etiquetaPago=tk.Label(ventanaPago, text="  ",bg='#D5CEC1',fg='#28342C',font=("Times New Roman",15))
        etiquetaPago.grid(sticky=tk.N,pady=20)
        #Boton de ver factura
        verFactura = tk.Button(ventanaPago, text="Ver Facturas", command=lambda:[mostrarFactura(diccProptodo,codigo.get())],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
        verFactura.grid(sticky=tk.N,pady=15)
        #Boton de pagar
        accionPagar = tk.Button(ventanaPago, text="Pagar", command=lambda:[pagar(diccProptodo,diccMembresias,codigo.get(),etiquetaPago),limpiar_texto(numTarjeta),limpiar_texto(fecha),limpiar_texto(codigoSeguridad)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
        accionPagar.grid(sticky=tk.N,pady=15)
        #Boton de Volver
        botonDeRegistroALogin = tk.Button(ventanaPago, text="Volver a menu", command=lambda:navegacionVentanas(ventanaLogin,ventanaPago,obtenerDimenciones(ventanaPago)),font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
        botonDeRegistroALogin.grid(sticky=tk.N,pady=15)
        ventanaLogin.mainloop()
def menu(tipoUsuario,codigoUsuario):
        ##########################################################################################################################################################################################       
        #Proceso para dar bienvenida
        global verificadorElementosMenu
        global etiquetaBienvenida
        global botonCerrarSesion
        global MusicaBoton
        global UsuariosBoton
        global ReproductorBoton
        global AlbumBoton
        global PagoBoton
        if verificadorElementosMenu==True:
                etiquetaBienvenida.destroy()
                botonCerrarSesion.destroy()
                MusicaBoton.destroy()
                UsuariosBoton.destroy()
                ReproductorBoton.destroy()
                AlbumBoton.destroy()
                PagoBoton.destroy()
                verificadorElementosMenu=False
        if not verificadorElementosMenu:
                if  tipoUsuario=="Usuario":
                        etiquetaBienvenida=tk.Label(VentanaMenu, text=f"Bienvenid@ {buscarProp(codigoUsuario,diccProptodo)}!",font=("Times New Roman",15),background='#D5CEC1')
                else:
                        etiquetaBienvenida=tk.Label(VentanaMenu, text=f"Bienvenid@ {buscarAdministrador(codigoUsuario,diccAdmintodo)}!",font=("Times New Roman",15),background='#D5CEC1')
                #Bienvenida
                etiquetaBienvenida.pack(pady=10)
                verificadorElementosMenu=True  
        
        # Configuración de la ventana menu
        VentanaMenu.title("Menu")
        VentanaMenu.configure(bg='#D5CeC1')

        #Creamos menubar
        menubar = tk.Menu(VentanaMenu)
        #PopUp globales para usuarios y admins
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

        if tipoUsuario=="Administrador":
                #Busqueda
                menubusqueda.add_command(label="Administrador",command=lambda:navegacionVentanas(VentanaBusquedaAdm,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                #Insertar
                menuinsercion = tk.Menu(menubar,tearoff=0)
                menuinsercion.configure(bg='#C1B2A6')
                menuinsercion.add_command(label="Propietario",command=lambda:navegacionVentanas(VentanaInsercionProp,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menuinsercion.add_command(label="Playlist",command=lambda:navegacionVentanas(VentanaInsercionPlaylist,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menuinsercion.add_command(label="Genero",command=lambda:navegacionVentanas(VentanaInsercionGen,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menuinsercion.add_command(label="Artista",command=lambda:navegacionVentanas(VentanaInsercionArtista,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menuinsercion.add_command(label="Album",command=lambda:navegacionVentanas(VentanaInsercionAlbum,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menuinsercion.add_command(label="Cancion",command=lambda:navegacionVentanas(VentanaInsercionCancion,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menuinsercion.add_command(label="Administrador",command=lambda:navegacionVentanas(VentanaInsercionAdm,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menubar.add_cascade(label="Insercion", menu=menuinsercion)
                #Eliminacion
                menueliminacion = tk.Menu(menubar,tearoff=0)
                menueliminacion.configure(bg='#C1B2A6')
                menueliminacion.add_command(label="Propietario",command=lambda:navegacionVentanas(VentanaEliminacionProp,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menueliminacion.add_command(label="Playlist",command=lambda:navegacionVentanas(VentanaEliminacionPlaylist,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menueliminacion.add_command(label="Genero",command=lambda:navegacionVentanas(VentanaEliminacionGen,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menueliminacion.add_command(label="Artista",command=lambda:navegacionVentanas(VentanaEliminacionCancion,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menueliminacion.add_command(label="Album",command=lambda:navegacionVentanas(VentanaEliminacionAlb,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menueliminacion.add_command(label="Cancion",command=lambda:navegacionVentanas(VentanaEliminacionCancion,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menueliminacion.add_command(label="Administrador",command=lambda:navegacionVentanas(VentanaEliminacionAdm,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menubar.add_cascade(label="Eliminación", menu=menueliminacion)
                #Modificacion
                menumodificacion = tk.Menu(menubar,tearoff=0)
                menumodificacion.configure(bg='#C1B2A6')
                menumodificacion.add_command(label="Propietario",command=lambda:navegacionVentanas(VentanaModificacionProp,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menumodificacion.add_command(label="Playlist",command=lambda:navegacionVentanas(VentanaModificacionPlaylist,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menumodificacion.add_command(label="Genero",command=lambda:navegacionVentanas(VentanaModificacionGen,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menumodificacion.add_command(label="Artista",command=lambda:navegacionVentanas(VentanaModificacionArt,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menumodificacion.add_command(label="Album",command=lambda:navegacionVentanas(VentanaModificacionAlb,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menumodificacion.add_command(label="Cancion",command=lambda:navegacionVentanas(VentanaModificacionCancion,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menumodificacion.add_command(label="Administrador",command=lambda:navegacionVentanas(VentanaModificacionAdm,VentanaMenu,obtenerDimenciones(VentanaMenu)))
                menubar.add_cascade(label="Modificación", menu=menumodificacion)
        elif tipoUsuario=="Usuario":
                #Busqueda
                menubusqueda.add_command(label="Administrador",foreground='#E4E4E4')
                #Insercion
                menuinsercion = tk.Menu(menubar,tearoff=0)
                menuinsercion.configure(bg='#C1B2A6')
                menuinsercion.add_command(label="Propietario",foreground='#E4E4E4')
                menuinsercion.add_command(label="Playlist",foreground='#E4E4E4')
                menuinsercion.add_command(label="Genero",foreground='#E4E4E4')
                menuinsercion.add_command(label="Artista",foreground='#E4E4E4')
                menuinsercion.add_command(label="Album",foreground='#E4E4E4')
                menuinsercion.add_command(label="Cancion",foreground='#E4E4E4')
                menuinsercion.add_command(label="Administrador",foreground='#E4E4E4')
                menubar.add_cascade(label="Insercion", background='#A6A6A6', menu=menuinsercion)
                #Eliminacion
                menueliminacion = tk.Menu(menubar,tearoff=0)
                menueliminacion.configure(bg='#C1B2A6')
                menueliminacion.add_command(label="Propietario",foreground='#E4E4E4')
                menueliminacion.add_command(label="Playlist",foreground='#E4E4E4')
                menueliminacion.add_command(label="Genero",foreground='#E4E4E4')
                menueliminacion.add_command(label="Artista",foreground='#E4E4E4')
                menueliminacion.add_command(label="Album",foreground='#E4E4E4')
                menueliminacion.add_command(label="Cancion",foreground='#E4E4E4')
                menueliminacion.add_command(label="Administrador",foreground='#E4E4E4')
                menubar.add_cascade(label="Eliminación", background='#A6A6A6', menu=menueliminacion)
                #Modificacion
                menumodificacion = tk.Menu(menubar,tearoff=0)
                menumodificacion.configure(bg='#C1B2A6')
                menumodificacion.add_command(label="Propietario",foreground='#E4E4E4')
                menumodificacion.add_command(label="Playlist",foreground='#E4E4E4')
                menumodificacion.add_command(label="Genero",foreground='#E4E4E4')
                menumodificacion.add_command(label="Artista",foreground='#E4E4E4')
                menumodificacion.add_command(label="Album",foreground='#E4E4E4')
                menumodificacion.add_command(label="Cancion",foreground='#E4E4E4')
                menumodificacion.add_command(label="Administrador",foreground='#E4E4E4')
                menubar.add_cascade(label="Modificación", background='#A6A6A6', menu=menumodificacion)
        VentanaMenu.config(menu=menubar)
        #Creamos imagenes
        Musicapng = tk.PhotoImage(file='./Musica.png')
        VentanaMenu.Musicapng = tk.PhotoImage(file='./Musica.png')
        MusicaBoton = tk.Button(VentanaMenu, image=VentanaMenu.Musicapng,command=lambda:BotonesMusica(VentanaMenu))
        MusicaBoton.configure(width=190, height=190)
        MusicaBoton.pack(side="left",pady=1,padx=50)
        
        Usuariospng = tk.PhotoImage(file='./Usuarios.png')
        VentanaMenu.Usuariospng = tk.PhotoImage(file='./Usuarios.png')
        UsuariosBoton = tk.Button(VentanaMenu, image=VentanaMenu.Usuariospng,command=lambda:BotonesUsuarios(VentanaMenu))
        UsuariosBoton.configure(width=190, height=190)
        UsuariosBoton.pack(side='right',padx=50)
        
        Reproductorpng = tk.PhotoImage(file='./Reproductor.png')
        VentanaMenu.Reproductorpng = tk.PhotoImage(file='./Reproductor.png')
        ReproductorBoton = tk.Button(VentanaMenu, image=VentanaMenu.Reproductorpng,command=lambda:reproductor(diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo,codigoUsuario,ColasDeReproduccion,diccProptodo))
        ReproductorBoton.configure(width=190, height=190)
        ReproductorBoton.pack(pady=15)
        
        Albumpng = tk.PhotoImage(file='./Album.png')
        VentanaMenu.Albumpng = tk.PhotoImage(file='./Album.png')
        AlbumBoton = tk.Button(VentanaMenu, image=VentanaMenu.Albumpng,command=lambda:BotonesAlbumes(VentanaMenu))
        AlbumBoton.configure(width=190, height=190)
        AlbumBoton.pack(side='left',padx=50)
        
        pagospng = tk.PhotoImage(file='./Pagos.png')
        VentanaMenu.pagospng = tk.PhotoImage(file='./Pagos.png')
        PagoBoton = tk.Button(VentanaMenu, image=VentanaMenu.pagospng)
        PagoBoton.configure(width=190, height=190)
        PagoBoton.pack(side="right",padx=50)    
        
        # Botón en la ventana menu para volver a login
        botonCerrarSesion = tk.Button(VentanaMenu, text="Cerrar sesion", command=lambda:navegacionVentanas(ventanaLogin,VentanaMenu,obtenerDimenciones(VentanaMenu)),font=("Times New Roman",15),background='#28342C',fg='#E4E4E4')
        botonCerrarSesion.pack(pady=100)
        ##########################################################################################################################################################################################
# Configuración de la ventana de busquedas
        VentanaBusquedaPropietario = tk.Toplevel(ventanaLogin)
        VentanaBusquedaPropietario.title("Busqueda")
        VentanaBusquedaPropietario.configure(bg='#D5CEC1')
        VentanaBusquedaPropietario.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaBusquedaPropietario.columnconfigure(0,weight=3)
        #Codigo de usuario
        TituloBusProp=tk.Label(VentanaBusquedaPropietario,text='Busqueda de proprietario', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloBusProp.grid(sticky=tk.N,pady=10)
        DigitecodProp=tk.Label(VentanaBusquedaPropietario,text='Digite el codigo de propietario:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodProp.grid(sticky=tk.N,pady=10)
        codigoBusquedaProp=tk.Entry(VentanaBusquedaPropietario,font=("Times New Roman",15),background='#E4E4E4')
        codigoBusquedaProp.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaProp=tk.Label(VentanaBusquedaPropietario, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaProp.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaPropietario, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaProp,buscarProp(codigoBusquedaProp.get(),diccProptodo)),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusqueda.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaPropietario, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaPropietario,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaProp),mostrarEnPantalla(etiquetaProp,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaPlaylist= tk.Toplevel(ventanaLogin)
        VentanaBusquedaPlaylist.title("Busqueda")
        VentanaBusquedaPlaylist.configure(bg='#D5CEC1')
        VentanaBusquedaPlaylist.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaBusquedaPlaylist.columnconfigure(0,weight=3)

        TituloBusPlaylist=tk.Label(VentanaBusquedaPlaylist,text='Busqueda de playlist', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloBusPlaylist.grid(sticky=tk.N,pady=10)
        DigitecodPlay=tk.Label(VentanaBusquedaPlaylist,text='Digite el codigo de playlist:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodPlay.grid(sticky=tk.N,pady=10)
        #Codigo de usuario
        codigoBusquedaPlaylist=tk.Entry(VentanaBusquedaPlaylist,font=("Times New Roman",15),background='#E4E4E4')
        codigoBusquedaPlaylist.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaPlaylist=tk.Label(VentanaBusquedaPlaylist, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaPlaylist.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaPlaylist, text="Buscar", command=lambda:mostrarEnPantallaBusqueda(etiquetaPlaylist, buscarPlaylist(codigoBusquedaPlaylist.get(),diccPlaylisttodo,diccProptodo)),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusqueda.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaPlaylist, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaPlaylist,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaPlaylist),mostrarEnPantalla(etiquetaPlaylist,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaGenero= tk.Toplevel(ventanaLogin)
        VentanaBusquedaGenero.title("Busqueda")
        VentanaBusquedaGenero.configure(bg='#D5CEC1')
        VentanaBusquedaGenero.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaBusquedaGenero.columnconfigure(0,weight=3)

        TituloBusGen=tk.Label(VentanaBusquedaGenero,text='Busqueda de genero', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloBusGen.grid(sticky=tk.N,pady=10)
        DigitecodGen=tk.Label(VentanaBusquedaGenero,text='Digite el codigo de genero:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodGen.grid(sticky=tk.N,pady=10)

        #Codigo de usuario
        codigoBusquedaGenero=tk.Entry(VentanaBusquedaGenero,font=("Times New Roman",15),background='#E4E4E4')
        codigoBusquedaGenero.grid(sticky=tk.N,pady=10)
        
        #Etiqueta display
        etiquetaGenero=tk.Label(VentanaBusquedaGenero, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaGenero.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaGenero, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaGenero, buscarGenero(codigoBusquedaGenero.get(),diccGentodo)),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusqueda.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaGenero, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaGenero,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaGenero),mostrarEnPantalla(etiquetaGenero,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
##############################################################################################################################################
# Configuración de la ventana de busquedas
        VentanaBusquedaAdm= tk.Toplevel(ventanaLogin)
        VentanaBusquedaAdm.title("Busqueda")
        VentanaBusquedaAdm.configure(bg='#D5CEC1')
        VentanaBusquedaAdm.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaBusquedaAdm.columnconfigure(0,weight=3)

        TituloBusAdm=tk.Label(VentanaBusquedaAdm,text='Busqueda de administrador', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloBusAdm.grid(sticky=tk.N,pady=10)
        DigitecodAdm=tk.Label(VentanaBusquedaAdm,text='Digite el codigo de administrador:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodAdm.grid(sticky=tk.N,pady=10)

        #Codigo de usuario
        codigoBusquedaAdm=tk.Entry(VentanaBusquedaAdm,font=("Times New Roman",15),background='#E4E4E4')
        codigoBusquedaAdm.grid(sticky=tk.N,pady=10)
        
        #Etiqueta display
        etiquetaAdm=tk.Label(VentanaBusquedaAdm, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaAdm.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaAdm, text="Buscar", command=lambda:mostrarEnPantalla(etiquetaAdm, buscarGenero(codigoBusquedaAdm.get(),diccAdmintodo)),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusqueda.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaAdm, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaAdm,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaAdm),mostrarEnPantalla(etiquetaAdm,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaArtista= tk.Toplevel(ventanaLogin)
        VentanaBusquedaArtista.title("Busqueda")
        VentanaBusquedaArtista.configure(bg='#D5CEC1')
        VentanaBusquedaArtista.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaBusquedaArtista.columnconfigure(0,weight=3)

        TituloBusArt=tk.Label(VentanaBusquedaArtista,text='Busqueda de artista', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloBusArt.grid(sticky=tk.N,pady=10)
        DigitecodArt=tk.Label(VentanaBusquedaArtista,text='Digite el codigo del artista:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodArt.grid(sticky=tk.N,pady=10)
        #Codigo de usuario
        codigoBusquedaArtista=tk.Entry(VentanaBusquedaArtista,font=("Times New Roman",15),background='#E4E4E4')
        codigoBusquedaArtista.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaArtista=tk.Label(VentanaBusquedaArtista, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaArtista.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaArtista, text="Buscar", command=lambda:mostrarEnPantallaBusqueda(etiquetaArtista, buscarArtista(codigoBusquedaArtista.get(),diccArttodo,diccGentodo)),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusqueda.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaArtista, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaArtista,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaArtista),mostrarEnPantalla(etiquetaArtista,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaAlbum= tk.Toplevel(ventanaLogin)
        VentanaBusquedaAlbum.title("Busqueda")
        VentanaBusquedaAlbum.configure(bg='#D5CEC1')
        VentanaBusquedaAlbum.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaBusquedaAlbum.columnconfigure(0,weight=3)

        TituloBusAlb=tk.Label(VentanaBusquedaAlbum,text='Busqueda de album', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloBusAlb.grid(sticky=tk.N,pady=10)
        DigitecodAlb=tk.Label(VentanaBusquedaAlbum,text='Digite el codigo del album:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodAlb.grid(sticky=tk.N,pady=10)
        #Codigo de usuario
        codigoBusquedaAlbum=tk.Entry(VentanaBusquedaAlbum,font=("Times New Roman",15),background='#E4E4E4')
        codigoBusquedaAlbum.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaAlbum=tk.Label(VentanaBusquedaAlbum, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaAlbum.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaAlbum, text="Buscar", command=lambda:mostrarEnPantallaBusqueda(etiquetaAlbum, buscarAlbum(codigoBusquedaAlbum.get(),diccAlbumtodo,diccArttodo)),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusqueda.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaAlbum, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaAlbum,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaAlbum),mostrarEnPantalla(etiquetaAlbum,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
##############################################################################################################################################
        # Configuración de la ventana de busquedas
        VentanaBusquedaCancion= tk.Toplevel(ventanaLogin)
        VentanaBusquedaCancion.title("Busqueda")
        VentanaBusquedaCancion.configure(bg='#D5CEC1')
        VentanaBusquedaCancion.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaBusquedaCancion.columnconfigure(0,weight=3)

        TituloBusCan=tk.Label(VentanaBusquedaCancion,text='Busqueda de canción', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloBusCan.grid(sticky=tk.N,pady=10)
        DigitecodCan=tk.Label(VentanaBusquedaCancion,text='Digite el codigo de la canción:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodCan.grid(sticky=tk.N,pady=10)
        #Codigo de usuario
        codigoBusquedaCancion=tk.Entry(VentanaBusquedaCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoBusquedaCancion.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaCancion=tk.Label(VentanaBusquedaCancion, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaCancion.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeBusqueda= tk.Button(VentanaBusquedaCancion, text="Buscar", command=lambda:mostrarEnPantallaBusqueda(etiquetaCancion, buscarCancion(codigoBusquedaCancion.get(),diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusqueda.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaBusquedaCancion, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaBusquedaCancion,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoBusquedaCancion),mostrarEnPantalla(etiquetaCancion,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
                # Configuración de la ventana de insercion
        VentanaInsercionProp= tk.Toplevel(ventanaLogin)
        VentanaInsercionProp.title("Insercion")
        VentanaInsercionProp.configure(bg='#D5CEC1')
        VentanaInsercionProp.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaInsercionProp.columnconfigure(0,weight=3)

        TituloInsProp=tk.Label(VentanaInsercionProp,text='Inserción de propietario', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloInsProp.grid(sticky=tk.N,pady=10)
        DigiteProp1=tk.Label(VentanaInsercionProp,text='Digite el código del propietario:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteProp1.grid(sticky=tk.N,pady=10)
        #Codigo de Propietario
        codigoInsericionProp=tk.Entry(VentanaInsercionProp,font=("Times New Roman",15),background='#E4E4E4')
        codigoInsericionProp.grid(sticky=tk.N,pady=10)

        DigiteNomProp1=tk.Label(VentanaInsercionProp,text='Digite el nombre del propietario:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomProp1.grid(sticky=tk.N,pady=10)
        #nombre de Prop
        nombreInsercionProp=tk.Entry(VentanaInsercionProp,font=("Times New Roman",15),background='#E4E4E4')
        nombreInsercionProp.grid(sticky=tk.N,pady=10)

        DigiteMem1=tk.Label(VentanaInsercionProp,text='Digite el código de memebresia del propietario:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteMem1.grid(sticky=tk.N,pady=10)
        #Codigo de membresia
        codigoInsercionMem=tk.Entry(VentanaInsercionProp,font=("Times New Roman",15),background='#E4E4E4')
        codigoInsercionMem.grid(sticky=tk.N,pady=10)

        DigiteEstMem1=tk.Label(VentanaInsercionProp,text='Digite el estado de la membresia:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteEstMem1.grid(sticky=tk.N,pady=10)
        #estado
        estadoInsercionMem=tk.Entry(VentanaInsercionProp,font=("Times New Roman",15),background='#E4E4E4')
        estadoInsercionMem.grid(sticky=tk.N,pady=10)

        #Etiqueta display
        etiquetaConfirmacionInsercionProp=tk.Label(VentanaInsercionProp, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionInsercionProp.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionProp, text="Insertar", command=lambda:insertProp(diccProptodo,diccMembresias,codigoInsericionProp,nombreInsercionProp,codigoInsercionMem,estadoInsercionMem,etiquetaConfirmacionInsercionProp),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeinsercion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionProp, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionProp,obtenerDimenciones(VentanaMenu)),limpiar_texto(nombreInsercionProp),limpiar_texto(codigoInsercionMem),limpiar_texto(estadoInsercionMem),limpiar_texto(codigoInsericionProp),mostrarEnPantalla(etiquetaConfirmacionInsercionProp,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de insercion
        VentanaInsercionPlaylist= tk.Toplevel(ventanaLogin)
        VentanaInsercionPlaylist.title("Insercion")
        VentanaInsercionPlaylist.configure(bg='#D5CEC1')
        VentanaInsercionPlaylist.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaInsercionPlaylist.columnconfigure(0,weight=3)

        TituloInsPlay=tk.Label(VentanaInsercionPlaylist,text='Inserción de playlist', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloInsPlay.grid(sticky=tk.N,pady=10)
        DigiteProp1=tk.Label(VentanaInsercionPlaylist,text='Digite el código de la playlist:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteProp1.grid(sticky=tk.N,pady=10)
        #Codigo de Playlist
        codigoInsericionPlaylist=tk.Entry(VentanaInsercionPlaylist,font=("Times New Roman",15),background='#E4E4E4')
        codigoInsericionPlaylist.grid(sticky=tk.N,pady=10)

        DigiteNomPlay1=tk.Label(VentanaInsercionPlaylist,text='Digite el nombre de la playlist:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomPlay1.grid(sticky=tk.N,pady=10)
        #Nombre de Playlist
        nombreInsercionPlaylist=tk.Entry(VentanaInsercionPlaylist,font=("Times New Roman",15),background='#E4E4E4')
        nombreInsercionPlaylist.grid(sticky=tk.N,pady=10)

        DigiteProp2=tk.Label(VentanaInsercionPlaylist,text='Digite el código del propietario de la playlist:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteProp2.grid(sticky=tk.N,pady=10)
        #Codigo Prop
        codigoPropInsercionPlaylist=tk.Entry(VentanaInsercionPlaylist,font=("Times New Roman",15),background='#E4E4E4')
        codigoPropInsercionPlaylist.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionInsercionPlaylist=tk.Label(VentanaInsercionPlaylist, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionInsercionPlaylist.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionPlaylist, text="Insertar", command=lambda:insertPlaylist(diccPlaylisttodo,diccProptodo,codigoInsericionPlaylist,nombreInsercionPlaylist,codigoPropInsercionPlaylist,etiquetaConfirmacionInsercionPlaylist),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeinsercion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionPlaylist, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionPlaylist,obtenerDimenciones(VentanaMenu)),limpiar_texto(nombreInsercionPlaylist),limpiar_texto(codigoInsericionPlaylist),limpiar_texto(codigoPropInsercionPlaylist),mostrarEnPantalla(etiquetaConfirmacionInsercionPlaylist,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de insercion
        VentanaInsercionGen= tk.Toplevel(ventanaLogin)
        VentanaInsercionGen.title("Insercion")
        VentanaInsercionGen.configure(bg='#D5CEC1')
        VentanaInsercionGen.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaInsercionPlaylist.columnconfigure(0,weight=3)

        TituloInsGen=tk.Label(VentanaInsercionGen,text='Inserción de género', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloInsGen.grid(sticky=tk.N,pady=10)
        DigiteGen1=tk.Label(VentanaInsercionGen,text='Digite el código del género:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteGen1.grid(sticky=tk.N,pady=10)
        #Codigo de Genero
        codigoInsericionGen=tk.Entry(VentanaInsercionGen,font=("Times New Roman",15),background='#E4E4E4')
        codigoInsericionGen.grid(sticky=tk.N,pady=10)

        DigiteNomGen1=tk.Label(VentanaInsercionGen,text='Digite el nombre del género:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomGen1.grid(sticky=tk.N,pady=10)
        #Nombre de Genero
        nombreInsercionGenero=tk.Entry(VentanaInsercionGen,font=("Times New Roman",15),background='#E4E4E4')
        nombreInsercionGenero.grid(sticky=tk.N,pady=10)
        
        #Etiqueta display
        etiquetaConfirmacionInsercionGen=tk.Label(VentanaInsercionGen, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionInsercionGen.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionGen, text="Insertar", command=lambda:insertGen(diccGentodo,codigoInsericionGen,nombreInsercionGenero,etiquetaConfirmacionInsercionGen),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeinsercion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionGen, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionGen,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoInsericionGen),limpiar_texto(nombreInsercionGenero),mostrarEnPantalla(etiquetaConfirmacionInsercionGen,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de insercion
        VentanaInsercionArtista= tk.Toplevel(ventanaLogin)
        VentanaInsercionArtista.title("Insercion")
        VentanaInsercionArtista.configure(bg='#D5CEC1')
        VentanaInsercionArtista.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaInsercionArtista.columnconfigure(0,weight=3)

        TituloInsArt=tk.Label(VentanaInsercionArtista,text='Inserción de artista', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloInsArt.grid(sticky=tk.N,pady=10)
        DigiteArt1=tk.Label(VentanaInsercionArtista,text='Digite el código del artista:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteArt1.grid(sticky=tk.N,pady=10)
        #Codigo de Artista
        codigoInsericionArt=tk.Entry(VentanaInsercionArtista,font=("Times New Roman",15),background='#E4E4E4')
        codigoInsericionArt.grid(sticky=tk.N,pady=10)

        DigiteNomArt1=tk.Label(VentanaInsercionArtista,text='Digite el nombre del artista:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomArt1.grid(sticky=tk.N,pady=10)
        #Nombre de Artista
        nombreInsercionArt=tk.Entry(VentanaInsercionArtista,font=("Times New Roman",15),background='#E4E4E4')
        nombreInsercionArt.grid(sticky=tk.N,pady=10)

        DigitecodGen1=tk.Label(VentanaInsercionArtista,text='Digite el código del género al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodGen1.grid(sticky=tk.N,pady=10)
        #Codigo Gen
        codigoGenInsercionArt=tk.Entry(VentanaInsercionArtista,font=("Times New Roman",15),background='#E4E4E4')
        codigoGenInsercionArt.grid(sticky=tk.N,pady=10)

        #Etiqueta display
        etiquetaConfirmacionInsercionArt=tk.Label(VentanaInsercionArtista, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionInsercionArt.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionArtista, text="Insertar", command=lambda:insertArt(diccArttodo,diccGentodo,codigoInsericionArt,nombreInsercionArt,codigoGenInsercionArt,etiquetaConfirmacionInsercionArt),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeinsercion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionArtista, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionArtista,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoInsericionArt),limpiar_texto(codigoGenInsercionArt),limpiar_texto(nombreInsercionArt),mostrarEnPantalla(etiquetaConfirmacionInsercionArt,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de insercion
        VentanaInsercionAlbum= tk.Toplevel(ventanaLogin)
        VentanaInsercionAlbum.title("Insercion")
        VentanaInsercionAlbum.configure(bg='#D5CEC1')
        VentanaInsercionAlbum.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaInsercionAlbum.columnconfigure(0,weight=3)

        TituloInsAlb=tk.Label(VentanaInsercionAlbum,text='Inserción de album', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloInsAlb.grid(sticky=tk.N,pady=10)
        DigiteAlb1=tk.Label(VentanaInsercionAlbum,text='Digite el código del album:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteAlb1.grid(sticky=tk.N,pady=10)
        #Codigo de Album
        codigoInsericionAlb=tk.Entry(VentanaInsercionAlbum,font=("Times New Roman",15),background='#E4E4E4')
        codigoInsericionAlb.grid(sticky=tk.N,pady=10)

        DigiteNomAlb1=tk.Label(VentanaInsercionAlbum,text='Digite el nombre del album:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomAlb1.grid(sticky=tk.N,pady=10)
        #Nombre de Album
        nombreInsercionAlb=tk.Entry(VentanaInsercionAlbum,font=("Times New Roman",15),background='#E4E4E4')
        nombreInsercionAlb.grid(sticky=tk.N,pady=10)

        DigitecodArt1=tk.Label(VentanaInsercionAlbum,text='Digite el código del artista al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodArt1.grid(sticky=tk.N,pady=10)
        #Codigo Art
        codigoArtInsercionAlb=tk.Entry(VentanaInsercionAlbum,font=("Times New Roman",15),background='#E4E4E4')
        codigoArtInsercionAlb.grid(sticky=tk.N,pady=10)

        #Etiqueta display
        etiquetaConfirmacionInsercionAlb=tk.Label(VentanaInsercionAlbum, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionInsercionAlb.grid(sticky=tk.N,pady=10)

        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionAlbum, text="Insertar", command=lambda:insertAlbum(diccAlbumtodo,diccArttodo,codigoInsericionAlb,nombreInsercionAlb,codigoArtInsercionAlb,etiquetaConfirmacionInsercionAlb),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeinsercion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionAlbum, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionAlbum,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoInsericionAlb),limpiar_texto(nombreInsercionAlb),limpiar_texto(codigoArtInsercionAlb),mostrarEnPantalla(etiquetaConfirmacionInsercionAlb,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de insercion
        VentanaInsercionCancion= tk.Toplevel(ventanaLogin)
        VentanaInsercionCancion.title("Insercion")
        VentanaInsercionCancion.configure(bg='#D5CEC1')
        VentanaInsercionCancion.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaInsercionCancion.columnconfigure(0,weight=3)

        TituloInsCan=tk.Label(VentanaInsercionCancion,text='Inserción de canciones', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloInsCan.grid(sticky=tk.N,pady=2)
        DigiteCan1=tk.Label(VentanaInsercionCancion,text='Digite el código de la canción:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteCan1.grid(sticky=tk.N,pady=2)
        #Codigo de Cancion
        codigoInsericionCancion=tk.Entry(VentanaInsercionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoInsericionCancion.grid(sticky=tk.N,pady=2)

        DigiteNomCan1=tk.Label(VentanaInsercionCancion,text='Digite el nombre de la canción:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomCan1.grid(sticky=tk.N,pady=2)
        #Nombre de Cancion
        nombreInsercionCancion=tk.Entry(VentanaInsercionCancion,font=("Times New Roman",15),background='#E4E4E4')
        nombreInsercionCancion.grid(sticky=tk.N,pady=2)

        DigitecodArt2=tk.Label(VentanaInsercionCancion,text='Digite el código del artista al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodArt2.grid(sticky=tk.N,pady=2)
        #Codigo Art
        codigoArtInsercionCancion=tk.Entry(VentanaInsercionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoArtInsercionCancion.grid(sticky=tk.N,pady=2)

        DigitecodAlb2=tk.Label(VentanaInsercionCancion,text='Digite el código del album al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodAlb2.grid(sticky=tk.N,pady=2)
        #Codigo Alb
        codigoAlbInsercionCancion=tk.Entry(VentanaInsercionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoAlbInsercionCancion.grid(sticky=tk.N,pady=2)

        DigitecodGen2=tk.Label(VentanaInsercionCancion,text='Digite el código del género al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodGen2.grid(sticky=tk.N,pady=2)
        #Codigo Gen
        codigoGenInsercionCancion=tk.Entry(VentanaInsercionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoGenInsercionCancion.grid(sticky=tk.N,pady=2)

        DigitecodPlay2=tk.Label(VentanaInsercionCancion,text='Digite el código de la playlist al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigitecodPlay2.grid(sticky=tk.N,pady=2)
        #Codigo Playlist
        codigoPlaylistInsercionCancion=tk.Entry(VentanaInsercionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoPlaylistInsercionCancion.grid(sticky=tk.N,pady=2)
        #Etiqueta display
        etiquetaConfirmacionInsercionCancion=tk.Label(VentanaInsercionCancion, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionInsercionCancion.grid(sticky=tk.N,pady=2)
        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionCancion, text="Insertar", command=lambda:insertCanciones(diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo,codigoInsericionCancion,nombreInsercionCancion,codigoArtInsercionCancion,codigoAlbInsercionCancion,codigoGenInsercionCancion,codigoPlaylistInsercionCancion,etiquetaConfirmacionInsercionCancion),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeinsercion.grid(row=13,column=0,pady=3)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionCancion, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionCancion,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoInsericionCancion),limpiar_texto(nombreInsercionCancion),limpiar_texto(codigoArtInsercionCancion),limpiar_texto(codigoAlbInsercionCancion),limpiar_texto(codigoGenInsercionCancion),limpiar_texto(codigoPlaylistInsercionCancion),mostrarEnPantalla(etiquetaConfirmacionInsercionCancion,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(row=14,column=0,pady=3)
        ##############################################################################################################################################
        # Configuración de la ventana de insercion
        VentanaInsercionAdm= tk.Toplevel(ventanaLogin)
        VentanaInsercionAdm.title("Insercion")
        VentanaInsercionAdm.configure(bg='#D5CEC1')
        VentanaInsercionAdm.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaInsercionAdm.columnconfigure(0,weight=3)

        TituloInsAdm=tk.Label(VentanaInsercionAdm,text='Inserción de administradores', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloInsAdm.grid(sticky=tk.N,pady=10)
        DigiteAdm=tk.Label(VentanaInsercionAdm,text='Digite el código de administrador:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteAdm.grid(sticky=tk.N,pady=10)
        #Codigo de Admin
        codigoInsericionAdm=tk.Entry(VentanaInsercionAdm,font=("Times New Roman",15),background='#E4E4E4')
        codigoInsericionAdm.grid(sticky=tk.N,pady=10)

        DigiteNomAdm=tk.Label(VentanaInsercionAdm,text='Digite el nombre de administrador:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomAdm.grid(sticky=tk.N,pady=10)
        #Nombre de Admin
        nombreInsercionAdm=tk.Entry(VentanaInsercionAdm,font=("Times New Roman",15),background='#E4E4E4')
        nombreInsercionAdm.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionInsercionAdm=tk.Label(VentanaInsercionAdm, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionInsercionAdm.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeinsercion= tk.Button(VentanaInsercionAdm, text="Insertar", command=lambda:insertAdm(diccAdmintodo,codigoInsericionAdm,nombreInsercionAdm,etiquetaConfirmacionInsercionAdm),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeinsercion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaInsercionAdm, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaInsercionAdm,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoInsericionAdm),limpiar_texto(nombreInsercionAdm),mostrarEnPantalla(etiquetaConfirmacionInsercionAdm,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de modificacion
        VentanaModificacionProp= tk.Toplevel(ventanaLogin)
        VentanaModificacionProp.title("Modificacion")
        VentanaModificacionProp.configure(bg='#D5CEC1')
        VentanaModificacionProp.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaModificacionProp.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloModProp=tk.Label(VentanaModificacionProp,text='Modificacion de propietarios', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloModProp.grid(sticky=tk.N,pady=10)
        DigiteModProp=tk.Label(VentanaModificacionProp,text='Digite el código de propietario:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModProp.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoModificacionProp=tk.Entry(VentanaModificacionProp,font=("Times New Roman",15),background='#E4E4E4')
        codigoModificacionProp.grid(sticky=tk.N,pady=10)
        #Instruccion en pantalla
        DigiteNomModProp=tk.Label(VentanaModificacionProp,text='Digite el nuevo nombre de propietario:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomModProp.grid(sticky=tk.N,pady=10)
        #Nombre de Prop
        nombreModificacionProp=tk.Entry(VentanaModificacionProp,font=("Times New Roman",15),background='#E4E4E4')
        nombreModificacionProp.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionModificacionProp=tk.Label(VentanaModificacionProp, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionModificacionProp.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeModificacion= tk.Button(VentanaModificacionProp, text="Modificar", command=lambda:modificarProp(codigoModificacionProp,diccProptodo,nombreModificacionProp,etiquetaConfirmacionModificacionProp),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeModificacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaModificacionProp, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaModificacionProp,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoModificacionProp),limpiar_texto(nombreModificacionProp),mostrarEnPantalla(etiquetaConfirmacionModificacionProp,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de modificacion
        VentanaModificacionGen= tk.Toplevel(ventanaLogin)
        VentanaModificacionGen.title("Modificacion")
        VentanaModificacionGen.configure(bg='#D5CEC1')
        VentanaModificacionGen.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaModificacionGen.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloModGen=tk.Label(VentanaModificacionGen,text='Modificacion de genero', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloModGen.grid(sticky=tk.N,pady=10)
        DigiteModGen=tk.Label(VentanaModificacionGen,text='Digite el código de genero:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModGen.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoModificacionGen=tk.Entry(VentanaModificacionGen,font=("Times New Roman",15),background='#E4E4E4')
        codigoModificacionGen.grid(sticky=tk.N,pady=10)
        #Instruccion en pantalla
        DigiteNomModGen=tk.Label(VentanaModificacionGen,text='Digite el nuevo nombre de genero:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomModGen.grid(sticky=tk.N,pady=10)
        #Nombre de Gen
        nombreModificacionGen=tk.Entry(VentanaModificacionGen,font=("Times New Roman",15),background='#E4E4E4')
        nombreModificacionGen.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionModificacionGen=tk.Label(VentanaModificacionGen, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionModificacionGen.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeModificacion= tk.Button(VentanaModificacionGen, text="Modificar", command=lambda:modificarGen(codigoModificacionGen,diccGentodo,nombreModificacionGen,etiquetaConfirmacionModificacionGen),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeModificacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaModificacionGen, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaModificacionGen,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoModificacionGen),limpiar_texto(nombreModificacionGen),mostrarEnPantalla(etiquetaConfirmacionModificacionGen,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de modificacion
        VentanaModificacionPlaylist= tk.Toplevel(ventanaLogin)
        VentanaModificacionPlaylist.title("Modificacion")
        VentanaModificacionPlaylist.configure(bg='#D5CEC1')
        VentanaModificacionPlaylist.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaModificacionPlaylist.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloModPlaylist=tk.Label(VentanaModificacionPlaylist,text='Modificacion de playlist', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloModPlaylist.grid(sticky=tk.N,pady=10)
        DigiteModPlaylist=tk.Label(VentanaModificacionPlaylist,text='Digite el código de playlist:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModPlaylist.grid(sticky=tk.N,pady=10)
        #Codigo de Playlist
        codigoModificacionPlaylist=tk.Entry(VentanaModificacionPlaylist,font=("Times New Roman",15),background='#E4E4E4')
        codigoModificacionPlaylist.grid(sticky=tk.N,pady=10)
        #Instruccion en pantalla
        DigiteNomModPlaylist=tk.Label(VentanaModificacionPlaylist,text='Digite el nuevo nombre de playlist:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomModPlaylist.grid(sticky=tk.N,pady=10)
        #Nombre de Playlist
        nombreModificacionPlaylist=tk.Entry(VentanaModificacionPlaylist,font=("Times New Roman",15),background='#E4E4E4')
        nombreModificacionPlaylist.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionModificacionPlaylist=tk.Label(VentanaModificacionPlaylist, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionModificacionPlaylist.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeModificacion= tk.Button(VentanaModificacionPlaylist, text="Modificar", command=lambda:modificarPlaylist(codigoModificacionPlaylist,diccPlaylisttodo,nombreModificacionPlaylist,etiquetaConfirmacionModificacionPlaylist),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeModificacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaModificacionPlaylist, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaModificacionPlaylist,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoModificacionPlaylist),limpiar_texto(nombreModificacionPlaylist),mostrarEnPantalla(etiquetaConfirmacionModificacionPlaylist,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de modificacion
        VentanaModificacionArt= tk.Toplevel(ventanaLogin)
        VentanaModificacionArt.title("Modificacion")
        VentanaModificacionArt.configure(bg='#D5CEC1')
        VentanaModificacionArt.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaModificacionArt.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloModArt=tk.Label(VentanaModificacionArt,text='Modificacion de artista', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloModArt.grid(sticky=tk.N,pady=10)
        DigiteModArt=tk.Label(VentanaModificacionArt,text='Digite el código de artista:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModArt.grid(sticky=tk.N,pady=10)
        #Codigo de Art
        codigoModificacionArt=tk.Entry(VentanaModificacionArt,font=("Times New Roman",15),background='#E4E4E4')
        codigoModificacionArt.grid(sticky=tk.N,pady=10)
        #Instruccion en pantalla
        DigiteNomModArt=tk.Label(VentanaModificacionArt,text='Digite el nuevo nombre de artista:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomModArt.grid(sticky=tk.N,pady=10)
        #Nombre de Art
        nombreModificacionArt=tk.Entry(VentanaModificacionArt,font=("Times New Roman",15),background='#E4E4E4')
        nombreModificacionArt.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionModificacionArt=tk.Label(VentanaModificacionArt, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionModificacionArt.grid(sticky=tk.N,pady=10)
        #Boton de modificar
        botonDeModificacion= tk.Button(VentanaModificacionArt, text="Modificar", command=lambda:modificarArt(codigoModificacionArt,diccArttodo,nombreModificacionArt,etiquetaConfirmacionModificacionArt),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeModificacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaModificacionArt, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaModificacionArt,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoModificacionArt),limpiar_texto(nombreModificacionArt),mostrarEnPantalla(etiquetaConfirmacionModificacionArt,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de modificacion
        VentanaModificacionAlb= tk.Toplevel(ventanaLogin)
        VentanaModificacionAlb.title("Modificacion")
        VentanaModificacionAlb.configure(bg='#D5CEC1')
        VentanaModificacionAlb.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaModificacionAlb.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloModAlb=tk.Label(VentanaModificacionAlb,text='Modificacion de album', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloModAlb.grid(sticky=tk.N,pady=10)
        DigiteModAlb=tk.Label(VentanaModificacionAlb,text='Digite el código de album:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModAlb.grid(sticky=tk.N,pady=10)
        #Codigo de Album
        codigoModificacionAlb=tk.Entry(VentanaModificacionAlb,font=("Times New Roman",15),background='#E4E4E4')
        codigoModificacionAlb.grid(sticky=tk.N,pady=10)
        #Instruccion en pantalla
        DigiteNomModAlb=tk.Label(VentanaModificacionAlb,text='Digite el nuevo nombre de album:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomModAlb.grid(sticky=tk.N,pady=10)
        #Nombre de Album
        nombreModificacionAlb=tk.Entry(VentanaModificacionAlb,font=("Times New Roman",15),background='#E4E4E4')
        nombreModificacionAlb.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionModificacionAlb=tk.Label(VentanaModificacionAlb, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionModificacionAlb.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeModificacion= tk.Button(VentanaModificacionAlb, text="Modificar", command=lambda: modificarAlbum(codigoModificacionAlb,diccAlbumtodo,nombreModificacionAlb,etiquetaConfirmacionModificacionAlb),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeModificacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaModificacionAlb, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaModificacionAlb,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoModificacionAlb),limpiar_texto(nombreModificacionAlb),mostrarEnPantalla(etiquetaConfirmacionInsercionAlb,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        ##############################################################################################################################################
        # Configuración de la ventana de modificacion
        VentanaModificacionCancion= tk.Toplevel(ventanaLogin)
        VentanaModificacionCancion.title("Modificacion")
        VentanaModificacionCancion.configure(bg='#D5CEC1')
        VentanaModificacionCancion.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaModificacionCancion.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloModCan=tk.Label(VentanaModificacionCancion,text='Modificacion de Cancion', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloModCan.grid(sticky=tk.N,pady=2)
        #Codigo de Cancion
        DigiteModCan=tk.Label(VentanaModificacionCancion,text='Digite el código de cancion:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModCan.grid(sticky=tk.N,pady=2)
        codigoModCancion=tk.Entry(VentanaModificacionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoModCancion.grid(sticky=tk.N,pady=2)
        #Nombre de Cancion
        DigiteNomCan=tk.Label(VentanaModificacionCancion,text='Digite el nombre de la canción:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomCan.grid(sticky=tk.N,pady=2)
        nombreModCancion=tk.Entry(VentanaModificacionCancion,font=("Times New Roman",15),background='#E4E4E4')
        nombreModCancion.grid(sticky=tk.N,pady=2)
        #Codigo Art
        DigiteModCodArt=tk.Label(VentanaModificacionCancion,text='Digite el código del artista al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModCodArt.grid(sticky=tk.N,pady=2)
        codigoArtModificacionCancion=tk.Entry(VentanaModificacionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoArtModificacionCancion.grid(sticky=tk.N,pady=2)
        #Codigo Alb
        DigiteModCodAlb=tk.Label(VentanaModificacionCancion,text='Digite el código del album al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModCodAlb.grid(sticky=tk.N,pady=2)
        codigoAlbModificacionCancion=tk.Entry(VentanaModificacionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoAlbModificacionCancion.grid(sticky=tk.N,pady=2)
        #Codigo Gen
        DigiteModCodGen=tk.Label(VentanaModificacionCancion,text='Digite el código del género al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModCodGen.grid(sticky=tk.N,pady=2)
        codigoGenModificacionCancion=tk.Entry(VentanaModificacionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoGenModificacionCancion.grid(sticky=tk.N,pady=2)
        #Codigo Playlist
        DigiteModCodPlaylist=tk.Label(VentanaModificacionCancion,text='Digite el código de la playlist al que pertenece:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteModCodPlaylist.grid(sticky=tk.N,pady=2)
        codigoPlaylistModificacionCancion=tk.Entry(VentanaModificacionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoPlaylistModificacionCancion.grid(sticky=tk.N,pady=2)
        #Etiqueta display
        etiquetaConfirmacionMoficacionCancion=tk.Label(VentanaModificacionCancion, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionMoficacionCancion.grid(sticky=tk.N,pady=2)
        #Boton de buscar
        botonDeModificacion= tk.Button(VentanaModificacionCancion, text="Modificar", command=lambda:modificarCancion(codigoModCancion,diccCancionestodo,nombreModCancion,codigoArtModificacionCancion,codigoAlbModificacionCancion,codigoGenModificacionCancion,codigoPlaylistModificacionCancion,etiquetaConfirmacionMoficacionCancion),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeModificacion.grid(row=13,column=0,pady=3)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaModificacionCancion, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaModificacionCancion,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoArtModificacionCancion),limpiar_texto(nombreModCancion),limpiar_texto(codigoAlbModificacionCancion),limpiar_texto(codigoGenModificacionCancion),limpiar_texto(codigoPlaylistModificacionCancion),limpiar_texto(codigoModCancion),mostrarEnPantalla(etiquetaConfirmacionMoficacionCancion,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(row=14,column=0,pady=3)
         ##############################################################################################################################################
        # Configuración de la ventana de modificacion
        VentanaModificacionAdm= tk.Toplevel(ventanaLogin)
        VentanaModificacionAdm.title("Modificacion")
        VentanaModificacionAdm.configure(bg='#D5CEC1')
        VentanaModificacionAdm.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaModificacionAdm.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloModAdm=tk.Label(VentanaModificacionAdm,text='Modificacion de administrador', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloModAdm.grid(sticky=tk.N,pady=10)
        TituloModAdm=tk.Label(VentanaModificacionAdm,text='Digite el código de administrador:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        TituloModAdm.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoModificacionAdm=tk.Entry(VentanaModificacionAdm,font=("Times New Roman",15),background='#E4E4E4')
        codigoModificacionAdm.grid(sticky=tk.N,pady=10)
        #Instruccion en pantalla
        DigiteNomModAdm=tk.Label(VentanaModificacionAdm,text='Digite el nuevo nombre de administrador:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteNomModAdm.grid(sticky=tk.N,pady=10)
        #Nombre de Gen
        nombreModificacionAdm=tk.Entry(VentanaModificacionAdm,font=("Times New Roman",15),background='#E4E4E4')
        nombreModificacionAdm.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionModificacionAdm=tk.Label(VentanaModificacionAdm, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionModificacionAdm.grid(sticky=tk.N,pady=10)
        #Boton de buscar
        botonDeModificacion= tk.Button(VentanaModificacionAdm, text="Modificar", command=lambda:modificarAdm(codigoModificacionAdm,diccAdmintodo,nombreModificacionAdm,etiquetaConfirmacionModificacionAdm),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeModificacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaModificacionAdm, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaModificacionAdm,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoModificacionAdm),limpiar_texto(nombreModificacionAdm),mostrarEnPantalla(etiquetaConfirmacionModificacionAdm,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
###########################################################################################################################################################################
        # Configuración de la ventana de eliminacion
        VentanaEliminacionProp= tk.Toplevel(ventanaLogin)
        VentanaEliminacionProp.title("Eliminacion")
        VentanaEliminacionProp.configure(bg='#D5CEC1')
        VentanaEliminacionProp.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaEliminacionProp.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloEliminacionProp=tk.Label(VentanaEliminacionProp,text='Eliminacion de Propietario', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloEliminacionProp.grid(sticky=tk.N,pady=10)
        DigiteEliminacionProp=tk.Label(VentanaEliminacionProp,text='Digite el código de propietarion:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteEliminacionProp.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoEliminacionProp=tk.Entry(VentanaEliminacionProp,font=("Times New Roman",15),background='#E4E4E4')
        codigoEliminacionProp.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionEliminacionProp=tk.Label(VentanaEliminacionProp, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionEliminacionProp.grid(sticky=tk.N,pady=10)
        #Boton de eliminacion
        botonDeEliminacion= tk.Button(VentanaEliminacionProp, text="Eliminar", command=lambda: eliminarProp(codigoEliminacionProp,diccProptodo,diccMembresias,diccPlaylisttodo,diccCancionestodo,etiquetaConfirmacionEliminacionProp),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeEliminacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaEliminacionProp, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaEliminacionProp,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoEliminacionProp),mostrarEnPantalla(etiquetaConfirmacionEliminacionProp,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
###########################################################################################################################################################################
        # Configuración de la ventana de eliminacion
        VentanaEliminacionPlaylist= tk.Toplevel(ventanaLogin)
        VentanaEliminacionPlaylist.title("Eliminacion")
        VentanaEliminacionPlaylist.configure(bg='#D5CEC1')
        VentanaEliminacionPlaylist.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaEliminacionPlaylist.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloEliminacionPlaylist=tk.Label(VentanaEliminacionPlaylist,text='Eliminacion de Playlist', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloEliminacionPlaylist.grid(sticky=tk.N,pady=10)
        DigiteEliminacionPlaylist=tk.Label(VentanaEliminacionPlaylist,text='Digite el código de Playlist:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteEliminacionPlaylist.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoEliminacionPlaylist=tk.Entry(VentanaEliminacionPlaylist,font=("Times New Roman",15),background='#E4E4E4')
        codigoEliminacionPlaylist.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionEliminacionPlaylist=tk.Label(VentanaEliminacionPlaylist, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionEliminacionPlaylist.grid(sticky=tk.N,pady=10)
        #Boton de eliminacion
        botonDeEliminacion= tk.Button(VentanaEliminacionPlaylist, text="Eliminar", command=lambda: eliminarPlaylist(codigoEliminacionPlaylist,diccPlaylisttodo,diccCancionestodo,etiquetaConfirmacionEliminacionPlaylist),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeEliminacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaEliminacionPlaylist, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaEliminacionPlaylist,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoEliminacionPlaylist),mostrarEnPantalla(etiquetaConfirmacionEliminacionPlaylist,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
###########################################################################################################################################################################
        # Configuración de la ventana de eliminacion
        VentanaEliminacionGen= tk.Toplevel(ventanaLogin)
        VentanaEliminacionGen.title("Eliminacion")
        VentanaEliminacionGen.configure(bg='#D5CEC1')
        VentanaEliminacionGen.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaEliminacionGen.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloEliminacionGen=tk.Label(VentanaEliminacionGen,text='Eliminacion de Genero', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloEliminacionGen.grid(sticky=tk.N,pady=10)
        DigiteEliminacionGen=tk.Label(VentanaEliminacionGen,text='Digite el código de Genero:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteEliminacionGen.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoEliminacionGen=tk.Entry(VentanaEliminacionGen,font=("Times New Roman",15),background='#E4E4E4')
        codigoEliminacionGen.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionEliminacionGen=tk.Label(VentanaEliminacionGen, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionEliminacionGen.grid(sticky=tk.N,pady=10)
        #Boton de eliminacion
        botonDeEliminacion= tk.Button(VentanaEliminacionGen, text="Eliminar", command=lambda:eliminarGenero(codigoEliminacionGen,diccGentodo,diccArttodo,diccAlbumtodo,diccCancionestodo,etiquetaConfirmacionEliminacionGen),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeEliminacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaEliminacionGen, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaEliminacionGen,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoEliminacionGen),mostrarEnPantalla(etiquetaConfirmacionEliminacionGen,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
###########################################################################################################################################################################
        # Configuración de la ventana de eliminacion
        VentanaEliminacionArt= tk.Toplevel(ventanaLogin)
        VentanaEliminacionArt.title("Eliminacion")
        VentanaEliminacionArt.configure(bg='#D5CEC1')
        VentanaEliminacionArt.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaEliminacionArt.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloEliminacionArt=tk.Label(VentanaEliminacionArt,text='Eliminacion de Artista', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloEliminacionArt.grid(sticky=tk.N,pady=10)
        DigiteEliminacionArt=tk.Label(VentanaEliminacionArt,text='Digite el código de Artista:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteEliminacionArt.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoEliminacionArt=tk.Entry(VentanaEliminacionArt,font=("Times New Roman",15),background='#E4E4E4')
        codigoEliminacionArt.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionEliminacionArt=tk.Label(VentanaEliminacionArt, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionEliminacionArt.grid(sticky=tk.N,pady=10)
        #Boton de eliminacion
        botonDeEliminacion= tk.Button(VentanaEliminacionArt, text="Eliminar", command=lambda:eliminarArt(codigoEliminacionArt,diccArttodo,diccAlbumtodo,diccCancionestodo,etiquetaConfirmacionEliminacionArt),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeEliminacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaEliminacionArt, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaEliminacionArt,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoEliminacionArt),mostrarEnPantalla(etiquetaConfirmacionEliminacionArt,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
###########################################################################################################################################################################
        # Configuración de la ventana de eliminacion
        VentanaEliminacionAlb= tk.Toplevel(ventanaLogin)
        VentanaEliminacionAlb.title("Eliminacion")
        VentanaEliminacionAlb.configure(bg='#D5CEC1')
        VentanaEliminacionAlb.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaEliminacionAlb.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloEliminacionAlb=tk.Label(VentanaEliminacionAlb,text='Eliminacion de Album', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloEliminacionAlb.grid(sticky=tk.N,pady=10)
        DigiteEliminacionAlb=tk.Label(VentanaEliminacionAlb,text='Digite el código de Album:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteEliminacionAlb.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoEliminacionAlb=tk.Entry(VentanaEliminacionAlb,font=("Times New Roman",15),background='#E4E4E4')
        codigoEliminacionAlb.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionEliminacionAlb=tk.Label(VentanaEliminacionAlb, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionEliminacionAlb.grid(sticky=tk.N,pady=10)
        #Boton de eliminacion
        botonDeEliminacion= tk.Button(VentanaEliminacionAlb, text="Eliminar", command=lambda:eliminarAlbum(codigoEliminacionAlb,diccAlbumtodo,diccCancionestodo,etiquetaConfirmacionEliminacionAlb),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeEliminacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaEliminacionAlb, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaEliminacionAlb,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoEliminacionAlb),mostrarEnPantalla(etiquetaConfirmacionEliminacionAlb,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
###########################################################################################################################################################################
        # Configuración de la ventana de eliminacion
        VentanaEliminacionCancion= tk.Toplevel(ventanaLogin)
        VentanaEliminacionCancion.title("Eliminacion")
        VentanaEliminacionCancion.configure(bg='#D5CEC1')
        VentanaEliminacionCancion.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaEliminacionCancion.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloEliminacionCancion=tk.Label(VentanaEliminacionCancion,text='Eliminacion de Cancion', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloEliminacionCancion.grid(sticky=tk.N,pady=10)
        DigiteEliminacionCancion=tk.Label(VentanaEliminacionCancion,text='Digite el código de Cancion:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteEliminacionCancion.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoEliminacionCancion=tk.Entry(VentanaEliminacionCancion,font=("Times New Roman",15),background='#E4E4E4')
        codigoEliminacionCancion.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionEliminacionCancion=tk.Label(VentanaEliminacionCancion, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionEliminacionCancion.grid(sticky=tk.N,pady=10)
        #Boton de eliminacion
        botonDeEliminacion= tk.Button(VentanaEliminacionCancion, text="Eliminar", command=lambda:eliminarCanciones(codigoEliminacionCancion,diccCancionestodo,etiquetaConfirmacionEliminacionCancion),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeEliminacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaEliminacionCancion, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaEliminacionCancion,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoEliminacionCancion),mostrarEnPantalla(etiquetaConfirmacionEliminacionCancion,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
###########################################################################################################################################################################
        # Configuración de la ventana de eliminacion
        VentanaEliminacionAdm= tk.Toplevel(ventanaLogin)
        VentanaEliminacionAdm.title("Eliminacion")
        VentanaEliminacionAdm.configure(bg='#D5CEC1')
        VentanaEliminacionAdm.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaEliminacionAdm.columnconfigure(0,weight=3)
        #Instruccion en pantalla
        TituloEliminacionAdm=tk.Label(VentanaEliminacionAdm,text='Eliminacion de Administrador', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        TituloEliminacionAdm.grid(sticky=tk.N,pady=10)
        DigiteEliminacionAdm=tk.Label(VentanaEliminacionAdm,text='Digite el código de Administrador:', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        DigiteEliminacionAdm.grid(sticky=tk.N,pady=10)
        #Codigo de Prop
        codigoEliminacionAdm=tk.Entry(VentanaEliminacionAdm,font=("Times New Roman",15),background='#E4E4E4')
        codigoEliminacionAdm.grid(sticky=tk.N,pady=10)
        #Etiqueta display
        etiquetaConfirmacionEliminacionAdm=tk.Label(VentanaEliminacionAdm, text="",font=("Times New Roman",15),background='#D5CEC1')
        etiquetaConfirmacionEliminacionAdm.grid(sticky=tk.N,pady=10)
        #Boton de eliminacion
        botonDeEliminacion= tk.Button(VentanaEliminacionAdm, text="Eliminar", command=lambda: eliminarAdministrador(codigoEliminacionAdm,diccAdmintodo,etiquetaConfirmacionEliminacionAdm),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeEliminacion.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaEliminacionAdm, text="Volver a menu", command=lambda:[navegacionVentanas(VentanaMenu,VentanaEliminacionAdm,obtenerDimenciones(VentanaMenu)),limpiar_texto(codigoEliminacionAdm),mostrarEnPantalla(etiquetaConfirmacionEliminacionAdm,"")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
###########################################################################################################################################################################
        menuinsercion.add_command(label="Prueba",command=lambda:reproductor(diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo,codigoUsuario,ColasDeReproduccion,diccProptodo,diccAdmintodo))
def BotonesMusica(window):
        global GenerosBoton, ArtistasBoton, AlbumesBoton, CancionesBoton, AdministradorBoton, PropietarioBoton
        # Create and display two additional buttons
        GenerosBoton.destroy()
        ArtistasBoton.destroy()
        #CancionesBoton.destroy()
        #AlbumesBoton.destroy()
        #AdministradorBoton.destroy()
        #PropietarioBoton.destroy()
        Generospng = tk.PhotoImage(file='./Generos.png')
        window.Generospng = tk.PhotoImage(file='./Generos.png')
        GenerosBoton = tk.Button(window, image=window.Generospng)
        GenerosBoton.pack(side="top", pady=10)
        Artistaspng = tk.PhotoImage(file='./Artistas.png')
        window.Artistaspng = tk.PhotoImage(file='./Artistas.png')
        ArtistasBoton = tk.Button(window, image=window.Artistaspng)
        ArtistasBoton.pack(side="top", pady=10)

def BotonesAlbumes(window):
        global GenerosBoton, ArtistasBoton, AlbumesBoton, CancionesBoton, AdministradorBoton, PropietarioBoton
        # Create and display two additional buttons
        #GenerosBoton.destroy()
        #ArtistasBoton.destroy()
        CancionesBoton.destroy()
        AlbumesBoton.destroy()
        #AdministradorBoton.destroy()
        #PropietarioBoton.destroy()
        Albumespng = tk.PhotoImage(file='./Albumes.png')
        window.Albumespng = tk.PhotoImage(file='./Albumes.png')
        AlbumesBoton = tk.Button(window, image=window.Albumespng)
        AlbumesBoton.pack(side="top", pady=10)
        Cancionespng = tk.PhotoImage(file='./Canciones.png')
        window.Cancionespng = tk.PhotoImage(file='./Canciones.png')
        CancionesBoton = tk.Button(window, image=window.Cancionespng)
        CancionesBoton.pack(side="top", pady=10)

def BotonesUsuarios(window):
        global GenerosBoton, ArtistasBoton, AlbumesBoton, CancionesBoton, AdministradorBoton, PropietarioBoton
        # Create and display two additional buttons
        #GenerosBoton.destroy()
        #ArtistasBoton.destroy()
        #CancionesBoton.destroy()
        #AlbumesBoton.destroy()
        AdministradorBoton.destroy()
        PropietarioBoton.destroy()
        Administradorpng = tk.PhotoImage(file='./Administrador.png')
        window.Administradorpng = tk.PhotoImage(file='./Administrador.png')
        AdministradorBoton = tk.Button(window, image=window.Administradorpng)
        AdministradorBoton.pack(side="top", pady=10)
        Propietariopng = tk.PhotoImage(file='./Propietario.png')
        window.Propietariopng = tk.PhotoImage(file='./Propietario.png')
        PropietarioBoton = tk.Button(window, image=window.Propietariopng)
        PropietarioBoton.pack(side="top", pady=10)
loginVentana()


