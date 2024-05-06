import tkinter as tk
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
    etiqueta.config(text=texto)