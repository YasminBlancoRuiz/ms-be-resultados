
from flask import jsonify, request, Blueprint
from controladores.ControladorMesa import ControladorMesa

controladorMesa = ControladorMesa()


endpointMesa = Blueprint("endpointsMesa", __name__ )


"""ENDPOINTS Para el modelo mesa"""

@endpointMesa.route("/mesa",methods=['GET'])
def index():

    json = controladorMesa.index()

    return jsonify(json)

@endpointMesa.route("/mesa/<string:id>",methods=['GET'])
def show(id):

    json = controladorMesa.show(id)

    return jsonify(json)

@endpointMesa.route("/mesa",methods=['POST'])
def create():
    data = request.get_json()

    json = controladorMesa.create(data)

    return jsonify(json)

@endpointMesa.route("/mesa/<string:id>",methods=['PUT'])
def update(id):
    data = request.get_json()

    json = controladorMesa.update(id, data)

    return jsonify(json)

@endpointMesa.route("/mesa/<string:id>",methods=['DELETE'])
def delete(id):

    json = controladorMesa.delete(id)
    return jsonify(json)

