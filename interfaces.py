import tkinter as tk
from functools import partial
from BlockChain import *
from logic import *

size = 20
listaEnlazada = ListaEnlazadaDoble()
listaEnlazada.insertar_inicio(
    MicroTarea("Nombre", "Empresa", "Descripcion", "Criterios", "Recompensa", "Links de los archivos"),
    "Genesis",
    "Genesis"
)
node = listaEnlazada.getNode()
prosumer = "Max"
blockchain = Blockchain()
def showHide(show, hide, state=0):
    if state == 1:
        hide.withdraw()
        show.deiconify()
    show.withdraw()
    hide.deiconify()


def save(estado, conjunto):
    global node, prosumer
    if estado == 2:
        node = reclamarTarea(conjunto, node, prosumer)
    elif estado == 1 or estado == 0:
        node = verify(conjunto, estado, node)


def seleccionar(mainScreen):
    global node, listaEnlazada, prosumer
    micro = node.getMicrotarea()

    # Screen
    mainScreen.withdraw()

    seleccionar = tk.Tk()
    seleccionar.title("Prototipo de blockchain en micro tareas")  # TODO
    seleccionar.geometry(str(290 + 25 * size) + "x" + str( 22 * size))
    seleccionar.resizable(False, False)
    seleccionar.configure(bg="#27242A")

    # Labels
    titleLabel = tk.Label(seleccionar, text="Buscar una microtarea",font=("Bold",20),fg="#00FF9F",bg="#27242A")
    titleLabel.place(x=25 * (int(size / 2)), y=10)

    agregarNombreLabel = tk.Label(seleccionar, text=micro.getNombre(),font=("Bold",15),fg="#00FF9F",bg="#27242A")
    agregarNombreLabel.place(x=5 * size, y=50)
    agregarEmpresaLabel = tk.Label(seleccionar, text=micro.getEmpresa(),font=("Bold",15),fg="#00FF9F",bg="#27242A")
    agregarEmpresaLabel.place(x=5 * size, y=100)
    agregarDescripcionLabel = tk.Label(seleccionar, text=micro.getDescripcion(),font=("Bold",15),fg="#00FF9F",bg="#27242A")
    agregarDescripcionLabel.place(x=5 * size, y=150)
    agregarCriteriosLabel = tk.Label(seleccionar, text=micro.getCriterios(),font=("Bold",15),fg="#00FF9F",bg="#27242A")
    agregarCriteriosLabel.place(x=5 * size, y=200)
    agregarRecompensaLabel = tk.Label(seleccionar, text=micro.getRecompensa(),font=("Bold",15),fg="#00FF9F",bg="#27242A")
    agregarRecompensaLabel.place(x=5 * size, y=250)
    agregarArchivosLabel = tk.Label(seleccionar, text=micro.getArchivos(),font=("Bold",15),fg="#00FF9F",bg="#27242A")
    agregarArchivosLabel.place(x=5 * size, y=300)

    conjunto = [agregarNombreLabel,
                agregarEmpresaLabel,
                agregarDescripcionLabel,
                agregarCriteriosLabel,
                agregarRecompensaLabel,
                agregarArchivosLabel]

    # Button
    anterior = tk.Button(seleccionar, text="Anterior",bg="#00FF9F")
    anterior.config(command=partial(save, 0, conjunto))
    anterior.place(x=5 * size, y=350)

    siguiente = tk.Button(seleccionar, text="Siguiente",bg="#00FF9F")
    siguiente.config(command=partial(save, 1, conjunto))
    siguiente.place(x=10 * size, y=350)

    reclamar = tk.Button(seleccionar, text="Reclamar",bg="#00FF9F")
    reclamar.config(command=partial(save, 2, conjunto))
    reclamar.place(x=15 * size, y=350)

    volverMainSel = tk.Button(seleccionar, text="Volver",bg="#FF8A6B")
    volverMainSel.place(x=5 * size, y=20 * size)
    volverMainSel.config(command=partial(showHide, seleccionar, mainScreen, 1))

    seleccionar.mainloop()


