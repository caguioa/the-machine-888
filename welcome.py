# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import http.client # only works on python3
from flask import Flask, jsonify, render_template
import json


CLIENT_ID = "d956fccb-1867-4a3f-8b45-69da913e1da0"
SECRET_ID ="uN4dY0jM4uM8uU2qR0jD8wP3hA5gX4nY3iJ4tW0gN1mP2kS1vR"


app = Flask(__name__)

@app.route('/')
def Welcome():
    conn = http.client.HTTPSConnection("api.us.apiconnect.ibmcloud.com")


    headers = {
          'x-ibm-client-id': CLIENT_ID,
          'x-ibm-client-secret': SECRET_ID,
          'content-type': "application/json",
          'accept': "application/json"
          }

    conn.request("GET", "/ubpapi-dev/sb/api/RESTs/getAccount?account_no=101438806941", headers=headers)

    res = conn.getresponse()
    data = res.read()

    ret = json.loads(data.decode("utf-8"))

    return render_template("index.html", name=ret[0]['account_name'], balance=ret[0]['current_balance'] )
    # return app.send_static_file('index.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
