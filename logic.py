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
    if node is not None:
        check1 = node.getNref()
        check2 = node.getPref()
        if node.getEstado() == "Genesis":
            if (node.getNref() is None) and (node.getPref() is None):
                messagebox.showerror(title="Error", message="No hay micro tareas existentes")
                return node
            else:
                node.setEstado("Inmutable")
                return rotar(lista, node.getNref())
        elif node.getEstado() == "Disponible" or node.getEstado() == "Genesis":
            if estado == 1:
                if node.getNref() is None:
                    messagebox.showerror(title="Error", message="No hay más micro tareas siguiente")
                    return node
                elif check1.getEstado() != "Disponible":
                    return verify(lista, estado, node.getNref())
                else:
                    return rotar(lista, node.getNref())
            elif estado == 0:
                check = node.getPref()
                if check.getEstado() == "Inmutable":
                    messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                    return node
                elif node.getPref() is None:
                    messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                    return node
                elif check2.getEstado() == "Disponible":
                    return verify(lista, estado, node.getPref)
                elif check.getEstado() != "Inmutable":
                    return rotar (lista, node.getPref())
        # Verifica si el anterior o siguiente esta disponible o no
        elif check1 is not None and estado == 1:
            if check1.getEstado() != "Disponible":
                if estado == 1 and node.getPref() is not None:
                    return verify(lista, estado, node.getPref())
            else:
                if estado == 1:
                    messagebox.showerror(title="Error", message="No hay más micro tareas siguiente")
                    return node
                else:
                    messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                    return node
        elif check2 is not None and estado == 0:
            if check2.getEstado() != "Disponible":
                if estado == 0 and node.getNref() is not None:
                    return verif(lista, estado, node.getNref())
            else:
                if estado == 1:
                    messagebox.showerror(title="Error", message="No hay más micro tareas siguiente")
                    return node
                else:
                    messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                    return node
        else:
            if estado == 1:
                messagebox.showerror(title="Error", message="No hay más micro tareas siguiente")
                return node
            else:
                messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                return node


def reclamarTarea(lista, node, prosumer):
    node.setEstado("En desarrollo")
    node.setProsumer(prosumer)
    node.toString()
    check1 = node.getNref()
    check2 = node.getPref()
    if not (check1 is None):
        print("why")
        if check1.getEstado() == "Disponible":
            print("reclamado sigue adelante")
            return rotar(lista, node.getNref())
    elif not (check2 is None):
        print("tho")
        if check2.getEstado() == "Disponible":
            print("reclamado sigue atras")
            return rotar(lista,node.getPref())
    else:
        messagebox.showerror(title="Error", message="No hay micro tareas disponibles")
        return node

def rotar(lista, node):
    micro = node.getMicrotarea()
    lista[0].config( text = micro.getNombre())
    lista[1].config( text = micro.getEmpresa())
    lista[2].config( text = micro.getDescripcion())
    lista[3].config( text = micro.getCriterios())
    lista[4].config( text = micro.getRecompensa())
    lista[5].config( text = micro.getArchivos())
    return node
