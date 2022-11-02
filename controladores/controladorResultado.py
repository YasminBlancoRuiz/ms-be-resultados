

from repositorios.ResultadoRepositorio import ResultadoRepositorio

from modelos.Resultado import Resultado


class ControladorResultado():

    """Clase que implementa el controlador para los endpoints relacionados con el Resultado"""

    def __init__(self):
        print(" >Creando Controlador resultado")
        self.repositorio = ResultadoRepositorio()

    def index(self):
        print("> Listar todos los resultados")
        x = self.repositorio.findAll()
        return x

  
    def create(self,data):
        print(" >Crear un resultado")
        elResultado = self.repositorio.save(Resultado(data))
        return elResultado

 
    def show(self,id):
        print(" >Mostrando un resultado con id ",id)
        elResultado = self.repositorio.findById(id)
        return elResultado

    def update(self,id, data):
        print(" >Actualizando partido con id ",id)
        resultadoActual = Resultado(self.repositorio.findById(id))
        resultadoActual.Cantidad_votos   = data["Cantidad_votos"]
        return self.repositorio.save(resultadoActual )

    def delete(self,id):
        print(" >Eliminando resultado con id ",id)
        return self.repositorio.delete(id)
        