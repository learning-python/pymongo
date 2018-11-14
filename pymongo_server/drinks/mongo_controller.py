import pymongo

client = pymongo.MongoClient('localhost', 27017)
drinks_db = client.drinks

def find(collection_name):
    collection = drinks_db[collection_name]
    return collection.find()

def insert_one(collection_name, doc):
    collection = drinks_db[collection_name]
    res = collection.insert_one(doc)
    return res