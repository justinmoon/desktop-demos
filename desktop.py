from flask import Flask
import threading
import webview

app = Flask(__name__)

@app.route('/')
def home():
    return 'Orange coin good, number go up'

if __name__ == '__main__':
    # run server
    server = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0'})
    server.start()
    # run webview
    webview.create_window('Bitcoin', 'http://localhost:5000')
    webview.start()
 
