import tkinter
from tkinter import*
import itertools
import os
import platform

#funcion para abrir ventana de ayuda
def ayudame():
    so = platform.system()
    o = os.path.abspath('Manual_de_usuario_de_Torneos.pdf')
    if so == 'Darwin':
        messagebox.showinfo(title='Programa de torneos de bola',message='Autor: Jose Pablo Murillo\n'
                                                                                'Fecha: Abril 2014\n'
                                                                                'Este programa sirve para hacer torneos de bola.')
        os.system('open Manual_de_usuario_de_Torneos.pdf')
        
    elif so == 'Windows':
        messagebox.showinfo(title='Programa de torneos de bola',message='Autor: Jose Pablo Murillo\n'
                                                                            'Fecha: Abril 2014\n'
                                                                            'Este programa sirve para hacer torneos de bola.')
        os.startfile('Manual_de_usuario_de_Torneos.pdf')

    else:
        messagebox.showinfo(title='Programa de torneos de bola',message='La funcion de abrir el pdf no esta posible en tu sistema operativo, debe abrir el archivo de manera manual')
        return
        
        
    
    return

#funcion para no destruir ventanas
def nosalir():
    messagebox.showinfo(title='Ventana de advertencia',message='No puede salir de esta manera,debe salir desde el menu principal')

###funciones ventana principal###
#Salir ventana principal
def salir():
    dec = messagebox.askquestion(title='Pregunta de cerrar',message='Esta seguro que quiere salir de la ventana?',icon = 'warning')
    if dec == 'yes':
        messagebox.showinfo(title='Aplicacion de futbol',message='Gracias por haber usado Goles v1.0')
        app.destroy()
        return
    else:
        return

#funcion salir de copia de ventana de configuracion
def salir2():
    config2.withdraw()
    app.deiconify()
    return

###funciones ventana de configuracion
#cancelar de menu config
def cancelar():
    nombre.set('')
    cantequipos.set('')
    cantclas.set('')
    cantgana.set('')
    cantempate.set('')
    config.withdraw()
    app.deiconify()

#aparecer menu config
def menuconfig():
    global configurar
    if configurar == False:
        app.withdraw()
        config.deiconify()
    else:
        app.withdraw()
        config2.deiconify()
        configl = Label(config2,text='Configuracion torneos de futbol').grid(row=0,column=1)
        configl2 = Label(config2,text='Datos Generales').grid(row=1,column=1)
        torneol = Label(config2,text='Nombre del torneo:').grid(row=2)
        a = nombre.get()
        etorneo = Entry(config2)
        etorneo.insert(0,a)
        etorneo.config(state='readonly')
        etorneo.grid(row=2,column=1)
        cant = Label(config2,text='Cantidad de equipos participantes:').grid(row=3,column=0)
        b = cantequipos.get()
        ecant = Entry(config2)
        ecant.insert(0,b)
        ecant.config(state='readonly')
        ecant.grid(row=3,column=1)
        clas = Label(config2,text='Cantidad de equipos que clasifican directamente:').grid(row=4,column=0)
        c = cantclas.get()
        eclas = Entry(config2)
        eclas.insert(0,c)
        eclas.config(state='readonly')
        eclas.grid(row=4,column=1)
        pganar = Label(config2,text='Puntos ganados por cada partido ganado:').grid(row=5,column=0)
        d = cantgana.get()
        eganar = Entry(config2)
        eganar.insert(0,d)
        eganar.config(state='readonly')
        eganar.grid(row=5,column=1)
        pempate = Label(config2,text='Puntos ganados por cada partido empatado:').grid(row=6,column=0)
        e = cantempate.get()
        eempate = Entry(config2)
        eempate.insert(0,e)
        eempate.config(state='readonly')
        eempate.grid(row=6,column=1)
        acept = Button(config2,text='Salir',command=salir2).grid(row=7)

#Validar datos de entrada de configuracion
def validar():
    a = nombre.get()
    b = cantequipos.get()
    c = cantclas.get()
    d = cantgana.get()
    e = cantempate.get()
    global configurar
    

    #Validacion nombre y cantidad de equipos
    if a != '':
        if len(a) >= 2 and len(a) <= 40:
            if b != '':
                try:
                    b = int(b)
                    if b >= 2:
                        if b%2 == 0:
                            pass
                        else:
                            messagebox.showerror(title ='Error en cantidad de equipos',message='La cantidad de quipos debe ser par')
                            return
                    else:
                        messagebox.showerror(title = 'Erorr en cantidad de quipos',message = 'La cantidad de equipos debe ser mayor o igual a 2')
                        return
                except ValueError:
                    messagebox.showerror(title = 'Error en cantidad de equipos',message = 'La cantidad de equipos no es un numero entero')
                    return
            else:
                messagebox.showerror(title='Error en ingreso de  cantidad de equipos',message='Debe ingresar un numero')
                return
        else:
            messagebox.showerror(title = 'Error en el nombre del torneo',message = 'El nombre debe ser entre 2 y 40 caracteres')
            return
    else:
        messagebox.showerror(title='Error en ingreso de nombre de campeonato',message='El campeonato debe tener un nombre')
        return

    #Validacion equipos a clasificar
    if c != '':
        try:
            c = int(c)
            if c >= 1:
                if c < b:
                    pass
                else:
                    messagebox.showerror(title='Error en cantidad de equipos que clasifican',message='El numero debe ser menor que la cantidad de equipos')
                    return
            else:
                messagebox.showerror(title='Error en cantidad de equipos que clasifican',message = 'El numero debe ser mayor o igual a 1')
                return
        except ValueError:
            messagebox.showerror(title = 'Error en cantidad de equipos que clasifican',message = 'La entrada debe ser un numero entero mayor o igual a 1')
            return
    else:
        messagebox.showerror(title='Error en ingreso de equipos que clasifican directamente',message = 'Debe haber una cantidad de quipos')
        return

    #Validacion puntos ganados
    if d != '':
        try:
            d = int(d)
            if d >= 1:
                pass
            else:
                messagebox.showerror(title='Error en cantidad de puntos por cada partido ganado',message = 'El numero debe ser mayor o igual a 1')
                return
        except ValueError:
            messagebox.showerror(title = 'Error en cantidad de puntos por cada partido ganado:',message = 'La entrada no es un numero')
            return
    else:
        messagebox.showerror(title='Error en puntos ganados por cada partido ganado',message='La cantidad de puntos debe ser una entrada numerica')
        return
    

    #Validacion puntos empate
    if e != '':
        try:
            e = int(e)
            if e >= 1:
                pass
            else:
                messagebox.showerror(title='Error en cantidad de puntos por cada partido empatado',message = 'El numero debe se mayor o igual a 1')
                return
        except ValueError:
            messagebox.showerror(title='Error en cantidad de puntos por cada partido empatado',message = 'La entrada debe ser un numero entero')
            return
    else:
        messagebox.showerror(title='Error en cantidad de puntos de empate',message='Debe haber una cantidad numerica para los puntos de empate')
        return

    if a != '' and b != '' and c != '' and d != '' and e != '':
        messagebox.showinfo(title='Ingreso de datos',message='Los datos de configuracion han sido ingresados con exito')
        configurar = True
        config.withdraw()
        ventequipos.deiconify()
    else:
        messagebox.showerror(title='Error en ingreso de datos',message='Debe ingresar todos los datos solicitados')
        return

###funciones de ventana de equipos

#funcion para cancelar ingreso de equipos y regresar a menu principal
def cancelar7():
    global configurar
    global equipos
    global codigos
    global paises
    paises = []
    codigos = []
    equipos = []
    codigo.set('')
    equipo.set('')
    nombre.set('')
    cantequipos.set('')
    cantclas.set('')
    cantgana.set('')
    cantempate.set('')
    messagebox.showinfo(title='Ventana de creacion de equipos',message='La configuracion ha sido eliminada')
    ventequipos.withdraw()
    configurar = False
    app.deiconify()
    return


        
#funcion para cancelar adicion a equipo
def cancelar2():
    codigo.set('')
    equipo.set('')
    messagebox.showinfo(title='informacion de equipo',message = 'El equipo no fue agregado')
    confirmar.withdraw()
    ventequipos.deiconify()

#funcion para cancelar consulta de equipo
def cancelar3():
    codigo.set('')
    consulta.withdraw()
    ventequipos.deiconify()
    

