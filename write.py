
import firebase_admin
from firebase_admin import credentials, db, firestore
import random

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {'projectId':'project2-79402'})

db = firestore.client()

fnames = db.collection('names').document('fname').get().to_dict()
lnames = db.collection('names').document('lname').get().to_dict()

fnames['first_names'].append("Yash")
lnames['last_name'].append('Vishwakarma')


fnames = db.collection('names').document('fname').set({'first_names':fnames['first_names']})

# fno = fnames['first_names'][random.randint(0,len(fnames['first_names'])-1)]
# lno = lnames['last_name'][random.randint(0,len(lnames['last_name'])-1)]
# print(fno,lno)



