def irVentana(ventana_principal,ventana_secundaria,tamaño):
    #ventana_secundaria.geometry(pos_secundaria)  # Restaura la posición de la ventana secundaria
    ventana_principal.withdraw()  # Oculta la ventana principal
    ventana_secundaria.geometry(tamaño)
    ventana_secundaria.deiconify()  # Muestra la ventana secundaria
    

def volverVentana(ventana_principal,ventana_secundaria,tamaño):
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
