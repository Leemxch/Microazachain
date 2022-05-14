import hashlib

class MicroTarea:
    def __init__(self,nombre,empresa,descripcion,criterios,recompensa,archivos):
        self.nombre = nombre
        self.empresa = empresa
        self.descripcion = descripcion
        self.criterios = criterios
        self.recompensa = recompensa
        self.archivos = archivos
    def getNombre():
        return self.nombre
    def setNombre(nombre):
        self.nombre = nombre
    def getEmpresa():
        return self.empresa
    def getDescripcion():
        return self.descripcion
    def setDescripcion(descripcion):
        self.descripcion = descripcion
    def getCriterios():
        return self.criterios
    def setCriterios(criterios):
        self.criterios = criterios
    def getRecompensa():
        return self.recompensa
    def setRecompensa(recompensa):
        self.recompensa = recompensa
    def getArchivos():
        return self.archivos
    def setArchivos(archivos):
        self.archivos = archivos
    

class Node:
    def __init__(self,microtarea,estado,prosumer):
        self.microtarea = microtarea
        self.estado = estado
        self.prosumer = prosumer
        self.nref = None
        self.pref = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.start_node = None

    def insertar_lista_vacia(self, microtarea,estado,prosumer):
        if self.start_node is None:
            new_node = Node(microtarea,estado,prosumer)
            self.start_node = new_node
        else:
            print("list is not empty")
    def insertar_inicio(self, microtarea,estado,prosumer):
        if self.start_node is None:
            new_node = Node(microtarea,estado,prosumer)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(microtarea,estado,prosumer)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node
    def insertar_fin(self, microtarea,estado,prosumer):
        if self.start_node is None:
            new_node = Node(microtarea,estado,prosumer)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(microtarea,estado,prosumer)
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

class MicroTareaBlock:
    
    def __init__(self, previous_block_hash, microtarea,estado,prosumer):

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
        self.chain.append(MicroTareaBlock("0",MicroTarea("Genesis Block","Genesis Buisness","",[],"",""),'Genesis','Genesis Prosumer'))
    
    def create_block(self, microtarea, estado, prosumer):
        previous_block_hash = self.last_block().block_hash
        self.chain.append(MicroTareaBlock(previous_block_hash,microtarea,estado,prosumer))

    def display_chain(self):
        for i in range(1,len(self.chain)):
            print(f"Data {i}: {self.chain[i].block_data}")
            print(f"Hash {i}: {self.chain[i].block_hash}\n")
            print()

    def last_block(self):
        return self.chain[-1]

mt1 = MicroTarea("Organizar una lista de pedidos por proveedor","Veterinaria Coronado","Se necesita organizar los pedidos del mes por proveedor",["Organiza los pedidos por proveedor","Solo muestra los pedidos organizados de los proveedores activos"],"Limpieza dental a mitad de precio","url")
mt2 = MicroTarea("Gestor pedidos","Zapateria la Estrella SA","Se precisa que se desarrolle un gestor de pedidos,debe agregar,modificar,eliminar y mostrar pedidos ordenados por un cliente en especifio",["Inserta pedido correctamente","Modifica pedido de manera correcta","Eliminar pedidos de manera correcta","Muestra la informacion correcta de los pedidos ordenados por un cliente"],"Cupón 2x1","url")


myblockchain = Blockchain()


myblockchain.create_block(mt1,"Finalizado","David")
myblockchain.create_block(mt2,"Finalizado","Max")

myblockchain.display_chain()
