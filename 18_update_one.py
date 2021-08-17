import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

# Note: If the query finds more than one record, only the first occurrence is updated.
# Change the address from "Valley 345" to "Canyon 123":
mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)