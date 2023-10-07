from tkinter import*
#Funciones del funcionamiento del banco
cuenta_de_banco = 0

def obtener():
    z = entrada_dinero.get()
    return int(z)

def ingreso():
    global cuenta_de_banco
    dineroingreso = obtener()
    cuenta_de_banco += dineroingreso

def mostrar_ingreso():
    global cuenta_de_banco
    mostrar_el_saldo.config(text = f'Su saldo es {cuenta_de_banco}')



def mostrar_salida():

    global cuenta_de_banco
    x = ingresar_dinero_retiro.get()

    if int(x) < cuenta_de_banco:
        cuenta_de_banco -= int(x)
        mostrar_el_saldo_cuatro.config(text=f'Su retiro de {x} fue exitoso')
    else:
        mostrar_el_saldo_cuatro.config(text=f'Tienes dinero insuficiente en la cuenta su saldo es {cuenta_de_banco}')
    return cuenta_de_banco





# Función para mostrar la segunda ventana
def mostrar_segunda_ventana():
    info = login_nombre_usuario_boton.get()
    segunda_ventana.deiconify()
    primera_ventana.withdraw()
    tercera_ventana.withdraw()
    cuarta_ventana.withdraw()
    quinta_ventana.withdraw()
    etiqueta_segunda.config(text= 'Bienvenido ' + info + '\na tu cuenta Bancolombia')

def mostrar_poner_dinero():
    tercera_ventana.deiconify()
    segunda_ventana.withdraw()

def mostrar_sacar_dinero():
    cuarta_ventana.deiconify()
    segunda_ventana.withdraw()

def mostrar_saldo():
    quinta_ventana.deiconify()
    segunda_ventana.withdraw()

# Función para volver a la primera ventana
def volver_a_primera_ventana():
    primera_ventana.deiconify()
    tercera_ventana.withdraw()
    segunda_ventana.withdraw()
    cuarta_ventana.withdraw()



    

# Configuración de la primera ventana
primera_ventana = Tk()
primera_ventana.config(background='yellow')
primera_ventana.title("Login al banco")
etiqueta_primera = Label(primera_ventana, text="INGRESO A BANCOLOMBIA", font= ('Times New Roman',70),bg='yellow', fg='blue')
etiqueta_primera.pack(expand= False)
etiqueta_primera = Label(primera_ventana,bg='yellow')
etiqueta_primera.pack(expand= False)
login_nombre_usuario = Label(primera_ventana, text= 'PONGA SU NOMBRE DE USUARIO', font=('Times New Roman',45),bg='yellow',fg='red')
login_nombre_usuario.pack(expand= False)
login_nombre_usuario_boton = Entry(primera_ventana, bg='white', fg='blue', justify=CENTER,)
login_nombre_usuario_boton.pack()
contraseña_nombre_usuario = Label(primera_ventana, text= 'INGRESE SU CONTRASEÑA',font=('Times New Roman',45),bg='yellow',fg='red')
contraseña_nombre_usuario.pack(expand= False)
contraseña_nombre_usuario_boton = Entry(primera_ventana, bg='white', fg='blue', justify=CENTER, show= '*')
contraseña_nombre_usuario_boton.pack( expand = False)
boton_mostrar_segunda = Button(primera_ventana, text="Ingresar", command=mostrar_segunda_ventana)

boton_mostrar_segunda.pack()

# Configuración de la segunda ventana
segunda_ventana = Toplevel()
segunda_ventana.config(background='yellow')
segunda_ventana.title("Cuenta de banco")
etiqueta_segunda = Label(segunda_ventana, text= '', font=('Times New Roman',65),bg='yellow',fg = 'blue')
etiqueta_segunda.pack()
indicaciones = Label(segunda_ventana, text='Que operación deseas realizar', font=('Times New Roman',45),bg='yellow',fg = 'blue')
indicaciones.pack()
ingresar_dinero = Button(segunda_ventana, text= 'Ingresar dinero', fg='red', font=('Times New Roman',30), command= mostrar_poner_dinero)
ingresar_dinero.pack()
sacar_dinero = Button(segunda_ventana, text= 'Retirar Dinero', fg='red', font=('Times New Roman',30),command= mostrar_sacar_dinero)
sacar_dinero.pack()
revisar_dinero = Button(segunda_ventana, text= 'Consultar Saldo', fg='red', font=('Times New Roman',30), command= mostrar_saldo)
revisar_dinero.pack()
boton_volver_a_primera = Button(segunda_ventana, text="Salir", font=('Times New Roman',35), command=volver_a_primera_ventana)
boton_volver_a_primera.pack()

