import os
from pymongo import MongoClient
from django.http import JsonResponse
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

def get_products(request):
    uri = os.getenv("MONGO_URI")
    print("Mongo URI:", uri)
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.server_info()
    print("MongoDB connection successful!")

    print("Databases:", client.list_database_names())

    db = client.get_database("testdb")

    collection = db.get_collection("products")
    docs = list(collection.find({}))

    for item in docs:
        item["_id"] = str(item["_id"])
    return JsonResponse(docs, safe=False)

