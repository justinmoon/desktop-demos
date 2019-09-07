from threading import Thread
import webview
from flask import Flask, jsonify
from hwilib import commands

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(commands.enumerate())

server = Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5001})
server.start()

webview.create_window('Hello world', 'http://localhost:5001/')
webview.start(debug=True)
