import random, flask
from flask import Flask, request
import requests
import datetime

import firebase_admin
from firebase_admin import credentials, db, firestore

cred = credentials.Certificate("app_key.json")
firebase_admin.initialize_app(cred, {'projectId':'dailttaskarithmatic'})

db = firestore.client()
docs = db.collection('arithmatic_operations').stream()
new_dict={}
for i in docs:
    new_dict[i.id] = i.to_dict()

print(new_dict)
    