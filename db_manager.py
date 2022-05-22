from pymongo import MongoClient
from pymongo.collection import Collection

def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class DBManager :
    name = 'gestionale2022_2'
    host =  'localhost'#'192.168.178.74'  #'172.20.10.2'
    port = 27017
    client = MongoClient(host=host , port=port , connect=True)
    db = client[name] #oppure client.gestionale2022_2 => non uso questa notazione poichè presente un underscore

    def insert (self , collection , mymap):
        collection.insert_one(mymap)

    def update(self, collection, searchKeysValuesPairs, changedKeysValuesPairs):
        collection.update_one(searchKeysValuesPairs, {'$set' : changedKeysValuesPairs})

    def readAll(self, collection):
        return collection.find()

    def read(self, collection, searchKeysValuesPairs):
        return collection.find(searchKeysValuesPairs)

    def readOne(self, collection, idToken):
        return collection.find_one({'idToken':idToken})

    def delete(self, collection, idToken):
        collection.delete_one({'idToken': idToken})

