import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "_id": 1, "name": 1, "address": 1 }):
  print(x)

print("\n\n")

for x in mycol.find({},{ "address": 0 }):
  print(x)