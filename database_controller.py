import collections
import pymongo
from pymongo import results

cluster = pymongo.MongoClient("mongodb+srv://abhijeet:1584@cluster0.3vcng.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Portfolio"]
collection = db["projects"]

post = {"_id": 0, "name": "Abhijeet", "Score": 5}

# collection.insert_one(post)
results = collection.find({"name":"Abhijeet"})

for r in results:
    print(r["name"])