from flask import Flask
from pyfladesk import init_gui
from app import app

if __name__ == '__main__':
    init_gui(app)
