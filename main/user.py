from flask import Flask, render_template, request, jsonify, Blueprint
from pymongo import MongoClient
import certifi

# db 연결
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.2jrn8.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.yoryjory

bp_user = Blueprint("user", __name__, url_prefix="/user")

@bp_user.route('/')
def home():
    return "this is user"