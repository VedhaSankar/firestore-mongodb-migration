from time import sleep
from google.cloud import firestore
from dotenv import load_dotenv
import os

from sqlalchemy import all_

load_dotenv()

FILE_PATH = os.environ.get('FILE_PATH')

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

    pass

def main():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FILE_PATH
    get_collection()

if __name__=='__main__':
    main()
