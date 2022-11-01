
from flask import jsonify, request, Blueprint
from controladores.ControladorResultado import ControladorResultado

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

@endpointResultado.route("/resultado",methods=['POST'])
def create():
    data = request.get_json()
    json = controladorResultado.create(data)
    return jsonify(json)

@endpointResultado.route("/resultado/<string:id>",methods=['PUT'])
def update(id):
    data = request.get_json()
    json = controladorResultado.update(id, data)
    return jsonify(json)

@endpointResultado.route("/resultado/<string:id>",methods=['DELETE'])
def delete(id):
    json = controladorResultado.delete(id)
    return jsonify(json)
    
    