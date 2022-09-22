from main import *
from flask import Blueprint, request
import certifi

# db 연결
ca = certifi.where()
client = MongoClient('mongodb://15.164.214.98', 27017, username="test", password="test")
db = client.yoryjory

SECRET_KEY = 'SPARTA'

bp_post = Blueprint("posts", __name__, url_prefix="/posts", template_folder='templates')


@bp_post.route('/posting', methods=['POST'])
def posting():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        selectFood_receive = request.form["selectFood_give"]
        content_receive = request.form["content_give"]
        file = request.files["file_give"]
        location_receive = request.form["location_give"]
        date_receive = request.form["date_give"]
        extension = file.filename.split('.')[-1]

        today = datetime.now()
        mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
        filename = f'file-{mytime}'
        save_to = f'main/static/{filename}.{extension}'
        file.save(save_to)

        doc = {
            "username": user_info["username"],
            "profile_name": user_info["profile_name"],
            "profile_pic_real": user_info["profile_pic_real"],
            'selectFood': selectFood_receive,
            'content':content_receive,
            'file': f'{filename}.{extension}',
            'location': location_receive,
            "date": date_receive
        }
        db.posts.insert_one(doc)

        return jsonify({"result": "success", 'msg': '포스팅 성공'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))