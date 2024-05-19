import tkinter as tk
from acciones import mostrarEnPantalla,limpiar_texto
from tkinter import messagebox
from busqueda import buscarCancion
import pygame
from pygame import mixer
import os#Se utiliza para ver si existe el archivo
def cortadorTexto(numerador,numCola,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo):#Se utiliza para mostrar solo 14 cracteres en la pantalla
    if type(buscarCancion(ColasDeReproduccion[prop][numCola],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo))==tuple:
        cont=0
        temp=''
        for i in buscarCancion(ColasDeReproduccion[prop][numCola],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
            temp+=i
            cont+=1
            if cont>=14 or temp==(buscarCancion(ColasDeReproduccion[prop][numCola],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]):
                return f"{numerador}-{temp}"
    else:
        return 'Espacio vacio'
#Agrega un cancion a cola y hace validaciones
def agregarACola(codigoCancion,codArt,codAlb,codGen,codPlaylist,codProp,diccCancionestodo,usuarioActual,ColasDeReproduccion,diccProptodo,diccAdmintodo):
    if usuarioActual not in list(ColasDeReproduccion.keys()) :
        ColasDeReproduccion[usuarioActual]=[]
    if len(ColasDeReproduccion[usuarioActual])>=5:#Validacion,--El codigo es el codProp que se logio--
        messagebox.showinfo("Alerta",'La cola de reproduccion ya esta en su limite, no se puede agregar mas canciones')
    elif codigoCancion.get() in list(diccCancionestodo.keys()) and diccCancionestodo[codigoCancion.get()]['codArt']==codArt.get() and diccCancionestodo[codigoCancion.get()]['codAlb']==codAlb.get() and diccCancionestodo[codigoCancion.get()]['codGen']==codGen.get() and diccCancionestodo[codigoCancion.get()]['codPlaylist']==codPlaylist.get() and ((codProp.get() in list(diccProptodo.keys()) and diccProptodo[codProp.get()]['estado']=='1')or codProp.get() in list(diccAdmintodo.keys()) ):
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
#Presenta un max de 10 caracteres en pantalla 
def actualizarCola(ColasDeReproduccion,et1,et2,et3,et4,et5,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo):
    if prop  in list(ColasDeReproduccion.keys()):
        eliminador=0
        for i in ColasDeReproduccion[prop]:#Elimina canciones de cola que son eliminadas eliminadas
            if i not in list(diccCancionestodo.keys()):
                ColasDeReproduccion[prop].pop(eliminador)
                eliminador+=1
        if len(ColasDeReproduccion[prop])==1:
            mostrarEnPantalla(et1,f'{cortadorTexto(1,0,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et2,f'Espacio vacio')
            mostrarEnPantalla(et3,f'Espacio vacio')
            mostrarEnPantalla(et4,f'Espacio vacio')
            mostrarEnPantalla(et5,f'Espacio vacio')
        elif len(ColasDeReproduccion[prop])==2:
            mostrarEnPantalla(et1,f'{cortadorTexto(1,0,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et2,f'{cortadorTexto(2,1,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et3,f'Espacio vacio')
            mostrarEnPantalla(et4,f'Espacio vacio')
            mostrarEnPantalla(et5,f'Espacio vacio')
        elif len(ColasDeReproduccion[prop])==3:
            mostrarEnPantalla(et1,f'{cortadorTexto(1,0,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et2,f'{cortadorTexto(2,1,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et3,f'{cortadorTexto(3,2,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et4,f'Espacio vacio')
            mostrarEnPantalla(et5,f'Espacio vacio')
        elif len(ColasDeReproduccion[prop])==4:
            mostrarEnPantalla(et1,f'{cortadorTexto(1,0,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et2,f'{cortadorTexto(2,1,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et3,f'{cortadorTexto(3,2,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et4,f'{cortadorTexto(4,3,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et5,f'Espacio vacio')
        elif len(ColasDeReproduccion[prop])==5:
            mostrarEnPantalla(et1,f'{cortadorTexto(1,0,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et2,f'{cortadorTexto(2,1,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et3,f'{cortadorTexto(3,2,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et4,f'{cortadorTexto(4,3,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
            mostrarEnPantalla(et5,f'{cortadorTexto(5,4,ColasDeReproduccion,prop,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)}')
        else:
            mostrarEnPantalla(et1,f'Espacio vacio')
            mostrarEnPantalla(et2,f'Espacio vacio')
            mostrarEnPantalla(et3,f'Espacio vacio')
            mostrarEnPantalla(et4,f'Espacio vacio')
            mostrarEnPantalla(et5,f'Espacio vacio')
#Vacia cola deacuerdo a la cancion que el usaurio quiera
def vaciarCola(ColasDeReproduccion,usuarioActual,numCancion):
    if numCancion==1 and len(ColasDeReproduccion[usuarioActual])>=1:
        ColasDeReproduccion[usuarioActual].pop(0)
    if numCancion==2 and len(ColasDeReproduccion[usuarioActual])>=2:
        ColasDeReproduccion[usuarioActual].pop(1)
    if numCancion==3 and len(ColasDeReproduccion[usuarioActual])>=3:
        ColasDeReproduccion[usuarioActual].pop(2)
    if numCancion==4 and len(ColasDeReproduccion[usuarioActual])>=4:
        ColasDeReproduccion[usuarioActual].pop(3)
    if numCancion==5 and len(ColasDeReproduccion[usuarioActual])>=5:
        ColasDeReproduccion[usuarioActual].pop(4)

def reproductor(VentanaMenu,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo,usuarioActual,ColasDeReproduccion,diccProptodo,diccAdmintodo):
    # Crear la ventana principal
    ventana = tk.Toplevel(VentanaMenu)
    ventana.title("Reproductor")
    ventana.configure(bg="#D5CEC1")
    ventana.geometry(f"{ventana.winfo_screenwidth()-200}x{ventana.winfo_screenheight()-200}")
    ventana.resizable(False, False)
    #Marco cola
    cola=tk.LabelFrame(ventana,text='Cola de reproduccion', font=("Times New Roman",12),bg="#D5CEC1",width=int(f'{ventana.winfo_screenwidth()}')//10,height=1000)
    cola.grid(row=5,column=1)
    #Caja para recibir codigo
    mostrar=tk.Label(cola,text='Inserte el codigo de cancion a agregar',font=("Times New Roman",10),bg="#D5CEC1")
    codigoCancion=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codigoCancion.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de artista vinculado',font=("Times New Roman",10),bg="#D5CEC1")
    codArt=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codArt.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de album vinculado',font=("Times New Roman",10),bg="#D5CEC1")
    codAlb=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codAlb.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de genero vinculado',font=("Times New Roman",10),bg="#D5CEC1")
    codGen=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codGen.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de playlist vinculado',font=("Times New Roman",10),bg="#D5CEC1")
    codPlaylist=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codPlaylist.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de propietario actual',font=("Times New Roman",10),bg="#D5CEC1")
    codProp=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codProp.pack()
    #Marco reproductor
    reproductor=tk.LabelFrame(ventana,text='Panel de reproduccion',font=("Times New Roman",15),bg="#D5CEC1" )
    reproductor.grid(row=5,column=90)
    #Iniciar Etiquetas
    titulo=tk.Label(cola, text="La cola es:",font=("Times New Roman",15),background='#D5CEC1')
    titulo.pack(pady=(int(f'{cola.winfo_screenheight()}')//100,0))
    
    #Etiquetas para mostrara canciones en cola y botones para eliminar
    cancion1=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion1.pack()
    cancion1.place(x=50, y=int(f'{cola.winfo_screenheight()}')-562)
    eliminarCancion1 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,1),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion1.pack(side='left')
    eliminarCancion1.place(x=0, y=int(f'{cola.winfo_screenheight()}')-562)
    ###
    cancion2=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion2.pack()
    cancion2.place(x=50, y=int(f'{cola.winfo_screenheight()}')-512)
    eliminarCancion2 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,2),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion2.pack(side='left')
    eliminarCancion2.place(x=0, y=int(f'{cola.winfo_screenheight()}')-512)
    ###
    cancion3=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion3.pack()
    cancion3.place(x=50, y=int(f'{cola.winfo_screenheight()}')-462)
    eliminarCancion3 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,3),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion3.pack(side='left')
    eliminarCancion3.place(x=0, y=int(f'{cola.winfo_screenheight()}')-462)
    ###
    cancion4=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion4.pack()
    cancion4.place(x=50, y=int(f'{cola.winfo_screenheight()}')-402)
    eliminarCancion4 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,4),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion4.pack(side='left')
    eliminarCancion4.place(x=0, y=int(f'{cola.winfo_screenheight()}')-402)
    ###
    cancion5=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion5.pack()
    cancion5.place(x=50, y=int(f'{cola.winfo_screenheight()}')-352)
    eliminarCancion5 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,5),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion5.pack(side='left')
    eliminarCancion5.place(x=0, y=int(f'{cola.winfo_screenheight()}')-352)
    actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)
    #boton agregar
    botonAgregar = tk.Button(cola, text="Insertar cancion a cola",command=lambda:[agregarACola(codigoCancion,codArt,codAlb,codGen,codPlaylist,codProp,diccCancionestodo,usuarioActual,ColasDeReproduccion,diccProptodo,diccAdmintodo),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonAgregar.pack(pady=(int(f'{cola.winfo_screenheight()}')-560,0))
    
    reproductor.Empezarpng = tk.PhotoImage(file='./Empezar.png')
    BotonEmpezar = tk.Button(reproductor, image=reproductor.Empezarpng,command=lambda:reproducirCancion('1', ColasDeReproduccion, usuarioActual))#,command=lambda:)
    BotonEmpezar.configure(width=110, height=107)
    BotonEmpezar.grid(row=0,column=2, padx=((int(f'{cola.winfo_screenwidth()}')-1300),10))
    

    reproductor.Pausarpng = tk.PhotoImage(file='./Pausar.png')
    botonPausar = tk.Button(reproductor, image=reproductor.Pausarpng,command=lambda:reproducirCancion('pausar',ColasDeReproduccion,usuarioActual))#,command=lambda:)
    botonPausar.configure(width=110, height=110)
    botonPausar.grid(row=0,column=3, padx=10, pady=(int(f'{cola.winfo_screenheight()}')-900,20))
    
        
    reproductor.Continuarpng = tk.PhotoImage(file='./Unpausar.png')
    botonContinuar = tk.Button(reproductor, image=reproductor.Continuarpng,command=lambda:[reproducirCancion('continuar',ColasDeReproduccion,usuarioActual)])
    botonContinuar.configure(width=110, height=110)
    botonContinuar.grid(row=0,column=4, padx=10, pady=(int(f'{cola.winfo_screenheight()}')-900,20))
    

    reproductor.Pararpng = tk.PhotoImage(file='./Parar.png')
    botonPararpng = tk.Button(reproductor, image=reproductor.Pararpng,command=lambda:[reproducirCancion('parar',ColasDeReproduccion,usuarioActual)])
    botonPararpng.configure(width=110,height=110)
    botonPararpng.grid(row=0,column=5, padx=(10), pady=(int(f'{cola.winfo_screenheight()}')-900,20))
  
    reproductor.Siguientepng = tk.PhotoImage(file='./Adelantar1.png')
    botonSiguiente = tk.Button(reproductor, image=reproductor.Siguientepng,command=lambda:[reproducirCancion('siguiente',ColasDeReproduccion,usuarioActual)])
    botonSiguiente.configure(width=110,height=110)
    botonSiguiente.grid(row=1,column=3, padx=(10), pady=(20))

    reproductor.atraspng = tk.PhotoImage(file='./Atrasar1.png')
    botonAtras = tk.Button(reproductor, image=reproductor.atraspng,command=lambda:[reproducirCancion('atras',ColasDeReproduccion,usuarioActual)])
    botonAtras.configure(width=110,height=110)
    botonAtras.grid(row=1,column=4,padx=10, pady=20)

    reproductor.adelantar10png = tk.PhotoImage(file='./Adelantar10.png')
    botonAdelantar10 = tk.Button(reproductor, image=reproductor.adelantar10png,command=lambda:[reproducirCancion('adelantar',ColasDeReproduccion,usuarioActual)])
    botonAdelantar10.configure(width=110,height=110)
    botonAdelantar10.grid(row=2,column=3,padx=10, pady=20)

    reproductor.Retroceder10png = tk.PhotoImage(file='./Retroceder10.png')
    botonRetroceder10png = tk.Button(reproductor, image=reproductor.Retroceder10png,command=lambda:[reproducirCancion('atrasar',ColasDeReproduccion,usuarioActual)])
    botonRetroceder10png.configure(width=110,height=110)
    botonRetroceder10png.grid(row=2,column=4, padx=(10,0), pady=10)
    
    reproductor.ir1png = tk.PhotoImage(file='./PasarA1.png')
    botonIR1 = tk.Button(reproductor, image=reproductor.ir1png,command=lambda:[reproducirCancion('1',ColasDeReproduccion,usuarioActual)])
    botonIR1.configure(width=110,height=110)
    botonIR1.grid(row=3,column=2, padx=(150,10))

    reproductor.ir2png = tk.PhotoImage(file='./PasarA2.png')
    botonIR2 = tk.Button(reproductor, image=reproductor.ir2png,command=lambda:[reproducirCancion('2',ColasDeReproduccion,usuarioActual)])
    botonIR2.configure(width=110,height=110)
    botonIR2.grid(row=3,column=3,padx=10, pady=20)

    reproductor.ir3png = tk.PhotoImage(file='./PasarA3.png')
    botonIR3 = tk.Button(reproductor, image=reproductor.ir3png ,command=lambda:[reproducirCancion('3',ColasDeReproduccion,usuarioActual)])
    botonIR3.configure(width=110,height=110)
    botonIR3.grid(row=3,column=4,padx=10, pady=20)
    
    reproductor.ir4png = tk.PhotoImage(file='./PasarA4.png')
    botonIR4 = tk.Button(reproductor, image=reproductor.ir4png,command=lambda:[reproducirCancion('4',ColasDeReproduccion,usuarioActual)])
    botonIR4.configure(width=110,height=110)
    botonIR4.grid(row=3,column=5,padx=10, pady=20)

    reproductor.ir5png = tk.PhotoImage(file='./PasarA5.png')
    botonIR5 = tk.Button(reproductor, image=reproductor.ir5png,command=lambda:[reproducirCancion('5',ColasDeReproduccion,usuarioActual)])
    botonIR5.configure(width=110,height=110)
    botonIR5.grid(row=3,column=6, padx=(10,(int(f'{cola.winfo_screenwidth()}')-900)), pady=10)
    
   
    


# Índice de la canción actual y anterior
cancionActual = 0
cancionAnterior = 0

# Función para avanzar rápidamente el archivo de música
def adelantar():
    tiempoActual = mixer.music.get_pos() /500 # Obtener la posición actual de reproducción en segundos
    tiempoNuevo = tiempoActual + 10  # Calcular la nueva posición después de avanzar rápidamente
    mixer.music.set_pos(tiempoNuevo)  # Establecer la nueva posición
def atrasar():
    tiempoActual = mixer.music.get_pos() /700 # Obtener la posición actual de reproducción en segundos
    tiempoNuevo = max(0, tiempoActual - 10)
    mixer.music.set_pos(tiempoNuevo)  # Establecer la nueva posición

# Función para pausar la música
def pausar():
    if pygame.mixer.music.get_busy():
        mixer.music.pause()

# Función para reanudar la música
def continuar():
    mixer.music.unpause()

# Función para detener la música
def parar():
    if pygame.mixer.music.get_busy():
        mixer.quit()
        
modaMusica=[]
# Función para reproducir una canción específica
def reproducir(numeroCancion,ColasDeReproduccion):
    global cancionActual, cancionAnterior,modaMusica
    cancionAnterior = cancionActual
    cancionActual = numeroCancion - 1  # Restar 1 porque las listas comienzan desde el índice 0
    modaMusica+=[cancionActual]#Almacena para tendencias
    if os.path.exists(ColasDeReproduccion[cancionActual]+'.wav'):
        mixer.music.load(ColasDeReproduccion[cancionActual]+'.wav')
    else:
        mixer.music.load(ColasDeReproduccion[cancionActual]+'.mp3')
    mixer.music.play()

# Función para reproducir la siguiente canción
def siguienteCancion(ColasDeReproduccion):
    global cancionActual,cancionAnterior
    cancionAnterior=cancionActual
    cancionActual = (cancionActual + 1) % len(ColasDeReproduccion)
    if os.path.exists(ColasDeReproduccion[cancionActual]+'.wav'):
        mixer.music.load(ColasDeReproduccion[cancionActual]+'.wav')
    else:
        mixer.music.load(ColasDeReproduccion[cancionActual]+'.mp3')
    mixer.music.play()
    

# Función para reproducir la canción anterior
def previaCancion(ColasDeReproduccion):
    global cancionActual
    cancionActual = cancionAnterior
    if os.path.exists(ColasDeReproduccion[cancionActual]+'.wav'):
        mixer.music.load(ColasDeReproduccion[cancionActual]+'.wav')
    else:
        mixer.music.load(ColasDeReproduccion[cancionActual]+'.mp3')
    mixer.music.play()
    
def reproducirCancion(accion,ColasDeReproduccion,prop):
    if prop in list(ColasDeReproduccion.keys()):
        if len(ColasDeReproduccion[prop])>0:
            mixer.init()
            if accion == 'adelantar':
                adelantar()  
            elif accion == 'atrasar':
                atrasar() 
            elif accion == 'pausar':
                pausar()
            elif accion == 'continuar':
                continuar()
            elif accion == 'parar':
                parar()
            elif accion == 'siguiente':
                siguienteCancion(ColasDeReproduccion[prop])
            elif accion == 'atras':
                previaCancion(ColasDeReproduccion[prop])
            elif accion.isdigit():
                numeroCancion = int(accion)
                if  numeroCancion <= len(ColasDeReproduccion[prop]):
                    reproducir(numeroCancion,ColasDeReproduccion[prop])
        elif accion == 'parar':
            parar()
        elif accion == 'pausar':
            pausar()




    