
from flask import Blueprint, jsonify,abort,make_response,request,json 
from api.models.models import User, Incident
from api.models.validators import Validator
from api.models.incidents import IncidentList
from datetime import datetime

appblueprint = Blueprint('api', __name__)\
incident = IncidentList()
is_valid = Validator()


@appblueprint.route('/')
def index():
	return 'Welcome to ireporter'

@appblueprint.route('/users', methods = ['POST'])
def register_users():

	if not request.json or not request.get_json()['firstname'] \
	or not request.get_json()['lastname'] or not request.get_json()['othername'] \
	or not request.get_json()['email'] or not request.get_json()['phone_number'] \
	or not request.get_json()['username']:

		return jsonify({"message":"Hello There"})


	firstname,lastname,othername,email,phone_number,username = \
	request.get_json()['firstname'], request.get_json()['lastname'], \
	request.get_json()['othername'], request.get_json()['email'], \
	request.get_json()['phone_number'], request.get_json()['username']

	user_id = Incident.user_id_generator()

	is_admin = False

	registerd = date_today = datetime.now().strftime('%d%m%y %H%M')
	new_user = User(user_id, firstname, lastname, othername, email, phone_number, username, registerd, is_admin)

	return jsonify({"Status Code": 201, "User": incident.user_list[-1]}),201


	@appblueprint.route('/users')
	def fetch_all_users():

		return jsonify({"Users":incident.fetch_all_users()}),200

