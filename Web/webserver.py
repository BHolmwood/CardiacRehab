from flask import Flask, request
from flask.ext.restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

patient_contacts = {}
doc_contacts = {}
phone_contacts = {}
pwd_infos = {}

def flask_post_json():
    if (request.json != None):
        return request.json
    elif (request.data != None and request.data != ''):
        return json.loads(request.data)
    else:
        return json.loads(request.form.keys()[0])

class doctorContacts(Resource):
	def get(self, clinician_id):
		if(len(doc_contacts) != 0):
			if(clinician_id in doc_contacts):
				return doc_contacts[clinician_id]
			else:
				return "no data"
		else:
			return "no data"
	
	def post(self, clinician_id):
		data = flask_post_json()
		doc_contact = {"address": data['address'], "name": data["name"], "id": data["id"],
		"session": data["session"], "assigned_index": data["assigned_index"]}
		doc_contacts[clinician_id] = doc_contact
		return doc_contact, 201
		
	def delete(self, clinician_id):
		if(clinician_id in doc_contacts):
			doc_contacts[clinician_id] = "no data"
			return "no data", 204
		else:
			return "no data"
		
class patientContacts(Resource):
	def get(self, clinician_id, patient_id):
		if(len(patient_contacts) != 0):
			if(clinician_id in patient_contacts):
				if(patient_id in patient_contacts[clinician_id]):
					return patient_contacts[clinician_id][patient_id]
				else:
					return "no data"
			else:
				return "no data"
		else:
			return "no data"
	
	def post(self, clinician_id, patient_id):
		data = flask_post_json()
		patient_contact = {"address": data['address'], "name": data["name"], "id": data["id"],
		"session": data["session"], "assigned_index": data["assigned_index"]}
		temp = {patient_id: patient_contact}
		patient_contacts[clinician_id] = temp
		
		return patient_contact, 201
		
	def delete(self, clinician_id, patient_id):
		if(clinician_id in patient_contacts):
			if(patient_id in patient_contacts[clinician_id]):
				patient_contacts[clinician_id][patient_id] = "no data"
				return "no data", 204
			else:
				return "no data"
		else:
			return "no data"
		
class phoneContacts(Resource):
	def get(self, macaddr):
		if(len(phone_contacts) != 0):
			if(macaddr in phone_contacts):
				print phone_contacts
				return phone_contacts[macaddr]
			else:
				return "no data"
		else:
			return "no data"
			
	def post(self, macaddr):
		data = flask_post_json()
		phone_contact = {"ssid": data['ssid'], "address": data['address']}
		phone_contacts[macaddr] = phone_contact
		return phone_contact, 201
		
	def delete(self, macaddr):
		if(macaddr in phone_contacts):
			phone_contacts[macaddr] = "no data"
			return "no data", 204
		else:
			return "no data"
		
class securityContacts(Resource):
	def get(self, rnd, macaddr):
		if(len(pwd_infos) != 0):
			if(rnd in pwd_infos):
				if(macaddr in pwd_infos[rnd]):
					return pwd_infos[rnd][macaddr]
				else:
					return "no data"
			else:
				return "no data"
		else:
			return "no data"
			
	def post(self, rnd, macaddr):
		data = flask_post_json()
		pwd_info = {"password": data['password']}
		temp = {macaddr: pwd_info}
		pwd_infos[rnd] = temp
		return pwd_info, 201
		
	def delete(self, rnd, macaddr):
		if(rnd in pwd_infos):
			if(macaddr in pwd_infos[rnd]):
				pwd_infos[rnd][macaddr] = "no data"
				return "no data", 204
			else:
				return "no data"
		else:
			return "no data"

api.add_resource(doctorContacts, '/doctors/<int:clinician_id>/')
api.add_resource(patientContacts, '/doctors/<int:clinician_id>/patients/<int:patient_id>/')
api.add_resource(phoneContacts, '/patientcmp/<string:macaddr>/')
api.add_resource(securityContacts, '/<string:rnd>/<string:macaddr>/')

if __name__ == '__main__':
	app.debug = True
	app.run(host='172.28.211.167', port=5050)
