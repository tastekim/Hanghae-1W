from flask import Flask
from . import posts, user

app = Flask(__name__)

app.register_blueprint(posts.bp_post)
app.register_blueprint(user.bp_user)

@app.route('/')
def home():
    return "this is home"