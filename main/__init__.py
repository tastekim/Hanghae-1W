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

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        print(token_receive)
        return render_template('index.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))