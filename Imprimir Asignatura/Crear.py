from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import sqlite3

con = sqlite3.connect("BD_UNIVERSIDAD")

def Abrir_Crear():

    ventana_crear = Toplevel()

    ventana_crear.title("Creando Asignatura")

    ventana_crear.geometry("550x250+700+200")

    #########################################

    #Funciones

    def CREAR():

        cursor_1 = con.cursor()
        lista = [(CA.get(),NA.get(),ND.get(),combo.get(),combo_HE.get(),combo_V.get(),Na.get())]
        cursor_1.execute("INSERT INTO Asignatura VALUES (?, ?, ?, ?, ?, ?)",lista)
        con.commit()
        mensaje = "Se ha creado la asignatura"
        messagebox.showinfo("Aviso", mensaje)


 #########################################

    #Variables

    NA = StringVar()

    ND = StringVar()

    Na = StringVar()

    CA = StringVar()


    #########################################

    #Nombre de la Asignatura

    label_E_0 = Label(ventana_crear, text = "  ")

    label_E_0.grid(column = 0,row = 0)

    label_NA = Label(ventana_crear, text = "Nombre de la Asignatura :")

    label_NA.grid(column = 1,row = 1)

    texto_NA = Entry(ventana_crear, width = 20, textvariable= NA)
    
    texto_NA.grid(column = 2, row = 1)

    label_E_1 = Label(ventana_crear, text = "  ")

    label_E_1.grid(column = 0,row = 2)

    #########################################

    #Docente de la Asignatura

    label_DA = Label(ventana_crear, text = "Docente de la Asignatura :")

    label_DA.grid(column = 1,row = 4)

    texto_DA = Entry(ventana_crear, width = 20, textvariable=ND)

    texto_DA.grid(column = 2, row = 4)

    label_E_2 = Label(ventana_crear, text = "  ")

    label_E_2.grid(column = 0,row = 5)

    #########################################

    #COMBOBOX Créditos

    label_Creditos = Label(ventana_crear, text = "Número de Créditos: ")

    label_Creditos.grid(column = 0, row = 6)

    combo = Combobox(ventana_crear)

    combo['values'] = ("1","2","3","4")

    combo.current(3)

    combo.grid(column = 1,  row = 6)

    #########################################

    #COMBOBOX Horas de estudio

    label_HE = Label(ventana_crear, text = "Horas de Estudio: ")

    label_HE.grid(column = 2, row = 6)

    combo_HE = Combobox(ventana_crear)

    combo_HE['values'] = ("1","2","3","4")

    combo_HE.current(3)

    combo_HE.grid(column = 3,  row = 6)

    #########################################

    #COMBOBOX Numero de Vacantes

    label_E_3 = Label(ventana_crear, text = "  ")

    label_E_3.grid(column = 0,row = 7)

    label_V = Label(ventana_crear, text = "Número de Vacantes: ")

    label_V.grid(column = 1, row = 8)

    combo_V = Combobox(ventana_crear)

    combo_V['values'] = ("10","20","30","40")

    combo_V.current(3)

    combo_V.grid(column = 2,  row = 8)

    label_E_4 = Label(ventana_crear, text = "  ")

    label_E_4.grid(column = 0,row = 9)

    #########################################

    #Nota aprobattoria

    label_NoA = Label(ventana_crear, text = "Nota aprobatoria :")

    label_NoA.grid(column = 0,row = 10)

    texto_NoA = Entry(ventana_crear, textvariable=Na, width = 10)

    texto_NoA.grid(column = 1, row = 10)

    #########################################

    #Códifo de asignatura

    label_CA = Label(ventana_crear, text = "Código de Asignatura :")

    label_CA.grid(column = 2,row = 10)

    texto_CA = Entry(ventana_crear, textvariable=CA ,width = 10)

    texto_CA.grid(column = 3, row = 10)

    label_E_5 = Label(ventana_crear, text = "  ")

    label_E_5.grid(column = 0,row = 11)

    #########################################

    texto_NA.focus()

    texto_DA.focus()

    texto_NoA.focus()

    texto_CA.focus()

    #########################################

    #Botón crear

    button_Crear = Button(ventana_crear, text = "Crear", command = CREAR)

    button_Crear.grid(column = 1, row = 12)

    #########################################

    #Botón Cancelar

    button_Cancelar = Button(ventana_crear, text = "Cancelar")

    button_Cancelar.grid(column = 2, row = 12)

    #########################################

    #Botón Limpiar

    button_Limpiar = Button(ventana_crear, text = "Limpiar")

    button_Limpiar.grid(column = 3, row = 12)

    #########################################