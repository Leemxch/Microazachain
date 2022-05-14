import tkinter as tk
from tkinter import ttk
from functools import partial

size = 30

def test(wii):
    for i in wii:
        print (i.get())

def start():
    # Main screen
    screen = tk.Tk()
    screen.title("Blockchain en micro tareas") #TODO
    screen.geometry(str(290+25*size) + "x" + str(70+25*size))
    screen.resizable(False, False)

    #Labels
    titleLabel = tk.Label(screen, text = "Agregar una nueva microtarea")
    titleLabel.place(x=30*(int(size/2)), y=10)

    microNombreLabel = tk.Label(screen, text = "Nombre")
    microNombreLabel.place(x = 5 * size, y = 50)
    microEmpresaLabel = tk.Label(screen, text = "Empresa")
    microEmpresaLabel.place(x = 5 * size, y = 100)
    microDescripcionLabel = tk.Label(screen, text = "Descripcion")
    microDescripcionLabel.place(x = 5 * size, y = 150)
    microCriteriosLabel = tk.Label(screen, text = "Criterios")
    microCriteriosLabel.place(x = 5 * size, y = 200)
    microRecompensaLabel = tk.Label(screen, text = "Recompensa")
    microRecompensaLabel.place(x = 5 * size, y = 250)
    microArchivosLabel = tk.Label(screen, text = "Link de los archivos")
    microArchivosLabel.place(x = 5 * size, y = 300)

    #Entries
    microNombreEntry = tk.Entry(screen, width = int(size * 4))
    microNombreEntry.place(x = 5 * size, y = 70)
    microEmpresaEntry = tk.Entry(screen, width = int(size * 4))
    microEmpresaEntry.place(x = 5 * size, y = 120)
    microDescripcionEntry = tk.Entry(screen, width = int(size * 4))
    microDescripcionEntry.place(x = 5 * size, y = 170)
    microCriteriosEntry = tk.Entry(screen, width = int(size * 4))
    microCriteriosEntry.place(x = 5 * size, y = 220)
    microRecompensaEntry = tk.Entry(screen, width = int(size * 4))
    microRecompensaEntry.place(x = 5 * size, y = 270)
    microArchivosEntry = tk.Entry(screen, width = int(size * 4))
    microArchivosEntry.place(x = 5 * size, y = 320)

    #Buttons
    publicarMicro = tk.Button(screen, text = "Publicar")
    publicarMicro.config(command = partial(test, [microNombreEntry,
                                                  microEmpresaEntry,
                                                  microDescripcionEntry,
                                                  microCriteriosEntry,
                                                  microRecompensaEntry,
                                                  microArchivosEntry]))
    publicarMicro.place(x = 5 * size, y = 350)


    screen.mainloop()