#funcion de confirmar ingreso de equipo
def confirma(codigo,equipo):
    ventequipos.withdraw()
    confirmar.deiconify()
    confirmar.title('Lista de equipos')
    confirmarl = Label(confirmar,text ='Esta apunto de agregar:').grid(row=0)
    confirmarl1 = Label(confirmar,text='Codigo de equipo:' + '  ' + codigo).grid(row=1)
    confirmarl2 = Label(confirmar,text='Nombre de equipo:' + '  ' + equipo).grid(row=2)
    acept = Button(confirmar,text='aceptar',command = agregar).grid(row=3)
    cancel = Button(confirmar,text='Cancelar',command = cancelar2).grid(row=3,column=1)


#funcion de validar equipo       
def validaequipo():
    cod = codigo.get()
    equi = equipo.get() 
    global equipos
    cantidadequipos = int(cantequipos.get())
    if len(cod) == 3:
        if len(equi) >= 5 and len(equi) <= 40:
            if cantidadequipos != len(equipos):
                if (cod,equi) not in equipos:
                    a = equipos
                    while a != []:
                        if cod == a[0][0] or equi == a[0][1]:
                            messagebox.showinfo(title='Error en ingreso de equipo',message='No pueden haber codigos ni equipos repetidos')
                            codigo.set('')
                            equipo.set('')
                            return
                        else:
                            a = a[1:]                            
                    return confirma(cod,equi)
                else:
                    messagebox.showerror(title='Error en entrada de codigo y equipo',message = 'Este equipo ya ha sido ingresado')
                    codigo.set('')
                    equipo.set('')
                    return
            else:
                messagebox.showerror(title='Error en cantidad de quipo',message='el equipo que desea agregar supera la cantidad maxima de equipos')
                codigo.set('')
                equipo.set('')
                return
        else:
            messagebox.showerror(title='Error en nombre de equipo',message = 'El nombre del equipo debe ser entre 5 y 40 caracteres')
            equipo.set('')
            return
    else:
        messagebox.showerror(title='Error en codigo de equipo',message = 'El codigo del equipo debe ser de 3 caracteres')
        codigo.set('')
        return
            

#Funcion de agregar equipo
def agregar():
    cantidadequipos = int(cantequipos.get())
    global codigos
    cod = codigo.get()
    equi = equipo.get()
    global equipos
    if cantidadequipos != 0:
        equipos = equipos + [(cod,equi)]
        codigos = codigos + [cod]
        cantidadequipos -= 1
        messagebox.showinfo(title='Agregar equipo',message = cod + ':' + equi + ', ha sido agregado con exito!')
        codigo.set('')
        equipo.set('')
        confirmar.withdraw()
        ventequipos.deiconify()
    else:
        messagebox.showinfo(title='Ventana de agregar equipos',message='El equipo que desea agregar supera la cantidad establecida de equipos')
        codigo.set('')
        equipo.set('')
        confirmar.withdraw()
        ventequipos.deiconify()


###funciones ventana de consultar equipo
#funcion consultar equipo
def consultar():
    ventequipos.withdraw()
    consulta.deiconify()
    consulta.title('Ventana de consulta de equipos')
    l1 = Label(consulta, text = 'Ingrese el codigo del equipo que desea consultar')
    l2 = Label(consulta,text='Codigo de equipo').grid(row=0)
    e1 = Entry(consulta,textvariable=codigo).grid(row=0,column=1)
    b1 = Button(consulta,text='Consultar',command = consultaux).grid(row=2,column=1)
    b2 = Button(consulta,text='Cancelar',command = cancelar3).grid(row=2,column=2)


#funcion consultar equipo auxiliar
def consultaux():
    c = codigo.get()
    global equipos
    e = list(equipos)
    if e == []:
        messagebox.showinfo(title='Ventana de consulta de equipos',message = 'No hay equipos registrados')
        codigo.set('')
        equipo.set('')
        consulta.withdraw()
        ventequipos.deiconify()
    else:
        while e != []:
            if c == e[0][0]:
                messagebox.showinfo(title='Ventana de consulta de equipos',message = 'El equipo correspondiente al codigo es' + '   ' + e[0][1])
                codigo.set('')
                de = messagebox.askquestion(title='ventana de consulta de qeuipos',message = 'Desea consultar otro equipo?')
                if de == 'yes':
                    codigo.set('')
                    return                    
                else:
                    consulta.withdraw()
                    ventequipos.deiconify()
                    return
            else:
                e = e[1:]
        consulta.withdraw()
        messagebox.showinfo(title = 'Ventana de consulta de quipos',message = 'Este equipo no esta registrado, no se puede consultar')
        ventequipos.deiconify()
        codigo.set('')
        equipo.set('')
        consulta.withdraw()

###funciones de ventana de modificar
        
#funcion cancelar de ventana de modificar
def cancelar4():
    codigo.set('')
    modificacion.withdraw()
    ventequipos.deiconify()

def cancelar5():
    nuevoequipo.set('')
    modi.withdraw()
    ventequipos.deiconify()

#funcion para salir de ventana de equipos aceptando la lista de equipos
def salir3():
    global equipos
    global configurar
    if len(equipos) < int(cantequipos.get()):
        messagebox.showinfo(title='Ventana de equipos',message='La cantidad de equipos es menor que la cantidad de la configuracion')
        return
    elif len(equipos) > int(cantequipos.get()):
        messagebox.showinfo(title='Ventana de equipos',message = 'La cantidad de equipos ingresados supera la cantidad maxima de la configuracion establecida')
        return
    else:
        configurar = True
        ventequipos.withdraw()
        app.deiconify()

#funcion de modificacion auxiliar2
def modificaux():
    global equipos
    nuevo = nuevoequipo.get()
    e = tuple(equipos)
    c = tuple(equipos)
    cod = codigo.get()
    if len(nuevo) >= 5 and len(nuevo) <= 40:
        if nuevo in e:
            messagebox.showinfo(title='Ventana de modificacion de equipos',message='El nombre del equipo ya existe')
            nuevoequipo.set('')
            return          
        cont = 0
        while c != []:
            if cod == c[0][0]:
                equipos[cont] = list(equipos[cont])
                equipos[cont][1] = nuevo
                equipos[0] = tuple(equipos[cont])
                messagebox.showinfo(title='Ventana de modificacion de equipos',message='El nombre del equipo ha sido cambiado con exito!')
                codigo.set('')
                modi.withdraw()
                modificacion.withdraw()
                ventequipos.deiconify()
                return
            
            else:
                cont += 1
                c = c[1:]
        return
    else:
        messagebox.showinfo(title='Ventana de modificacion de equipos',message='El nuevo nombre de equipo no esta entre 5 y 40 caracteres')
        nuevoequipo.set('')
        
        


    
#Funcion de modificar equipo auxiliar

def modifica():
    ventequipos.withdraw()
    global equipos
    c = codigo.get()
    e = equipos
    if e== []:
        messagebox.showinfo(title='Ventana de moficiacion de equipos',text='No hay ninguna cantidad de quipos')
    else:
        if len(c) == 3:
            while e != []:
                if c == e[0][0]:
                    modificacion.withdraw()
                    modi.deiconify()
                    return
                else:
                    e = e[1:]
            else:
                messagebox.showinfo('Este equipo no esta registrado,no se puede modificar')
                codigo.set('')
                return
        else:
            messagebox.showinfo(title='Ventana de modificacion de quipos',message='el codigo no es de 3 letras')
            
    
               
    
    
#Funcion modificar un equipo               
def modificar():
    modificacion.deiconify()
    ventequipos.withdraw()
    modificacion.title('Ventana de modificacion de quipos')
    l1 = Label(modificacion,text='Ingrese el codigo de equipo que desea modificar').grid(row=0)
    l2 = Label(modificacion,text='Codigo de equipo:').grid(row=1)
    e1 = Entry(modificacion,textvariable=codigo).grid(row=1,column=1)
    b1 = Button(modificacion,text='modificar',command=modifica).grid(row=2)
    b2 = Button(modificacion,text='cancelar',command=cancelar4).grid(row=2,column=1)
    
    
### funciones ventana de eliminar

def cancelar6():
    codigo.set('')
    elimiminar.withdraw()
    ventequipos.deiconify()

#funcion para abrir ventana de eliminar equipos
def elimina():
    ventequipos.withdraw()
    eliminar.deiconify()

#funcion para confirmar eliminacion de equipo

