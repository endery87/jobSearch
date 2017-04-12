from flask import Flask, render_template,request, jsonify
import json
import re
import mysql.connector

app = Flask(__name__)


#handling get requests
@app.route("/", methods=['GET'])
def get():
    cnx = mysql.connector.connect(user='enro', password='sql123',
                              host='localhost',
                              database='vacancies')
    cursor=cnx.cursor()
    query = ("SELECT * FROM jobs")
    cursor.execute(query)
    data={}
    data['jobs']=[]
    counter=0;
    
    for a in cursor:
        data['jobs'].append({  
        'name': a[0],
        'company': a[2],
        'location': a[1],
        'id':a[3],
        'applied':a[4]
    })
        
    return json.dumps(data) #return json

#handling put requests
@app.route("/<id>",methods=['PUT'])
def put(id):
    cnx = mysql.connector.connect(user='enro', password='sql123',
                              host='localhost',
                              database='vacancies')
    cursor=cnx.cursor()
    cursor.execute("UPDATE jobs SET APPLIED=%s WHERE ID=%s",(1,id))
    cnx.commit()
    return id   #return id of the applied job

if(__name__=="__main__"):#run configurations, from localhost:5050,    
    app.run(host="127.0.0.1",port=5050,debug=True)
    print("apprunning")

print("apprunning")
