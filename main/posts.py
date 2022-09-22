from main import *
from flask import Blueprint, request
import certifi

bp_login = Blueprint("login", __name__, url_prefix="/login", template_folder='templates')

# db 연결
ca = certifi.where()
client = MongoClient('mongodb://15.164.214.98', 27017, username="test", password="test")
db = client.yoryjory

SECRET_KEY = 'SPARTA'

bp_post = Blueprint("posts", __name__, url_prefix="/posts", template_folder='templates')



@bp_post.route('/posting', methods=['POST'])
def posting():
    selectFood_receive = request.form["selectFood_give"]
    content_receive = request.form["content_give"]
    file = request.files["file_give"]
    location_receive = request.form["location_give"]

    extension = file.filename.split('.')[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}'
    save_to = f'main/static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'selectFood': selectFood_receive,
        'content':content_receive,
        'file': f'{filename}.{extension}',
        'location': location_receive
    }
    db.posts.insert_one(doc)

    return jsonify({'msg':'업로드 완료!'})