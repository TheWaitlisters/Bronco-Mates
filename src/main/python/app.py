import datetime
import re
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

loginInfo = [{'username' : 'testusername', 'password' : 'testpassword'}]

@app.route("/")
def homePage():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route("/databasetest")
def databaseTesting():
    return render_template('database_test.html', content = messages)

@app.route('/login', methods =["GET", 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form['password']
    
        if not username: 
            flash('Please enter a valid username')
        elif not password:
           flash('Please enter your password')
        else:
            loginInfo.append({"username" : username, 'password' : password})
            return redirect(url_for('homePage'))
    return render_template('login.html')

@app.route("/accountsettings", methods =["GET", "POST"])
def accountSettings():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        phoneNumber = request.form["phoneNumber"]
        email = request.form["email"]
        age = request.form["age"]
        gender = request.form["gender"]
        standing = request.form["standing"]
        major = request.form["major"]
        minor = request.form["minor"]
        smoker = request.form["smoker"]
        pets = request.form["pets"]
        budget = request.form["budget"]
        children = request.form["children"]
        ocupation = request.form["ocupation"]
        workSchedule = { "Monday" : (request.form["mSchedule1"], request.form["mSchedule2"]),
                        "Tuesday" : (request.form["tSchedule1"], request.form["tSchedule2"]),
                        "Wednesday" : (request.form["wSchedule1"], request.form["wSchedule2"]),
                        "Thursday" : (request.form["thSchedule1"], request.form["thSchedule2"]),
                        "Friday" : (request.form["fSchedule1"], request.form["fSchedule2"]),
                        "Saturday" : (request.form["satSchedule1"], request.form["satSchedule2"]),
                        "Sunday" : (request.form["sunSchedule1"], request.form["sunSchedule2"]) }
        moveDate = request.form["moveDate"]
        bio = request.form["bio"]

        if not username:
            flash("Username required")
        elif not password:
            flash("Password required")
        else:
            messages.append({
                "username" : username,
                "password" : password,
                "phoneNumber" : phoneNumber,
                "email" : email,
                "age" : age,
                "gender" : gender,
                "standing" : standing,
                "major" : major,
                "minor" : minor,
                "smoker" : smoker,
                "pets" : pets,
                "budget" : budget,
                "children" : children,
                "ocupation" : ocupation,
                "workSchedule" : workSchedule,
                "moveDate" : moveDate,
                "bio" : bio
            })
            return redirect(url_for("homePage"))

    return render_template("account_settings.html")

@app.route("/createlisting", methods =("GET", "POST"))
def createListing():
    return render_template("listing_description.html")

@app.route("/favorites", methods =("GET", "POST"))
def favorites():
    return render_template("favorites.html")

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
