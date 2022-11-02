
from flask import jsonify, request, Blueprint

from controladores.ControladorPartido import ControladorPartido

controladorPartido = ControladorPartido()

endpointPartido = Blueprint("endpointsPartido", __name__ )


"""ENDPOINTS Para el modelo Partido"""

@endpointPartido.route("/partido",methods=['GET'])
def index():
    json = controladorPartido.index()
    return jsonify(json)

@endpointPartido.route("/partido/<string:id>",methods=['GET'])
def show(id):
    json = controladorPartido.show(id)
    return jsonify(json)

@endpointPartido.route("/partido",methods=['POST'])
def create():
    data = request.get_json()
    json = controladorPartido.create(data)
    return jsonify(json)

@endpointPartido.route("/partido/<string:id>",methods=['PUT'])
def update(id):
    data = request.get_json()
    json = controladorPartido.update(id, data)
    return jsonify(json)

@endpointPartido.route("/partido/<string:id>",methods=['DELETE'])
def delete(id):
    json = controladorPartido.delete(id)
    return jsonify(json)

