from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for,Blueprint
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import certifi




# db 연결
ca = certifi.where()
client = MongoClient('mongodb://15.164.214.98', 27017, username="test", password="test")
db = client.yoryjory

bp_list = Blueprint("lists", __name__, url_prefix="/list", template_folder='templates')


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'


@bp_list.route('/')
def listpage():
    return render_template('index.html')

# post 쪽에서 이걸 받아와야함 승훈님이 보내주신 것에는 id/username/date/프로필사진이 없으니까 이걸 받아와야할 함수?가 필요
# user_info = db.users.find_one({"username": payload["id"]})
# comment_receive = request.form["comment_give"]
# date_receive = request.form["date_give"]
# doc = {
#     "username": user_info["username"],
#     "profile_name": user_info["profile_name"],
#     "profile_pic_real": user_info["profile_pic_real"],
#     "comment": comment_receive,
#     "date": date_receive
# }
# db.posts.insert_one(doc)




@bp_list.route("/get_posts", methods=['GET'])
def get_posts():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        posts = list(db.posts.find({}).sort("date", -1).limit(20))
        for post in posts:
            post["_id"] = str(post["_id"])
        return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.","posts":posts})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


# 일단 지금 포스트 받아오는 함수를 가져옴