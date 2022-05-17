from BlockChain import *
from tkinter import messagebox


def createMicroTask(task, lista, prosumer="", estado="Disponible"):
    # Instancia de un nuevo objeto tipo MicroTarea
    microTarea = MicroTarea(task[0].get(),
                            task[1].get(),
                            task[2].get(),
                            task[3].get(),
                            task[4].get(),
                            task[5].get())

    # Insertar a la lista doble enlazada
    lista.insertar_fin(microTarea, estado, prosumer)
    messagebox.showinfo(message=task[0].get(), title="Se ha publicado con éxito")


def verify(lista, estado, node):
    # Variables para revisar aspectos del siguiente y anterior nodo
    check1 = node.getNref()
    check2 = node.getPref()
    # If inicial de la busqueda
    if node.getEstado() == "Genesis":
        # Validación si no hay una micro tarea insertada
        if (node.getNref() is None) and (node.getPref() is None):
            messagebox.showerror(title="Error", message="No hay micro tareas existentes")
            return node
        else:
            # Cambio de estado del Genesis para no mostrarlo durante la navegacion
            node.setEstado("Inmutable")
            return rotar(lista, node.getNref())
    # Flujo normal del programa
    elif node.getEstado() == "Disponible" or node.getEstado() == "Genesis":
        # Validacion si el usuario hizo click en el boton de siguiente
        if estado == 1:
            # Validación si el nodo siguiente es nulo para dar error
            if node.getNref() is None:
                messagebox.showerror(title="Error", message="No hay más micro tareas siguiente")
                return node
            # Validación si el siguiente nodo tiene otro estado
            elif check1 is not None:
                if check1.getEstado() != "Disponible":
                    return verify(lista, estado, node.getNref())
                else:
                    return rotar(lista, node.getNref())
        # Validacion si el usuario hizo click en el boton de anterior
        elif estado == 0:
            check = node.getPref()
            # Validacion para ignorar el Genesis
            if check.getEstado() == "Inmutable":
                messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                return node
            elif check.getEstado() != "Disponible":
                return verify(lista, estado, node.getPref())
            # Validacionn para ver si el nodo anterior es nulo para dar error
            elif node.getPref() is None:
                messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                return node
            # Validacion si el estado del siguente nodo es Disponible
            elif check2 is not None:
                if check2.getEstado() != "Inmutable":
                    if check2.getEstado() == "Disponible":
                        print("disponible")
                        return rotar(lista, node.getPref())
                    elif check2.getEstado() == "Inmutable":
                        print("desarrollo")
                        return verify(lista, estado, node.getPref())
                    else:
                        messagebox.showerror(title="Error", message="No hay más micro tareas anterior")
                        return node
            # Flujo normal
            elif check.getEstado() != "Inmutable":
                return rotar(lista, node.getPref())
    # Verifica si el anterior o siguiente esta disponible o no para buscar el siguiente con recursión
    elif check1 is not None and estado == 1:
        if check1.getEstado() != "Disponible":
            if estado == 1 and node.getPref() is not None:
                return verify(lista, estado, node.getPref())
        elif check1.getEstado() == "Disponible":
            return rotar(lista, check1)
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
                return verify(lista, estado, node.getPref())
        elif check2.getEstado() == "Disponible":
            return rotar(lista, check2)
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
    # Cambio de los valores del estado y prosumer
    node.setEstado("En desarrollo")
    node.setProsumer(prosumer)
    # Variables para revisar transicion de nodo
    check1 = node.getNref()
    check2 = node.getPref()
    if not (check1 is None):
        # Verificar siguiente
        if check1.getEstado() == "Disponible":
            return rotar(lista, node.getNref())
    elif not (check2 is None):
        # Verificar anterior
        if check2.getEstado() == "Disponible":
            return rotar(lista, node.getPref())
    else:
        messagebox.showerror(title="Error", message="No hay micro tareas disponibles")
        return node


def rotar(lista, node):
    # Cambiar los datos de los labels
    micro = node.getMicrotarea()
    lista[0].config(text=micro.getNombre())
    lista[1].config(text=micro.getEmpresa())
    lista[2].config(text=micro.getDescripcion())
    lista[3].config(text=micro.getCriterios())
    lista[4].config(text=micro.getRecompensa())
    lista[5].config(text=micro.getArchivos())
    return node

def publicarTarea(lista, prosumer):
    node = lista.getNode()
    while node.getNref() is not None:
        if node.getProsumer() == prosumer:
            datos = node.getMicrotarea()
            return [node,
                    datos.getNombre(),
                    datos.getEmpresa(),
                    datos.getDescripcion(),
                    datos.getCriterios(),
                    datos.getRecompensa(),
                    datos.getArchivos()

            ]
        node = node.getNref()
    messagebox.showerror(title="Error", message="No hay micro tareas reclamadas")
    return ["",
            "No hay reclamadas",
            "No hay reclamadas",
            "No hay reclamadas",
            "No hay reclamadas",
            "No hay reclamadas",
            "No hay reclamadas"
            ]

def eliminarDeLista(lista, node, block):
    eliminar = node.getMicrotarea()
    #lista.borrar_por_elemento(eliminar)
    block.create_block(eliminar, "Finalizado", node.getProsumer())
    showText = block.display_chain()
    messagebox.showinfo(title="Success!", message=showText)