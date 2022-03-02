import datetime
import sys
from flask import Flask, render_template
from flask_pymongo import PyMongo
from matplotlib.pyplot import plt

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

@app.route("/ana")
def ana(name):
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 5, 6, 6]

    plt.plot(x,y)
    return render_template('ana.html', plt.show())


@app.route("/Andy/<name>")
def AndyA3(name):
    return f'My part for A3 {name}'

@app.route("/Alex/<name>")
def AlexA3(name):
    return f'hello {name}, welcome to our page' #commit test

def start(out):
        out.write("Successfully starting up")

if __name__ == "__main__":
    app.run(debug=True)