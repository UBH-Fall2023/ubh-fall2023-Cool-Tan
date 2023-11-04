import firebase_admin
import foodClass
from firebase_admin import firestore
from firebase_admin import credentials

# Application Default credentials are automatically created.
fireBaseApp = firebase_admin.initialize_app()
db = firestore.client()


def addToDB (food):
    db.collection("foods").document(food.getName(food)).set(food.to_dict())
