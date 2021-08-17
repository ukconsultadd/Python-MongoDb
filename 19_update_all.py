import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

# Update all documents where the address starts with the letter "S":
x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")