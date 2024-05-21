#Avance final proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
#Importaciones
import tkinter as tk
from busqueda import buscarProp #buscarProp
from lecturaArchivos import *
from tkinter import messagebox

#Funcion para hacer transicion entre ventanas
diccProptodo=leerProp()[0]
contFacturas=0
def navegacionVentanas(ventana_principal,ventana_secundaria,tamaño):
    ventana_secundaria.withdraw()  # Oculta la ventana secundaria
    ventana_principal.geometry(tamaño)
    ventana_principal.deiconify()  # Muestra la ventana principal
    
#Funcion aux que obtiene la dimencion de la pantalla actual para pasar a la otra con la misma dimension
def obtenerDimenciones(ventana):
    ventana.update_idletasks()  # Actualiza la interfaz de usuario para asegurar que se haya renderizado completamente
    ancho = ventana.winfo_width()
    largo = ventana.winfo_height()
    x=ventana.winfo_x()
    y=ventana.winfo_y()
    return f"{ancho}x{largo}+{x}+{y}" 

#Rescribe algo nuevo en una etiqueta
def mostrarEnPantalla(etiqueta,dato):
    if dato==None:
        texto='No existe'
    else:
        texto = dato 
    etiqueta.config(text=texto)  # Actualiza el texto de la etiqueta con el texto ingresado
#Funcion especial para busquedas
def mostrarEnPantallaBusqueda(etiqueta,dato):
    if dato==None:
        texto='No existe'
    else:
        texto = dato[0]
    etiqueta.config(text=texto,bg="#D5CEC1")
#Limpia el texto de una entry
def limpiar_texto(caja):
    caja.delete(0, tk.END)  # Borra todo el contenido del cuadro de texto   

#Permite el regitro de un propietario
def registar(diccTodo,diccMembresias,nombre,etiqueta):
    estado='0Nuevo'
    cod=1
    codMem=1
    while str(cod) in list(diccTodo.keys()):
        cod+=1
    while str(codMem) in list(diccMembresias.values()):
        codMem+=1
    diccTodo[str(cod)]={'nombre':nombre,'codMem':str(codMem),'estado':estado}#Añade  un propietario al dict
    diccMembresias[str(cod)]=str(codMem)
    mostrarEnPantalla(etiqueta,f"Registrado! \nSu codigo de propietario es: {cod}\nSu codigo de membresia membresia es: {codMem}")
    
#Se definen los descuentos por defecto
descuentoUsuarioActivo=25
descuentoUsuarioInactivo=75
descuentoUsuarioNuevo=0
Precio=40