def elim():
    eliminar.withdraw()
    global equipos
    global codigos
    cantidadequipos = int(cantequipos.get())
    c = codigo.get()
    e = equipos
    if len (c) != 3:
        messagbox.showinfo(title='Ventana de eliminar equipos',message='El codigo de equipo no es de 3 caracteres')
        codigo.set('')
        return
    elif cantidadequipos == 2:
        messagebox.showinfo(title='Ventana de eliminar equipos',message='Deben existir al menos 2 equipos para el campeonato')
        codigo.set('')
        ventequipos.deiconify()
        return
    else:
        while e != []:
            if c == e[0][0]:
                equipo = e[0][1]
                dec = messagebox.askquestion(title='Ventana de eliminar equipo',message='Seguro que desea eliminar:' +'  ' + c + '   ' +equipo + '?')
                if dec == 'yes':
                    equipos.remove((c,equipo))
                    codigos.remove(c)
                    cantidadequipos -= 1
                    messagebox.showinfo(title='Ventana de eliminar equipos',message = 'El equipo ha sido eliminado')
                    d = messagebox.askquestion(title='Ventana de eliminar equipos',message = 'Desea eliminar otro equipo?')
                    if d == 'yes':
                        codigo.set('')
                        eliminar.deiconify()
                        return
                    else:
                        codigo.set('')
                        ventequipos.deiconify()
                        return
                else:
                    codigo.set('')
                    eliminar.withdraw()
                    ventequipos.deiconify()
            else:
                e= e[1:]
        messagebox.showinfo(title='Ventana de eliminar equipos',message='El equipo no existe, no se puede eliminar')
        codigo.set('')
        if cantidadequipos%2 != 0:
            messagebox.showinfo(title='Ventana de eliminar equipos',message='Debe haber una cantidad par de equipos')
            codigo.set('')
            eliminar.withdraw()
            ventequipos.deiconify()
            return
        else:
            eliminar.withdraw()
            ventequipos.deiconify()
            return

        
        
###funciones ventana calendario

#funcion salir de ventana de calendario de juegos
def salir4():
    calendar.withdraw()
    app.deiconify()

def cambiacodigo(codigo):
    global equipos
    cont = 0
    while cont != len(equipos):
        if codigo == equipos[cont][0]:
            return equipos[cont][1]
        else:
            cont += 1

#funcion para crear fechas
def crearfechas(partidosxfecha,cantfechas,juego):
    juego = list(juego)
    nom = nombre.get()
    nom = 'Torneo: ' + nom
    calendar.deiconify()
    lb = Label(calendar,text=nom).pack
    lb2 = Label(calendar,text='Calendario de juegos').pack()
    lst = Listbox(calendar)
    inicio = 1
    while cantfechas != 0:
        lst.insert(END,'Fecha:' + str(inicio))
        for i in range(0,partidosxfecha):
            juego[0]= list(juego[0])
            juego[0][0] = cambiacodigo(juego[0][0])
            juego[0][1] = cambiacodigo(juego[0][1])
            juego[0] = tuple(juego[0])
            temp = juego[0][0] + ' -vs- ' + juego[0][1]
            lst.insert(END,temp)
            juego = juego[1::]
        else:
            cantfechas -= 1
            inicio += 1
    else:
        lst.pack()
        b = Button(calendar,text='Salir',command=salir4).pack()
            

#funcion para crear lista de juegos
def crearcalendario():
    global codigos
    global juegos
    global cal
    n = int(cantequipos.get())
    c = set(codigos)
    temp = []
    inv = []
    if n == 2:
        juegos = juegos + [(codigos[0],codigos[1]),(codigos[1],codigos[0])]
        partidosxfecha = n//2
        cantfechas = 2
        cal = True
        return crearfechas(partidosxfecha,cantfechas,juegos)
    else:
        partidos = list(itertools.permutations(codigos,2))
        cont = len(partidos)
        lar = cont//2
        while len(juegos) != lar and len(inv) != lar:
            if partidos != []:
                if partidos[0][0] in c and partidos[0][1] in c:
                    c.remove(partidos[0][0])
                    c.remove(partidos[0][1])
                    juegos = juegos + [partidos[0]]
                    i = partidos[0][::-1]
                    inv = inv + [i]
                    partidos.remove(i)
                    partidos.remove(partidos[0])
                else:
                    temp = temp + [partidos[0]]
                    partidos.remove(partidos[0])
            else:
                partidos = temp
                c = set(codigos)
                temp = []
        else:
            final = juegos + inv
            juegos = final
            partidosxfecha = n//2
            cantfechas = n*(n-1)//(len(codigos)//2)
            cal = True
            return crearfechas(partidosxfecha,cantfechas,juegos)
                               
#Fucion para llamar funcion de crear calendario de juegos
def calendario():
    global equipos
    global cal
    global configurar
    if configurar == False:
        messagebox.showinfo(title='Ventana de crear calendarios',message='La configuracion no ha sido establecida')
        return
    elif cal == False:
        app.withdraw()
        return crearcalendario()
    else:
        app.withdraw()
        calendar.deiconify()
        

###Funciones ventana de resultados

#funcion para cancelar ventana de resultados
def cancelar8():
    global resultados
    global res
    global d
    res = False
    resultados = []
    jugadores = []
    d = dict()
    messagebox.showinfo(title='Ventana de resultados',message='Todos los datos ingresados sobre partidos han sido borrados')
    codc.set('')
    codv.set('')
    equic.set('')
    equiv.set('')
    mcasa.set('')
    mvisita.set('')
    resulta.withdraw()
    app.deiconify()


    
#funcion para salir de ventana de resultados
def salir5():
    global res
    global resultados
    a = list(resultados)
    for i in resultados:
        if i != ('',''):
            res = True
            resulta.withdraw()
            app.deiconify()
            return
        else:
            pass
    else:
        messagebox.showinfo(title='Mensaje de resultados',message='No se han ingresado ningun resultado de partidos')
        return
        
#funcion que valida datos ingresados en ventana de resultados
def validaresul():
     casac = codc.get()
     visitac = codv.get()
     equic = equic.get()
     equiv = equiv.get()
     mcasa = mcasa.get()
     mvisita = mvisita.get()
     global equipos
     global juegos
     if mcasa == '' or mvisita == '':
         messagebox.showerror(title='Ventana de resultados',message='El marcador no puede quedar vacio')
         return
     elif casac == visitac:
         messagebox.showerror(title='Ventana de resultados',message='Los codigos no pueden ser iguales')
         return
     elif equic == equiv:
        messagebox.showerror(title='Ventana de resultados',message='Los equipos no pueden ser iguales')
        return
     elif (casac,equic) not in equipos or (visitac,equiv) not in equipos:
        messagebox.showerror(title='Ventana de resultados',message='Ambos equipos deben exisir en los equipos registrados con su codigo correspondiente')
        return
     elif (equic,equiv) not in juegos:
         messagebox.showerror(title='Ventana de resultados',message='Ese partido no pertenece a los partidos oficiales')
         return
     else:
         try:
             mcasa = int(mcasa)
             mvisita = int(mvisita)
             if mcasa > 8 or mvisita > 8:
                 messagebox.showerror(title='Ventana de resultados',message='Los marcadores deben ser numero enteros menores o iguales a 8')
                 mcasa.set('')
                 mvisita.set('')
                 return
             if mcasa < 0 or mvisita < 0:
                 messagebox.showerror(title='Ventana de resultados',message='Las anotaciones deben ser numeros positiovs')
                 mcasa.set('')
                 mvisita.set('')
                 return
             else:
                 return True
         except ValueError:
             messagebox.showerror(title='Ventana de resultados',message = 'El marcador debe consistir de numeros')
             mcasa.set('')
             mvisita.set('')
             return

##agregar goles

#funcion que valida que no falten goleadores por ingresar
def listogol():
    global indicav
    global indicac
    if indicav == True and indicac == False:
        messagebox.showinfo(title='Ventana de goleadores',message='Faltan goleadores por ingresar del equipo  de casa!')
        return
        
    elif indicav == False and indicac == True:
        messagebox.showinfo(title='Ventana de goleadores',message='Faltan goladores por ingresar del equipo de visita!')
        return
    elif indicav == False and indicav == False:
        messagebox.showinfo(title='Ventana de goleadores',message='Faltan goleadores por agregar')
        return
    else:
        golcod.set('')
        jugador.set('')
        minuto.set('')
        indicac = False
        indicav = False
        agregargoles.withdraw()
        resulta.deiconify()
    
