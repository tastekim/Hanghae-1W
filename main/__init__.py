from flask import Flask, render_template
from . import posts, user, lists

app = Flask(__name__)

app.register_blueprint(posts.bp_post)
app.register_blueprint(user.bp_user)
app.register_blueprint(lists.bp_list)

@app.route('/')
def home():
    return "this is home"