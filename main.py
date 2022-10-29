
from flask import Flask
from flask_cors import CORS
from waitress import serve
import json
from flask import jsonify



app = Flask(__name__)

#Permite a un servidor hacer peticiones de diferentes varios dominios distintos
cors = CORS(app)


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)



def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])