#funcion para cancelar ingreso de jugador
def cancelar9():
    messagebox.showinfo(title='Ventana de goleadores',message='El goleador no fue agregado')
    golcod.set('')
    minuto.set('')
    jugador.set('')
    return

#funcion de agregar goles de ambos equipos
def agregargol():
    global d
    global jugaodres
    global goleadores1
    global goleadores2
    global indicav
    global indicac
    global indice
    cod = golcod.get()
    cod1 = codc.get()
    cod2 = codv.get()
    player = jugador.get()
    minu = int(minuto.get())
    if indicac:
        if goleadores2 == 0:
            indicav = True
            messagebox.showinfo(title='Ventana de goleadores',message = 'Todos los goleadores de visita y casa han sido agregados')
            golcod.set('')
            minuto.set('')
            jugador.set('')
            return
        else:
            de = messagebox.askquestion(title='Ventana de goleadores',message='El gol fue autogol?')
            if de == 'yes':
                goleadores2 -= 1
                cod1 = cambiacodigo(cod2)
                d[cod1] += [player]
                minu = abs(minu)
                minu = -minu
                messagebox.showinfo(title='Ventana de goleadores',message='El goleador ' + player + ' fue agregado con exito.')
                jugadores[indice] = list(jugadores[indice])
                jugadores[indice][0] = list(jugadores[indice][0])
                jugadores[indice][0] += [(player,minu)]
                jugadores[indice][0] = tuple(jugadores[indice][0])
                jugadores[indice] = tuple(jugadores[indice])
                if goleadores2 == 0:
                    indicav = True
                else:
                    pass
                return
            else:
                goleadores2 -= 1
                cod2 = cambiacodigo(cod2)
                d[cod2] += [player]
                minu = abs(minu)
                messagebox.showinfo(title='Ventana de goleadores',message='El goleador ' + player + ' fue agregado con exito.')
                jugadores[indice] = list(jugadores[indice])
                jugadores[indice][1] = list(jugadores[indice][1])
                jugadores[indice][1] += [(player,minu)]
                jugadores[indice][1] = tuple(jugadores[indice][1])
                jugadores[indice] = tuple(jugadores[indice])
                golcod.set('')
                jugador.set('')
                minuto.set('')
                if goleadores2 == 0:
                    indicav = True
                else:
                    pass
                return
                
    elif indicav:
        if goleadores1 == 0:
            indicac = True
            messagebox.showinfo(title='Ventana de goleadores',message = 'Todos los goleadores de casa han y visita sido agregados')
            golcod.set('')
            minuto.set('')
            jugador.set('')
            return
        else:
            de = messagebox.askquestion(title='Ventana de goleadores',message='El gol fue autogol?')
            if de == 'yes':
                goleadores1 -= 1
                cod2 = cambiacodigo(cod2)
                d[cod2] += [player]
                minu = abs(minu)
                minu = -minu
                messagebox.showinfo(title='Ventana de goleadores',message='El goleador ' + player + ' fue agregado con exito.')
                jugadores[indice] = list(jugadores[indice])
                jugadores[indice][1] = list(jugadores[indice][0])
                jugadores[indice][1] += [(player,minu)]
                jugadores[indice][1] = tuple(jugadores[indice][0])
                jugadores[indice] = tuple(jugadores[indice])
                golcod.set('')
                jugador.set('')
                minuto.set('')
                if goleadores1 == 0:
                    indicac = True
                else:
                    pass
                return
            else:
                goleadores1 -= 1
                cod1 = cambiacodigo(cod1)
                d[cod1] += [player]
                minu = abs(minu)
                messagebox.showinfo(title='Ventana de goleadores',message='El goleador ' + player + ' fue agregado con exito.')
                jugadores[indice] = list(jugadores[indice])
                jugadores[indice][0] = list(jugadores[indice][1])
                jugadores[indice][0] += [(player,minu)]
                jugadores[indice][0] = tuple(jugadores[indice][1])
                jugadores[indice] = tuple(jugadores[indice])
                golcod.set('')
                jugador.set('')
                minuto.set('')
                if goleadores1 == 0:
                    indicac = True
                else:
                    pass
                return
    else:
        if cod == cod1:
            de = messagebox.askquestion(title='Ventana de goleadores',message = 'Desea agregar a:' + player + ' ?')
            if de == 'yes':
                pregu = messagebox.askquestion(title='Ventana de goleadores',message='Fue un autogol?')
                if pregu == 'yes':
                    goleadores2 -= 1
                    cod1 = cambiacodigo(cod1)
                    d[cod1] += [player]
                    minu = abs(minu)
                    minu = -minu
                    jugadores[indice] = list(jugadores[indice])
                    jugadores[indice][1] = list(jugadores[indice][0])
                    jugadores[indice][1] += [(player,minu)]
                    jugadores[indice][1] = tuple(jugadores[indice][0])
                    jugadores[indice] = tuple(jugadores[indice])
                    messagebox.showinfo(title='Ventana de goleadores',message= player + ' fue agregado')
                    golcod.set('')
                    jugador.set('')
                    minuto.set('')
                    if goleadores2 == 0:
                        indicav = True
                    else:
                        pass
                    return
                else:
                    goleadores1 -= 1
                    cod1 = cambiacodigo(cod1)
                    d[cod1] += [player]
                    minu = abs(minu)
                    jugadores[indice] = list(jugadores[indice])
                    jugadores[indice][0] = list(jugadores[indice][0])
                    jugadores[indice][0] += [(player,minu)]
                    jugadores[indice][0] = tuple(jugadores[indice][0])
                    jugadores[indice] = tuple(jugadores[indice])
                    messagebox.showinfo(title='Ventana de goleadores',message= player + ' fue agregado')
                    golcod.set('')
                    jugador.set('')
                    minuto.set('')
                    if goleadores1 == 0:
                        indicac = True
                    else:
                        pass
                    return
            else:
                messagebox.showinfo('Ventana de goleadores',message='El jugador no fue agregado')
                golcod.set('')
                jugador.set('')
                minuto.set('')
                return
        else:
            de = messagebox.askquestion(title='Ventana de goleadores',message = 'Desea agregar a:' + player + ' ?')
            if de == 'yes':
                pregu = messagebox.askquestion(title='Ventana de goleadores',message='Fue un autogol?')
                if pregu == 'yes':

                    goleadores1 -= 1
                    cod2 = cambiacodigo(cod2)
                    d[cod2] += [player]
                    minu = abs(minu)
                    minu = -minu
                    jugadores[indice] = list(jugadores[indice])
                    jugadores[indice][0] = list(jugadores[indice][1])
                    jugadores[indice][0] += [(player,minu)]
                    jugadores[indice][0] = tuple(jugadores[indice][1])
                    jugadores[indice] = tuple(jugadores[indice])
                    messagebox.showinfo(title='Ventana de goleadores',message= player + ' fue agregado')
                    golcod.set('')
                    jugador.set('')
                    minuto.set('')
                    if goleadores1 == 0:
                        indicac = True
                    else:
                        pass
                    return
                else:
                    goleadores2 -= 1
                    cod2 = cambiacodigo(cod2)
                    d[cod2] += [player]
                    minu = abs(minu)
                    jugadores[indice] = list(jugadores[indice])
                    jugadores[indice][0] = list(jugadores[indice][1])
                    jugadores[indice][0] += [(player,minu)]
                    jugadores[indice][0] = tuple(jugadores[indice][1])
                    jugadores[indice] = tuple(jugadores[indice])
                    messagebox.showinfo(title='Ventana de goleadores',message= player + ' fue agregado')
                    golcod.set('')
                    jugador.set('')
                    minuto.set('')
                    if goleadores2 == 0:
                        indicac = True
                    else:
                        pass
                    return
            else:
                messagebox.showinfo('Ventana de goleadores',message='El jugador no fue agregado')
                golcod.set('')
                jugador.set('')
                minuto.set('')
                return

