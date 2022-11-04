from repositorios.CandidatoRepositorio import CandidatoRepositorio
from repositorios.PartidoRepositorio import PartidoRepositorio
from modelos.Candidato import Candidato
from modelos.Partido import Partido


class ControladorCandidato():

    """Clase que implementa el controlador para los endpoints relacionados con el Candidato"""

    def __init__(self):
        print(" >Creando Controlador candidato")
        self.repositoriocandidato = CandidatoRepositorio()
        self.repositoriopartido= PartidoRepositorio()

    def index(self):
        print("> Listar todos los candidatos")
        x = self.repositoriocandidato.findAll()
        return x

  
    def create(self,data):
        print(" >Crear un candidato")
        elCandidato = self.repositoriocandidato.save(Candidato(data))
        return elCandidato

 
    def show(self,id):
        print(" >Mostrando un candidato con id ",id)
        elCandidato = self.repositoriocandidato.findById(id)
        return elCandidato

    def update(self,id, data):
        print(" >Actualizando candidato con id ",id)
        candidatoActual = Candidato(self.repositoriocandidato.findById(id))
        candidatoActual.Num_resolucion   = data["Num_resolucion"]
        candidatoActual.Cedula   = data["Cedula"]
        candidatoActual.Nombre   = data["Nombre"]
        candidatoActual.Apellido = data["Apellido"]
        return self.repositoriocandidato.save(candidatoActual)

    def delete(self,id):
        print(" >Eliminando candidato con id ",id)

        return self.repositoriocandidato.delete(id)

    """
    Relación departamento y materia
    """
    def asignarPartido(self, id, id_Partido):
        print(" >Asignando Partido a candidato",id)
        candidatoActual = Candidato(self.repositoriocandidato.findById(id))
        partidoActual = Partido(self.repositoriopartido.findById(id_Partido))
        candidatoActual.partido = partidoActual
        return self.repositoriocandidato.save(candidatoActual)
