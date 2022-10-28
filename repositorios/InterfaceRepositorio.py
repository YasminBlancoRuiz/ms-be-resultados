import pymongo
import certifi
from bson import DBRef
from bson.objectid import ObjectId
from typing import TypeVar, Generic, List, get_origin, get_args
import json


#Me permite tener parametros de clase
T = TypeVar('T')

class InterfaceRepositorio(Generic[T]):
    def __init__(self):
        ca = certifi.where()  #Obtengo el certificado de la entidad certificadora
        dataConfig = self.loadFileConfig() #Información del archivo de configuración
        client = pymongo.MongoClient(dataConfig["data-db-connection"], lsCAFile=ca) #Creo el objeto Mongo y conexión a la BD con el certificado
        self.baseDatos = client[dataConfig["name-db"]]  #Atributo de la base de datos y la extrae
        theClass = get_args(self.__orig_bases__[0]) #Extracción de la T  // Extrae el modelo tipo de objeto
        self.coleccion = theClass[0].__name__.lower() #Extracción de la T



#Abre archivo de configuración y lo lee
#Necesita adicionar lo que hay en el secrets
def loadFileConfig(self):
    with open('config.json') as f:
        data = json.load(f)
    with open('secrets.json') as f:
        data.update(f)
    return data


def save(self, item: T):
    laColeccion = self.baseDatos[self.coleccion] #Colección que se obtuvo al conectarse a la BD
    elId = ""  #variable vacia, luego se llena con un id
    item = self.transformRefs(item)
    if hasattr(item, "_id") and item._id != "":  #Se cumple cuando el item existe y tiene información
        elId = item._id
        _id = ObjectId(elId)
        laColeccion = self.baseDatos[self.coleccion]
        delattr(item, "_id")
        item = item.__dict__  #convierte el item en diccionario
        updateItem = {"$set": item}  #lo actualiza
        x = laColeccion.update_one({"_id": _id}, updateItem)  #actualiza un solo elemento
    else:
        _id = laColeccion.insert_one(item.__dict__) #sino existe, lo inserta
        elId = _id.inserted_id.__str__()
    x = laColeccion.find_one({"_id": ObjectId(elId)})  #lo verifica que si haya quedado almacenado
    x["_id"] = x["_id"].__str__()  #lo convierte en string la parte delo id
    return self.findById(elId)  # lo devuelve