#funcion de validar datos de ingreso de goles
def validagol():
    cod = golcod.get()
    cod1 = codc.get()
    cod2 = codv.get()
    minu = minuto.get()
    player = jugador.get()
    global goleadores1
    global goleadores2
    global indicac
    global indicav
    if cod == '' or player == '' or minu =='':
        messagebox.showerror(title='Ventana de ingreso de goleadores',message='No puede dejar datos en blanco')
        return
    elif len(cod) != 3:
        messagebox.showerror(title='Ventana de ingreso de goleadores',message='El codigo no es de 3 caracteres')
        golcod.set('')
        return
    elif cod != cod1 and cod != cod2:
        messagebox.showerror(title='Ventana de ingreso de goleadores',message='El codigo no pertenece a ninguno de los del partido actual')
        golcod.set('')
        return
    elif len(player) < 2 or len(player) > 40:
        messagebox.showerror(title='Ventana de ingreso de goleadores',message='El jugador debe tener un nombre entre 2 y 40 caracteres')
        jugador.set('')
        return
    else:
        if goleadores2 == 0:
            indicav = True
        elif goleadores1 == 0:
            indicac = True
        
    if indicac == True and indicav == True:
        messagebox.showerror(title='Ventana de ingreso de goleadores',message='No se pueden agregar mas goleadores para ningun equipo')
        golcol.set('')
        minuto.set('')
        jugador.set('')
        return
    else:
        agregargol()
            
#funcion que abre ventana de agregar jugadores
def agregresul():
    global resultados
    global indice
    global juegos
    global goleadores1
    global goleadores2
    global indicac
    global indicav
    global d
    cont = 0
    if validaresul:
        if mcasa.get() == '' or mvisita.get() == '':
            messagebox.showinfo(title='Ventana de resultados',message='El marcador debe tener numeros')
            return
        cod1 = codc.get()
        cod2 = codv.get()
        casa = int(mcasa.get())
        empate = int(cantempate.get())
        gana = int(cantgana.get())
        visita = int(mvisita.get())
        if casa > 8 or visita > 8:
            messagebox.showinfo(title='Ventana de resultados',message='Solo puede haber un maximo de 8 goles por equipo')
            mcasa.set('')
            mvisita.set('')
            return
        decision = messagebox.askquestion(title='Ventana de agregar resultados',message='Desea agregar los resultados del partido?')
        if decision == 'no':
            messagebox.showinfo(title='Ventana de resultados',message='Los resultados no fueron agregados')
            mcasa.set('')
            mvisita.set('')
            return
        else:
            while cont != len(juegos):
                if (cod1,cod2) == juegos[cont]:
                    indice = cont
                    if resultados[cont] != ('',''):
                        messagebox.showerror(title='Ventana de agregar goles',message='Ese partido ya se jugo')
                        mcasa.set('')
                        mvisita.set('')
                        return
                    elif int(casa) == 0 and int(visita) == 0:
                        messagebox.showinfo(title='Ventana de agregar marcadores',message='El marcador:' + str(casa) + '-' + str(visita) + ' ha sido agregado')
                        mcasa.set('')
                        mvisita.set('')
                        resultados[indice] = (0,0)
                        return
                    elif int(casa) > int(visita):
                        goleadores1 = int(casa)
                        goleadores2 = int(visita)
                        messagebox.showinfo(title='Ventana de agregar marcadores',message='El marcador:' + str(casa) + '-' + str(visita) + ' ha sido agregado')
                        d[cod1] += gana
                        resultados[indice] = (int(casa),int(visita))
                        mcasa.set('')
                        mvisita.set('')
                        resulta.withdraw()
                        agregargoles.deiconify()
                        return
                    elif int(casa) < int(visita):
                        goleadores1 = int(casa)
                        goleadores2 = int(visita)
                        messagebox.showinfo(title='Ventana de agregar marcadores',message='El marcador:' + str(casa) + '-' + str(visita) + ' ha sido agregado')
                        d[cod2] += gana
                        resultados[indice] = (int(mcasa.get()),int(mvisita.get()))
                        mcasa.set('')
                        mvisita.set('')
                        resulta.withdraw()
                        agregargoles.deiconify()
                        return
                    else:
                        goleadores1 = int(casa)
                        goleadores2 = int(visita)
                        messagebox.showinfo(title='Ventana de agregar marcadores',message='El marcador:' + str(casa) + '-' + str(visita) + ' ha sido agregado')
                        resultados[indice] = (int(casa),int(visita))
                        mcasa.set('')
                        mvisita.set('')
                        resulta.withdraw()
                        agregargoles.deiconify()
                        return
                else:
                    cont += 1
            else:
                messagebox.showerror(title='Ventana de agregar marcador',message='Ese partido no existe')
                return

##funciones consulta de resultados

#funcion de consultar marcador
def consultagol():
    global indice
    global resultados
    casa = codc.get()
    visita = codv.get()
    match = resultados[indice]
    messagebox.showinfo(title='Ventana de resultados',message= 'El marcador del parido: ' + codc + '-vs-' + codv + 'tiene el resultado de: ' + str(resultados[indice]))
    codc.set('')
    codv.set('')
    consulgoles.withdraw()
    resulta.deiconify()

#funcion que valida datos para consultar
def conresul():
    global juegos
    global resultados
    global indice
    mcasa.set('')
    mvisita.set('')
    casa = codc.get()
    visita = codv.get()
    cont = 0
    largo = len(juegos)
    if casa == '' or visita == '':
        messagebox.showerror(title='Ventana de consulta de goles',message='Los codigos no pueden ser en blanco')
        codc.set('')
        codv.set('')
        return
    elif casa == visita:
        messagebox.showerror(title='Ventana de consulta de goles',message='Los codigos no pueden ser iguales')
        codc.set('')
        codv.set('')
        return
    else:
        while cont != largo:
            if (casa,visita) == juegos[cont]:
                if resultados[cont] == ('',''):
                    messagebox.showinfo(title='Ventana de consulta de goles',message='El partido: ' + codc + '-vs-' + codv + ' no se ha jugado, no se puede consultar su puntaje')
                    codc.set('')
                    codv.set('')
                    return
                else:
                    indice = cont
                    resulta.withdraw()
                    consulgoles.deiconify()
                    e1 = Entry(consulgoles,textvariable=codc,state='readonly').grid(row=2)
                    e2 = entry(consulgoles,textvariable=codv,state='readonly').grid(row=2,column=1)
            else:
                cont += 1
        else:
            messagebox.showinfo(title='Ventana de consulta de goles',message='El partido que desea consultar no existe')
            codc.set('')
            codv.set('')
            return

##funciones de ventana de modificar resultado

#funcion para cancelar modificacion
def cancelar10():
    messagebox.showinfo(title='Ventana de modificar resultados',message='El resultado no fue alterado')
    mcasa.set('')
    mvisita.set('')
    modigoles.withdraw()
    return

#funcion de modificar el resultado de un partido
def modgol():
    global indice
    global resultados
    global jugadores
    global d
    global goleadores1
    global goleadores2
    empa = int(cantempate.get())
    gana = int(cantgana.get())
    cantcasa = int(mcasa.get())
    cantvisi = int(mvisita.get())
    casa = codc.get()
    visita = codv.get()
    casatem = resultados[indice][0]
    visitatem = resultados[indice][1]
    if casatem == visitatem:
        d[casa] -= cantempate
        d[visita] -= cantempate
        casa = cambiacodigo(casa)
        for i in jugadores[indice][0]:
            d[casa].remove(jugadores[indice][i][0])
        visita = cambiacodigo(visita)
        for j in jugadores[indice][1]:
            d[visita].remove(jugadores[indice][i][1])
        else:
            goleadores1 = int(mcasa.get())
            goleadores2 = int(mvisita.get())
            jugadores[indice] = ((),())
            resultados[indice] = (cantcasa,cantvisi)
            messagebox.showinfo(title='Ventana de modificar goles',message='El marcador ha sido cambiado, ahora debe agregar los goleadores')
            agregargoles.deiconify()
            modigoles.withdraw()
            
    elif casatem > visitatem:
        d[casa] -= gana
        casa = - cambiacodigo(casa)
        for i in jugadores[indice][0]:
            d[casa].remove(jugadores[indice][i][0])
        visita = cambiacodigo(visita)
        for j in jugadores[indice][1]:
            d[visita].remove(jugadores[indice][i][1])
        else:
            goleadores1 = int(mcasa)
            goleadores2 = int(mvisita)
            jugadores[indice] = ((),())
            resultados[indice] = (cantcasa,cantvisi)
            messagebox.showinfo(title='Ventana de modificar goles',message='El marcador ha sido cambiado, ahora debe agregar los goleadores')
            agregargoles.deiconify()
            modigoles.withdraw()

    else:
        d[visita] -= gana
        casa = - cambiacodigo(casa)
        for i in jugadores[indice][0]:
            d[casa].remove(jugadores[indice][i][0])
        visita = cambiacodigo(visita)
        for j in jugadores[indice][1]:
            d[visita].remove(jugadores[indice][i][1])
        else:
            goleadores1 = int(mcasa)
            goleadores2 = int(mvisita)
            jugadores[indice] = ((),())
            resultados[indice] = (cantcasa,cantvisi)
            messagebox.showinfo(title='Ventana de modificar goles',message='El marcador ha sido cambiado, ahora debe agregar los goleadores')
            agregargoles.deiconify()
            modigoles.withdraw()

            