def agregar(mainScreen):
    global listaEnlazada
    lista = listaEnlazada
    mainScreen.withdraw()

    # Main screen
    agregar = tk.Tk()
    agregar.title("Prototipo de blockchain en micro tareas")  # TODO
    agregar.geometry(str(250 + 20 * size) + "x" + str(70 + 25 * size))
    agregar.resizable(False, False)
    agregar.configure(bg="#27242A")

    # Labels
    titleLabel = tk.Label(agregar, text="Agregar una nueva microtarea",font=("Bold",20),fg="#00FF9F",bg="#27242A")
    titleLabel.place(x=13 * (int(size / 2)), y=10)

    microNombreLabel = tk.Label(agregar, text="Nombre",fg="#00FF9F",bg="#27242A")
    microNombreLabel.place(x=4 * size, y=60)
    microEmpresaLabel = tk.Label(agregar, text="Empresa",fg="#00FF9F",bg="#27242A")
    microEmpresaLabel.place(x=4 * size, y=120)
    microDescripcionLabel = tk.Label(agregar, text="Descripcion",fg="#00FF9F",bg="#27242A")
    microDescripcionLabel.place(x=4 * size, y=180)
    microCriteriosLabel = tk.Label(agregar, text="Criterios",fg="#00FF9F",bg="#27242A")
    microCriteriosLabel.place(x=4 * size, y=240)
    microRecompensaLabel = tk.Label(agregar, text="Recompensa",fg="#00FF9F",bg="#27242A")
    microRecompensaLabel.place(x=4 * size, y=300)
    microArchivosLabel = tk.Label(agregar, text="Link de los archivos",fg="#00FF9F",bg="#27242A")
    microArchivosLabel.place(x=4 * size, y=360)

    # Entries
    microNombreEntry = tk.Entry(agregar, width=int(size * 4))
    microNombreEntry.place(x=4 * size, y=90)
    microEmpresaEntry = tk.Entry(agregar, width=int(size * 4))
    microEmpresaEntry.place(x=4 * size, y=150)
    microDescripcionEntry = tk.Entry(agregar, width=int(size * 4))
    microDescripcionEntry.place(x=4 * size, y=210)
    microCriteriosEntry = tk.Entry(agregar, width=int(size * 4))
    microCriteriosEntry.place(x=4 * size, y=270)
    microRecompensaEntry = tk.Entry(agregar, width=int(size * 4))
    microRecompensaEntry.place(x=4 * size, y=330)
    microArchivosEntry = tk.Entry(agregar, width=int(size * 4))
    microArchivosEntry.place(x=4 * size, y=390)

    # Buttons
    publicarMicro = tk.Button(agregar, text="Publicar",bg="#00FF9F")
    publicarMicro.config(command=partial(createMicroTask, [microNombreEntry,
                                                           microEmpresaEntry,
                                                           microDescripcionEntry,
                                                           microCriteriosEntry,
                                                           microRecompensaEntry,
                                                           microArchivosEntry],
                                         lista))
    publicarMicro.place(x=4 * size, y=420)
    volverMain = tk.Button(agregar, text="Volver",bg="#FF8A6B")
    volverMain.place(x=7.5 * size, y=420)
    volverMain.config(command=partial(showHide, agregar, mainScreen, 1))

    agregar.mainloop()

def publicar(mainScreen):
    global listaEnlazada, prosumer, blockchain
    mainScreen.withdraw()

    labelsNames = publicarTarea(listaEnlazada, prosumer)
    # Screen
    publicarScreen = tk.Tk()
    publicarScreen.title("Prototipo de blockchain en micro tareas")  # TODO
    publicarScreen.geometry(str(290 + 25 * size) + "x" + str(70 + 25 * size))
    publicarScreen.resizable(False, False)
    publicarScreen.configure(bg="#27242A")
    
    # Labels
    titleLabel = tk.Label(publicarScreen, text="Publicar una solución de microtarea",font=("Bold",20),fg="#00FF9F",bg="#27242A")
    titleLabel.place(x=17 * (int(size / 2)), y=10)

    publicarNombreLabel = tk.Label(publicarScreen, text=labelsNames[1],font=("Bold",15),fg="#00FF9F",bg="#27242A")
    publicarNombreLabel.place(x=5 * size, y=60)
    publicarEmpresaLabel = tk.Label(publicarScreen, text=labelsNames[2],font=("Bold",15),fg="#00FF9F",bg="#27242A")
    publicarEmpresaLabel.place(x=5 * size, y=120)
    publicarDescripcionLabel = tk.Label(publicarScreen, text=labelsNames[3],font=("Bold",15),fg="#00FF9F",bg="#27242A")
    publicarDescripcionLabel.place(x=5 * size, y=180)
    publicarCriteriosLabel = tk.Label(publicarScreen, text=labelsNames[4],font=("Bold",15),fg="#00FF9F",bg="#27242A")
    publicarCriteriosLabel.place(x=5 * size, y=240)
    publicarRecompensaLabel = tk.Label(publicarScreen, text=labelsNames[5],font=("Bold",15),fg="#00FF9F",bg="#27242A")
    publicarRecompensaLabel.place(x=5 * size, y=300)
    publicarArchivosLabel = tk.Label(publicarScreen, text=labelsNames[6],font=("Bold",15),fg="#00FF9F",bg="#27242A")
    publicarArchivosLabel.place(x=5 * size, y=360)

    # Button
    publicar = tk.Button(publicarScreen, text="Publicar solución",bg="#00FF9F")
    publicar.config(command=partial(eliminarDeLista, listaEnlazada, labelsNames[0], blockchain))
    publicar.place(x=5 * size, y=420)


    volverMainSel = tk.Button(publicarScreen, text="Volver",bg="#FF8A6B")
    volverMainSel.place(x=5 * size, y=25 * size)
    volverMainSel.config(command=partial(showHide, publicarScreen, mainScreen, 1))

    publicarScreen.mainloop()


def start():
    global listaEnlazada
    # Main screen
    screen = tk.Tk()
    screen.title("Prototipo de blockchain en micro tareas")  # TODO
    screen.geometry(str(290 + 25 * size) + "x" + str(20 * size))
    screen.resizable(False, False)
    screen.configure(bg="#27242A")

    # Labels
    titleLabel = tk.Label(screen, text="Prueba de blockchain",font=("Bold",30),fg="#00FF9F",bg="#27242A")

    titleLabel.place(x=20 * (int(size / 2)), y=10)

    # Buttons

    agregarButton = tk.Button(screen, text="Agregar una micro tarea")
    agregarButton.config(command=partial(agregar, screen),bg="#00FF9F",height= 2,width=25,font=("Arial",16) )
    agregarButton.place(x=12 * size, y=100)

    seleccionarButton = tk.Button(screen, text="Seleccionar una micro tarea")
    seleccionarButton.config(command=partial(seleccionar, screen),bg="#00FF9F",height= 2,width=25,font=("Arial",16))
    seleccionarButton.place(x=12 * size, y=200)

    solucionButton = tk.Button(screen, text="Publicar una solucion")
    solucionButton.config(command=partial(publicar, screen),bg="#00FF9F",height= 2,width=25,font=("Arial",16))
    solucionButton.place(x=12 * size, y=300)

    screen.mainloop()
