from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import jsonify
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


app = Flask(__name__)

from . import posts
from . import login
from . import user


app.register_blueprint(posts.bp_post)
app.register_blueprint(user.bp_user)
app.register_blueprint(login.bp_login)

#
# @app.route('/')
# def home():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#
#         return render_template('index.html')
#     except jwt.ExpiredSignatureError:
#         return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
#     except jwt.exceptions.DecodeError:
#         return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))