#funcion que valida datos para modificar el marcador
def modresul():
    global indice
    global resultados
    global juegos
    global jugadores
    global d
    casa = codc.get()
    visita = codv.get()
    cont = 0
    largo = len(juegos)
    casa = codc.get()
    visita = codv.get()
    cas1 = mcasa.get()
    vis1 = mvisita.get()
    if validaresul():
        while cont != largo:
            if (codc,codv) == juegos[cont]:
                if (cas1,vis1) == resultados[cont]:
                    messagebox.showinfo(title='Ventana de modificar goles',message='El marcador es el mismo que se agrego a ese partido antes')
                    codc.set('')
                    codv.set('')
                    mcasa.set('')
                    mvisita.set('')
                else:
                    indice = cont
                    resulta.withdraw()
                    modigoles.deiconify()
                    e1 = Entry(modigoles,textvariable=mcasa,state='readonly').grid(row=1,column=1)
                    e2 = Entry(modigoles,textvariable=mvisita,state='readonly').grid(row=2,column=1)
            else:
                cont += 1

#funcion de eliminacion de resultados
def eliminagol():
    global indice
    global resultados
    global jugadores
    global d
    empa = int(cantempate.get())
    gana = int(cantgana.get())
    casa = codc.get()
    visita = codv.get()
    casatem = resultados[indice][0]
    visitatem = resultados[indice][1]
    if casatem == visitatem:
        d[casa] -= cantempate
        d[visita] -= cantempate
        casa = cambiacodigo(casa)
        for i in jugadores[indice][0]:
            d[casa].remove(i[0])
        visita = cambiacodigo(visita)
        for j in jugadores[indice][1]:
            d[visita].remove(j[0])
        else:
            jugadores[indice] = ((),())
            resultados[indice] = ('','')
            messagebox.showinfo(title='Ventana de eliminar resultados',message='El marcador ha sido eliminado')
            return
    elif casatem > visitatem:
        d[casa] -= gana
        casa = - cambiacodigo(casa)
        for i in jugadores[indice][0]:
            d[casa].remove(i[0])
        visita = cambiacodigo(visita)
        for j in jugadores[indice][1]:
            d[visita].remove(j[0])
        else:
            jugadores[indice] = ((),())
            resultados[indice] = ('','')
            messagebox.showinfo(title='Ventana de eliminar resultados',message='El marcador ha sido eliminado')
            return
    else:
        d[visita] -= gana
        casa = - cambiacodigo(casa)
        for i in jugadores[indice][0]:
            d[casa].remove(i[0])
        visita = cambiacodigo(visita)
        for j in jugadores[indice][1]:
            d[visita].remove(j[0])
        else:
            jugadores[indice] = ((),())
            resultados[indice] = ('','')
            messagebox.showinfo(title='Ventana de eliminar resultados',message='El marcador ha sido eliminado')
            return
            
    
    

#funcion que valida eliminar resultados
def eliresul():
    global codigos
    global indice
    global equipos
    global resultados
    mcasa.set('')
    mvisita.set('')
    de = messagebox.askquestion(title='Ventana de eliminar resultados',message='Seguro que desea elliminar el resultado de ese partido?')
    if de == 'yes':
        cod1 = codc.get()
        cod2 = codv.get()
        equi1 = equic.get()
        equi2 = equiv.get()
        if (cod1,equi1) in equipos and (cod2,equi2) in equipos:
            if cod1 != cod2:
                if equi1 != equi2:
                    cont = 0
                    largo = len(equipos)
                    while cont != largo:
                        if (cod1,cod2) == equipos[cont]:
                            if resultados[cont] == ('',''):
                                messagebox.howerror(title='Ventana de eliminar resultados',message='El partido no tiene resultados, no se puede eliminar')
                                return
                            else:
                                indice = cont
                                return eliminagol()
                        else:
                            cont += 1
                    else:
                        messagebox.showerror(title='Ventana de eliminacion de equipos',message='EL partido no existe')
                        return
                else:
                    messagebox.showerror(title='Ventana de eliminacion de resultados',message='Los equipos no deben ser iguales entre ellos')
                    return
            else:
                messagebox.showerror(title='Ventana de eliminacion de resultados',message='Los codigos de los equipos no pueden ser iguales')
                return
        else:
            messagebox.showerror(title='Ventana de eliminacion de resultados',message='Ese partido no existe')
            return
                
#funcion que hace ventana de resultados aparecer
def apareceresul():
    global d
    global codigos
    global equipos
    global juegos
    global paises
    global jugadores
    global resultados
    app.withdraw()
    resulta.deiconify()
    resulta.title('Ventana de registro de resultados')
    nom = nombre.get()
    nom = 'Torneo: ' + nom
    lb = Label(resulta,text=nom).grid(row=0,column=0)
    lb2 = Label(resulta,text='Seleccione el codigo y nombre de equipo de casa').grid(row=1)
    s1 = Spinbox(resulta,values=codigos,textvariable=codc).grid(row=2,column=0)
    s2 = Spinbox(resulta,values=paises,textvariable=equic).grid(row=2,column=1)
    lb3 = Label(resulta,text='Selecicone el codigo y nombre del equipo de visita').grid(row=3)
    s3 = Spinbox(resulta,values=codigos,textvariable=codv).grid(row=4,column=0)
    s4 = Spinbox(resulta,values=paises,textvariable=equiv).grid(row=4,column=1)
    lb3 = Label(resulta,text='Marcador final:').grid(row=5)
    lb4 = Label(resulta,text='Casa:').grid(row=6,column=0)
    lb5 = Label(resulta,text='Visita:').grid(row=6,column=1)
    e1 = Entry(resulta,textvariable=mcasa).grid(row=7,column=0)
    e2 = Entry(resulta,textvariable=mvisita).grid(row=7,column=1)
    b1 = Button(resulta,image=agregari,command=agregresul).grid(row=8,column=0)
    b2 = Button(resulta,image=consultari,command=conresul).grid(row=8,column=1)
    b3 = Button(resulta,image=modificari,command=modresul).grid(row=9,column=0)
    b4 = Button(resulta,image=eliminari,command=eliresul).grid(row=9,column=1)
    b5 = Button(resulta,text='Cancelar',command=cancelar8).grid(row=10,column=0)
    b6 = Button(resulta,text='Salir',command=salir5).grid(row=10,column=1)
    ls2 = Listbox(resulta)
    ls.insert(END,'Equipos registrados')
    ls.insert(END,'               ')
    ls.insert(END,'codigo   equipo')
    ls.insert(END,'               ')
    
    for i in codigos:
        temp = cambiacodigo(i)
        ls.insert(END,(i,temp))
    
    ls2.insert(END,'Juegos en orden')
    ls2.insert(END,'               ')
    j = list(juegos)
    for i in j:
        jugadores.append(((),()))
        resultados.append(('',''))
        ls2.insert(END,i)
        if d == {}:
            for m in codigos:
                d[m] = 0
            for n in paises:
                d[n] = []
    ls.grid(row=0,column=1)
    ls2.grid(row=0,column=2)
      
#funcion para llamar funcion de aparecer ventana de resultados
def resultado():
    global equipos
    global configurar
    global cal
    global paises
    global res
    if configurar == False:
        messagebox.showinfo(title='Ventana de agregar resultados',message='La configuracion no ha sido establecida')
        return
    elif cal == False:
        messagebox.showinfo(title='Ventana de agregar resultados',message='No se ha creado un calendario')
        return
    
    if paises == []:
        for i in equipos:
            paises = paises + [i[1]]
    else:
        return apareceresul()


##Funciones de ventana de posiciones

#funcion de salir de tabla de posiciones
def salir6():
    posiciones.withdraw()
    app.deiconify()

