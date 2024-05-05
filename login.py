#Primer avance proyecto del reproductor de musica
#Estudiantes:
#Matthew Cordero Salazar
#Brian Ramirez Arias 
from busqueda import buscarProp #buscarProp
from acciones import *
def login(tipoUsuario,codigo,diccTodo,ventanaLogin,VentanaMenu):
    if codigo not in list(diccTodo.keys()) :
        print('RegiSTRARSE')
    elif codigo in list(diccTodo.keys()) and diccTodo[codigo]['estado']=='0':
        print('pAGAR')
    else:
         return irVentana(ventanaLogin,VentanaMenu,obtenerDimenciones(ventanaLogin))
def registar(diccTodo,diccMembresias):
    estado='0'
    nombre= str(input('\n-->Digite el nombre de propiertario: '))
    cod=1
    codMem=1
    while str(cod) in list(diccTodo.keys()):
        cod+=1
    while str(codMem) in list(diccMembresias.values()):
        codMem+=1
    diccTodo[str(cod)]={'nombre':nombre,'codMem':str(codMem),'estado':estado}#Añade  un propietario al dict
    diccMembresias[cod]=codMem
    print(f'\n---> El nuevo propietario se ha registrado')
    print('\nIMPORTANTE:\n')
    print(f'>>>Su codigo de propietario es: {cod}')
    print(f'\n>>>Su codigo de membresia es: {codMem}')

def factura(diccTodo,codigo):
    print('\n--- Factura ---\n')
    print('-----------------------------------------------')
    print('-->Identificacion propietario : ',codigo)
    print('-----------------------------------------------')
    print('-->Nombre propietario : ',diccTodo[codigo]['nombre'])
    print('-----------------------------------------------')
    print('-->Codigo de membresia: ',diccTodo[codigo]['codMem'])
    print('-----------------------------------------------')
    if diccTodo[codigo]['estado']=='0':
        print('-->Estado de membresia: INACTIVA')
    elif diccTodo[codigo]['estado']=='1':
        print('-->Estado de membresia: ACTIVA')
    print('-----------------------------------------------')
    print('-->Precio: $5/mes')
        
def exportarTXT(diccTodo,codigo,contFacturas):
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
    reporte.write('\n>>>Precio: $5/mes')
    reporte.close()#Cierra el archivo
    print(f'\n ---> La factura  se ha creado correctamente')
    
def pagar(diccTodo,diccMembresias,codigo):
    print('\n--- Pago ---\n')
    print('-----------------------------------------------')
    temp=str(input('Digite los ultimos cuatro digitos de su tarjeta: '))
    print('-----------------------------------------------')
    temp=str(input('\nDigite la fecha de vencimiento de su tarjeta(mes/año): '))
    print('-----------------------------------------------')
    temp=str(input('\nDigite sus 3 digitos de seguridad en su tarjeta: '))
    print('-----------------------------------------------')
    print('\n -->La cuenta a sido activada, disfrute del reproductor!')
    diccTodo[codigo]['estado']='1'
    diccMembresias[codigo]='1'
    
    

    


    