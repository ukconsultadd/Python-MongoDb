import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Delete the "customers" collection:
dropped = mycol.drop()
print(dropped)