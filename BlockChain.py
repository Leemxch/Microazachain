import hashlib


class MicroTarea:
    def __init__(self, nombre, empresa, descripcion, criterios, recompensa, archivos):
        self.nombre = nombre
        self.empresa = empresa
        self.descripcion = descripcion
        self.criterios = criterios
        self.recompensa = recompensa
        self.archivos = archivos

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEmpresa(self):
        return self.empresa

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(descripcion, self):
        self.descripcion = descripcion

    def getCriterios(self):
        return self.criterios

    def setCriterios(self, criterios):
        self.criterios = criterios

    def getRecompensa(self):
        return self.recompensa

    def setRecompensa(self, recompensa):
        self.recompensa = recompensa

    def getArchivos(self):
        return self.archivos

    def setArchivos(self, archivos):
        self.archivos = archivos

    def toString(self):
        print("Nombre: " + self.nombre,
              "Empresa: " + self.empresa,
              "Descripcion: " + self.descripcion,
              "Criterios: " + self.criterios,
              "Recompensa" + self.recompensa,
              "Archivos: " + self.archivos)


class Node:
    def __init__(self, microtarea, estado, prosumer):
        self.microtarea = microtarea
        self.estado = estado
        self.prosumer = prosumer
        self.nref = None
        self.pref = None

    def getMicrotarea(self):
        return self.microtarea

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getProsumer(self):
        return self.prosumer

    def setProsumer(self, prosumer):
        self.prosumer = prosumer

    def getNref(self):
        return self.nref

    def getPref(self):
        return self.pref

    def toString(self):
        print(self.microtarea.getNombre(), self.estado, self.prosumer)


class ListaEnlazadaDoble:

    def __init__(self):
        self.start_node = None

    def insertar_lista_vacia(self, microtarea, estado, prosumer):
        if self.start_node is None:
            new_node = Node(microtarea, estado, prosumer)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insertar_inicio(self, microtarea, estado, prosumer):
        if self.start_node is None:
            new_node = Node(microtarea, estado, prosumer)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(microtarea, estado, prosumer)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insertar_fin(self, microtarea, estado, prosumer):
        if self.start_node is None:
            new_node = Node(microtarea, estado, prosumer)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(microtarea, estado, prosumer)
        n.nref = new_node
        new_node.pref = n

    def borrar_por_elemento(self, microtarea):
        if self.start_node is None:
            print("La lista no tiene elementos")
            return
        if self.start_node.nref is None:
            if self.start_node.microtarea == microtarea:
                self.start_node = None
            else:
                print("Item not found")
            return

        if self.start_node.microtarea == microtarea:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("No encontro el elemento")

    def toString(self):
        if self.start_node is None:
            print("La lista esta vacia")
            return
        elif self.start_node.nref is None:
            print(self.start_node.toString())
            return
        else:
            n = self.start_node
            while n is not None:
                test = n.microtarea
                print(n.microtarea.toString(), n.prosumer)
                n = n.nref
            return

    def getNode(self):
        return self.start_node


class MicroTareaBlock:

    def __init__(self, previous_block_hash, microtarea, estado, prosumer):
        self.previous_block_hash = previous_block_hash
        self.microtarea = microtarea
        self.estado = estado
        self.prosumer = prosumer
        self.block_data = f"Microtarea: {microtarea.nombre} - Empresa: {microtarea.empresa} - Estado: {estado} - Prosumer: {prosumer} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(
            MicroTareaBlock("0", MicroTarea("Genesis Block", "Genesis Buisness", "", [], "", ""), 'Genesis',
                            'Genesis Prosumer'))

    def create_block(self, microtarea, estado, prosumer):
        previous_block_hash = self.last_block().block_hash
        self.chain.append(MicroTareaBlock(previous_block_hash, microtarea, estado, prosumer))

    def display_chain(self):
        str = ""
        for i in range(1, len(self.chain)):
            str += f"Data {i}: {self.chain[i].block_data}"
            str += f"Hash {i}: {self.chain[i].block_hash}\n"
        return str

    def last_block(self):
        return self.chain[-1]


mt1 = MicroTarea("Organizar una lista de pedidos por proveedor", "Veterinaria Coronado",
                 "Se necesita organizar los pedidos del mes por proveedor", ["Organiza los pedidos por proveedor",
                                                                             "Solo muestra los pedidos organizados de los proveedores activos"],
                 "Limpieza dental a mitad de precio", "url")
mt2 = MicroTarea("Gestor pedidos", "Zapateria la Estrella SA",
                 "Se precisa que se desarrolle un gestor de pedidos,debe agregar,modificar,eliminar y mostrar pedidos ordenados por un cliente en especifio",
                 ["Inserta pedido correctamente", "Modifica pedido de manera correcta",
                  "Eliminar pedidos de manera correcta",
                  "Muestra la informacion correcta de los pedidos ordenados por un cliente"], "Cupón 2x1", "url")

myblockchain = Blockchain()

myblockchain.create_block(mt1, "Finalizado", "David")
myblockchain.create_block(mt2, "Finalizado", "Max")

myblockchain.display_chain()
