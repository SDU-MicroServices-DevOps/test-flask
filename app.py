from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World New Revision Kage er godt Meget kage meget godt!</p>"