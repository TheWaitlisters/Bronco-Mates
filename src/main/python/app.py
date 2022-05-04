import datetime
import re
import sys
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_pymongo import pymongo
from pymongo import MongoClient
from .db import db

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "0b5b1309c9ab64665514a3fd8b28ca95686360ca302d111e"
    

    return app




app = createApp()

accountDB = []

listingDB = []

#listing db 


loginInfo = [{'username' : 'testusername', 'password' : 'testpassword'}]

@app.route("/")
def homePage(): 
    
    return render_template('index.html',listing = list(db.db.listing.find()), account = list(db.db.accountInfo.find()) )

@app.route("/database")
def test():
    # db.Account_Information.insert_one({"username": "helloworld"})
    # db.db.collection.insert_one({"username": "helloworld"})
    # db.db.collection.insert_one({"password" : "hi123"})
    return "connected to the database!"

@app.route("/createlisting", methods =("GET", "POST"))
def createListing():
    
    if request.method == "POST":
        # INFORMATION ABOUT LISTING
        address = request.form["address"]
        address2 = request.form["address2"]
        city = request.form["city"]
        state = request.form["state"]
        zip = request.form["zip"]
        deleteKey = request.form["deleteKey"]
        beds = request.form["beds"]
        roomSize = request.form["roomSize"]
        baths = request.form["baths"]
        price = request.form["price"]
        pets = request.form["pets"]
        phoneNumber = request.form["phoneNumber"]
        email = request.form["email"]
        amenities = request.form["amenities"]
        addInfo = request.form["addInfo"]

        # INFORMATION ABOUT SELF
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
        socials = { "facebook" : request.form["facebook"], "instagram" : request.form["instagram"], "snapchat" : request.form["snapchat"],
                    "twitter" : request.form["twitter"]}
        workSchedule = { "Monday" : (request.form["mSchedule1"], request.form["mSchedule2"]),
                        "Tuesday" : (request.form["tSchedule1"], request.form["tSchedule2"]),
                        "Wednesday" : (request.form["wSchedule1"], request.form["wSchedule2"]),
                        "Thursday" : (request.form["thSchedule1"], request.form["thSchedule2"]),
                        "Friday" : (request.form["fSchedule1"], request.form["fSchedule2"]),
                        "Saturday" : (request.form["satSchedule1"], request.form["satSchedule2"]),
                        "Sunday" : (request.form["sunSchedule1"], request.form["sunSchedule2"]) }
        moveDate = request.form["moveDate"]
        bio = request.form["bio"]

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
        elif not deleteKey:
            flash("Delete key is required")
        elif not phoneNumber:
            if not email:
                flash("One contact method must be provided")
        else:
            db.db.listing.insert_one({'address' : address, 'address2' : address2, 'city' : city, 'state': state, 
            'zip' : zip, 'deleteKey' : deleteKey, 'beds' : beds, 'roomSize' : roomSize, 'baths': baths, 'price': price, 'pets' : pets, 
            'phoneNumber' : phoneNumber, 'email' : email, 'amenities': amenities, 'addInfo' : addInfo})

            db.db.accountInfo.insert_one({"age" : age, "gender" : gender, "standing" : standing, "major" : major, "minor" : minor,
                "smoker" : smoker, "pets" : pets, "budget" : budget, "children" : children, "ocupation" : ocupation, 
                "workSchedule" : workSchedule, "moveDate" : moveDate, "socials" : socials, "bio" : bio})
            # listingDB.append({
            #     "address" : address,
            #     "address2" : address2,
            #     "city" : city,
            #     "state" : state,
            #     "zip" : zip,
            #     "suite" : "N/A",
            #     "beds" : beds,
            #     "roomsize" : roomSize,
            #     "baths" : baths,
            #     "price" : price,
            #     "amenities" : amenities,
            #     "addInfo" : addInfo
            # })
            return redirect(url_for("homePage"))
        

    return render_template("listing_description.html")

@app.route('/oncampus', methods =["GET", 'POST'])
def onCampus():
    if request.method == 'POST':
        suite = request.form["suite"]
        roomSize = request.form["roomSize"]
        addInfo = request.form["addInfo"]
        beds = request.form["beds"]
        baths = request.form["baths"]
        price = request.form["price"]
    
        if not suite: 
            flash('Please select a suite!')
        elif not roomSize:
           flash('Please enter your room size!')
        elif not beds:
            flash('Please enter amount of bedrooms!')
        elif not baths: 
            flash('Please enter amount of bathrooms!')
        elif not price:
            flash('Please enter price!')
        else:
            db.db.listing.insert_one({"suite": suite, "roomsize" : roomSize, "beds" : beds, "price" : price, 
            "address" : "3801 West Temple Avenue", "city" : "Pomona", "state" : "Ca", "zip" : "91768", "addInfo" : addInfo})
            return redirect(url_for('homePage'))
    return render_template('on_campus.html')


if __name__ == "__main__":
    app.run(debug=True)
