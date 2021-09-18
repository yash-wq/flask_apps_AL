import firebase_admin
from firebase_admin import credentials, db, firestore
import random
from flask import Flask, request
from flask_restful import Api, Resource
import requests

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {'projectId':'project2-79402'})

db = firestore.client()

def generate_name():

    fnames = db.collection('names').document('fname').get().to_dict()
    lnames = db.collection('names').document('lname').get().to_dict()

    random_name = fnames['first_names'][random.randint(0,len(fnames['first_names'])-1)] +" "+ lnames['last_name'][random.randint(0,len(lnames['last_name'])-1)]
    nn = random_name
    return(nn)

def generate_lastname(fname):
    lnames = db.collection('names').document('lname').get().to_dict()
    name = fname+" "+lnames['last_name'][random.randint(0,len(lnames['last_name'])-1)]
    return(name)



app = Flask(__name__)
api = Api(app)

class welcome(Resource):
    
    def get(self):
        
        return{"Message":generate_name()}

class urlp(Resource):
    def get(self, stst):
        
        return {"name":generate_lastname(stst)}


api.add_resource(urlp, "/urlp/<string:stst>")

@app.route('/body/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json()
    fname = content['mytext']
    
    return {"name":generate_lastname(fname)}

@app.route('/books', methods=['GET'])
def home():
    
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

api.add_resource(welcome,'/generate')

if __name__ == "__main__":
    app.run(debug=True)







