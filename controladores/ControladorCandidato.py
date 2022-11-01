from repositorios.CandidatoRepositorio import CandidatoRepositorio
from modelos.Candidato import Candidato


class ControladorCandidato():

    """Clase que implementa el controlador para los endpoints relacionados con el Candidato"""

    def __init__(self):
        print(" >Creando Controlador candidato")
        self.repositorio = CandidatoRepositorio()

    def index(self):
        print("> Listar todos los candidatos")
        x = self.repositorio.findAll()
        return x

  
    def create(self,data):
        print(" >Crear un candidato")
        elCandidato = self.repositorio.save(Candidato(data))
        return elCandidato

 
    def show(self,id):
        print(" >Mostrando un candidato con id ",id)
        elCandidato = self.repositorio.findById(id)
        return elCandidato

    def update(self,id, data):
        print(" >Actualizando candidato con id ",id)
        candidatoActual = Candidato(self.repositorio.findById(id))
        candidatoActual.Num_resolucion   = data["Num_resolucion"]
        candidatoActual.Cedula   = data["Cedula"]
        candidatoActual.Nombre   = data["Nombre"]
        candidatoActual.Apellido = data["Apellido"]
        return self.repositorio.save(candidatoActual)

    def delete(self,id):
        print(" >Eliminando candidato con id ",id)
        return self.repositorio.delete(id)

