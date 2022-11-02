
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import json
import endpoints


app = Flask(__name__)

#Permite a un servidor hacer peticiones de diferentes varios dominios distintos
cors = CORS(app)


#se importan las rutas de estudiante en el main
app.register_blueprint(endpoints.endpointCandidato)
app.register_blueprint(endpoints.endpointPartido)
app.register_blueprint(endpoints.endpointMesa)
app.register_blueprint(endpoints.endpointResultado)



def __loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running .Pruebas.."
    return jsonify(json)


def __loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__=='__main__':
    dataConfig = __loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    
    #Para hacer una prueba de conexión

    if dataConfig["test"] == "true":
        print("Testing DB conecction...")
        from repositorios.InterfaceRepositorio import InterfaceRepositorio
        repo = InterfaceRepositorio()
    else:
        serve(app,host=dataConfig["url-backend"],port=dataConfig["port"]) #production -grade WSGI server

