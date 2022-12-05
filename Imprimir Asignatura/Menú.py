from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *

import sqlite3

import Agrupar
import Buscar
import Crear
import Editar

ventana = Tk()

ventana.title("Menú")

ventana.geometry("500x280+190+100")

con = sqlite3.connect("BD_UNIVERSIDAD")

############################################################

#Tabla de Asignaturas

label_E_8 = Label(ventana, text = " REGISTRO DE ASIGNATURAS  ").place(x=120, y=10)

label_E_6 = Label(ventana, text = "  ")

label_E_6.grid(column = 0,row = 2)

tv = ttk.Treeview(ventana, columns= ("col_1","col_2","col_3"))

tv.column("#0", width=80)
tv.column("col_1", width=80, anchor=CENTER)
tv.column("col_2", width=80, anchor=CENTER)
tv.column("col_3", width=80, anchor=CENTER)

tv.heading("#0", text="Nombre de la Asignatura",anchor=CENTER)
tv.heading("col_1", text="Docente",anchor=CENTER)
tv.heading("col_2", text="Créditos",anchor=CENTER)
tv.heading("col_3", text="Código de la Asignatura",anchor=CENTER)

tv.place(x=40, y=30)

############################################################

def Crear_Asignatura():

    Crear.Abrir_Crear()

boton_Crear = Button(ventana, text = "Crear", command = Crear_Asignatura).place(x=390, y=40)

############################################################
def Editar_Asignatura():

    Editar.Abrir_Editar()

boton_Editar = Button(ventana, text = "Editar", command = Editar_Asignatura).place(x=390, y=70)

############################################################

def agrupar():
    Agrupar.Abrir_Agrupar()

boton_Agrupar = Button(ventana, text = "Agrupar", command = agrupar).place(x=390, y=100)

############################################################

boton_Imprimir = Button(ventana, text = "Imprimir").place(x=390, y=130)

############################################################

ventana.mainloop()