#funcion que crea la tabla de posiciones
def crearposiciones():
    global d
    global juegos
    global resultados
    global codigos
    global players
    clasifican = int(cantclas.get())
    temp = []
    clasificados = []
    a = list(d.items())
    lar = len(a)
    cont = 0
    while lar != 0:
        if type(a[cont][1]) == list:
            cont += 1
            lar -= 1
        else:
            temp = temp + [a[cont]]
            cont += 1
            lar -= 1
    for i in range(0,len(temp)):
        temp[i] = temp[i][::-1]
    temp.sort()
    temp.reverse()

            
    jj = 0
    jg = 0
    je = 0
    jp = 0
    gf = 0
    gc = 0
    gd = 0

    copion = d

#agregando display de puntos
    while clasifican != 0:
        cod = temp[0][1]
        for i in range(0,len(juegos)):
            if juegos[i][0] == cod:
                if resultados[i] == ('',''):
                    pass
                elif resultados[i][0] == resultados[i][1]:
                    jj += 1
                    je += 1
                    gf += resultados[i][0]
                    gc += resultados[i][1]
                elif resultados[i][0] > resultados[i][1]:
                    jj += 1
                    jg += 1
                    gf += resultados[i][0]
                    gc += resultados[i][1]
                else:
                    jj += 1
                    jp += 1
                    gf += resultados[i][0]
                    gc += resultados[i][1]
            elif juegos[i][1] == cod:
                if resultados[i] == ('',''):
                    pass
                elif resultados[i][1] == resultados[i][0]:
                    jj += 1
                    je += 1
                    gf += resultados[i][1]
                    gc += resultados[i][0]
                elif resultados[i][1] > resultados[i][0]:
                    jj += 1
                    jg += 1
                    gf += resultados[i][1]
                    gc += resultados[i][0]
                else:
                    jj += 1
                    jp += 1
                    gf += resultados[i][1]
                    gc += resultados[i][0]
            else:
                pass
        else:
            gd = gf - gc
            if gd < 0:
                gd = '-'+str(gd)
            elif gd == 0:
                gd = '0'
            else:
                gd = '+' + str(gd)
            cod = cambiacodigo(cod)
            clasificados += [(cod,jj,jg,je,jp,gf,gc,gd,temp[0][0])]                                      
            temp = temp[1:]
            clasifican -= 1
            jj = 0
            jg = 0
            je = 0
            jp = 0
            gf = 0
            gc = 0
            gc = 0
            gd = 0
    
    posiciones.deiconify()
    fila = 3
 
       
    for i in clasificados:
        a = i[0]
        b = str(i[1])
        c = str(i[2])
        d = str(i[3])
        e = str(i[4])
        f = str(i[5])
        g = str(i[6])
        h = str(i[7])
        i = str(i[8])
        j = Label(posiciones,text=a).grid(row=fila,column=0)
        k = Label(posiciones,text=b).grid(row=fila,column=1)
        l = Label(posiciones,text=c).grid(row=fila,column=2)
        m = Label(posiciones,text=d).grid(row=fila,column=3)
        n = Label(posiciones,text=e).grid(row=fila,column=4)
        o = Label(posiciones,text=f).grid(row=fila,column=5)
        p = Label(posiciones,text=g).grid(row=fila,column=6)
        q = Label(posiciones,text=h).grid(row=fila,column=7)
        r = Label(posiciones,text=i).grid(row=fila,column=8)
        fila += 1

    
    copia = list(clasificados)
    repetidos = []
    temporal = []
    for i in copia:
        if i[8] in temporal:
            repetidos += [i[8]]
        else:
            temporal += [i[8]]

                    
    l = Listbox(posiciones)
    l.config(width='30')
    l.insert(END,'Equipos clasificados a la fecha')
    alafecha = 1
    for i in clasificados:
        if i[8] in repetidos:
            l.insert(END,str(alafecha)+'-'+str(i[0]) + ' EMPATADO')
            alafecha += 1
        else:
            l.insert(END,str(alafecha)+'-'+str(i[0]))
            alafecha += 1
    l.grid(row=1,column=9)

    te = []
    goles = list(copion.items())
    lar = len(goles)
    cont = 0
    while lar != 0:
        if type(goles[cont][1]) == int:
            cont += 1
            lar -= 1
        else:
            te = te + [goles[cont]]
            cont += 1
            lar -= 1
    for i in range(0,len(te)):
        te[i] = te[i][::-1]

    for i in te:
        if len(i[0]) == 0:
            pass
        elif len(i[0]) == 1:
            if (i[0],i[1]) in list(players.keys()):
                
                players[tuple(i[0]+[i[1]])] += 1
            else:
                players[tuple(i[0]+[i[1]])] = 1
        else:
            for j in i[0]:
                print(i[1],type(i[1]))
                if (j,i[1]) in list(players.keys()):
                    players[tuple([j]+[i[1]])] += 1
                else:
                    players[tuple([j]+[i[1]])] = 1


    else:
        mejores = list(players.items())
        for i in range(0,len(mejores)):
            mejores[i] = mejores[i][::-1]
        mejores.sort()
        mejores.reverse()
        l3 = Listbox(posiciones)
        l3.insert(END,'Tabla de goleadores')
        l3.insert(END,'Goles {jugador,equipo}')
        for i in mejores:
            l3.insert(END,i)
        l3.grid(row=1,column=10)
    b = Button(posiciones,text='Listo',command=salir6).grid(row=fila)
    d = copion
    

#funcion que valida si se puede accesar ventana de posiciones
def traepos():
    global configurar
    global cal
    global res
    if configurar == False:
        messagebox.showinfo(title='Ventana de posiciones',message='La configuracion no ha sido establecida')
        return
    elif cal == False:
        messagebox.showinfo(title='Ventana de posiciones',message='El calendario de juegos no ha sido creado')
        return
    elif res == False:
        messagebox.showinfo(title='Ventana de posiciones',message='No hay resultados registrados, no se puede generar la tabla de posiciones')
        return
    else:
        app.withdraw()
        return crearposiciones()






####ventanas GUI y variables




#Ventana principal
app = tkinter.Tk()
app.geometry('550x550')
app.title('Menu principal')
titulo = Label(app,text='Torneos de futbol').pack()
config = Button(app,text = 'Configuracion del torneo',command=menuconfig).pack()
crear = Button (app,text = 'Crear/Consultar el calendario de juegos',command=calendario).pack()
registrar = Button(app,text = 'Registrar los resultados de cada fecha',command=resultado).pack()
tabla = Button(app,text = 'Tabla de posiciones y goleadores',command=traepos).pack()
ayuda = Button(app,text = 'Ayuda',command=ayudame).pack()
salir = Button(app,text = 'Salir',command = salir).pack()

#variables#
        
#Entradas
nombre = StringVar()
cantequipos = StringVar()
cantclas = StringVar()
cantgana = StringVar()
cantempate = StringVar()
codigo = StringVar()
equipo = StringVar()
nuevoequipo = StringVar()
golcod = StringVar()
jugador = StringVar()
minuto = StringVar()
codc = StringVar()
codv = StringVar()
equic = StringVar()
equiv = StringVar()
mcasa = StringVar()
mvisita = StringVar()


#globales
configurar = False
cal = False
res = False
indicac = False
indicav = False
goleadores1 = 0
goleadores2 = 0
indice = 0
d = dict()
players = dict()

#Listas
equipos = []
juegos = []
jugadores = []
resultados = []
codigos = []
paises = []

#imagenes
agregari = PhotoImage(file='add.gif')
modificari = PhotoImage(file='mod.gif')
consultari = PhotoImage(file='consulta.gif')
eliminari = PhotoImage(file='delete.gif')

#ventana de configuracion
config = Toplevel()
config.title('Menu de configuracion')
config.geometry('550x550')
configl = Label(config,text='Configuracion torneos de futbol').grid(row=0,column=1)
configl2 = Label(config,text='Datos Generales').grid(row=1,column=1)
torneol = Label(config,text='Nombre del torneo:').grid(row=2)
etorneo = Entry(config,textvariable=nombre).grid(row=2,column=1)
cant = Label(config,text='Cantidad de equipos participantes:').grid(row=3,column=0)
ecant = Entry(config,textvariable=cantequipos).grid(row=3,column=1)
clas = Label(config,text='Cantidad de equipos que clasifican directamente:').grid(row=4,column=0)
eclas = Entry(config,textvariable=cantclas).grid(row=4,column=1)
pganar = Label(config,text='Puntos ganados por cada partido ganado:').grid(row=5,column=0)
eganar = Entry(config,textvariable=cantgana).grid(row=5,column=1)
pempate = Label(config,text='Puntos ganados por cada partido empatado:').grid(row=6,column=0)
eempate = Entry(config,textvariable=cantempate).grid(row=6,column=1)
cancel = Button(config,text='Cancelar',command=cancelar).grid(row=10)
acept = Button(config,text='Aceptar',command=validar).grid(row=10,column=1)
config.protocol('WM_DELETE_WINDOW',nosalir)
config.withdraw()

