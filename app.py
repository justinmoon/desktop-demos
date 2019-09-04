from flask import Flask, jsonify
from hwilib import commands

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(commands.enumerate())

if __name__ == '__main__':
    app.run()
