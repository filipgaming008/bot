from flask import Flask
from threading import Thread
from flask import request
from flask import jsonify

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"


def run():
    app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
