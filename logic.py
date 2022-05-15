from BlockChain import *
from tkinter import messagebox

def createMicroTask(task, lista, prosumer, estado = "Disponible"):
    microTarea = MicroTarea(task[0].get(),
                            task[1].get(),
                            task[2].get(),
                            task[3].get(),
                            task[4].get(),
                            task[5].get())

    lista.insertar_fin(microTarea, estado, prosumer)
    lista.toString()
    messagebox.showinfo(message = task[0].get(), title = "Se ha publicado con éxito")

def mostrarSiguiente(screen, lista):
    print()