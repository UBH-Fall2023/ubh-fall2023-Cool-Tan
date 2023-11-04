import firebase_admin
import foodClass
from firebase_admin import firestore

# Application Default credentials are automatically created.
app = firebase_admin.initialize_app()
db = firestore.client()


def addToDB (food):
    db.collection("foods").document(food.getName(food)).set(food.to_dict())
