#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from lecturaArchivos import *#leerAlbum,leerArt,leerCanciones,leerGen,leerPlaylist,leerProp
from insercion import *#insertAlbum,insertArt,insertCanciones,insertGen,insertPlaylist,insertProp
from busqueda import * #buscarAlbum,buscarArtista,buscarCancion,buscarGenero,buscarPlaylist,buscarProp
from login import *#registar,pagar,exportarTXT,factura
import tkinter as tk
from acciones import * 
def menu():
   
        bandera=False
        # Configuración de la ventana principal
        ventanaLogin = tk.Tk()
        ventanaLogin.title("Login")
        ventanaLogin.geometry("700x200+500+100")
        ventanaLogin.attributes('-topmost', True)  # Mantiene la ventana en la parte superior

        
        # Configuración de la ventana secundaria
        VentanaMenu = tk.Toplevel(ventanaLogin)
        VentanaMenu.title("Menu")
        VentanaMenu.withdraw()  # Oculta la ventana secundaria inicialmente

        # Botón en la ventana principal para ir a la secundaria
        botonIrSecundaria = tk.Button(ventanaLogin, text="Ir a menu", command= lambda:ir_a_ventana_secundaria(ventanaLogin,VentanaMenu,obtener_ancho_ventana(ventanaLogin)))
        botonIrSecundaria.pack(pady=20)

        # Botón en la ventana secundaria para volver a la principal
        botonVolverMenuPrincipal = tk.Button(VentanaMenu, text="Volver a login", command=lambda:volver_a_ventana_principal(ventanaLogin,VentanaMenu,obtener_ancho_ventana(VentanaMenu)))
        botonVolverMenuPrincipal.pack(pady=20)

        ventanaLogin.mainloop()
    
menu()