#ventana de copia de configuracion
config2 = Toplevel()
config2.title('Menu de configuracion')
config2.geometry('550x550')
config2.protocol('WM_DELETE_WINDOW',nosalir)
config2.withdraw()

               
#Ventana de datos de equipos
ventequipos = Toplevel()
ventequipos.title('Menu de equipos')
ventequiposl = Label(ventequipos,text='Datos de los equipos').grid(row=0,column=1)
ventaequiposl2 = Label(ventequipos,text = 'Lista de equipos').grid(row=1)
ventequiposagregar = Button(ventequipos,image=agregari,command=validaequipo).grid(row=2)
ventequiposagregarl = Label(ventequipos,text='Agregar equipos').grid(row=2,column=1)
ventequiposcon = Button(ventequipos,image=consultari,command=consultar).grid(row=3)
ventequiposconl2 = Label(ventequipos,text='Consultar equipos').grid(row=3,column=1)
ventequiposmodifi = Button(ventequipos,image=modificari,command=modificar).grid(row=4)
ventequiposmodfil = Label(ventequipos,text='Modificar equipos').grid(row=4,column=1)
ventequiposeli = Button(ventequipos,image=eliminari,command=elimina).grid(row=5)
ventequiposelil = Label(ventequipos,text='Eliminar equipos').grid(row=5,column=1)
codigol = Label(ventequipos,text='Codigo del equipo').grid(row=6)
codigoe = Entry(ventequipos,textvariable=codigo).grid(row=6,column=1)
nombrel = Label(ventequipos,text='Nombre del equipo').grid(row=7)
nombree = Entry(ventequipos,textvariable=equipo).grid(row=7,column=1)
ventequipossal = Button(ventequipos,text='Listo',command=salir3).grid(row=8)
ventequiposcan = Button(ventequipos,text='Cancelar',command = cancelar7).grid(row=8,column=1)
ventequipos.protocol('WM_DELETE_WINDOW',nosalir)
ventequipos.withdraw()

#Ventana de comfirmacion de equipos
confirmar = Toplevel()
confirmar.protocol('WM_DELETE_WINDOW',nosalir)
confirmar.withdraw()

#ventana de consulta de quipos
consulta = Toplevel()
consulta.protocol('WM_DELETE_WINDOW',nosalir)
consulta.withdraw()

#ventana de modificacion de equipos
modificacion = Toplevel()
modificacion.protocol('WM_DELETE_WINDOW',nosalir)
modificacion.withdraw()

#ventana de modificacion auxiliar
modi = Toplevel()
modi.title('Ventana de modificacion de equipo')
l1 = Label(modi,text='Ingrese el nuevo nombre de equipo').grid()
l2 = Label(modi,text='Nuevo nombre de equipo:').grid()
e1 = Entry(modi,textvariable = nuevoequipo).grid(row=1,column=1)
b1 = Button(modi,text='Modificar',command=modificaux).grid(row=2)
b2 = Button(modi,text='Cancelar',command=cancelar5).grid(row=2,column=1)
modi.protocol('WM_DELETE_WINDOW',nosalir)
modi.withdraw()

#ventana de eliminacion de equipos
eliminar = Toplevel()
eliminar.title('Ventana de eliminacion de equipos')
l1 = Label(eliminar,text='Ingrese el codigo del equipo que desea eliminar').grid()
l2 = Label(eliminar,text='Codigo de equipo que desea eliminar:').grid(row=1)
e1 = Entry(eliminar,textvariable=codigo).grid(row=1,column=1)
b1 = Button(eliminar,text='eliminar',command=elim).grid(row=2)
b2 = Button(eliminar,text='cancelar',command=cancelar6).grid(row=2,column=1)
eliminar.protocol('WM_DELETE_WINDOW',nosalir)
eliminar.withdraw()

#Ventana de calendario de juegos
calendar = Toplevel()
calendar.title('Ventana de creacion de fechas')
calendar.protocol('WM_DELETE_WINDOW',nosalir)
calendar.withdraw()

#Ventana de  resultados
resulta = Toplevel()
resulta.geometry('750x500')
ls = Listbox(resulta)
resulta.protocol('WM_DELETE_WINDOW',nosalir)
resulta.withdraw()

#ventana de resultados pero solo consulta
resultaux = Toplevel()
resultaux.geometry('750x500')
resultaux.protocol('WM_DELETE_WINDOW',nosalir)
resultaux.withdraw()

#ventana de agregar goles
agregargoles = Toplevel()
agregargoles.title('Ventana de agregar goles')
l = Label(agregargoles,text='Seleccione el codigo del equipo que metio gol').grid(row=0)
l2 = Label(agregargoles,text='Ingrese el nombre del jugador').grid(row=1)
l3 = Label(agregargoles,text='Ingrese el minuto del gol').grid(row=2)
e1 = Entry(agregargoles,textvariable = golcod).grid(row=0,column=1)
e2 = Entry(agregargoles,textvariable = jugador).grid(row=1,column=1)
e3 = Entry(agregargoles,textvariable = minuto).grid(row=2,column=1)
b1 = Button(agregargoles,text='Agregar',command=validagol).grid(row=3)
b2 = Button(agregargoles,text='Cancelar',command=cancelar9).grid(row=3,column=1)
b3 = Button(agregargoles,text='Listo',command=listogol).grid(row=3,column=2)
agregargoles.protocol('WM_DELETE_WINDOW',nosalir)
agregargoles.withdraw()

#ventana de consultar marcadores
consulgoles = Toplevel()
consulgoles.title('Ventana de Consulta de goles')
l = Label(consulgoles,text='Desea consultar:').grid(row=0)
l2 = Label(consulgoles,text='Casa:').grid(row=1)
l3 = Label(consulgoles,text='Visita:').grid(row=1,column=1)
b1 = Button(consulgoles,text='Consultar',command=consultagol).grid(row=3)
b2 = Button(consulgoles,text='Cancelar').grid(row=3,column=1)
consulgoles.protocol('WM_DELETE_WINDOW',nosalir)
consulgoles.withdraw()

#ventana de modificar marcadores
modigoles = Toplevel()
modigoles.title('Ventana de modificacion de goles')
l = Label(modigoles,text='Este es el nuevo marcador del partido?').grid(row=0)
l2 = Label(modigoles,text='Casa:').grid(row=1)
l3 = Label(modigoles,text='Visita:').grid(row=2)
b1 = Button(modigoles,text='Si',command=modgol).grid(row=3)
b2 = Button(modigoles,text='Cancelar',command=cancelar10).grid(row=3,column=1)
modigoles.protocol('WM_DELETE_WINDOW',nosalir)
modigoles.withdraw()

#ventana de tabla de posiciones
posiciones = Toplevel()
nom = str(nombre.get())
cla = str(cantclas.get())
posiciones.title('Tabla de posiciones')
l1 = Label(posiciones,text='Torneo: ' + nom).grid(row=0,column=0)
l2 = Label(posiciones,text=' Equipos que clasifican:' + cla).grid(row=1,column=0)
l3 = Label(posiciones,text='Equipo').grid(row=2,column=0)
l4 = Label(posiciones,text='JJ').grid(row=2,column=1)
l5 = Label(posiciones,text='JG').grid(row=2,column=2)
l6 = Label(posiciones,text='JE').grid(row=2,column=3)
l7 = Label(posiciones,text='JP').grid(row=2,column=4)
l8 = Label(posiciones,text='GF').grid(row=2,column=5)
l9 = Label(posiciones,text='GC').grid(row=2,column=6)
l10 = Label(posiciones,text='GD').grid(row=2,column=7)
l11 = Label(posiciones,text='Puntos').grid(row=2,column=8)
l = Listbox(posiciones)
posiciones.protocol('WM_DELETE_WINDOW',nosalir)
posiciones.withdraw()


app.mainloop()



