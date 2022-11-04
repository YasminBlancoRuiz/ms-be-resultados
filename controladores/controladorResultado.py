from modelos.Resultado import Resultado
from modelos.Mesa import Mesa
from modelos.Candidato import Candidato
from repositorios.ResultadoRepositorio import ResultadoRepositorio
from repositorios.MesaRepositorio import MesaRepositorio
from repositorios.CandidatoRepositorio import CandidatoRepositorio

class ControladorResultado():
    def __init__(self):
        print(" >Creando Controlador resultado")
        self.resultadoRepositorio = ResultadoRepositorio()
        self.mesaRepositorio = MesaRepositorio()
        self.candidatoRepositorio = CandidatoRepositorio()
    def index(self):
        print("> Listar todos los resultados")
        return self.resultadoRepositorio.findAll()
    """
     Asignacion mesa y candidato a resultado
    """
    def create(self,data,id_mesa,id_candidato):
         print(" >Crear un resultado")
         nuevoResultado= Resultado(data)
         laMesa=Mesa(self.mesaRepositorio.findById(id_mesa))
         elCandidato=Candidato(self.candidatoRepositorio.findById(id_candidato))
         nuevoResultado.mesa=laMesa
         nuevoResultado.candidato=elCandidato
         return self.resultadoRepositorio.save(nuevoResultado)
    def show(self,id):
        print(" >Mostrando un resultado con id ",id)
        elResultado=Resultado(self.resultadoRepositorio.findById(id))
        return elResultado.__dict__
    """
    Modificación de resultado (mesa y candidato)
    """
    
    def update(self,id,data,id_mesa,id_candidato):
        print(" >Actualizando resultado con id ",id)
        elResultado=Resultado(self.resultadoRepositorio.findById(id))
        elResultado.cant_votos =data["cant_votos"]
        laMesa = Mesa(self.mesaRepositorio.findById(id_mesa))
        elCandidato=Candidato(self.candidatoRepositorio.findById(id_candidato))
        elResultado.mesa= laMesa
        elResultado.candidato =elCandidato
        return self.resultadoRepositorio.save(elResultado)
    
    def delete(self, id):
        print(" >Eliminando resultado con id ",id)
        return self.resultadoRepositorio.delete(id)
        