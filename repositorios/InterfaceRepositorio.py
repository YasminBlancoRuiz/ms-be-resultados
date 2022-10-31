import pymongo
import certifi
from bson import DBRef
from bson.objectid import ObjectId
from typing import TypeVar, Generic, List, get_origin, get_args
import json


# Me permite tener parametros de clase
T = TypeVar('T')


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    with open('secrets.json') as f:
        data.update(json.load(f))
    return data


class InterfaceRepositorio(Generic[T]):
    def __init__(self):
        ca = certifi.where()  # Obtengo el certificado de la entidad certificadora
        dataConfig = loadFileConfig()  # Información del archivo de configuración
        client = pymongo.MongoClient(dataConfig["mongo-db-conecction-string"],
                                     tlsCAFile=ca)  # Creo el objeto Mongo y conexión a la BD con el certificado
        self.baseDatos = client[dataConfig["name-db"]]  # Atributo de la base de datos y la extrae
        theClass = get_args(self.__orig_bases__[0])  # Extracción de la T  // Extrae el modelo tipo de objeto
        self.coleccion = theClass[0].__name__.lower()  # Extracción de la T

    # Abre archivo de configuración y lo lee
    # Necesita adicionar lo que hay en el secrets

    def loadFileConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        with open('secrets.json') as f:
            data.update(json.load(f))
        return data

    def save(self, item: T):
        laColeccion = self.baseDatos[self.coleccion]  # Colección que se obtuvo al conectarse a la BD
        elId = ""  # variable vacia, luego se llena con un id
        item = self.__transformRefs(item)
        if hasattr(item, "_id") and item._id != "":  # Se cumple cuando el item existe y tiene información
            elId = item._id
            _id = ObjectId(elId)
            laColeccion = self.baseDatos[self.coleccion]
            delattr(item, "_id")
            item = item.__dict__  # convierte el item en diccionario
            updateItem = {"$set": item}  # lo actualiza
            x = laColeccion.update_one({"_id": _id}, updateItem)  # actualiza un solo elemento
        else:
            _id = laColeccion.insert_one(item.__dict__)  # sino existe, lo inserta
            elId = _id.inserted_id.__str__()
        x = laColeccion.find_one({"_id": ObjectId(elId)})  # lo verifica que si haya quedado almacenado
        x["_id"] = x["_id"].__str__()  # lo convierte en string la parte delo id
        return self.findById(elId)  # lo devuelve

    def delete(self, id):
        laColeccion = self.baseDatos[self.coleccion]
        cuenta = laColeccion.delete_one({"_id": ObjectId(id)}).deleted_count
        return {"deleted_count": cuenta}

    def update(self, id, item: T):
        _id = ObjectId(id)
        laColeccion = self.baseDatos[self.coleccion]
        delattr(item, "_id")
        item = item.__dict__
        updateItem = {"$set": item}
        x = laColeccion.update_one({"_id": _id}, updateItem)
        return {"updated_count": x.matched_count}

    def findById(self, id):
        laColeccion = self.baseDatos[self.coleccion]
        x = laColeccion.find_one({"_id": ObjectId(id)})
        x = self.__getValuesDBRef(x)
        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()

        return x

    def findAll(self):
        laColeccion = self.baseDatos[self.coleccion]
        data = []
        for x in laColeccion.find():
            x["_id"] = x["_id"].__str__()
            x = self.__transformObjectIds(x)
            x = self.__getValuesDBRef(x)
            data.append(x)
        return data

    def __query(self, theQuery):
        laColeccion = self.baseDatos[self.coleccion]
        data = []
        for x in laColeccion.find(theQuery):
            x["_id"] = x["_id"].__str__()
            x = self.__transformObjectIds(x)
            x = self.__getValuesDBRef(x)
            data.append(x)
        return data

    def __queryAggregation(self, theQuery):
        laColeccion = self.baseDatos[self.coleccion]
        data = []
        for x in laColeccion.aggregate(theQuery):
            x["_id"] = x["_id"].__str__()
            x = self.__transformObjectIds(x)
            x = self.__getValuesDBRef(x)
            data.append(x)
        return data

    def __getValuesDBRef(self, x):
        keys = x.keys()
        for k in keys:
            if isinstance(x[k], DBRef):

                laColeccion = self.baseDatos[x[k].collection]
                valor = laColeccion.find_one({"_id": ObjectId(x[k].id)})
                valor["_id"] = valor["_id"].__str__()
                x[k] = valor
                x[k] = self.__getValuesDBRef(x[k])
            elif isinstance(x[k], list) and len(x[k]) > 0:
                x[k] = self.__getValuesDBRefFromList(x[k])
            elif isinstance(x[k], dict):
                x[k] = self.__getValuesDBRef(x[k])
        return x

    def __getValuesDBRefFromList(self, theList):
        newList = []
        laColeccion = self.baseDatos[theList[0]._id.collection]
        for item in theList:
            value = laColeccion.find_one({"_id": ObjectId(item.id)})
            value["_id"] = value["_id"].__str__()
            newList.append(value)
        return newList

    def __transformObjectIds(self, x):
        for attribute in x.keys():
            if isinstance(x[attribute], ObjectId):
                x[attribute] = x[attribute].__str__()
            elif isinstance(x[attribute], list):
                x[attribute] = self.__formatList(x[attribute])
            elif isinstance(x[attribute], dict):
                x[attribute] = self.__transformObjectIds(x[attribute])
        return x

    def __formatList(self, x):
        newList = []
        for item in x:
            if isinstance(item, ObjectId):
                newList.append(item.__str__())
        if len(newList) == 0:
            newList = x
        return newList

    def __transformRefs(self, item):
        theDict = item.__dict__
        keys = list(theDict.keys())
        for k in keys:
            if theDict[k].__str__().count("object") == 1:
                newObject = self.__ObjectToDBRef(getattr(item, k))
                setattr(item, k, newObject)
        return item

    def __ObjectToDBRef(self, item: T):
        nameCollection = item.__class__.__name__.lower()
        return DBRef(nameCollection, ObjectId(item._id))
