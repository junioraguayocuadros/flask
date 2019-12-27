import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'flask-prueba-263314'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {
    'projectId': project_id
})

db = firestore.client()


def get_users():
    return db.collection('users').get()


