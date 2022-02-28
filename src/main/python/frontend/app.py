import datetime
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:5000/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route("/goodbye")
def goodbye():
    goodbyeMsg = ["Sad to see you go!",
                  "But at least you were here for the show.",
                  "Enjoy these fancy boxes!",
                  "I promise there's no foxes."
                 ]

    return render_template('goodbye.html', goodbyeMsg = goodbyeMsg)

@app.route("/Ana/<name>")
def AnaA3(name):
    return f'This is my part for A3 {name}'

@app.route("/Andy/<name>")
def AndyA3(name):
    return f'My part for A3 {name}'

@app.route("/Alex/<name>")
def AlexA3(name):
    return f'hello {name}, welcome to our page'
    
if __name__ == "__main__":
    app.run(debug=True)