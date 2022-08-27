from audioop import add
from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
# test to make sure data can be read by Insomnia
def getdata():
    return {'yes': 'm'}