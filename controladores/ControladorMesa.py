
from repositorios.MesaRepositorio import MesaRepositorio
from modelos.Mesa import Mesa


class ControladorMesa():
    """Clase que implementa el controlador para los endpoints relacionados con la Mesa"""

    def __init__(self):
        print(" >Creando controlador mesa")
        self.repositorios = MesaRepositorio()

    def index(self):
        print(" >Listar todas las mesas")
        x = self.repositorios.findAll()
        return x

    def create(self, data):
        print(" >Crear una mesa")
        laMesa = self.repositorios.save(Mesa(data))
        return laMesa

    def show(self, id):
        print(" >Mostrando la mesa con id ", id)
        laMesa = self.repositorios.findById(id)
        return laMesa

    def update(self, id, data):
        print(" >Actualizando candidato con id ", id)
        mesaActual = Mesa(self.repositorios.findById(id))
        mesaActual.Numero_mesa = data["Numero_mesa"]
        mesaActual.Cedulas_inscritas = data["Cedulas_inscritas"]
        return self.repositorios.save(mesaActual)

    def delete(self, id):
        print(" >Eliminando mesa con id ", id)
        return self.repositorios.delete(id)
        

