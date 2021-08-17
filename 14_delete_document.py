import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

# Note: If the query finds more than one document, only the first occurrence is deleted.
# Delete the document with the address "Mountain 21":
mycol.delete_one(myquery)