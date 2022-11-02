
from repositorios.PartidoRepositorio import PartidoRepositorio
from modelos.Partido import Partido


class ControladorPartido():

    """Clase que implementa el controlador para los endpoints relacionados con el Partido"""

    def __init__(self):
        print(" >Creando Controlador partido")
        self.repositorio = PartidoRepositorio()

    def index(self):
        print("> Listar todos los partidos")
        x = self.repositorio.findAll()
        return x

  
    def create(self,data):
        print(" >Crear un partido")
        elPartido = self.repositorio.save(Partido(data))
        return elPartido

 
    def show(self,id):
        print(" >Mostrando un partido con id ",id)
        elPartido = self.repositorio.findById(id)
        return elPartido

    def update(self,id, data):
        print(" >Actualizando partido con id ",id)
        PartidoActual = Partido(self.repositorio.findById(id))
        PartidoActual.Nombre   = data["Nombre"]
        PartidoActual.Lema = data["Lema"]
        return self.repositorio.save(PartidoActual)

    def delete(self,id):
        print(" >Eliminando partido con id ",id)
        return self.repositorio.delete(id)
        
        

