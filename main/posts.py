from flask import Flask, render_template, request, jsonify, Blueprint
app = Flask(__name__)

from datetime import datetime
from pymongo import MongoClient
import certifi

# db 연결
ca = certifi.where()
client = MongoClient('mongodb://15.164.214.98', 27017, username="test", password="test")
db = client.yoryjory

# client = MongoClient('mongodb+srv://test:sparta@cluster0.iilav5q.mongodb.net/?retryWrites=true&w=majority')


bp_post = Blueprint("posts", __name__, url_prefix="/posts", template_folder='templates')

@bp_post.route('/')
def home():
    return render_template('posting.html')

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
    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'selectFood': selectFood_receive,
        'content':content_receive,
        'file': f'{filename}.{extension}',
        'location': location_receive
    }
    db.posts.insert_one(doc)

    return jsonify({'msg':'업로드 완료!'})