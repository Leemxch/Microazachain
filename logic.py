from BlockChain import *
from tkinter import messagebox

def createMicroTask(task, lista, prosumer = "", estado = "Disponible"):
    microTarea = MicroTarea(task[0].get(),
                            task[1].get(),
                            task[2].get(),
                            task[3].get(),
                            task[4].get(),
                            task[5].get())

    lista.insertar_fin(microTarea, estado, prosumer)
    lista.toString()
    messagebox.showinfo(message = task[0].get(), title = "Se ha publicado con éxito")

def verify(lista, estado, node):
    if node.getEstado() == "Genesis":
        if (node.getNref() is None) and (node.getPref() is None):
            print("No hay nada en los extremos")
            messagebox.showerror(title="Error", message="No hay más micro tareas")
            return node
        else:
            node.setEstado("Inmutable")
            return rotar(lista, node.getNref())
    elif node.getEstado() != "Disponible":
        if estado == 1:
            return verify(lista, estado, node.getNref())
        elif estado == 0:
            return verify(lista, estado, node.getPref())
    elif node.getEstado() == "Disponible":
        if estado == 1:
            if node.getNref() is None:
                messagebox.showerror(title="Error", message="No hay más micro tareas siguiente")
                print("No hay mas info")
                return node
            print("Hay otro nodo")
            return rotar(lista, node.getNref())
        else:
            if node.getPref() is None:
                messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                print("No hay mas info")
                return node
            print("Hay otro nodo")
            return rotar (lista, node.getPref())

def rotar(lista, node):
    micro = node.getMicrotarea()
    lista[0].config( text = micro.getNombre())
    lista[1].config( text = micro.getEmpresa())
    lista[2].config( text = micro.getDescripcion())
    lista[3].config( text = micro.getCriterios())
    lista[4].config( text = micro.getRecompensa())
    lista[5].config( text = micro.getArchivos())

    return node
