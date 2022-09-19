from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

# db 연결
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.2jrn8.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.yoryjory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
