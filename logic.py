from BlockChain import *

def createMicroTask(task, lista, prosumer, estado = "En proceso"):
    microTarea = MicroTarea(task[0].get(),
                            task[1].get(),
                            task[2].get(),
                            task[3].get(),
                            task[4].get(),
                            task[5].get())

    lista.insertar_fin(microTarea, estado, prosumer)
    lista.toString()

def mostrarSiguiente(screen, lista):
    print()