from tkinter import *
from tkinter import ttk

ventana_buscar = Tk()

ventana_buscar.title("Agrupando Asignaturas")

ventana_buscar.geometry("700x500")

#########################################

#Nombre de la Asignatura

label_E_0 = Label(ventana_buscar, text = "  ")

label_E_0.grid(column = 0,row = 0)

label_NA = Label(ventana_buscar, text = "Nombre de la Asignatura :")

label_NA.grid(column = 1,row = 1)

texto_NA = Entry(ventana_buscar, width = 20)
  
texto_NA.grid(column = 2, row = 1)

label_E_1 = Label(ventana_buscar, text = "  ")

label_E_1.grid(column = 0,row = 2)

#########################################

#Código de la Asignatura

label_CoA = Label(ventana_buscar, text = "Código de la Asignatura :")

label_CoA.grid(column = 1,row = 4)

texto_CoA = Entry(ventana_buscar, width = 20)

texto_CoA.grid(column = 2, row = 4)

label_E_2 = Label(ventana_buscar, text = "  ")

label_E_2.grid(column = 0,row = 5)

#########################################

texto_NA.focus()

texto_CoA.focus()

#########################################

#Botón Buscar

button_Buscar = Button(ventana_buscar, text = "Buscar")

button_Buscar.grid(column = 1, row = 6)

#########################################

#Botón Cancelar

button_Cancelar = Button(ventana_buscar, text = "Cancelar")

button_Cancelar.grid(column = 2, row = 6)

label_E_3 = Label(ventana_buscar, text = "  ")

label_E_3.grid(column = 0,row = 7)

label_E_4 = Label(ventana_buscar, text = "  ")

label_E_4.grid(column = 0,row = 8)

#########################################

#Tabla de Asignaturas

label_E_5 = Label(ventana_buscar, text = "  ")

label_E_5.grid(column = 7,row = 0)

tv = ttk.Treeview(ventana_buscar, columns= ("col_1","col_2","col_3"))

tv.column("#0", width=80)
tv.column("col_1", width=80, anchor=CENTER)
tv.column("col_2", width=80, anchor=CENTER)
tv.column("col_3", width=80, anchor=CENTER)

tv.heading("#0", text="Nombre de la Asignatura",anchor=CENTER)
tv.heading("col_1", text="Docente",anchor=CENTER)
tv.heading("col_2", text="Créditos",anchor=CENTER)
tv.heading("col_3", text="Código de la Asignatura",anchor=CENTER)

tv.grid(column=2, row=9)

#########################################


ventana_buscar.mainloop()