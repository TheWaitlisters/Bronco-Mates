from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Johnny")
def johnnyA3():
    return "<p> I hope this is what you do for A3 part 3 otherwise i dunno </p>"