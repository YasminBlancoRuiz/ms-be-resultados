from flask import jsonify, request, Blueprint
from controladores.ControladorCandidato import ControladorCandidato

controladorCandidato = ControladorCandidato()

endpointCandidato = Blueprint("endpointsCandidato", __name__ )


"""ENDPOINTS Para el modelo Candidato"""

@endpointCandidato.route("/candidato",methods=['GET'])
def index():
    json = controladorCandidato.index()
    return jsonify(json)

@endpointCandidato.route("/candidato/<string:id>",methods=['GET'])
def show(id):
    json = controladorCandidato.show(id)
    return jsonify(json)

@endpointCandidato.route("/candidato",methods=['POST'])
def create():
    data = request.get_json()
    json = controladorCandidato.create(data)
    return jsonify(json)

@endpointCandidato.route("/candidato/<string:id>",methods=['PUT'])
def update(id):
    data = request.get_json()
    json = controladorCandidato.update(id, data)
    return jsonify(json)

@endpointCandidato.route("/candidato/<string:id>",methods=['DELETE'])
def delete(id):
    json = controladorCandidato.delete(id)
    return jsonify(json)