from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

def Abrir_Editar():
    
    ventana_Editar = Toplevel()

    ventana_Editar.title("Editanto Asignatura")

    ventana_Editar.geometry("550x250+700+200")

    #########################################

    #Nombre de la Asignatura

    label_E_0 = Label(ventana_Editar, text = "  ")

    label_E_0.grid(column = 0,row = 0)

    label_NA = Label(ventana_Editar, text = "Nombre de la Asignatura :")

    label_NA.grid(column = 1,row = 1)

    texto_NA = Entry(ventana_Editar, width = 20)
    
    texto_NA.grid(column = 2, row = 1)

    label_E_1 = Label(ventana_Editar, text = "  ")

    label_E_1.grid(column = 0,row = 2)

    #########################################

    #Docente de la Asignatura

    label_DA = Label(ventana_Editar, text = "Docente de la Asignatura :")

    label_DA.grid(column = 1,row = 4)

    texto_DA = Entry(ventana_Editar, width = 20)

    texto_DA.grid(column = 2, row = 4)

    label_E_2 = Label(ventana_Editar, text = "  ")

    label_E_2.grid(column = 0,row = 5)

    #########################################

    texto_NA.focus()

    texto_DA.focus()

    #########################################

    #COMBOBOX Créditos

    label_Creditos = Label(ventana_Editar, text = "Número de Créditos: ")

    label_Creditos.grid(column = 0, row = 6)

    combo_créditos = Combobox(ventana_Editar)

    combo_créditos['values'] = ("1 CRÉDITO","2 CRÉDITOS","3 CRÉDITOS","4 CRÉDITOS")

    combo_créditos.current(3)

    combo_créditos.grid(column = 1,  row = 6)

    #########################################

    #COMBOBOX Horas de estudio

    label_HE = Label(ventana_Editar, text = "Horas de Estudio: ")

    label_HE.grid(column = 2, row = 6)

    combo_HE = Combobox(ventana_Editar)

    combo_HE['values'] = ("1 HORA","2 HORAS","3 HORAS","4 HORAS")

    combo_HE.current(3)

    combo_HE.grid(column = 3,  row = 6)

    #########################################

    #COMBOBOX Numero de Vacantes

    label_E_3 = Label(ventana_Editar, text = "  ")

    label_E_3.grid(column = 0,row = 7)

    label_V = Label(ventana_Editar, text = "Número de Vacantes: ")

    label_V.grid(column = 1, row = 8)

    combo_V = Combobox(ventana_Editar)

    combo_V['values'] = ("10 VACANTES","20 VACANTES","30 VACANTES","40 VACANTES")

    combo_V.current(3)

    combo_V.grid(column = 2,  row = 8)

    label_E_4 = Label(ventana_Editar, text = "  ")

    label_E_4.grid(column = 0,row = 9)

    #########################################

    #Nota aprobattoria

    label_NoA = Label(ventana_Editar, text = "Nota aprobatoria :")

    label_NoA.grid(column = 0,row = 10)

    texto_NoA = Entry(ventana_Editar, width = 10)

    texto_NoA.grid(column = 1, row = 10)

    #########################################

    #Códifo de asignatura

    label_CA = Label(ventana_Editar, text = "Código de Asignatura :")

    label_CA.grid(column = 2,row = 10)

    texto_CA = Entry(ventana_Editar, width = 10)

    texto_CA.grid(column = 3, row = 10)

    label_E_5 = Label(ventana_Editar, text = "  ")

    label_E_5.grid(column = 0,row = 11)

    #########################################

    #Botón crear

    def Guardar():

        mensaje = "Los cambios se han guardado con éxito."

        messagebox.showinfo("Aviso", mensaje)

    button_Guardar = Button(ventana_Editar, text = "Guardar", command = Guardar)

    button_Guardar.grid(column = 1, row = 12)

    #########################################

    #Botón Cancelar

    button_Cancelar = Button(ventana_Editar, text = "Cancelar")

    button_Cancelar.grid(column = 2, row = 12)

    #########################################