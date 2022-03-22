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

accountDB = []   

listingDB = []

loginInfo = [{'username' : 'testusername', 'password' : 'testpassword'}]

@app.route("/")
def homePage():
    return render_template('index.html', account = accountDB, listing = listingDB)

@app.route("/databasetest")
def databaseTesting():
    return render_template('database_test.html', account = accountDB)

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
            accountDB.append({
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
    if request.method == "POST":
        address = request.form["address"]
        address2 = request.form["address2"]
        city = request.form["city"]
        state = request.form["state"]
        zip = request.form["zip"]
        beds = request.form["beds"]
        baths = request.form["baths"]
        price = request.form["price"]
        amenities = request.form["amenities"]
        addInfo = request.form["addInfo"]

        if not address:
            flash("Address required")
        elif not city:
            flash("City required")
        elif state == "Choose..." or not state:
            flash("State required")
        elif not zip:
            flash("ZIP code required")
        elif not beds:
            flash("Number of beds required")
        elif not baths:
            flash("Number of baths required")
        elif not price:
            flash("Price required")
        else:
            listingDB.append({
                "address" : address,
                "address2" : address2,
                "city" : city,
                "state" : state,
                "zip" : zip,
                "beds" : beds,
                "baths" : baths,
                "price" : price,
                "amenities" : amenities,
                "addInfo" : addInfo
            })
            return redirect(url_for("homePage"))

    return render_template("listing_description.html")

@app.route("/favorites", methods =("GET", "POST"))
def favorites():
    return render_template("favorites.html")

if __name__ == "__main__":
    app.run(debug=True)
