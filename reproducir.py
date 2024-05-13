import tkinter as tk
from acciones import mostrarEnPantalla,limpiar_texto
from tkinter import messagebox
from busqueda import buscarCancion
import os#Se utiliza para ver si existe el archivo

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
        cont=0
        if len(ColasDeReproduccion[prop])==1:
            temp=''
            for i in buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            mostrarEnPantalla(et1,f'1-{temp}')
            mostrarEnPantalla(et2,f'Espacio vacio')
            mostrarEnPantalla(et3,f'Espacio vacio')
            mostrarEnPantalla(et4,f'Espacio vacio')
            mostrarEnPantalla(et5,f'Espacio vacio')
        elif len(ColasDeReproduccion[prop])==2:
            temp=''
            for i in buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp2=''
            for i in buscarCancion(ColasDeReproduccion[prop][1],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp2+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            mostrarEnPantalla(et1,f'1-{temp}')
            mostrarEnPantalla(et2,f'2-{temp2}')
            mostrarEnPantalla(et3,f'Espacio vacio')
            mostrarEnPantalla(et4,f'Espacio vacio')
            mostrarEnPantalla(et5,f'Espacio vacio')
        elif len(ColasDeReproduccion[prop])==3:
            temp=''
            for i in buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp2=''
            for i in buscarCancion(ColasDeReproduccion[prop][1],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp2+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp3=''
            for i in buscarCancion(ColasDeReproduccion[prop][2],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp3+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            mostrarEnPantalla(et1,f'1-{temp}')
            mostrarEnPantalla(et2,f'2-{temp2}')
            mostrarEnPantalla(et3,f'3-{temp3}')
            mostrarEnPantalla(et4,f'Espacio vacio')
            mostrarEnPantalla(et5,f'Espacio vacio')
        elif len(ColasDeReproduccion[prop])==4:
            temp=''
            for i in buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp2=''
            for i in buscarCancion(ColasDeReproduccion[prop][1],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp2+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp3=''
            for i in buscarCancion(ColasDeReproduccion[prop][2],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp3+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp4=''
            for i in buscarCancion(ColasDeReproduccion[prop][3],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp4+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            mostrarEnPantalla(et1,f'1-{temp}')
            mostrarEnPantalla(et2,f'2-{temp2}')
            mostrarEnPantalla(et3,f'3-{temp3}')
            mostrarEnPantalla(et4,f'4-{temp4}')
            mostrarEnPantalla(et5,f'Espacio vacio')
        elif len(ColasDeReproduccion[prop])==5:
            temp=''
            for i in buscarCancion(ColasDeReproduccion[prop][0],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp2=''
            for i in buscarCancion(ColasDeReproduccion[prop][1],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp2+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp3=''
            for i in buscarCancion(ColasDeReproduccion[prop][2],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp3+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp4=''
            for i in buscarCancion(ColasDeReproduccion[prop][3],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp4+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            temp5=''
            for i in buscarCancion(ColasDeReproduccion[prop][4],diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)[0]:
                temp5+=i
                cont+=1
                if cont==10:
                    cont=0
                    break
            mostrarEnPantalla(et1,f'1-{temp}')
            mostrarEnPantalla(et2,f'2-{temp2}')
            mostrarEnPantalla(et3,f'3-{temp3}')
            mostrarEnPantalla(et4,f'4-{temp4}')
            mostrarEnPantalla(et5,f'5-{temp5}')
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
def reproductor(diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo,usuarioActual,ColasDeReproduccion,diccProptodo,diccAdmintodo):
    # Crear la ventana principal
    ventana = tk.Tk()
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
    mostrar=tk.Label(cola,text='Inserte el codigo de artista a agregar',font=("Times New Roman",10),bg="#D5CEC1")
    codArt=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codArt.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de album a agregar',font=("Times New Roman",10),bg="#D5CEC1")
    codAlb=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codAlb.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de genero a agregar',font=("Times New Roman",10),bg="#D5CEC1")
    codGen=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codGen.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de playlist a agregar',font=("Times New Roman",10),bg="#D5CEC1")
    codPlaylist=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codPlaylist.pack()
    mostrar=tk.Label(cola,text='Inserte el codigo de propietario a agregar',font=("Times New Roman",10),bg="#D5CEC1")
    codProp=tk.Entry(cola,font=("Times New Roman",10))
    mostrar.pack()
    codProp.pack()
    #Marco reproductor
    reproductor=tk.LabelFrame(ventana,text='Panel de reproduccion',font=("Times New Roman",15),padx=int(f'{cola.winfo_screenwidth()-1000}'),bg="#D5CEC1" )
    reproductor.grid(row=5,column=90)
    temp=tk.Label(reproductor, text="Aqui va todo para reproducirr\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",font=("Times New Roman",15),background='#D5CEC1')
    temp.pack(side='right',pady=(int(f'{cola.winfo_screenheight()}')//30,0))
    #Iniciar Etiquetas
    titulo=tk.Label(cola, text="La cola es:",font=("Times New Roman",15),background='#D5CEC1')
    titulo.pack(pady=(int(f'{cola.winfo_screenheight()}')//100,0))
    #Etiquetas para mostrara canciones en cola y botones para eliminar
    cancion1=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion1.pack(pady=(int(f'{cola.winfo_screenheight()}')//50,0),padx=20)
    eliminarCancion1 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,1),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion1.pack(side='left')
    eliminarCancion1.place(x=0, y=int(f'{cola.winfo_screenheight()}')-612)
    cancion2=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion2.pack(pady=(int(f'{cola.winfo_screenheight()}')//50,0),padx=20)
    eliminarCancion2 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,2),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion2.pack(side='left')
    eliminarCancion2.place(x=0, y=int(f'{cola.winfo_screenheight()}')-562)
    cancion3=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion3.pack(pady=(int(f'{cola.winfo_screenheight()}')//45,0),padx=20)
    eliminarCancion3 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,3),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion3.pack(side='left')
    eliminarCancion3.place(x=0, y=int(f'{cola.winfo_screenheight()}')-512)
    cancion4=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion4.pack(pady=(int(f'{cola.winfo_screenheight()}')//30,0),padx=20)
    eliminarCancion4 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,4),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion4.pack(side='left')
    eliminarCancion4.place(x=0, y=int(f'{cola.winfo_screenheight()}')-462)
    cancion5=tk.Label(cola, text="Espacio vacio",font=("Times New Roman",15),background='#D5CEC1')
    cancion5.pack(pady=(int(f'{cola.winfo_screenheight()}')//30,0),padx=20)
    eliminarCancion5 = tk.Button(cola, text="-",command=lambda:[vaciarCola(ColasDeReproduccion,usuarioActual,5),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    eliminarCancion5.pack(side='left')
    eliminarCancion5.place(x=0, y=int(f'{cola.winfo_screenheight()}')-402)
    #Boton para refrescar la cola
    actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)
    #boton agregar
    botonAgregar = tk.Button(cola, text="Insertar cancion a cola",command=lambda:[agregarACola(codigoCancion,codArt,codAlb,codGen,codPlaylist,codProp,diccCancionestodo,usuarioActual,ColasDeReproduccion,diccProptodo,diccAdmintodo),actualizarCola(ColasDeReproduccion,cancion1,cancion2,cancion3,cancion4,cancion5,usuarioActual,diccCancionestodo,diccArttodo,diccAlbumtodo,diccGentodo,diccPlaylisttodo)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonAgregar.pack(pady=(int(f'{cola.winfo_screenheight()}')//10,0))
    botonEmpezar = tk.Button(reproductor, text="empezar",command=lambda:[reproducirCancion('1',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonEmpezar.pack()
    botonPausar = tk.Button(reproductor, text="pausar",command=lambda:[reproducirCancion('pausar',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonPausar.pack()
    botonContinuar = tk.Button(reproductor, text="continuar",command=lambda:[reproducirCancion('continuar',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonContinuar.pack()
    botonSiguiente = tk.Button(reproductor, text="adelantar",command=lambda:[reproducirCancion('siguiente',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonSiguiente.pack()
    botonAtras = tk.Button(reproductor, text="atras",command=lambda:[reproducirCancion('atras',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonAtras.pack()
    botonPista3 = tk.Button(reproductor, text="pasar a 3",command=lambda:[reproducirCancion('3',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonPista3.pack()
    botonAdelantar = tk.Button(reproductor, text="adelanta10segs",command=lambda:[reproducirCancion('adelantar',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonAdelantar.pack()
    botonAtrasar = tk.Button(reproductor, text="atrasar10segs",command=lambda:[reproducirCancion('atrasar',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonAtrasar.pack()
    botonFinalizar = tk.Button(reproductor, text="Parar",command=lambda:[reproducirCancion('parar',ColasDeReproduccion,usuarioActual)],font=("Times New Roman",15),bg='#C1B2A6',fg='#102512')
    botonFinalizar.pack()
    # Iniciar el bucle de la ventana
    ventana.mainloop()



import pygame
from pygame import mixer
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
    mixer.music.pause()

# Función para reanudar la música
def continuar():
    mixer.music.unpause()

# Función para detener la música
def parar():
    mixer.quit()

# Función para reproducir una canción específica
def reproducir(numeroCancion,ColasDeReproduccion):
    global cancionActual, cancionAnterior
    cancionAnterior = cancionActual
    cancionActual = numeroCancion - 1  # Restar 1 porque las listas comienzan desde el índice 0
    if os.path.exists(ColasDeReproduccion[cancionActual]+'.wav'):
        mixer.music.load(ColasDeReproduccion[cancionActual]+'.wav')
    else:
        mixer.music.load(ColasDeReproduccion[cancionActual]+'.mp3')
    mixer.music.play()

# Función para reproducir la siguiente canción
def siguienteCancion(ColasDeReproduccion):
    global cancionActual
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




    