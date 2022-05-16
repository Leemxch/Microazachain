import tkinter as tk
from functools import partial
from BlockChain import *
from logic import *

size = 30
listaEnlazada = ListaEnlazadaDoble()
listaEnlazada.insertar_inicio(
    MicroTarea("Nombre", "Empresa", "Descripcion", "Criterios", "Recompensa", "Links de los archivos"),
    "Genesis",
    "Genesis"
)
node = listaEnlazada.getNode()
prosumer = "Max"

def showHide(show, hide, state=0):
    if state == 1:
        hide.withdraw()
        show.deiconify()
    show.withdraw()
    hide.deiconify()

def save(estado, conjunto):
    global node
    node = verify(conjunto, estado, node)
    check = node.getMicrotarea()
    print(check.getNombre())

def seleccionar(mainScreen):
    global node, listaEnlazada, prosumer
    micro = node.getMicrotarea()


    #Screen
    mainScreen.withdraw()

    seleccionar = tk.Tk()
    seleccionar.title("Prototipo de blockchain en micro tareas")  # TODO
    seleccionar.geometry(str(290 + 25 * size) + "x" + str(70 + 25 * size))
    seleccionar.resizable(False, False)

    # Labels
    titleLabel = tk.Label(seleccionar, text="Buscar una microtarea")
    titleLabel.place(x=30 * (int(size / 2)), y=10)

    agregarNombreLabel = tk.Label(seleccionar, text= micro.getNombre())
    agregarNombreLabel.place(x=5 * size, y=50)
    agregarEmpresaLabel = tk.Label(seleccionar, text= micro.getEmpresa())
    agregarEmpresaLabel.place(x=5 * size, y=100)
    agregarDescripcionLabel = tk.Label(seleccionar, text= micro.getDescripcion())
    agregarDescripcionLabel.place(x=5 * size, y=150)
    agregarCriteriosLabel = tk.Label(seleccionar, text= micro.getCriterios())
    agregarCriteriosLabel.place(x=5 * size, y=200)
    agregarRecompensaLabel = tk.Label(seleccionar, text= micro.getRecompensa())
    agregarRecompensaLabel.place(x=5 * size, y=250)
    agregarArchivosLabel = tk.Label(seleccionar, text= micro.getArchivos())
    agregarArchivosLabel.place(x=5 * size, y=300)

    conjunto = [agregarNombreLabel,
                agregarEmpresaLabel,
                agregarDescripcionLabel,
                agregarCriteriosLabel,
                agregarRecompensaLabel,
                agregarArchivosLabel]

    # Button
    anterior = tk.Button(seleccionar, text="Anterior")
    anterior.config(command=partial(save, 0, conjunto))
    anterior.place(x=5 * size, y=350)

    siguiente = tk.Button(seleccionar, text="Siguiente")
    siguiente.config(command=partial(save, 1, conjunto))
    siguiente.place(x=10 * size, y=350)

    reclamar = tk.Button(seleccionar, text="Reclamar")
    reclamar.config(command=partial(reclamarTarea, conjunto, node, prosumer))
    reclamar.place(x=15 * size, y=350)

    volverMainSel = tk.Button(seleccionar, text="Volver")
    volverMainSel.place(x=5 * size, y=25 * size)
    volverMainSel.config(command=partial(showHide, seleccionar, mainScreen, 1))

    seleccionar.mainloop()

def agregar(lista, mainScreen):
    mainScreen.withdraw()

    # Main screen
    agregar = tk.Tk()
    agregar.title("Prototipo de blockchain en micro tareas")  # TODO
    agregar.geometry(str(290 + 25 * size) + "x" + str(70 + 25 * size))
    agregar.resizable(False, False)

    # Labels
    titleLabel = tk.Label(agregar, text="Agregar una nueva microtarea")
    titleLabel.place(x=30 * (int(size / 2)), y=10)

    microNombreLabel = tk.Label(agregar, text="Nombre")
    microNombreLabel.place(x=5 * size, y=50)
    microEmpresaLabel = tk.Label(agregar, text="Empresa")
    microEmpresaLabel.place(x=5 * size, y=100)
    microDescripcionLabel = tk.Label(agregar, text="Descripcion")
    microDescripcionLabel.place(x=5 * size, y=150)
    microCriteriosLabel = tk.Label(agregar, text="Criterios")
    microCriteriosLabel.place(x=5 * size, y=200)
    microRecompensaLabel = tk.Label(agregar, text="Recompensa")
    microRecompensaLabel.place(x=5 * size, y=250)
    microArchivosLabel = tk.Label(agregar, text="Link de los archivos")
    microArchivosLabel.place(x=5 * size, y=300)

    # Entries
    microNombreEntry = tk.Entry(agregar, width=int(size * 4))
    microNombreEntry.place(x=5 * size, y=70)
    microEmpresaEntry = tk.Entry(agregar, width=int(size * 4))
    microEmpresaEntry.place(x=5 * size, y=120)
    microDescripcionEntry = tk.Entry(agregar, width=int(size * 4))
    microDescripcionEntry.place(x=5 * size, y=170)
    microCriteriosEntry = tk.Entry(agregar, width=int(size * 4))
    microCriteriosEntry.place(x=5 * size, y=220)
    microRecompensaEntry = tk.Entry(agregar, width=int(size * 4))
    microRecompensaEntry.place(x=5 * size, y=270)
    microArchivosEntry = tk.Entry(agregar, width=int(size * 4))
    microArchivosEntry.place(x=5 * size, y=320)

    # Buttons
    publicarMicro = tk.Button(agregar, text="Publicar")
    publicarMicro.config(command=partial(createMicroTask, [microNombreEntry,
                                                           microEmpresaEntry,
                                                           microDescripcionEntry,
                                                           microCriteriosEntry,
                                                           microRecompensaEntry,
                                                           microArchivosEntry],
                                         lista))
    publicarMicro.place(x=5 * size, y=350)
    volverMain = tk.Button(agregar, text="Volver")
    volverMain.place(x=5 * size, y=25*size)
    volverMain.config(command=partial(showHide, agregar, mainScreen, 1))

    agregar.mainloop()


def start():
    global listaEnlazada
    # Main screen
    screen = tk.Tk()
    screen.title("Prototipo de blockchain en micro tareas")  # TODO
    screen.geometry(str(290 + 25 * size) + "x" + str(70 + 25 * size))
    screen.resizable(False, False)

    # Labels
    titleLabel = tk.Label(screen, text="Inicio")
    titleLabel.place(x=30 * (int(size / 2)), y=10)

    # Buttons
    seleccionarButton = tk.Button(screen, text="Seleccionar una micro tarea")
    seleccionarButton.config(command=partial(seleccionar, screen))
    seleccionarButton.place(x=13 * size, y=200)

    agregarButton = tk.Button(screen, text="Agregar una micro tarea")
    agregarButton.config(command=partial(agregar, listaEnlazada, screen))
    agregarButton.place(x=13 * size, y=400)

    screen.mainloop()
