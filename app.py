from time import sleep
from tkinter import PROJECTING
from google.cloud import firestore
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from dotenv import load_dotenv
import os

load_dotenv()

FILE_PATH = os.environ.get('FILE_PATH')

def quickstart_get_collection():
    db = firestore.Client()
    users_ref = db.collection("ariana")
    docs = users_ref.stream()

    for doc in docs:
        print(doc.to_dict())

def main():

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FILE_PATH
    quickstart_get_collection()

if __name__=='__main__':
    main()