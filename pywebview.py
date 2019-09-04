import webview
from app import app
from threading import Thread

server = Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5001})
server.start()

webview.create_window('Hello world', 'http://localhost:5001/')
webview.start(debug=True)