from tkinter import *
from tkinter import messagebox

def Abrir_Agrupar():

    ventana_agrupar = Toplevel()

    ventana_agrupar.title("Agrupar Asignatura")

    ventana_agrupar.geometry("250x100+700+200")

    ############################################################

    label_CA = Label(ventana_agrupar, text = "Código de la Asignatura: ")

    label_CA.grid(column = 0, row = 0)

    texto_CA = Entry(ventana_agrupar, width = 10)

    texto_CA.grid(column = 1, row = 0)

    label_E1 = Label(ventana_agrupar, text = "  ")

    label_E1.grid(column = 0, row = 1)

    ############################################################

    boton_agrupar = Button(ventana_agrupar, text = "Agrupar")

    boton_agrupar.grid(column = 0, row = 2)

    ############################################################

    boton_CANCELAR = Button(ventana_agrupar, text = "Cancelar")

    boton_CANCELAR.grid(column = 1, row = 2)

    ############################################################
