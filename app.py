from google.cloud import firestore
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

FILE_PATH = os.environ.get('FILE_PATH')
MONGO_URI = os.environ.get('MONGO_URI')
DATABASE = 'firestore-data'
COLLECTION = 'firestore-data'


client = MongoClient(MONGO_URI) 
DB_NAME = 'firestore-data'
database = client[DB_NAME]

def get_collection():
    db = firestore.Client()
    list_of_collection_names = []
    for collection_name in db.collections():

        list_of_collection_names.append(collection_name.id)

    json_doc = {}

    for collection in list_of_collection_names:

        all_docs = []
        current_doc = {}

        users_ref = db.collection(collection)

        docs = users_ref.stream()

        for doc in docs:

            current_doc[doc.id] = doc.to_dict()

        all_docs.append(current_doc)

        json_doc[collection] = all_docs

    return json_doc

def transfer_to_mongo():

    result = get_collection()
    collection_name = 'data'
    new_collection = database[collection_name]
    data = {}

    for one in result:
        data[one] = result[one] 
        # print (data)
    x = new_collection.insert_one(data)
    print(x)


def main():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FILE_PATH
    # get_collection()
    transfer_to_mongo()

if __name__=='__main__':
    main()
