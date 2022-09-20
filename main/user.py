from flask import Flask, render_template, request, jsonify, Blueprint
from pymongo import MongoClient
import certifi

# db 연결
ca = certifi.where()
client = MongoClient('mongodb://15.164.214.98', 27017, username="test", password="test")
db = client.yoryjory

bp_user = Blueprint("user", __name__, url_prefix="/user", template_folder='templates')

@bp_user.route('/')
def userpage():
    return render_template('profile.html')

@bp_user.route('/detail', methods=["GET"])
def userpage_detail():
    return jsonify({})
