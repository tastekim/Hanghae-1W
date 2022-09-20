from flask import Flask, render_template, request, jsonify, Blueprint
from pymongo import MongoClient
import certifi

# db 연결
ca = certifi.where()
client = MongoClient('mongodb://15.164.214.98', 27017, username="test", password="test")
db = client.yoryjory

bp_post = Blueprint("posts", __name__, url_prefix="/post", template_folder='templates')

@bp_post.route('/')
def home():
    return "this is post"