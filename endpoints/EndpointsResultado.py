
from flask import jsonify, request, Blueprint
from controladores.controladorResultado import ControladorResultado


controladorResultado = ControladorResultado()

endpointResultado = Blueprint("endpointsResultado", __name__ )


"""ENDPOINTS Para el modelo Resultado"""

@endpointResultado.route("/resultado",methods=['GET'])
def index():
    json = controladorResultado.index()
    return jsonify(json)


@endpointResultado.route("/resultado/<string:id>",methods=['GET'])
def show(id):
    json = controladorResultado.show(id)
    return jsonify(json)

@endpointResultado.route("/resultado/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST'])
def create(id_mesa,id_candidato):
    data = request.get_json()
    json = controladorResultado.create(data,id_mesa,id_candidato)
    return jsonify(json)

@endpointResultado.route("/resultado/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['PUT'])
def update(id_resultado,id_mesa,id_candidato):
    data = request.get_json()
    json = controladorResultado.update(id_resultado, data,id_mesa,id_candidato)
    return jsonify(json)

@endpointResultado.route("/resultado/<string:id>",methods=['DELETE'])
def delete(id):
    json = controladorResultado.delete(id)
    return jsonify(json)
    
    