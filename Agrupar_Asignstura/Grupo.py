from tkinter import *
from tkinter import messagebox

ventana = Tk()

ventana.title("Agrupar Asignatura")

ventana.geometry("250x100")

############################################################

label_G = Label(ventana, text = "Nombre del Grupo: ")

label_G.grid(column = 0, row = 0)

texto_CA = Entry(ventana, width = 10)

texto_CA.grid(column = 1, row = 0)

label_E1 = Label(ventana, text = "  ")

label_E1.grid(column = 0, row = 1)

############################################################

boton_agrupar = Button(ventana, text = "Agrupar")

boton_agrupar.grid(column = 0, row = 2)

############################################################

boton_CANCELAR = Button(ventana, text = "Cancelar")

boton_CANCELAR.grid(column = 1, row = 2)

############################################################

ventana.mainloop()