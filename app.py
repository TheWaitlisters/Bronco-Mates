from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Johnny/<name>")
def johnnyA3(name):
    return f'I hope this is what you do for A3, also hi {name}'

@app.route("/Ana/<name>")
def AnaA3(name):
    return f'This is my part for A3 {name}'