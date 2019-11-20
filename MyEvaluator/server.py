from flask import Flask, request, render_template, send_from_directory,jsonify
import os
from scripts import identify_user
from models import*

#app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/",methods=['POST','GET'])
def main() :

	return "Server is Active"

@app.route("/validate_mail",methods=['POST','GET'])
def validate_mail() :
	data = request.get_json()
	email = data['email']
	if email.endswith('medtech.tn'):
		response = "Email valid"
		type = identify_user(email)
		add_person
		return jsonify({"response ": response,"type":type})

	else :
		response = "Invalid Email"
		return jsonify({"response ": response})

			
@app.route("/add_user",methods=['POST','GET'])
def add_user() :
	data = request.get_json()
	name = data['name']
	email = data['email']
	me = Professor(name =name,mail = email)
	me.add_person()
	
	return "Server is Active"

	

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port=80,threaded = True)	
