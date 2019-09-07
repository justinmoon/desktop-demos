from flask import Flask
from pyfladesk import init_gui

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(commands.enumerate())

if __name__ == '__main__':
    init_gui(app)
