import collections
import pymongo
from pymongo import results

cluster = pymongo.MongoClient("mongodb+srv://{}@cluster0.3vcng.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Portfolio"]
collection = db["projects"]

def getData():
    return collection.find()