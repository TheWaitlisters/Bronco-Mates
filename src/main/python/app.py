import datetime
import sys
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_pymongo import pymongo
from matplotlib import pyplot as plt

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "0b5b1309c9ab64665514a3fd8b28ca95686360ca302d111e"
    app.config["MONGO_URI"] = "mongodb://localhost:5000/myDatabase"

    return app

app = createApp()

messages = [{"username" : 'username1',
             "email" : "email1" }]   

# @app.route("/", methods=["GET", "POST"])
# def home():

#     if request.method == "POST":
#         content = request.form["content"]
#         return "POST method called"

#     return "GET method called"

@app.route("/")
def homePage():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route("/databasetest")
def databaseTesting():
    return render_template('database_test.html', content = messages)

@app.route("/accountsettings", methods =["GET", "POST"])
def accountSettings():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        phoneNumber = request.form["phoneNumber"]
        standing = request.form["standing"]
        major = request.form["major"]
        minor = request.form["minor"]
        addInfo = request.form["addInfo"]

        if not username:
            flash("Username is required!")
        elif not email:
            flash("Email is required!")
        else:
            messages.append({"username" : username, "email" : email, "phoneNumber" : phoneNumber,
                             "standing" : standing, "major" : major, "minor" : minor, "addInfo" : addInfo})
            return redirect(url_for("homePage"))

    return render_template("account_settings.html")

@app.route("/createlisting", methods =("GET", "POST"))
def createListing():
    return render_template("listing_description.html")

@app.route("/ana")
def ana(name):
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 5, 6, 6]

    plt.plot(x,y)
    return render_template('ana.html', plt.show())

@app.route("/insertdocument")
def insertdocument():
    client = MongoClient()
    db = client.bronco_mates
    collection = db.students
    record = {"student" : "Andy Munoz",
              "major" : "Computer Science"}
    post_id = collection.insert_one(record).inserted_id
    return render_template('insertdocument.html', print(post_id))

if __name__ == "__main__":
    app.run(debug=True)