#Permite generar la factura de un propietario
def mostrarFactura(diccTodo,codigo,listaFacturas):
    # Configuración de la ventana de modificacion
        VentanaFacturas= tk.Tk()
        VentanaFacturas.title("Factura")
        VentanaFacturas.configure(bg='#D5CEC1')
        VentanaFacturas.withdraw()  # Oculta la ventana secundaria inicialmente
        VentanaFacturas.columnconfigure(0,weight=3)
        VentanaFacturas.deiconify()  # Muestra la ventana principal
        #Instruccion en pantalla
        Titulo=tk.Label(VentanaFacturas,text='Factura', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
        Titulo.grid(sticky=tk.N,pady=10)
        usuario=tk.Label(VentanaFacturas,text=f"Usuario: {diccTodo[codigo]['nombre']}", font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        usuario.grid(sticky=tk.N,pady=10)
        id=tk.Label(VentanaFacturas,text=f'Identificacion: {codigo}', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        id.grid(sticky=tk.N,pady=10)
        membresia=tk.Label(VentanaFacturas,text=f"Membresia: {diccTodo[codigo]['codMem']}", font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
        membresia.grid(sticky=tk.N,pady=10)
        if diccTodo[codigo]['estado']=='0' or diccTodo[codigo]['estado']=='0Nuevo':#Estado
            estado=tk.Label(VentanaFacturas,text=f'>>>Estado de membresia: INACTIVA', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')  
        else:
            estado=tk.Label(VentanaFacturas,text=f'>>>Estado de membresia: ACTIVA', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')        
        if diccTodo[codigo]['estado']=='0':#Descuento
            descuento=tk.Label(VentanaFacturas,text=f'>>>Precio ${round(Precio-(Precio*(descuentoUsuarioInactivo/100)),2)}, descuento de {descuentoUsuarioInactivo}% por ser usuario', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')  
        elif diccTodo[codigo]['estado']=='1':
            descuento=tk.Label(VentanaFacturas,text=f'>>>Precio ${round(Precio-(Precio*(descuentoUsuarioActivo/100)),2)}, descuento de {descuentoUsuarioActivo}% por ser usuario', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')  
            if codigo in listaFacturas:
                aviso=tk.Label(VentanaFacturas,text='Tiene una factura pendiente generada por el administrador', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
                aviso.grid(sticky=tk.N,pady=10)
                botonDePagar= tk.Button(VentanaFacturas, text="Pagar", command=lambda:[pagar(diccTodo,{},codigo,aviso,listaFacturas),messagebox.showinfo("Confirmacion", "La factura se ha pagado correctamente!")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
                botonDePagar.grid(sticky=tk.N,pady=10)
            else:
                aviso=tk.Label(VentanaFacturas,text='No tiene pagos pendientes', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
                aviso.grid(sticky=tk.N,pady=10)
        else:
            descuento=tk.Label(VentanaFacturas,text=f'>>>Precio ${round(Precio-(Precio*(descuentoUsuarioNuevo/100)),2)}, descuento de {descuentoUsuarioNuevo}% ', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')  
        descuento.grid(sticky=tk.N,pady=10)
        estado.grid(sticky=tk.N,pady=10)
        #Boton de exportar factura
        botonDeExportar= tk.Button(VentanaFacturas, text="Exportar", command=lambda:[exportarFactura(diccTodo,codigo,listaFacturas),messagebox.showinfo("Confirmacion", "La factura se ha exportado correctamente!")],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeExportar.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaFacturas, text="Cerrar", command=lambda:[VentanaFacturas.withdraw(),estado.destroy(),membresia.destroy(),id.destroy,Titulo.destroy(),descuento.destroy()],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
  
#Permite que propietarios y admins exporten facturas      
def exportarFactura(diccTodo,codigo,listaFacturas):
    global contFacturas
    contFacturas+=1
    reporte = open(f"Factura-{buscarProp(codigo,diccTodo)}-{contFacturas}.txt", "a")#Crea un nuevo archivo .txt
    reporte.write(f'\n--- Factura ---\n')#Agerga datos al archivo
    reporte.write(f'\n-----------------------------------------------')#Agerga datos al archivo
    reporte.write(f'\n>>>Identificacion propietario : {codigo}')#Agerga datos al archivo
    reporte.write(f'\n-----------------------------------------------')#Agerga datos al archivo
    nombreTemp=diccTodo[codigo]['nombre']
    reporte.write(f'\n>>>Nombre propietario : {nombreTemp}')#Agerga datos al archivo
    reporte.write(f'\n-----------------------------------------------')#Agerga datos al archivo
    codMemTemp=diccTodo[codigo]['codMem']
    reporte.write(f'\n>>>Codigo de membresia: {codMemTemp}')#Agerga datos al archivo
    reporte.write(f'\n-----------------------------------------------')#Agerga datos al archivo
    if diccTodo[codigo]['estado']=='0':
        reporte.write(f'\n>>>Estado de membresia: INACTIVA')#Agerga datos al archivo
    elif diccTodo[codigo]['estado']=='1':
        reporte.write(f'\n>>>Estado de membresia: ACTIVA')#Agerga datos al archivo
        if codigo in listaFacturas:
            reporte.write(f'\n>>>Tiene una factura pendiente generada por el administrador')#Agerga datos al archivo
        else:
            reporte.write(f'\n>>>No tiene pagos pendientes')#Agerga datos al archivo
    reporte.write(f'\n-----------------------------------------------')#Agerga datos al archivo
    if diccTodo[codigo]['estado']=='0':#Descuento
        reporte.write(f'\n>>>Precio ${round(Precio-(Precio*(descuentoUsuarioInactivo/100)),2)}, descuento de {descuentoUsuarioInactivo}% por ser usuario')  
    elif diccTodo[codigo]['estado']=='1':
        reporte.write(f'\n>>>Precio ${round(Precio-(Precio*(descuentoUsuarioActivo/100)),2)}, descuento de {descuentoUsuarioActivo}% por ser usuario')  
    else:
        reporte.write(f'\n>>>Precio ${round(Precio-(Precio*(descuentoUsuarioNuevo/100)),2)}, descuento de {descuentoUsuarioNuevo}% ')  

    reporte.close()#Cierra el archivo
    print(f'\n ---> La factura  se ha creado correctamente')

#Simula el pago de un propietario en la ventana de pagos antes de loguearse
def pagar(diccTodo,diccMembresias,codigo,etiqueta,listaFacturas):
    if diccTodo[codigo]['estado']=='0' or diccTodo[codigo]['estado']=='0Nuevo':
        diccTodo[codigo]['estado']='1'
    elif codigo in listaFacturas:
        for i in range(len(listaFacturas)):
            if listaFacturas[i]==codigo:
                listaFacturas.pop(i)
                break   
    mostrarEnPantalla(etiqueta,"Su usuario ha sido activado, por favor vuelva al login")
    #diccMembresias[codigo]='1'

#Funcion especial para mostrar emergentes en el icono de canciones con 3 emergentes en el menu principal
def mostrarEmergenteMenuTresOpciones(emergente,VentanaMenu,tipousuario,Ventana1,Ventana2,Ventana3,Ventana4,Ventana5,Ventana6,Ventana7,Ventana8,Ventana9,Ventana10,Ventana11,Ventana12):
    # Eliminar el menú anterior, si existe
    try:
        emergente.delete(0, tk.END)
    except tk.TclError:
        pass
    emergenteAux= tk.Menu(VentanaMenu, tearoff=0)
    # Crear el menú emergente con otra imagen
    imagenGeneros = tk.PhotoImage(file="generos.png") 
    emergente.add_command(image=imagenGeneros, command=lambda:mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana1,Ventana2,Ventana3,Ventana4))
    emergente.image = imagenGeneros  
    imagenArtistas = tk.PhotoImage(file="Artistas.png") 
    emergente.add_command(image=imagenArtistas, command=lambda: mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana5,Ventana6,Ventana7,Ventana8))
    emergente.image = imagenArtistas 
    imagenPlaylist = tk.PhotoImage(file="Playlist.png") 
    emergente.add_command(image=imagenPlaylist, command=lambda: mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana9,Ventana10,Ventana11,Ventana12))
    emergente.image = imagenPlaylist 
    # Mostrar el menú emergente
    emergente.post(VentanaMenu.winfo_pointerx(), VentanaMenu.winfo_pointery())

#Emergente en todos los demas iconos del menu principal
def mostrarEmergenteMenu(emergente,VentanaMenu,id,tipousuario,Ventana1,Ventana2,Ventana3,Ventana4,Ventana5,Ventana6,Ventana7,Ventana8):
    # Eliminar el menú anterior, si existe
    try:
        emergente.delete(0, tk.END)
    except tk.TclError:
        pass
    emergenteAux= tk.Menu(VentanaMenu, tearoff=0)
    # Crear el menú emergente con otra imagen
    if id==2:
        imagenAlbumes = tk.PhotoImage(file="Albumes.png") 
        emergente.add_command(image=imagenAlbumes, command=lambda:mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana1,Ventana2,Ventana3,Ventana4))
        emergente.image = imagenAlbumes  
        imagenCanciones = tk.PhotoImage(file="Canciones.png") 
        emergente.add_command(image=imagenCanciones, command=lambda:mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana5,Ventana6,Ventana7,Ventana8))
        emergente.image = imagenCanciones 
    if id==3:
        imagenAdministrador = tk.PhotoImage(file="Administrador.png") 
        emergente.add_command(image=imagenAdministrador, command=lambda:mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana1,Ventana2,Ventana3,Ventana4))
        emergente.image = imagenAdministrador
        imagenPropietario = tk.PhotoImage(file="Propietario.png") 
        emergente.add_command(image=imagenPropietario, command=lambda:mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana5,Ventana6,Ventana7,Ventana8))
        emergente.image = imagenPropietario
    if id==4:
        #Caso especial, se los parametro de ventana se utilizan diferente
        #Ventana1=diccProptodo
        #Ventana2=codigoUsuario
        if tipousuario=='Usuario':
            imagenFacturas = tk.PhotoImage(file="Facturacion.png") 
            emergente.add_command(image=imagenFacturas, command=lambda:mostrarFactura(Ventana1,Ventana2,Ventana3))#Ventan3 son la listas de las facturas y 1 diccproptodo y 2 codigo de user
            emergente.image = imagenFacturas
        else:
            imagenFacturas = tk.PhotoImage(file="Facturacion.png")
            emergente.add_command(image=imagenFacturas,command=lambda:administrarFacturas(Ventana3,Ventana1))#Ventan3 son la listas de las facturas y 1 diccproptodo
            imagenDescuentos = tk.PhotoImage(file="Descuentos.png") 
            emergente.add_command(image=imagenDescuentos,command=lambda:administrarDescuentos())
    # Mostrar el menú emergente
    emergente.post(VentanaMenu.winfo_pointerx(), VentanaMenu.winfo_pointery())

#Aux de mostrarEmergente menu
def mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana1,Ventana2,Ventana3,Ventana4):
    # Eliminar el menú anterior, si existe
    try:
        emergenteAux.delete(0, tk.END)
    except tk.TclError:
        pass
    # Crear el menú emergente con otra imagen
    if tipousuario=='Usuario':
        emergenteAux.add_command(label="Busqueda" ,command=lambda:navegacionVentanas(Ventana3,VentanaMenu,obtenerDimenciones(VentanaMenu)))           
    else:
        emergenteAux.add_command(label="Insercion",command=lambda:navegacionVentanas(Ventana1,VentanaMenu,obtenerDimenciones(VentanaMenu)))           
        emergenteAux.add_command(label="Modificacion", command=lambda:navegacionVentanas(Ventana2,VentanaMenu,obtenerDimenciones(VentanaMenu)))           
        emergenteAux.add_command(label="Busqueda" ,command=lambda:navegacionVentanas(Ventana3,VentanaMenu,obtenerDimenciones(VentanaMenu)))           
        emergenteAux.add_command(label="Eliminacion",command=lambda:navegacionVentanas(Ventana4,VentanaMenu,obtenerDimenciones(VentanaMenu)))           
    emergenteAux.post(VentanaMenu.winfo_pointerx(), VentanaMenu.winfo_pointery())

#Funcion que muestra una ventana al administrador para modificar descuentos y precios
def administrarDescuentos():
    global descuentoUsuarioActivo,descuentoUsuarioInactivo,descuentoUsuarioNuevo,Precio
    # Configuración de la ventana de modificacion
    VentanaDescuentos= tk.Tk()
    VentanaDescuentos.title("Administrador de descuentos")
    VentanaDescuentos.configure(bg='#D5CEC1')
    VentanaDescuentos.columnconfigure(0,weight=3)
    #VentanaDescuentos.deiconify()  # Muestra la ventana principal
    #Instruccion en pantalla
    Titulo=tk.Label(VentanaDescuentos,text='Modificar descuentos', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
    Titulo.grid(sticky=tk.N,pady=10)
    precioActual=tk.Label(VentanaDescuentos,text=f"El precio actual es de ${round(Precio)}", font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
    precioActual.grid(sticky=tk.N,pady=10)
    PrecioNuevo=tk.Entry(VentanaDescuentos,font=("Times New Roman",15),background='#E4E4E4')
    PrecioNuevo.grid(sticky=tk.N,pady=10)
    Cambio = tk.Button(VentanaDescuentos, text="Cambiar",command=lambda:[modificadorPrecios('Precio',PrecioNuevo.get(),precioActual),limpiar_texto(PrecioNuevo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    Cambio.grid(sticky=tk.N,pady=10)
    decuentoUsuariosActivos=tk.Label(VentanaDescuentos,text=f'El descuento a usuarios activos es de {descuentoUsuarioActivo}%', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
    decuentoUsuariosActivos.grid(sticky=tk.N,pady=10)
    decuentoUsuariosActivosNuevo=tk.Entry(VentanaDescuentos,font=("Times New Roman",15),background='#E4E4E4')
    decuentoUsuariosActivosNuevo.grid(sticky=tk.N,pady=10)
    Cambio = tk.Button(VentanaDescuentos, text="Cambiar",command=lambda:[modificadorPrecios('Activos',decuentoUsuariosActivosNuevo.get(),decuentoUsuariosActivos),limpiar_texto(decuentoUsuariosActivosNuevo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    Cambio.grid(sticky=tk.N,pady=10)
    decuentoUsuariosInactivos=tk.Label(VentanaDescuentos,text=f'El descuento a usuarios inactivo es de {descuentoUsuarioInactivo}%', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
    decuentoUsuariosInactivos.grid(sticky=tk.N,pady=10)
    decuentoUsuariosInactivosNuevo=tk.Entry(VentanaDescuentos,font=("Times New Roman",15),background='#E4E4E4')
    decuentoUsuariosInactivosNuevo.grid(sticky=tk.N,pady=10)
    Cambio = tk.Button(VentanaDescuentos, text="Cambiar",command=lambda:[modificadorPrecios('Inactivos',decuentoUsuariosInactivosNuevo.get(),decuentoUsuariosInactivos),limpiar_texto(decuentoUsuariosInactivosNuevo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    Cambio.grid(sticky=tk.N,pady=10)
    descuentoUsuariosNuevos=tk.Label(VentanaDescuentos,text=f'El descuento a usuarios nuevos es de {descuentoUsuarioNuevo}%', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')
    descuentoUsuariosNuevos.grid(sticky=tk.N,pady=10)
    descuentoUsuariosNuevosNuevo=tk.Entry(VentanaDescuentos,font=("Times New Roman",15),background='#E4E4E4')
    descuentoUsuariosNuevosNuevo.grid(sticky=tk.N,pady=10)
    Cambio = tk.Button(VentanaDescuentos, text="Cambiar",command=lambda:[modificadorPrecios('Nuevos',descuentoUsuariosNuevosNuevo.get(),descuentoUsuariosNuevos),limpiar_texto(descuentoUsuariosNuevosNuevo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    Cambio.grid(sticky=tk.N,pady=10)

#Aux que mofdifica los precios
def modificadorPrecios(cambio,nuevoDescuento,etiqueta):
    global descuentoUsuarioActivo,descuentoUsuarioInactivo,descuentoUsuarioNuevo,Precio
    if nuevoDescuento.isdecimal():
        if cambio=='Nuevos':
            descuentoUsuarioNuevo=int(nuevoDescuento)
            mostrarEnPantalla(etiqueta,f'El descuento a usuarios nuevos es de {nuevoDescuento}%')
        elif cambio=='Inactivos':
            descuentoUsuarioInactivo=int(nuevoDescuento)
            mostrarEnPantalla(etiqueta,f'El descuento a usuarios inactivos es de {nuevoDescuento}%')
        elif cambio=='Activos':
            descuentoUsuarioActivo=int(nuevoDescuento)
            mostrarEnPantalla(etiqueta,f'El descuento a usuarios activos es de {nuevoDescuento}%')
        elif cambio=='Precio':
            Precio=int(nuevoDescuento)
            mostrarEnPantalla(etiqueta,f'El precio actual es de ${round(int(nuevoDescuento))}')
    else:
        messagebox.showinfo("Alerta", "El dato digitado no es valido!")

#Funcion que le premite al admin generar,exportar y eliminar cobros
def administrarFacturas(listaFacturas,diccPropTodo):
    # Configuración de la ventana de modificacion
    VentanaFacturacion= tk.Tk()
    VentanaFacturacion.title("Administrador de descuentos")
    VentanaFacturacion.configure(bg='#D5CEC1')
    VentanaFacturacion.columnconfigure(0,weight=3)
    Titulo=tk.Label(VentanaFacturacion,text='Generar Factura', font=("Sitka Text Semibold",25),bg='#28342C',fg='#E4E4E4')
    Titulo.grid(sticky=tk.N,pady=10)
    UsuarioBuscar=tk.Entry(VentanaFacturacion,font=("Times New Roman",15),background='#E4E4E4')
    UsuarioBuscar.grid(sticky=tk.N,pady=10)
    verificar = tk.Button(VentanaFacturacion, text="Ver facturas",command=lambda:[botones(VentanaFacturacion,diccPropTodo,UsuarioBuscar.get(),listaFacturas)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    verificar.grid(sticky=tk.N,pady=10)
    
#Variable para evitar repeticiones a la hora de mostrar
verificadorBotones=False
#Aux que muetra botones de opiciones en adminstrarFacturas
def botones(ventana,diccPropTodo,usuario,listaFacturas):
    global verificadorBotones
    if usuario in list(diccPropTodo.keys()):
        if verificadorBotones==True:
            generar.destroy()
            exportar.destroy()
            pagar.destroy()
            verificadorBotones=True
        #Instruccion en pantalla
        generar = tk.Button(ventana, text="Generar factura",command=lambda:[generarFactura(listaFacturas,usuario,diccPropTodo),messagebox.showinfo("Confirmacion", "Se ha generado la factura!")],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
        generar.grid(sticky=tk.N,pady=10)
        exportar = tk.Button(ventana, text="Exportar factura",command=lambda:[exportarFactura(diccPropTodo,usuario,listaFacturas),messagebox.showinfo("Confirmacion", "Se ha exportado la factura!")],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
        exportar.grid(sticky=tk.N,pady=10)
        pagar = tk.Button(ventana, text="Eliminar factura",command=lambda:[eliminarFactura(diccPropTodo,listaFacturas,usuario),messagebox.showinfo("Confirmacion", "Se ha cancelado la factura!")],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
        pagar.grid(sticky=tk.N,pady=10)
    else:
        messagebox.showinfo("Alerta", "El usuario no existe!")

#Funcion Aux que genera facturas 
def generarFactura(listaFacturas,usuario,diccPropTodo):#Si un usaurio esta activo y le genero facturas
    if usuario not in listaFacturas and diccPropTodo[usuario]['estado']=='1':
        listaFacturas+=[usuario]
        
#Funcion aux que borra una factura
def eliminarFactura(diccPropTodo,listaFacturas,usuario):#Si un usuario se le elimina la facura
    if diccPropTodo[usuario]['estado']=='0' or diccPropTodo[usuario]['estado']=='0Nuevo':
        diccPropTodo[usuario]['estado']='1'
    elif usuario in listaFacturas:
        for i in range(len(listaFacturas)):
            if listaFacturas[i]==usuario:
                listaFacturas.pop(i)
                break