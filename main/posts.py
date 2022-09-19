import flask
from flask import Flask, render_template, request, jsonify, Blueprint
from pymongo import MongoClient
import certifi

# db 연결
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.2jrn8.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.yoryjory

bp_post = Blueprint("posts", __name__, url_prefix="/post", template_folder='templates')

@bp_post.route('/')
def home():
    return render_template('index.html')