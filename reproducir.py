import tkinter as tk
from acciones import mostrarEnPantalla,limpiar_texto
from tkinter import messagebox
from busqueda import buscarCancion
def agregarACola(codigoCancion,codArt,codAlb,codGen,codPlaylist,codProp,diccCancionestodo,usuarioActual,ColasDeReproduccion,diccProptodo):
    if usuarioActual not in list(ColasDeReproduccion.keys()):
        ColasDeReproduccion[usuarioActual]=[]
    if len(ColasDeReproduccion[usuarioActual])>=5:#Validacion,--El codigo es el codProp que se logio--
        messagebox.showinfo("Alerta",'La cola de reproduccion ya esta en su limite, no se puede agregar mas canciones')
    elif codigoCancion.get() in list(diccCancionestodo.keys()) and diccCancionestodo[codigoCancion.get()]['codArt']==codArt.get() and diccCancionestodo[codigoCancion.get()]['codAlb']==codAlb.get() and diccCancionestodo[codigoCancion.get()]['codGen']==codGen.get() and diccCancionestodo[codigoCancion.get()]['codPlaylist']==codPlaylist.get() and codProp.get() in list(diccProptodo.keys()) and diccProptodo[codProp.get()]['estado']=='1':
        if codProp.get()==usuarioActual:
            ColasDeReproduccion[usuarioActual]+=[codigoCancion.get()]#Agrega a la lista
            messagebox.showinfo("Confirmacion",f'Se ha agregado la cancion con el codigo: {codigoCancion.get()} a la cola de reproduccion, actualize para ver cambios!')
            limpiar_texto(codProp)
            limpiar_texto(codArt)
            limpiar_texto(codAlb)
            limpiar_texto(codGen)
            limpiar_texto(codPlaylist)
            limpiar_texto(codigoCancion)
        else: 
            messagebox.showinfo("Alerta","El codigo del propietario que digito no es el mismo que inicio sesion, por favor ingrese el codigo del propietario actual!")
            limpiar_texto(codProp)
    else:
        messagebox.showinfo("Alerta", "Cancion inexsistente o los datos relacionados son incorrectos!")
        limpiar_texto(codigoCancion)
        
def actualizarCola(ColasDeReproduccion,et1,et2,et3,et4,et5,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo):
    if len(ColasDeReproduccion[prop])==1:
        mostrarEnPantalla(et1,f'1-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
    elif len(ColasDeReproduccion[prop])==2:
        mostrarEnPantalla(et1,f'1-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et2,f'2-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
    elif len(ColasDeReproduccion[prop])==3:
        mostrarEnPantalla(et1,f'1-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et2,f'2-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et3,f'3-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
    elif len(ColasDeReproduccion[prop])==4:
        mostrarEnPantalla(et1,f'1-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et2,f'2-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et3,f'3-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et4,f'4-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
    elif len(ColasDeReproduccion[prop])==5:
        mostrarEnPantalla(et1,f'1-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et2,f'2-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et3,f'3-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et4,f'4-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
        mostrarEnPantalla(et5,f'5-{buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]}')
def reproductor(diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo,usaurioActual,ColasDeReproduccion,diccProptodo):
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Barra de Navegación")
    ventana.geometry(f"{ventana.winfo_screenwidth()}x{ventana.winfo_screenheight()}")
    #Marco cola
    cola=tk.LabelFrame(ventana,text='Cola de reproduccion',width=int(f'{ventana.winfo_screenwidth()}')//10,height=1000)
    cola.grid(row=5,column=1)
    #Caja para recibir codigo
    mostrar=tk.Label(cola,text='Inserte el codigo de cancion a agregar')
    codigoCancion=tk.Entry(cola)
    mostrar.pack()
    codigoCancion.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de artista a agregar')
    codArt=tk.Entry(cola)
    mostrar.pack()
    codArt.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de album a agregar')
    codAlb=tk.Entry(cola)
    mostrar.pack()
    codAlb.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de genero a agregar')
    codGen=tk.Entry(cola)
    mostrar.pack()
    codGen.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de playlist a agregar')
    codPlaylist=tk.Entry(cola)
    mostrar.pack()
    codPlaylist.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de propietario a agregar')
    codProp=tk.Entry(cola)
    mostrar.pack()
    codProp.pack()
    
    #Marco reproductor
    reproductor=tk.LabelFrame(ventana,text='Marco',padx=int(f'{ventana.winfo_screenwidth()}')//3 )
    reproductor.grid(row=5,column=90)
    en2=tk.Entry(reproductor)
    en2.pack()
    #boton agregar
    botonAgregar = tk.Button(cola, text="Insertar cancion",command=lambda:[agregarACola(codigoCancion,codArt,codAlb,codGen,codPlaylist,codProp,diccCancionestodo,usaurioActual,ColasDeReproduccion,diccProptodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonAgregar.pack(pady=int(f'{ventana.winfo_screenheight()}')//50)
    #Iniciar Etiquetas
    titulo=tk.Label(cola, text="La cola es",font=("Times New Roman",15),background='#D5CEC1')
    titulo.pack(pady=(int(f'{ventana.winfo_screenheight()}')//100,0))
    #Etiquetas para mostrara canciones en cola
    cancion1=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion1.pack(pady=(int(f'{ventana.winfo_screenheight()}')//20,0))
    cancion2=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion2.pack(pady=(int(f'{ventana.winfo_screenheight()}')//20,0))
    cancion3=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion3.pack(pady=(int(f'{ventana.winfo_screenheight()}')//20,0))
    cancion4=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion4.pack(pady=(int(f'{ventana.winfo_screenheight()}')//20,0))
    cancion5=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion5.pack(pady=(int(f'{ventana.winfo_screenheight()}')//20,int(f'{ventana.winfo_screenheight()}')//3000))
    #Boton para refrescar la cola
    botonActualizar = tk.Button(cola, text="Actualizar cola",command=lambda:actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usaurioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo),font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonActualizar.pack(pady=(int(f'{ventana.winfo_screenheight()}')//50,int(f'{ventana.winfo_screenheight()}')//50))
    # Iniciar el bucle de la ventana
    ventana.mainloop()



