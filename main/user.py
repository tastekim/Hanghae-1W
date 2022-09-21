from flask import Flask, render_template, request, jsonify, Blueprint, redirect, url_for
from pymongo import MongoClient
import certifi
from werkzeug.utils import secure_filename

import jwt

import jwt

# db 연결
ca = certifi.where()
client = MongoClient('mongodb://15.164.214.98', 27017, username="test", password="test")
db = client.yoryjory

SECRET_KEY = 'SPARTA'

bp_user = Blueprint("user", __name__, url_prefix="/user", template_folder='templates')

@bp_user.route('/<username>')
def user(username):
    # 각 사용자의 프로필과 글을 모아볼 수 있는 공간
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        status = (username == payload["id"])  # 내 프로필이면 True, 다른 사람 프로필 페이지면 False
        user_info = db.users.find_one({"username": username}, {"_id": False})
        return render_template('profile.html', user_info=user_info, status=status)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

<<<<<<< HEAD
=======
@bp_user.route('/update_profile', methods=['POST'])
def save_img():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        username = payload["id"]
        name_receive = request.form["name_give"]
        about_receive = request.form["about_give"]
        new_doc = {
            "profile_name": name_receive,
            "profile_info": about_receive
        }
        if 'file_give' in request.files:
            file = request.files["file_give"]
            filename = secure_filename(file.filename)
            extension = filename.split(".")[-1]
            file_path = f"profile_pics/{username}.{extension}"
            file.save("./main/static/" + file_path)
            new_doc["profile_pic"] = filename
            new_doc["profile_pic_real"] = file_path
        db.users.update_one({'username': payload['id']}, {'$set': new_doc})
        return jsonify({"result": "success", 'msg': '프로필을 업데이트했습니다.'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))
>>>>>>> bp
