from flask import Flask 
from flask_pymongo import pymongo
from pymongo import MongoClient
import ssl
#from app import app
 
CONNECTION_STRING = "mongodb+srv://ana23:qwer1234@cluster0.3ghbk.mongodb.net/Account?retryWrites=true&w=majority&authSource=admin"

client = pymongo.MongoClient(CONNECTION_STRING, ssl_cert_reqs=ssl.CERT_NONE)
db = client.get_database('Account')
listing_collection = pymongo.collection.Collection(db, 'listing')
accountinfo_collection = pymongo.collection.Collection(db, 'Account_Information')
