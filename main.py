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

def add(a,b):
    return(int(a)+int(b))

def sub(a,b):
    return(int(a)-int(b))

def mult(a,b):
    return(int(a)*int(b))

app = Flask(__name__)


@app.route('/<op>/<fno>/<lno>', methods=['GET'])

def testing(op,fno,lno):
    now = datetime.datetime.now()

  
    if op == 'add':
        nos = fno+" "+lno
        db.collection('arithmatic_operations').document("GET",now.strftime("%H:%M:%S")).set({'Addition':{nos:add(fno,lno)}})
        return({'operation':'Addition', 'Result':add(fno,lno)})
    elif op == 'sub':
        nos = fno+" "+lno
        db.collection('arithmatic_operations').document("GET",now.strftime("%H:%M:%S")).set({'Substraction':{nos:sub(fno,lno)}})
        return({'operation':'Substraction', 'Result':sub(fno,lno)})
    elif op == 'mult':
        nos = fno+" "+lno
        db.collection('arithmatic_operations').document("GET",now.strftime("%H:%M:%S")).set({'Multiplication':{nos:mult(fno,lno)}})
        return({'operation':'Multiplication', 'Result':mult(fno,lno)})
    return({'Ans':"BAD CALL"})


@app.route('/', methods=['POST'])

def post_handling():
    content = request.get_json()
    # "POST {}".format(
    no = content['fno']+","+content['lno']
    now = datetime.datetime.now()
    if(content['operation']=='add'):
        
        db.collection('arithmatic_operations').document(now.strftime("%H:%M:%S")).set({'Addition':{no:{int(content['fno'])+int(content['lno'])}}})
        return({"Result":int(content['fno'])+int(content['lno'])})
    if(content['operation']=='sub'):
        db.collection('arithmatic_operations').document(now.strftime("%H:%M:%S")).set({'Substraction':{no:{int(content['fno'])-int(content['lno'])}}})
        return({"Result":int(content['fno'])-int(content['lno'])})
    if(content['operation']=='mult'):
        db.collection('arithmatic_operations').document(now.strftime("%H:%M:%S")).set({'Multiplication':{no:{int(content['fno'])*int(content['lno'])}}})
        return({"Result":int(content['fno'])*int(content['lno'])})

@app.route('/get_docs', methods=['GET','POST'])
def return_docs():
    new_dict={}
    for i in docs:
        new_dict[i.id] = i.to_dict()
    return(new_dict)


if __name__ == "__main__":
    app.run(debug=True)