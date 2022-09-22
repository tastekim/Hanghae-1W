from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import jwt
import certifi
import datetime
import hashlib
from flask import jsonify
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


app = Flask(__name__)

from . import posts
from . import login
from . import user
from . import lists


app.register_blueprint(posts.bp_post)
app.register_blueprint(user.bp_user)
app.register_blueprint(login.bp_login)
app.register_blueprint(lists.bp_lists)

SECRET_KEY = 'SPARTA'

# db 연결
ca = certifi.where()
client = MongoClient('mongodb://15.164.214.98', 27017, username="test", password="test")
db = client.yoryjory
