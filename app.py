from time import sleep
from google.cloud import firestore
from dotenv import load_dotenv
import os

load_dotenv()

FILE_PATH = os.environ.get('FILE_PATH')

def quickstart_get_collection():
    db = firestore.Client()
    list_of_collection_names = []
    for collection_name in db.collections():

        list_of_collection_names.append(collection_name.id)

    for collection in list_of_collection_names:

        users_ref = db.collection(collection)

        docs = users_ref.stream()

        for doc in docs:
            print(doc.to_dict())


def main():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FILE_PATH
    quickstart_get_collection()

if __name__=='__main__':
    main()
