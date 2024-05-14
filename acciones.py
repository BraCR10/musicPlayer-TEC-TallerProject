#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
import tkinter as tk
from busqueda import buscarProp #buscarProp
from lecturaArchivos import *
from tkinter import messagebox

diccProptodo=leerProp()[0]
contFacturas=0
def navegacionVentanas(ventana_principal,ventana_secundaria,tamaño):
    ventana_secundaria.withdraw()  # Oculta la ventana secundaria
    ventana_principal.geometry(tamaño)
    ventana_principal.deiconify()  # Muestra la ventana principal
    

def obtenerDimenciones(ventana):
    ventana.update_idletasks()  # Actualiza la interfaz de usuario para asegurar que se haya renderizado completamente
    ancho = ventana.winfo_width()
    largo = ventana.winfo_height()
    x=ventana.winfo_x()
    y=ventana.winfo_y()

    return f"{ancho}x{largo}+{x}+{y}"

def verificadorUsuario(tipoUsuario):
    if tipoUsuario=="Administrador":
        tipoUsuario= "Administrador"
    else:
        tipoUsuario= "Usuario" 

def mostrarEnPantalla(etiqueta,dato):
    if dato==None:
        texto='No existe'
    else:
        texto = dato 
    etiqueta.config(text=texto)  # Actualiza el texto de la etiqueta con el texto ingresado
    
def limpiar_texto(caja):
    caja.delete(0, tk.END)  # Borra todo el contenido del cuadro de texto
    
def verTipoUsuario(permisos,tipoUsuario):
    permisos.set(tipoUsuario.get())

def mostrarEnPantallaBusqueda(etiqueta,dato):
    if dato==None:
        texto='No existe'
    else:
        texto = dato[0]
    etiqueta.config(text=texto,bg="#D5CEC1")
    

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
    

        
def mostrarFactura(diccTodo,codigo):
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
            descuento=tk.Label(VentanaFacturas,text=f'>>>Precio $19, descuento de 1% por ser usuario', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')  
        elif diccTodo[codigo]['estado']=='1':
            descuento=tk.Label(VentanaFacturas,text=f'>>>Precio $15, descuento de 5% por ser usuario', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')  
        else:
            descuento=tk.Label(VentanaFacturas,text=f'>>>Precio $20', font=("Sitka Text Semibold",15),bg='#28342C',fg='#E4E4E4')  
        descuento.grid(sticky=tk.N,pady=10)
        estado.grid(sticky=tk.N,pady=10)
        #Boton de exportar factura
        botonDeExportar= tk.Button(VentanaFacturas, text="Exportar", command=lambda:exportarFactura(diccTodo,codigo),font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeExportar.grid(sticky=tk.N,pady=10)
        #Boton de volver
        botonDeBusquedaAMenu = tk.Button(VentanaFacturas, text="Cerrar", command=lambda:[VentanaFacturas.withdraw(),estado.destroy(),membresia.destroy(),id.destroy,Titulo.destroy,descuento.destroy()],font=('Times New Roman',15),bg='#102512',fg='#E4E4E4')
        botonDeBusquedaAMenu.grid(sticky=tk.N,pady=10)
        
def exportarFactura(diccTodo,codigo):
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
    reporte.write(f'\n-----------------------------------------------')#Agerga datos al archivo
    if diccTodo[codigo]['estado']=='0':#Descuento
        reporte.write(f'\n>>>Precio $19, descuento de 1% por ser usuario')  
    elif diccTodo[codigo]['estado']=='1':
        reporte.write(f'\n>>>>Precio $15, descuento de 5% por ser usuario')  
    else:
        reporte.write(f'\n>>>>Precio $20')  

    reporte.close()#Cierra el archivo
    print(f'\n ---> La factura  se ha creado correctamente')

def pagar(diccTodo,diccMembresias,codigo,etiqueta):
    diccTodo[codigo]['estado']='1'
    mostrarEnPantalla(etiqueta,"Su usuario ha sido activado, por favor vuelva al login")
    #diccMembresias[codigo]='1'

def mostrarEmergenteMenu(emergente,VentanaMenu,id,tipousuario,Ventana1,Ventana2,Ventana3,Ventana4,Ventana5,Ventana6,Ventana7,Ventana8):
    # Eliminar el menú anterior, si existe
    try:
        emergente.delete(0, tk.END)
    except tk.TclError:
        pass
    emergenteAux= tk.Menu(VentanaMenu, tearoff=0)
    # Crear el menú emergente con otra imagen
    if id==1:
        imagenGeneros = tk.PhotoImage(file="generos.png") 
        emergente.add_command(image=imagenGeneros, command=lambda:mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana1,Ventana2,Ventana3,Ventana4))
        emergente.image = imagenGeneros  
        imagenArtistas = tk.PhotoImage(file="Artistas.png") 
        emergente.add_command(image=imagenArtistas, command=lambda: mostrarEmergenteMenu2(emergenteAux,VentanaMenu,tipousuario,Ventana5,Ventana6,Ventana7,Ventana8))
        emergente.image = imagenArtistas 
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
        if tipousuario=='Usuario':
            imagenFacturas = tk.PhotoImage(file="Facturacion.png") 
            emergente.add_command(image=imagenFacturas, command=lambda:mostrarFactura(Ventana1,Ventana2))#En ventana uno esta diccPropTodo y en ventana2 el codigo de usuario
            emergente.image = imagenFacturas
        else:
            imagenFacturas = tk.PhotoImage(file="Facturacion.png") 
            emergente.add_command(image=imagenFacturas,command=lambda:messagebox.showinfo("Alerta", "El administrador no cuenta con serivicios de facturacion!"))
    # Mostrar el menú emergente
    emergente.post(VentanaMenu.winfo_pointerx(), VentanaMenu.winfo_pointery())

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