segunda_ventana.withdraw()  # Ocultar la segunda ventana al inicio


#Creando ventana ingresar dinero
tercera_ventana = Toplevel()
tercera_ventana.config(background='yellow')
tercera_ventana.title('Ingresar dinero a tu cuenta')
espacio = Label(tercera_ventana,bg='yellow')
espacio.pack()
titulo_pantalla_tres = Label(tercera_ventana, text= 'BIENVENIDO A LA SECCIÓN \n DE INGRESAR DINERO', justify= CENTER, bg= 'yellow',fg='Blue',font=('Times New Roman',45))
titulo_pantalla_tres.pack()
espacio = Label(tercera_ventana,bg='yellow')
espacio.pack()
titulo_pantalla_tres_1 = Label(tercera_ventana, text= 'Pon la cantidad deseas ingresar', justify= CENTER, bg= 'yellow',fg='Blue',font=('Times New Roman',25))
titulo_pantalla_tres_1.pack()
entrada_dinero = Entry(tercera_ventana, bg= 'white',fg='black',justify= CENTER,font=('Times New Roman',29) )
entrada_dinero.pack()
boton_mostrar_segunda_en_tercera = Button(tercera_ventana, text="Salir", command=mostrar_segunda_ventana)
boton_mostrar_segunda_en_tercera.pack()
boton_mostrar_segunda_en_tercera2 = Button(tercera_ventana, text="Aceptar", command=ingreso)
boton_mostrar_segunda_en_tercera2.pack()
tercera_ventana.withdraw() #Ocultar la tercera ventana al inicio

#Creando ventana de sacar dinero
cuarta_ventana = Toplevel()
cuarta_ventana.config(background='yellow')
cuarta_ventana.title('Retirando Dinero')
espacio4 = Label(cuarta_ventana,bg='yellow')
espacio4.pack()
titulo_pantalla_cuatro = Label(cuarta_ventana,text='BIENVENIDO A LA SECCIÓN \n DE RETIRAR DINERO',justify= CENTER, bg= 'yellow',fg='Blue',font=('Times New Roman',45))
titulo_pantalla_cuatro.pack()
ingresar_dinero_retiro = Entry(cuarta_ventana,bg= 'white',fg='black',justify= CENTER,font=('Times New Roman',29))
ingresar_dinero_retiro.pack()
boton_para_decir_retirto = Button(cuarta_ventana,text='Hacer desembolso',command=mostrar_salida)
boton_para_decir_retirto.pack()
espacio4 = Label(cuarta_ventana,bg='yellow')
espacio4.pack()
mostrar_el_saldo_cuatro = Label(cuarta_ventana, text="")
mostrar_el_saldo_cuatro.pack()
espacio4 = Label(cuarta_ventana,bg='yellow')
espacio4.pack()
boton_mostrar_segunda_en_cuarta = Button(cuarta_ventana, text="Salir", command=mostrar_segunda_ventana)
boton_mostrar_segunda_en_cuarta.pack()

cuarta_ventana.withdraw()


#Creamos la ventana de consultar saldo
quinta_ventana = Toplevel()
quinta_ventana.config(background='yellow')
quinta_ventana.title('Revisar Saldo')
espacio5 = Label(quinta_ventana,bg='yellow')
espacio5.pack()
titulo_pantalla_cinco = Label(quinta_ventana,text='BIENVENIDO A LA SECCIÓN \n DE REVISAR SALDO',justify= CENTER, bg= 'yellow',fg='Blue',font=('Times New Roman',45))
titulo_pantalla_cinco.pack()
mostrar_el_saldo = Label(quinta_ventana, text="")
mostrar_el_saldo.pack()
boton_info = Button(quinta_ventana, text = "Ver saldo", command= mostrar_ingreso)
boton_info.pack()
boton_salir_cinco = Button(quinta_ventana,text='Salir',command=mostrar_segunda_ventana)
boton_salir_cinco.pack()
quinta_ventana.withdraw()


primera_ventana.mainloop()
